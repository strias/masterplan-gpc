#!/usr/bin/env python3
"""Separa voces por audio para las transcripciones de Whisper (archivo/<ID>-...whisper.srt).

Genera la base de scripts/voces/<ID>.tsv cuando las voces se separan por audio y no solo por
contenido (fuentes en VOCES_AUDIO de scripts/transcripciones.py). Los nombres de las voces los
asigna una persona (o Claude) leyendo el contenido; este script solo dice qué tramos suenan igual.

Pasos:

  1. huellas: calcula una huella de voz (ECAPA, speechbrain) por ventana de 1,5 s cada 0,75 s.
       python3 scripts/voces_audio.py huellas archivo/F-0031-....wav 360 3310 /tmp/F-0031.npy

  2. Una de estas dos formas de agrupar, que escribe una etiqueta por subtítulo:
     - referencias: compara cada ventana con un tramo de referencia de cada voz. Sirve cuando una
       voz suena distinta (por ejemplo, un entrevistado por Zoom). Usado en F-0030.
       python3 scripts/voces_audio.py referencias /tmp/F-0030.npy 2280 archivo/F-0030-....whisper.srt \\
           Britos=00:44:09-00:44:48,00:51:10-00:51:50 Conductor=00:38:15-00:38:50 > /tmp/F-0030.voces
     - grupos: KMeans en k voces. Sirve cuando todos están en el mismo estudio. Usado en F-0031 (k=3).
       python3 scripts/voces_audio.py grupos /tmp/F-0031.npy 360 archivo/F-0031-....whisper.srt 3 > /tmp/F-0031.voces

  3. tsv: une los subtítulos seguidos de la misma voz en turnos y escribe el archivo de voces con
     la frase exacta donde empieza cada turno, que es lo que lee transcripciones.py.
       python3 scripts/voces_audio.py tsv /tmp/F-0031.voces archivo/F-0031-....whisper.srt \\
           V1="José Decurnex" V2="Alexis (conductor)" V0="Virginia Lafuente (conductora)" > scripts/voces/F-0031.tsv
     Después se agregan a mano, al principio, los comentarios (#) con el método y las dudas, y se
     corrigen los cortes que el contenido muestre equivocados.

Requiere: pip install -r scripts/requirements-voces.txt. La primera vez descarga el modelo
speechbrain/spkrec-ecapa-voxceleb de Hugging Face a archivo/modelos/ (no se sube al repo).
"""
import sys
from pathlib import Path

VENTANA, PASO = 1.5, 0.75
SR = 16000
MODELO = Path("archivo/modelos/spkrec-ecapa-voxceleb")


def seg(t):
    h, m, s = t.replace(",", ".").split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def hms(s):
    s = int(s)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def leer_srt(p):
    """[(inicio, fin, texto)] tal como los escribe whisper-cli, sin unir ni limpiar."""
    subs = []
    for bloque in Path(p).read_text().strip().split("\n\n"):
        ls = bloque.strip().split("\n")
        if len(ls) >= 3:
            a, b = ls[1].split(" --> ")
            subs.append((seg(a), seg(b), " ".join(ls[2:]).strip()))
    return subs


def huellas(wav, ini, fin, salida):
    import numpy as np
    import soundfile as sf
    import torch
    from speechbrain.inference.speaker import EncoderClassifier

    audio, sr = sf.read(wav, start=int(float(ini) * SR), stop=int(float(fin) * SR), dtype="float32")
    assert sr == SR, "el audio tiene que ser mono a 16 kHz, como el que usa Whisper"
    disp = "mps" if torch.backends.mps.is_available() else "cpu"
    enc = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir=str(MODELO),
                                         run_opts={"device": disp})
    inicios = np.arange(0, len(audio) / SR - VENTANA, PASO)
    lotes = []
    with torch.no_grad():
        for i in range(0, len(inicios), 64):
            x = np.stack([audio[int(s * SR):int((s + VENTANA) * SR)] for s in inicios[i:i + 64]])
            lotes.append(enc.encode_batch(torch.tensor(x)).squeeze(1).cpu().numpy())
            if i % 1280 == 0:
                print(f"{i}/{len(inicios)}", file=sys.stderr, flush=True)
    E = np.concatenate(lotes)
    np.save(salida, E / np.linalg.norm(E, axis=1, keepdims=True))


def etiquetar(E, ini, srt, voz_por_ventana, puntaje):
    """Una voz por subtítulo: la mayoritaria entre las ventanas centradas dentro de él."""
    import numpy as np

    centros = float(ini) + np.arange(len(E)) * PASO + VENTANA / 2
    for a, b, t in leer_srt(srt):
        m = (centros >= a) & (centros <= b)
        if not m.any():  # subtítulo más corto que el paso: ventana más cercana
            m = np.zeros(len(E), bool)
            m[np.argmin(np.abs(centros - (a + b) / 2))] = True
        voz, conf = puntaje(voz_por_ventana, m)
        print(f"{a:.2f}\t{b:.2f}\t{voz}\t{conf:.2f}\t{t}")


def referencias(npy, ini, srt, *refs):
    import numpy as np

    E = np.load(npy)
    centros = float(ini) + np.arange(len(E)) * PASO + VENTANA / 2
    nombres, C = [], []
    for r in refs:
        nombre, tramos = r.split("=")
        m = np.zeros(len(E), bool)
        for tr in tramos.split(","):
            a, b = (seg(x) for x in tr.split("-"))
            m |= (centros >= a) & (centros <= b)
        c = E[m].mean(0)
        nombres.append(nombre)
        C.append(c / np.linalg.norm(c))
    S = E @ np.stack(C).T  # similitud coseno de cada ventana con cada referencia

    def puntaje(S, m):  # voz más parecida y margen sobre la segunda
        s = S[m].mean(0)
        o = np.argsort(-s)
        return nombres[o[0]], s[o[0]] - s[o[1]]

    etiquetar(E, ini, srt, S, puntaje)


def grupos(npy, ini, srt, k):
    import numpy as np
    from sklearn.cluster import KMeans

    E = np.load(npy)
    lab = KMeans(int(k), n_init=20, random_state=0).fit_predict(E)

    def puntaje(lab, m):  # grupo mayoritario y su proporción
        v = np.bincount(lab[m], minlength=int(k))
        return f"V{v.argmax()}", v.max() / v.sum()

    etiquetar(E, ini, srt, lab, puntaje)


def tsv(voces, srt, *nombres):
    """Turnos con su frase de inicio. Un subtítulo de menos de 2 s entre dos de la misma voz toma esa voz."""
    nombre = dict(n.split("=", 1) for n in nombres)
    filas = [l.rstrip("\n").split("\t") for l in Path(voces).read_text().splitlines()]
    subs = leer_srt(srt)
    assert len(filas) == len(subs), "el archivo de voces no corresponde a estos subtítulos"
    lab = [f[2] for f in filas]
    for i in range(1, len(lab) - 1):
        if lab[i - 1] == lab[i + 1] != lab[i] and float(filas[i][1]) - float(filas[i][0]) < 2:
            lab[i] = lab[i - 1]
    texto, pos = "", []
    for _, _, t in subs:
        pos.append(len(texto))
        texto += t + " "
    print("# Cada línea marca dónde empieza a hablar alguien: minuto aproximado, frase exacta de la transcripción, hablante.")
    anterior, desde = None, 0
    for i, (a, _, t) in enumerate(subs):
        if lab[i] == anterior:
            continue
        anterior = lab[i]
        frase, j = "", i
        while len(frase) < 30 and j < len(subs) and lab[j] == lab[i]:  # frase larga para que sea única
            frase = (frase + " " + subs[j][2]).strip()
            j += 1
        p = texto.find(frase, desde)
        assert pos[i] <= p <= pos[i] + 2, f"la frase de {hms(a)} aparece antes en el texto: {frase!r}"
        desde = p + 1
        print(f"{hms(a)}\t{frase}\t{nombre.get(lab[i], lab[i])}")


if __name__ == "__main__":
    pasos = {"huellas": huellas, "referencias": referencias, "grupos": grupos, "tsv": tsv}
    if len(sys.argv) < 2 or sys.argv[1] not in pasos:
        sys.exit(__doc__)
    pasos[sys.argv[1]](*sys.argv[2:])
