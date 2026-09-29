#!/usr/bin/env python3
"""Genera las transcripciones publicadas en transcripciones/.

Fuentes de entrada (en archivo/, locales, no se suben al repo):
  - <ID>-...transcripcion.txt  transcripción con separación de voces (youtubetotext)
  - <ID>-...subtitulos.vtt     subtítulos automáticos de YouTube

Si hay transcripción con voces, es la base y los subtítulos se usan para
contrastar cifras: cada bloque donde los números no coinciden lleva debajo
el texto de YouTube para ese mismo tramo. Si solo hay subtítulos, se
publican agrupados en bloques de ~30 s.

En los dos casos se corrigen nombres propios mal transcritos (lista FIX) y
se agrega al final la tabla de correcciones aplicadas.

Uso: python3 scripts/transcripciones.py  (desde la raíz del repo)
"""
import hashlib
import re
from collections import Counter
from pathlib import Path

# Correcciones de nombres propios. Solo casos inequívocos por contexto.
FIX = [
    (r"\b(?:Sepé|Sepe|SPA|CPAU|CP|CPA) Ferr(?:er|ero|y|ere)\b", "CPA Ferrere"),
    (r"\bFerrer(?=,? CPA)", "Ferrere"),
    (r"\bmodelo de SPA\b", "modelo de CPA"),
    (r"\bCP que me lo escriba\b", "CPA que me lo escriba"),
    (r"\b(?:José )?(?:de )?(?:Curnek|Curnext|Cournext|Curnex)\b",
     lambda m: ("José " if m.group(0).startswith("José") else "") + "Decurnex"),
    (r"\bDe Cur ?네(?:ks)?\b", "Decurnex"),
    (r"\b(?:De ?Curplex|Decurplex|Decournex|Decourplex|Decurné|Decurc)\b", "Decurnex"),
    (r"\bJosé de Curné\b", "José Decurnex"),
    (r"\b(?:Permand|Persman|Perma|Perman)\b", "Perchman"),
    (r"\bRicardo (?:Airó|Bairo|Bayro)\b", "Ricardo Vairo"),
    (r"\b(?:Bairo|Bayro)\b", "Vairo"),
    (r"\bLluria\b", "Giuria"),
    (r"\bNono Yuria\b", "Nono Giuria"),
    (r"\bJavier G[oó]mez (?:Oro|Zoro|Coro|Sol[oó]|Soro|Toro)\b", "Javier Gomensoro"),
    (r"\bG[oó]mez (?:Oro|Zoro|Coro|Sol[oó]|Soro|Toro|Solórzano)\b", "Gomensoro"),
    (r"\bFederico Brito\b", "Federico Britos"),
    (r"\bBrito,", "Britos,"),
    (r"\bMaro Nadal\b", "Amaro Nadal"),
    (r"\bAlejandro (?:Valvi|Balvi)\b", "Alejandro Balbi"),
    (r"\b(?:Valvi|Balvi)\b", "Balbi"),
    (r"\bSigleti Bardanca\b", "Singlet y Bardanca"),
    (r"\b(?:Sigleti|Siglé|Singlés|Singlett|Saint Led|Singlede|Singué|Singlé)\b", "Singlet"),
    (r"\bSingle(?= y Barranca| y Bardanca)", "Singlet"),
    (r"\b(?:Barranca|Bardanga)\b", "Bardanca"),
    (r"\b(?:Aldavalde|Alvalde|Alavalde|Lavalde)\b", "Aldabalde"),
    (r"\bAldabal(?= le ha| la semana)", "Aldabalde"),
    (r"\bla Carone\b", "la Scarone"),
    (r"\bescarones\b", "Scarone"),
    (r"\bAtila García\b", "Atilio García"),
    (r"\bAbdon\b", "Abdón"),
    (r"\bPasión y Color Play\b", "Pasión Tricolor Play"),
    (r"\bEduardo Hache\b", "Eduardo Ache"),
    (r"\bGuerra de Rosas\b", "Guerra De Rossa"),
    (r"\bVares, otro estudio\b", "Varesi, otro estudio"),
    (r"\bIgnacio Massena\b", "Ignacio Masena"),
    (r"\bcuota del Bage\b", "cuota del básquet"),
]

JOBS = [
    # id, slug, título, url, fecha
    ("F-0014", "pasion-tricolor-aldabalde-2026-09-25",
     "Nos visita Santiago Aldabalde responde todas las dudas del master plan del GPC",
     "https://www.youtube.com/live/zOnJazksi08", "2026-09-25"),
    ("F-0015", "territorio-nacional-decurnex-2026-09-21",
     "Territorio Nacional | Club Social y Master Plan",
     "https://www.youtube.com/watch?v=ErxVag75_mA", "2026-09-21"),
    ("F-0016", "espectador-aldabalde-2026-09-17",
     "Santiago Aldabalde salió al cruce de las críticas al Masterplan del GPC: “no tienen plan B”",
     "https://www.youtube.com/watch?v=anYgHKGhDWo", "2026-09-17"),
    ("F-0017", "pasion-tricolor-singlet-bardanca-2026-09-24",
     "Las dudas sobre el master plan del GPC - Nos visitan CR. Singlet y CR. Bardanca",
     "https://www.youtube.com/watch?v=dowYxCNXN7k", "2026-09-24"),
    ("F-0018", "espectador-aldabalde-2026-07-16",
     "SANTIAGO ALDABALDE Y LOS DETALLES DEL MASTER PLAN DEL GRAN PARQUE CENTRAL | 16/7/2026",
     "https://www.youtube.com/watch?v=PDYIvpms7r4", "2026-07-16"),
    ("F-0019", "pasion-tricolor-reaccion-decurnex-2026-09-22",
     "Habló Decurnex: Máster plan GPC y club social - REACCIONAMOS",
     "https://www.youtube.com/watch?v=-lKaALmO6ao", "2026-09-22"),
]

ARCHIVO = Path("archivo")
SALIDA = Path("transcripciones")


def seg(t):
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s


def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def corregir(texto, cont):
    for pat, rep in FIX:
        def r(m, rep=rep):
            nuevo = rep(m) if callable(rep) else rep
            if nuevo != m.group(0):
                cont[(m.group(0), nuevo)] += 1
            return nuevo
        texto = re.sub(pat, r, texto)
    return texto


def leer_vtt(p):
    """Subtítulos automáticos: devuelve [(segundos, texto)] sin repeticiones."""
    out, t, vistos = [], None, set()
    for linea in p.read_text().split("\n"):
        m = re.match(r"(\d\d:\d\d:\d\d)\.\d+ -->", linea)
        if m:
            t = m.group(1)
            continue
        linea = re.sub(r"<[^>]+>", "", linea).strip()
        if not linea or t is None or linea in vistos or linea.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        vistos.add(linea)
        out.append((seg(t), linea))
    return out


def leer_voces(p):
    """Transcripción youtubetotext: devuelve [(inicio, fin, hablante, texto)]."""
    lineas = p.read_text().split("\n")
    out = []
    for i, linea in enumerate(lineas):
        m = re.match(r"(\d\d:\d\d:\d\d) --> (\d\d:\d\d:\d\d)$", linea)
        if m and i + 1 < len(lineas):
            h = re.match(r"(Speaker \d+): (.*)", lineas[i + 1])
            if h:
                out.append((seg(m.group(1)), seg(m.group(2)), h.group(1), h.group(2)))
    return out


def hms(s):
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def numeros(texto):
    """Cifras normalizadas (sin separadores de miles) de 2 o más dígitos."""
    t = re.sub(r"(?<=\d)[ .,](?=\d{3}\b)", "", texto)
    return {n.replace(",", ".") for n in re.findall(r"\d+(?:[.,]\d+)?", t) if len(n.replace(",", "").replace(".", "")) >= 2}


def combinar(voces, subs):
    bloques, divergencias = [], 0
    for ini, fin, hablante, texto in voces:
        yt = " ".join(l for t, l in subs if ini - 2 <= t <= fin + 2)
        linea = f"[{hms(ini)}] {hablante}: {texto}"
        if yt and numeros(texto) != numeros(yt) and (numeros(texto) | numeros(yt)):
            linea += f"\n> *YouTube ({hms(ini)}):* {yt}"
            divergencias += 1
        bloques.append(linea)
    return "\n\n".join(bloques), divergencias


def agrupar(subs, ventana=30):
    bloques, actual, inicio = [], [], None
    for t, l in subs:
        if inicio is None:
            inicio = t
        actual.append(l)
        if t - inicio >= ventana:
            bloques.append(f"[{hms(inicio)}] {' '.join(actual)}")
            actual, inicio = [], None
    if actual:
        bloques.append(f"[{hms(inicio)}] {' '.join(actual)}")
    return "\n\n".join(bloques)


def main():
    SALIDA.mkdir(exist_ok=True)
    for fid, slug, titulo, url, fecha in JOBS:
        voces_p = ARCHIVO / f"{fid}-{slug}.transcripcion.txt"
        subs_p = ARCHIVO / f"{fid}-{slug}.subtitulos.vtt"
        subs = leer_vtt(subs_p) if subs_p.exists() else []
        origenes = []
        if voces_p.exists():
            cuerpo, div = combinar(leer_voces(voces_p), subs)
            origenes.append(f"transcripción con separación de voces (youtubetotext), aportada por el autor del repo. SHA-256: `{sha256(voces_p)}`")
            if subs:
                origenes.append(f"subtítulos automáticos de YouTube, usados para contrastar cifras. SHA-256: `{sha256(subs_p)}`")
            modo = (f"La base es la transcripción con voces. En los {div} bloques donde las cifras no coinciden con los "
                    "subtítulos de YouTube, debajo se muestra el texto de YouTube para ese tramo (línea que empieza con *YouTube*). "
                    "La separación de voces es imperfecta: a veces mezcla a los entrevistados con los conductores.")
        elif subs:
            cuerpo = agrupar(subs)
            origenes.append(f"subtítulos automáticos de YouTube. SHA-256: `{sha256(subs_p)}`")
            modo = "Solo hay subtítulos automáticos: sin separación de voces, agrupados en bloques de unos 30 segundos."
        else:
            print(f"{fid}: sin archivos de entrada, se omite")
            continue
        cont = Counter()
        cuerpo = corregir(cuerpo, cont)
        tabla = "\n".join(f"| {a} | {b} | {n} |" for (a, b), n in sorted(cont.items())) or "| (ninguna) | | |"
        texto = f"""# Transcripción: {titulo}

- Fuente: [{fid}](../fuentes/) · {url}
- Fecha de emisión: {fecha}
- Origen:
""" + "".join(f"  - {o}\n" for o in origenes) + f"""
> **Aviso.** Transcripción automática, sin revisión humana completa. Solo se corrigieron nombres propios mal transcritos (lista al final). Puede tener errores de palabras, cifras o atribución de voces. Antes de citar, verificar contra el video en la marca de tiempo indicada. El contenido es de sus autores y del medio; se publica para que cualquiera pueda verificar las citas de este repositorio.
>
> {modo}

Generada con [`scripts/transcripciones.py`](../scripts/transcripciones.py).

---

{cuerpo}

---

## Correcciones aplicadas

| Transcrito | Corregido | Veces |
|---|---|---|
{tabla}
"""
        destino = SALIDA / f"{fid}-{slug}.md"
        destino.write_text(texto)
        print(f"{destino}: {sum(cont.values())} correcciones")


if __name__ == "__main__":
    main()
