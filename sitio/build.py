import html, os, re

ACTUALIZADO = "01/10/2026"
TITULO = "Contrapunto del Master Plan"
DESCRIPCION = "Preguntas, respuestas y fuentes del debate sobre el Master Plan del Gran Parque Central."
HEAD = open("head.html").read()  # fuentes y estilos compartidos


SITIO = "https://masterplangpc.com"
# Imagen de las vistas previas. Si cambia, cambiar también el nombre: X guarda la imagen vieja en caché.
OG_IMAGEN = "og-2026-09-29.jpg"

def tarjeta(titulo, descripcion, ruta):
    """Metadatos Open Graph y Twitter Card, para que X, WhatsApp y otros muestren la vista previa con imagen."""
    t, d, u = html.escape(titulo), html.escape(descripcion), f"{SITIO}/{ruta}"
    return (f'<link rel="canonical" href="{u}">\n'
            f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="Master Plan GPC">\n'
            f'<meta property="og:locale" content="es_UY">\n<meta property="og:title" content="{t}">\n'
            f'<meta property="og:description" content="{d}">\n<meta property="og:url" content="{u}">\n'
            f'<meta property="og:image" content="{SITIO}/{OG_IMAGEN}">\n<meta property="og:image:width" content="1200">\n'
            f'<meta property="og:image:height" content="630">\n<meta property="og:image:type" content="image/jpeg">\n'
            f'<meta property="og:image:alt" content="Qué se vota el 24 de octubre: la moción del Master Plan del Gran Parque Central, con fuentes.">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="{t}">\n'
            f'<meta name="twitter:description" content="{d}">\n<meta name="twitter:image" content="{SITIO}/{OG_IMAGEN}">\n')

REPO = "https://github.com/strias/masterplan-gpc"
# Franja superior de todas las páginas: el sitio se genera desde el repositorio público.
AVISO_GIT = (f'<a class="gitbar" href="{REPO}" target="_blank" rel="noopener">'
             '<svg viewBox="0 0 16 16" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"/></svg>'
             '<span>Este sitio se genera desde un repositorio público en GitHub: fuentes, método e historial de cambios <b>strias/masterplan-gpc →</b></span></a>')

def documento(titulo, descripcion, cuerpo, extra="", ruta=""):
    """Documento HTML completo y autónomo, listo para copiar a cualquier servidor."""
    return (f'<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>{html.escape(titulo)}</title>\n<meta name="description" content="{html.escape(descripcion)}">\n'
            f'{tarjeta(titulo, descripcion, ruta)}{HEAD}{extra}</head>\n<body>\n{AVISO_GIT}\n{cuerpo}\n</body>\n</html>\n')

YT = {"F-0014": "zOnJazksi08", "F-0015": "ErxVag75_mA", "F-0016": "anYgHKGhDWo",
      "F-0017": "dowYxCNXN7k", "F-0018": "PDYIvpms7r4", "F-0019": "-lKaALmO6ao",
      "F-0021": "SOkgIuhLvB4", "F-0022": "X_yghFec4j8"}
NOMBRE = {
    "F-0003": "Sitio oficial de la Asamblea", "F-0004": "Anteproyecto (PDF oficial)",
    "F-0006": "Aclaración de los autores (PDF)", "F-0007": "Moción oficial (PDF)",
    "F-0009": "La Abdón: moción filtrada", "F-0010": "La Abdón: qué se propone",
    "F-0011": "La Abdón: Decurnex y Aldabalde", "F-0012": "La Abdón: Singlet, Bardanca y Aldabalde",
    "F-0014": "Pasión Tricolor, Aldabalde (25/09)", "F-0015": "Territorio Nacional, Decurnex (21/09)",
    "F-0016": "El Espectador, Aldabalde (17/09)", "F-0017": "Pasión Tricolor, Singlet y Bardanca (24/09)",
    "F-0018": "El Espectador, Aldabalde (16/07)", "F-0019": "Pasión Tricolor, reacción a Decurnex (22/09)",
    "F-0021": "Pasión Tricolor, Gomensoro (30/09)", "F-0022": "Cuestión Stream, Decurnex (01/10)",
    "F-0023": "Moción de la agrupación Atilio García (imagen en X)",
}
URL = {
    "F-0003": "https://asambleagpc.nacional.uy/",
    "F-0004": "https://asambleagpc.nacional.uy/Anteproyecto.pdf",
    "F-0006": "https://asambleagpc.nacional.uy/InformacionAdicional1.pdf",
    "F-0023": "https://pbs.twimg.com/media/HTaL8_8WYAA7_1w?format=jpg&name=large",
    "F-0007": "https://asambleagpc.nacional.uy/Moci%C3%B3n%20Asamblea%20General%20Extraordinaria.pdf",
    "F-0009": "https://laabdon.com/noticias/se-filtro-la-mocion-del-master-plan-que-se-propone-votar-el-24-de-octubre",
    "F-0010": "https://laabdon.com/noticias/master-plan-del-gran-parque-central-que-se-propone-y-que-significa-para-nacional",
    "F-0011": "https://laabdon.com/noticias/el-futuro-del-gran-parque-central-que-propone-cada-uno-y-donde-estan-las-diferencias",
    "F-0012": "https://laabdon.com/noticias/master-plan-del-gpc-las-dudas-de-singlet-y-bardanca-y-las-respuestas-de-aldabalde-frente-a-frente",
}

# Diferencia entre la página impresa que se cita y la del visor del PDF (el anteproyecto no numera la portada).
PAGINA_VISOR = {"F-0004": 1}

# Fuentes que no son públicas: se citan con minuto, sin enlace.
PRIVADAS = {"F-0020": "Grabación del autor de la reunión informativa virtual del 30/09, cerrada a socios. No es pública."}

def ref(fid, ts=None, page=None):
    """Enlace a la fuente, al minuto exacto si es video."""
    if fid in PRIVADAS:
        label = fid + (f" · {ts}" if ts else "")
        return f'<span class="ref ref-priv" title="{html.escape(PRIVADAS[fid])}">{label}</span>'
    if ts and fid in YT:
        h, m, s = map(int, ts.split(":"))
        href = f"https://www.youtube.com/watch?v={YT[fid]}&t={h*3600+m*60+s}s"
        label = f"{fid} · {ts}"
    else:
        href = URL.get(fid, "#fuentes")
        label = fid + (f" · p. {page}" if page else "")
        if page and href.endswith(".pdf"):
            href += f"#page={int(page.split('-')[0]) + PAGINA_VISOR.get(fid, 0)}"
    return f'<a class="ref" href="{href}" target="_blank" rel="noopener" title="{html.escape(NOMBRE.get(fid, fid))}">{label}</a>'

def R(s):
    """Escapa el texto y reemplaza marcas: {F-0014 01:08:44} o {F-0004 p.42} por enlaces a la fuente,
    **negrita**, [[#id|texto]] por un enlace interno, [[>ruta|texto]] por un enlace a otra página y [[CG]] por la etiqueta de conocimiento general."""
    def sub(m):
        fid, rest = m.group(1), (m.group(2) or "").strip()
        if rest.startswith("p."):
            return ref(fid, page=rest[2:].strip())
        return ref(fid, rest or None)
    s = html.escape(s, quote=False)
    s = re.sub(r"\{(F-\d{4})\s*([^}]*)\}", sub, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[\[#([\w-]+)\|([^\]]+)\]\]", r'<a href="#\1">\2</a>', s)
    s = re.sub(r"\[\[&gt;([\w./#-]+)\|([^\]]+)\]\]", r'<a href="\1">\2</a>', s)  # [[>ruta|texto]], ya escapado
    s = s.replace("[[CG]]", '<span class="cg" title="Conocimiento general: no sale de una fuente registrada">conocimiento general</span>')
    return s

ESTADOS = {
    "coinciden": ("Coinciden en el dato", "ok"),
    "consistente": ("Consistente con documento", "ok"),
    "mocion": ("Consistente con la moción", "ok"),
    "atribucion": ("Atribución de prensa incorrecta", "bad"),
    "distintos": ("Mismo actor, dichos distintos", "warn"),
    "cuenta": ("La cuenta no cierra", "warn"),
    "parcial": ("Parcialmente consistente", "soft"),
    "pendiente": ("Pendiente", "pend"),
}
def compartir(texto, ruta=""):
    """Enlace para publicar en X (Twitter) con el texto y la dirección de la página. Sin JavaScript."""
    from urllib.parse import urlencode
    q = urlencode({"text": texto, "url": f"{SITIO}/{ruta}"})
    return f'<a class="share" href="https://x.com/intent/post?{html.escape(q)}" target="_blank" rel="noopener">Compartir en X</a>'

def chip(k):
    t, c = ESTADOS[k]
    return f'<span class="chip chip-{c}">{t}</span>'

# ---------- Preguntas ----------
PREGUNTAS = [
 dict(id="plata", q="¿Nacional pone plata en el proyecto?",
  pregunta=[("Conductor de El Espectador", "“Si Nacional no llega a esas cifras, las tiene que poner de su caja. Vos recién decís que no…”", "{F-0016 00:06:27}")],
  resp=[
   ("Aldabalde", "“Nacional no interviene un solo dólar, salvo el flujo de los palcos”, que “no está en los flujos recurrentes del club”. Al fideicomiso van palcos, sus gastos comunes y el Club Social.", "{F-0016 00:06:59} {F-0014 02:28:39}"),
   ("Decurnex", "21/09: “Nacional está poniendo 147 millones de dólares” de palcos, Club Social y gastos comunes. 30/09: esa plata “ya es de Nacional”, y propone guardarla “en un fideicomiso aparte” solo para el estadio, para no quedar “rehén” del financiamiento global.", "{F-0015 00:09:37} {F-0022 00:06:40} {F-0022 00:34:25}"),
   ("Gomensoro", "Que esos flujos vayan con destino exclusivo al estadio se agregó a la moción “a solicitud de José Decurnex”.", "{F-0021 00:01:04}"),
  ],
  estado=["coinciden", "mocion"],
  lectura="Hablan de los mismos flujos y con casi las mismas cifras (Aldabalde también da 93 M de palcos y unos 30 M del Club Social, {F-0014 01:44:58}). La moción oficial asigna al proyecto justamente esos flujos, y dice que los ya existentes solo pueden ir al estadio {F-0007 p.7}. En eso ya hay acuerdo. La diferencia que queda es de estructura: Decurnex quiere esa plata en un vehículo aparte, no en el mismo fideicomiso que paga la deuda de todo el proyecto {F-0022 00:34:25}."),
 dict(id="costo", q="¿Cuánto cuesta la obra?",
  pregunta=[("Conductor de El Espectador", "“El costo total está tasado en 112 millones, con el costo financiero se iría a 140…”", "{F-0016 00:06:27}")],
  resp=[
   ("Aldabalde", "16/07: “en torno a los 100 millones”. 17/09: “está en 112 millones de dólares”, con todas las actualizaciones. En la reunión informativa del 30/09: “de 93 estamos en 110”.", "{F-0018 00:07:58} {F-0016 00:07:30} {F-0020 00:13:57}"),
   ("Decurnex", "21/09: RDA estimó “arriba de los 150 millones”. 30/09: el proyecto completo va a estar “en el eje de los 150, 160 millones”, y una empresa de plaza les dio “una cotización de 170 millones con todos los recados”.", "{F-0015 00:08:11} {F-0022 00:05:09} {F-0022 00:35:55}"),
   ("Singlet", "El material entregado a la Directiva parte de 93 M y llega a 105 M, y “no incluye césped, equipamiento deportivo, honorarios de arquitectura e ingeniería, seguros de obra ni costos financieros durante la obra”.", "{F-0017 00:51:51}"),
   ("Gomensoro", "La primera presentación “llegaba a 110 millones”, y sobre eso “hay que hacer un ajuste de hasta 20%”.", "{F-0021 00:28:11}"),
  ],
  estado=["distintos", "pendiente"],
  lectura="Las cifras cambian con el tiempo de los dos lados: Aldabalde pasó de 112 a 110 M, Decurnex de “más de 150” a 150-170 M. Con el ajuste de hasta 20% que menciona Gomensoro, el lado oficial llega a unos 132 M (cuenta propia); el crítico arranca en 150. El “140 M” que La Abdón le atribuyó a Aldabalde lo dijo el entrevistador ({F-0016 00:06:27}). El anteproyecto no trae costos ({F-0004}). Falta el desglose de cada cifra y la cotización que cita Decurnex."),
 dict(id="cuota", q="¿Va a haber una cuota extra? ¿Es obligatoria?",
  pregunta=[("Conductor de Territorio Nacional", "“¿Eso es opcional, José, o es obligatorio?”", "{F-0015 00:13:25}"),
            ("Conductor de Pasión Tricolor", "“La cuota o el dinero este que tienen que sacar de los socios, ¿nunca va a ser obligatorio?”", "{F-0014 02:32:26}")],
  resp=[
   ("Aldabalde", "17/09: cuotas de 40, 50 o 100 pesos, voluntarias, “ni se habla de 10 dólares”. 25/09: los USD 10 por mes eran “una celda de un Excel” de marzo. 30/09: “siempre voluntarios”; uno de los modelos es un tercio de los socios con USD 10 por mes durante la obra.", "{F-0016 00:09:10} {F-0014 00:59:29} {F-0020 00:06:24}"),
   ("Gomensoro", "“Siempre va a ser voluntaria”, con el esquema del básquetbol: “por defecto quedás adentro, pero te podés bajar”, por ejemplo durante cinco años.", "{F-0021 00:20:03}"),
   ("Decurnex", "El modelo supone 26 M de aporte de socios, “que se dice que es voluntario, que no es voluntario”: ante un financiador “no hay otra que sea a través de una suba de cuota”. Suma 8,5 M pensados de exjugadores y glorias.", "{F-0022 00:04:09} {F-0022 00:04:39} {F-0015 00:14:44}"),
   ("Bardanca", "El financiador exige un aporte propio de 15 a 20% y no acepta que sea voluntario.", "{F-0017 00:54:19}"),
  ],
  estado=["distintos", "cuenta", "pendiente"],
  lectura="Los dos lados coinciden en que el modelo pide unos 26 M de aporte de socios; discrepan en si puede ser voluntario. Gomensoro agrega un dato nuevo: sería voluntaria, pero con permanencia por defecto, como la del básquetbol. Eso no es lo mismo que una cuota a la que hay que adherir. La moción no define el mecanismo ({F-0007 p.7}). Los componentes que da Decurnex suman 23,5 M, no 26 ({F-0015 00:14:05}). Se resuelve con el modelo económico, que todavía no está publicado ({F-0003})."),
 dict(id="570", q="¿El proyecto genera 570 millones de dólares?",
  pregunta=[("Conductor de Pasión Tricolor", "“Según Santiago Aldabalde, el proyecto generaría 570 millones de dólares. Pero dentro de esa cifra se incluyen los ingresos de tres renovaciones de palcos…”", "{F-0014 01:43:03}")],
  resp=[
   ("Aldabalde", "El fideicomiso genera 570 M en 30 años, más 150 M que van directo al club. Acepta el valor presente: “si esos 570 millones, sacando los palcos, son 82 hoy, los 94 de los palcos son 22”. El 30/09 agregó unos 5 M por año que irían directo al club desde que opera el estadio.", "{F-0016 00:05:03} {F-0014 01:44:58} {F-0020 00:26:42}"),
   ("Bardanca", "Sumar los ingresos de 30 años “es un error financiero grave y básico”. Traídos al presente, “esos 570 millones son 103 millones de dólares”, y además incluyen palcos, gastos comunes y Club Social, que existirían sin el proyecto.", "{F-0017 00:30:29} {F-0017 00:33:40}"),
   ("Decurnex", "“El dólar dentro de 30 años no tiene nada que ver con el dólar de hoy”: hay que traer los flujos a valor presente, y parte de ellos, unos 147 M, “ya son de Nacional”.", "{F-0022 00:12:02} {F-0022 00:12:32}"),
  ],
  estado=["coinciden"],
  lectura="Coinciden casi exactamente: 82 + 22 = 104 M según Aldabalde, 103 M según Bardanca. El desacuerdo es qué cifra comunicar y qué ingresos son propios del proyecto. Los 5 M por año fuera del fideicomiso que mencionó Aldabalde el 30/09 incluyen más entradas vendidas, pero en la misma reunión dijo que el modelo supone que no se vende “una entrada más” ({F-0020 00:50:28}); falta ver si son dos cuentas distintas."),
 dict(id="parking", q="¿El estacionamiento da ganancia?",
  pregunta=[("Conductor de Pasión Tricolor", "“Lo que generó ruido es lo del garage, los estacionamientos. Decime esa.”", "{F-0017 00:37:56}")],
  resp=[
   ("Singlet", "“980 plazas. El supuesto del proyecto es que hay una ocupación del 90% durante los 30 años.” Decurnex repitió el 30/09: “880 estacionamientos ocupados durante 30 años”.", "{F-0017 00:39:24} {F-0022 00:05:39}"),
   ("Bardanca", "Con el Excel de CPA y sin cambiar sus supuestos, el valor actual neto del estacionamiento da “menos siete millones de dólares”. La arena tampoco genera valor; el zócalo comercial sí.", "{F-0017 00:43:21} {F-0017 00:57:13}"),
   ("Aldabalde", "El 90% “es la curva de lo que le vamos a cobrar al operador”, no la ocupación; “es un negocio de 2 millones de dólares”. El 30/09: según CPA, es la unidad “menos rentable” pero “sigue siendo rentable”, y en el análisis por unidad “hubo un error en la asignación de los fondos” de inversión. Además, es obligatorio por norma municipal.", "{F-0014 01:11:08} {F-0014 01:13:45} {F-0020 00:30:55} {F-0020 00:31:08}"),
  ],
  estado=["pendiente", "cuenta"],
  lectura="Es un desacuerdo sobre qué dice el modelo, y se resuelve leyendo el documento. Aldabalde dice que el análisis negativo tenía un error en la asignación de la inversión, pero no dice de quién ni en qué documento. Además miden cosas distintas: valor actual neto de la inversión contra resultado anual. En la cuenta de Aldabalde del 25/09, 3 M con un castigo del 30% dan 2,1 M, no 2,5. Los 980 lugares sí están en el anteproyecto ({F-0004 p.42})."),
 dict(id="solo", q="¿Se puede terminar solo el estadio?",
  pregunta=[("Conductor de El Espectador", "“Hay plan B. El plan B, por ejemplo, es terminar exclusivamente el parque.”", "{F-0016 00:16:01}"),
            ("Conductor de Pasión Tricolor", "“¿Con los flujos de Nacional solamente construir el parque sin todos los negocios anexos, eso para vos es inviable?”", "{F-0014 02:14:26}")],
  resp=[
   ("Aldabalde", "“Para hacer el parque solo no dan los números.” Con los palcos hay 17 M en 10 años, unos 13 M a valor presente. El 30/09: “el parque solo no se puede hacer; se puede hacer […] un parche”, o ir “de a pedacitos” en “10, 15, 20 años”.", "{F-0016 00:16:13} {F-0014 02:14:43} {F-0020 00:42:23} {F-0020 00:43:04}"),
   ("Decurnex", "Un grupo de técnicos evaluó si el parque se puede terminar con los flujos propios del club: “la respuesta es que sí. Capaz que sin techo, seguramente sin techo”. Los demás negocios, con inversores y sin riesgo para el club.", "{F-0022 00:12:32} {F-0022 00:13:02} {F-0022 00:06:40}"),
   ("Bardanca", "Trabajan sobre el Excel de CPA con cambios, por ejemplo sin techo, y “tenemos indicios de que se podría llegar a estructurar”.", "{F-0017 01:20:05}"),
   ("Gomensoro", "Si no sale la moción principal, estaría dispuesto a considerar otro proyecto para el estadio, “porque yo quiero que haya obras y no necesariamente que incluyan todo”.", "{F-0021 00:17:48}"),
  ],
  estado=["pendiente"],
  lectura="Falta el análisis de CPA del escenario de solo estadio y la evaluación de los técnicos que cita Decurnex, que no está publicada. Las dos partes coinciden en que sin techo el problema cambia de escala: el techo es un 22 a 23% del costo según Aldabalde el 30/09 ({F-0020 00:08:26}), y 21,5 M según Singlet ({F-0017 01:41:45}). La moción alternativa de la agrupación Atilio García pide justamente analizar el estadio por separado y el techo aparte ({F-0023})."),
 dict(id="orden", q="¿Qué se hace primero?",
  pregunta=[("Conductor de Cuestión Stream", "“¿Se puede modificar el orden? […] para que en realidad sea el parque que se empiece a construir primero, en lugar de […] el estacionamiento.”", "{F-0022 00:22:02}")],
  resp=[
   ("Gomensoro", "Que primero van el estacionamiento o el zócalo es “una gran falacia”: el estudio “ordenó en 14 etapas […] pero no a título de secuencial”. La moción dice que “deberá priorizarse” el estadio.", "{F-0021 00:18:00} {F-0021 00:18:16} {F-0021 00:19:17}"),
   ("Decurnex", "“Yo creo que sí se puede” cambiar el orden. Hoy el estadio “empieza en la fase tres, fase cuatro”. Propone partir el proyecto “por unidades de negocio, no por fases arquitectónicas”, empezando por el estadio.", "{F-0022 00:22:30} {F-0022 00:23:00} {F-0022 00:36:28}"),
   ("Aldabalde", "Si hay financiamiento completo, “tratemos de hacer todo juntos, con la prioridad del estadio”.", "{F-0020 00:33:22}"),
  ],
  estado=["pendiente"],
  lectura="El anteproyecto empieza por el estacionamiento y el zócalo, y lo justifica por el equilibrio entre egresos e ingresos ({F-0004 p.38}); el techo va en las etapas 12 y 13 ({F-0004 p.41}). La moción pide priorizar el estadio “en función de los flujos y plazos disponibles” ({F-0007 p.6}). Las dos partes dicen que el estadio va primero; ningún documento fija el orden. Ver [[>../anteproyecto/#orden|el anteproyecto, etapa por etapa]]."),
 dict(id="sobrecosto", q="¿Qué pasa si la obra sale más cara?",
  pregunta=[("Conductor de El Espectador", "“El sobrecosto que puede tener, como tuvo el Camp Nou, como tuvo el Real Madrid, como tuvo el Antel Arena […] ¿quién se hace cargo?”", "{F-0016 00:23:57}")],
  resp=[
   ("Aldabalde", "“El fideicomiso es el responsable de toda la financiación.” En el peor caso, se tarda más en pagar: el primer modelo daba 10 años; con menos presión, 15.", "{F-0016 00:24:12} {F-0020 00:36:44}"),
   ("Decurnex", "“Tenés que extender el tiempo de repago, es la única alternativa”; el repago va a estar “más cerca de los 15” años. El Club Social se planteó en 4 M y costó unos 6,5 M. Hay que prever “entre un 15, 18%” de imprevistos.", "{F-0022 00:29:46} {F-0022 00:31:17} {F-0022 00:35:25}"),
   ("Gomensoro", "“Estaremos más tiempo en la duración del fideicomiso”, como en el Club Social, que “se iba a pagar en cuatro años y van ocho”.", "{F-0021 00:12:01} {F-0021 00:29:25}"),
   ("Bardanca", "Estadios como el Real Madrid o el Barcelona tuvieron desvíos del 50 o 60%: “Nosotros un desvío de obra del 60% no lo resistimos.”", "{F-0017 01:08:11}"),
  ],
  estado=["coinciden", "mocion", "pendiente"],
  lectura="Las dos partes coinciden en qué pasa: se estira el repago, a unos 15 años. Según la moción, el club no aporta capital para sobrecostos {F-0007 p.7} y ninguna etapa empieza sin financiamiento para completarla {F-0007 p.7}. La diferencia es qué arriesga el club mientras tanto: para Decurnex, los flujos propios quedan atados al financiamiento global {F-0022 00:34:25}. Decurnex bajó su previsión de imprevistos de 20-25% ({F-0015 00:36:50}) a 15-18%."),
 dict(id="voto", q="¿Qué se vota el 24 de octubre y con qué mayoría?",
  pregunta=[("Conductor de Territorio Nacional", "“La Asamblea, ¿para qué sirve?”", "{F-0015 00:21:40}"),
            ("Oyente, leído en Pasión Tricolor", "“Si se aprueba por el 75% o por el 50 más 1. Que hay un debate ahí.”", "{F-0014 02:12:06}")],
  resp=[
   ("Gomensoro", "Rige el Estatuto vigente, 50% más uno: una moción que pida el 75% “no tiene valor alguno”. Ve muy difícil que la reforma esté vigente el 24/10. Si hay dos mociones contradictorias, se votan en orden y, si sale la primera, la otra no se vota.", "{F-0021 00:59:59} {F-0021 01:00:48} {F-0021 00:15:13}"),
   ("Aldabalde", "La Asamblea “aprueba el master plan y aprueba un sistema de trabajo”. El 30/09: la reforma pide 75% para proyectos de más de 2,5 M, no rige hasta que la apruebe el MEC, y “capaz que hay que hacer otra asamblea cuando realmente se apruebe la ejecución”; dijo que eso lo tienen que responder los abogados.", "{F-0014 01:56:05} {F-0020 00:17:00} {F-0020 00:18:19}"),
   ("Decurnex", "Reconoce que la reforma difícilmente esté vigente, pero el 75% es “un tema de conciencia”. Cada etapa “tiene que pasar necesariamente por asamblea”.", "{F-0022 00:21:13} {F-0022 00:20:12}"),
   ("Singlet", "La reforma del 7 de julio fijó el 75% para proyectos de más de USD 2 M.", "{F-0017 00:05:19}"),
  ],
  estado=["coinciden", "pendiente"],
  lectura="Todos coinciden en que la reforma existe y no rige. El desacuerdo es jurídico y de valores. La moción no fija la mayoría de la Asamblea; se remite a los Estatutos “sin perjuicio de cualquier exigencia estatutaria más rigurosa que resulte vigente” {F-0007 p.5}. Para las decisiones de la Directiva pide unanimidad de los once {F-0007 p.8}; según Gomensoro, el 9 de 11 pasó a 11 de 11 el 29/09, en la misma sesión en que se votó 7 a 4 {F-0021 00:02:05}. El umbral de la reforma no coincide entre los actores: 2 M, 2,5 M o “2 millones de UI”."),
]

# ---------- Contrapunto ----------
FILAS = [
 ("¿Pone plata Nacional?", "coinciden", "#plata"),
 ("Fideicomiso único o aparte para los flujos del estadio", "pendiente", "#plata"),
 ("570 M: nominal y valor presente", "coinciden", "#570"),
 ("Costo de la obra", "distintos", "#costo"),
 ("“140 M con costo financiero”", "atribucion", "#costo"),
 ("Costo del proyecto ejecutivo: 2,5 M", "atribucion", None),
 ("Proyecto ejecutivo antes de votar", "mocion", None),
 ("Aporte de socios voluntario", "pendiente", "#cuota"),
 ("Sobrecuota con permanencia por defecto", "pendiente", "#cuota"),
 ("Los USD 10 por mes", "distintos", "#cuota"),
 ("Cuentas de los 26 M y del estacionamiento", "cuenta", None),
 ("Ocupación y valor del estacionamiento", "pendiente", "#parking"),
 ("Ocupación comercial de 97,5%", "pendiente", None),
 ("Superficie del zócalo comercial", "parcial", None),
 ("Mantenimiento: 1,2 M hoy", "coinciden", None),
 ("“10 mil butacas nuevas”", "parcial", None),
 ("Solo estadio", "pendiente", "#solo"),
 ("¿Qué se hace primero?", "pendiente", "#orden"),
 ("Repago si los negocios rinden menos", "coinciden", "#sobrecosto"),
 ("Imprevistos: 20-25% o 15-18%", "distintos", "#sobrecosto"),
 ("Informe de CPA “lapidario”", "pendiente", None),
 ("Garantías de la moción", "mocion", None),
 ("Mayoría especial de la Directiva", "mocion", None),
 ("Mayoría del 75%", "coinciden", "#voto"),
 ("Umbral de la reforma del Estatuto", "distintos", "#voto"),
]
NOTAS = {
 "Fideicomiso único o aparte para los flujos del estadio": "La moción reserva los flujos propios para el estadio dentro del mismo fideicomiso {F-0007 p.6-7}. Decurnex quiere un vehículo aparte para no quedar “rehén” del financiamiento global {F-0022 00:34:25}. Según Gomensoro, el destino exclusivo se agregó a pedido de Decurnex {F-0021 00:01:04}.",
 "Costo del proyecto ejecutivo: 2,5 M": "La Abdón publicó 2,5 M; Aldabalde dijo “del entorno de los 2 millones” {F-0016 00:21:22}. Decurnex: “un par de millones de dólares” {F-0022 00:02:46}; Gomensoro: “dos millones de dólares” como mínimo {F-0021 00:13:37}.",
 "Proyecto ejecutivo antes de votar": "La moción exige ejecutivo antes de cada etapa, no antes de la Asamblea {F-0007 p.7}. La moción alternativa lo pone primero, en 180 días {F-0023}. Es un desacuerdo de valores sobre qué hay que saber antes de votar.",
 "Sobrecuota con permanencia por defecto": "Gomensoro: “por defecto quedás adentro, pero te podés bajar” {F-0021 00:20:03}. La moción no define el mecanismo {F-0007 p.7}. Decurnex: ante un financiador “no hay otra que sea a través de una suba de cuota” {F-0022 00:04:39}.",
 "Ocupación comercial de 97,5%": "Bardanca {F-0017 01:16:57} y Decurnex {F-0022 00:05:39}; Aldabalde: “100% alquilado, con precontratos” {F-0014 01:08:44}. Falta el modelo.",
 "Superficie del zócalo comercial": "Aldabalde habla de modelos de 3.500 y 7.000 m² {F-0014 01:08:14}; el anteproyecto da 3.080 m² de locales comerciales y 14.266 m² de superficies rentables {F-0004 p.42}.",
 "Mantenimiento: 1,2 M hoy": "Singlet, último balance: 1,2 M bruto {F-0017 01:31:00}. Aldabalde el 30/09: 1,2 M “sin inversión” {F-0020 00:27:00}; el 17/09 había hablado de un ahorro de 3 o 4 M por año {F-0016 00:06:05}, que puede incluir la inversión postergada.",
 "“10 mil butacas nuevas”": "Aldabalde {F-0014 01:52:45}. Sumando las etapas del anteproyecto salen 10.116 y el aforo pasa de unos 34.000 a más de 43.000 {F-0004 p.64}, pero la misma memoria da 16.544 butacas nuevas en total {F-0004 p.42}. Ver [[>../anteproyecto/#cuentas|las cuentas del anteproyecto]].",
 "Informe de CPA “lapidario”": "Aldabalde lo anunció así {F-0016 00:16:50}. En un mail leído al aire, un socio de CPA escribe que “no es lapidario ni pretende serlo” {F-0017 00:47:34}. Para Decurnex, “la palabra avalar es muy determinante”: CPA armó el modelo con datos de Nacional {F-0022 00:40:17}. Falta el informe.",
 "Cuentas de los 26 M y del estacionamiento": "Los componentes que da Decurnex suman 23,5 M, no 26 {F-0015 00:13:06}; en el estacionamiento, 3 M con un castigo del 30% dan 2,1 M, no 2,5 {F-0014 01:13:45}. Ver [[#cuota|la cuota]] y [[#parking|el estacionamiento]].",
 "Imprevistos: 20-25% o 15-18%": "Decurnex dijo 20 a 25% el 21/09 {F-0015 00:36:50} y 15 a 18% el 30/09 {F-0022 00:35:25}. Gomensoro habla de un ajuste de hasta 20% sobre 110 M {F-0021 00:28:17}.",
 "Garantías de la moción": "Fideicomiso separado, sin hipoteca ni deuda del club, unanimidad de la Directiva para las decisiones centrales, vuelta a la Asamblea ante cambios sustanciales y plazo de 30 meses {F-0007 p.6-9}. Un conductor de Pasión Tricolor pide sanciones para quien incumpla {F-0014 01:58:43}; Gomensoro acompañaría una moción complementaria con responsabilidad personal de los dirigentes {F-0021 00:50:40}. Qué cubre un sobrecosto: [[#sobrecosto|la pregunta del sobrecosto]].",
 "Mayoría especial de la Directiva": "La moción pide el voto unánime de los once directivos {F-0007 p.8}. Según Gomensoro, pasó de 9 a 11 el 29/09 {F-0021 00:02:05}. Si no hay unanimidad y la mayoría simple quiere seguir, decide una nueva Asamblea en 30 días.",
 "Umbral de la reforma del Estatuto": "Singlet: más de USD 2 M {F-0017 00:05:19}. Aldabalde: 2,5 M {F-0020 00:17:00}. Decurnex: “2 millones de UI, que estamos hablando de 3 millones de dólares” {F-0022 00:19:41}, una cuenta que no parece cerrar. Falta el texto de la reforma.",
}

COINCIDEN = [
 ("Ingresos a valor presente", "unos 104 M según Aldabalde; 103 M según Bardanca", "{F-0014 01:44:58} {F-0017 00:31:30}"),
 ("Palcos en 30 años", "93 M, con renovaciones que vencen en distintas fechas", "{F-0015 00:09:37} {F-0014 01:44:58} {F-0020 00:29:40}"),
 ("Flujos propios solo para el estadio", "lo dice la moción y lo piden los críticos", "{F-0007 p.7} {F-0021 00:01:04} {F-0022 00:06:40}"),
 ("Repago si los negocios rinden menos", "se estira, a unos 15 años", "{F-0022 00:29:46} {F-0020 00:36:44}"),
 ("Proyecto ejecutivo", "cuesta unos 2 M", "{F-0016 00:21:22} {F-0022 00:02:46} {F-0021 00:13:37}"),
 ("Techo", "unos 20 M o un 22 a 23% según Aldabalde; 21,5 M según Singlet", "{F-0014 00:53:46} {F-0020 00:08:26} {F-0017 01:41:45}"),
 ("Aporte de socios en el modelo", "unos 26 M", "{F-0014 01:06:00} {F-0022 00:04:09}"),
 ("Reforma del Estatuto (75%)", "existe y todavía no rige", "{F-0014 02:16:38} {F-0021 01:00:48} {F-0022 00:21:13}"),
 ("Pasivo del club", "entre 36 y 40 M", "{F-0014 01:48:47} {F-0015 00:33:36}"),
 ("Ingresos de los negocios", "los modeló la CPO; CPA arma el modelo con esos insumos", "{F-0015 00:19:01} {F-0014 01:15:43} {F-0022 00:40:17}"),
 ("Objetivo", "terminar el estadio, con el Mundial 2030 como oportunidad", "{F-0016 00:14:00} {F-0015 00:33:02} {F-0017 01:20:05} {F-0017 01:35:00}"),
]

FALTA = [
 ("Modelo económico financiero", "Costo vigente, cuota, aporte voluntario, supuestos comerciales. Según Aldabalde, CPA está agregando los análisis que pidió la Directiva"),
 ("Votación de la Directiva sobre la moción", "Acta: 7 a 4 según Gomensoro"),
 ("Versión revisada de la moción alternativa", "Si incluye el 75% y una Asamblea por etapa, como dice Decurnex"),
 ("Material entregado a la Directiva el 11/03/2026", "Qué incluye el costo, ocupación del estacionamiento, techo"),
 ("Excel de CPA “evaluación unidad de negocio v3” e informe de CPA", "Valor de cada negocio, el “error en la asignación”, solo estadio"),
 ("Cotizaciones de RDA y de la empresa de plaza", "Costo de 150 a 170 M"),
 ("Evaluación de los técnicos de Decurnex", "Estadio con flujos propios, sin techo"),
 ("Texto de la reforma del Estatuto", "Mayoría del 75% y umbral"),
 ("Último balance del club", "Mantenimiento y pasivo"),
]

POSTURAS = [
 ("Santiago Aldabalde", "Presidente de la CPO · postura oficialista",
  "El Master Plan es la única forma de terminar el estadio y cambiar la economía del club. Cinco hectáreas en el centro de Montevideo que hoy rinden casi solo los días de partido pueden pagar la obra con arena, estacionamiento, zócalo comercial y plaza. El riesgo queda en un fideicomiso: sin hipotecas, sin deuda del club y sin empezar ninguna etapa sin financiamiento. Si los números salen peor, se estira el repago. Costo estimado: unos 110 M.",
  "{F-0014 00:50:14} {F-0016 00:02:32} {F-0020 00:04:16} {F-0020 00:36:44}"),
 ("Javier Gomensoro", "Prosecretario de la Directiva · corredactor de la moción",
  "Con la moción “el club no arriesga, el club está blindado”. Exigir primero un proyecto ejecutivo de 2 M sin inversor es “un entierro de lujo”. Como miembro informante de la reforma del Estatuto, sostiene que rige el 50% más uno. Acompañaría sanciones para dirigentes que se aparten de la moción.",
  "{F-0021 00:08:00} {F-0021 00:13:37} {F-0021 00:59:59} {F-0021 00:50:40}"),
 ("José Decurnex", "Vocal de la Directiva · votó contra la moción",
  "Lo que quieren los socios es el estadio, y ahí deben ir los recursos del club: unos 147 M en 30 años, en un fideicomiso aparte. Los negocios complementarios, con inversores y sin riesgo para el club, evaluados uno por uno. El proyecto completo costaría entre 150 y 170 M; sin proyecto ejecutivo no hay costo cierto. Apoya la moción alternativa y pide el 75%, aunque busca una moción única.",
  "{F-0022 00:06:40} {F-0022 00:05:09} {F-0022 00:17:02} {F-0022 00:21:13}"),
 ("Enrique Singlet y Joaquín Bardanca", "Contadores · agrupación Atilio García",
  "Crítica técnica sobre los documentos de CPA: los 570 M son nominales; con los propios supuestos de CPA, el estacionamiento y la arena no generan valor; el costo de 105 M deja rubros afuera; un financiador no acepta un aporte voluntario. Su agrupación presentó una moción alternativa: proyecto ejecutivo primero, con el estadio y el techo por separado.",
  "{F-0017 00:11:21} {F-0017 01:24:00} {F-0023}"),
 ("Tatiana Villaverde", "Contadora de la Directiva",
  "El dinero genuino del club debe ir al estadio; las unidades de negocio, a inversores externos a su riesgo, con concesiones temporales como la del restaurante o la tienda. (Mensaje leído al aire.)",
  "{F-0014 01:24:49}"),
]

FUENTES = ["F-0003", "F-0004", "F-0007", "F-0011", "F-0012", "F-0014", "F-0015", "F-0016", "F-0017", "F-0018", "F-0019", "F-0020", "F-0021", "F-0022", "F-0023"]

def src_link(fid):
    if fid in PRIVADAS:
        return f'<span>{html.escape(PRIVADAS[fid])}</span>'
    if fid in YT:
        return f'<a href="https://www.youtube.com/watch?v={YT[fid]}" target="_blank" rel="noopener">{NOMBRE[fid]}</a>'
    return f'<a href="{URL[fid]}" target="_blank" rel="noopener">{NOMBRE[fid]}</a>'

out = []
A = out.append
A('<main class="wrap">')
A('''<header class="hero">
  <a class="back" href="../">← La moción, artículo por artículo</a> · <a class="back" href="../anteproyecto/">El anteproyecto, etapa por etapa</a>
  <p class="eyebrow">Gran Parque Central · Master Plan · El debate</p>
  <h1>Qué dice cada uno, y qué se puede comprobar</h1>
  <p class="lede">Las preguntas centrales del debate, con las respuestas de cada parte y un enlace al minuto exacto en que se dijo cada cosa. Donde hay un documento, se contrasta con él.</p>
  <dl class="facts">
    <div><dt>Asamblea</dt><dd>24 de octubre de 2026, 10:00 · Polideportivo</dd></div>
    <div><dt>Estado</dt><dd>Preliminar · actualizado el ''' + ACTUALIZADO + '''</dd></div>
    <div><dt>Falta publicar</dt><dd>Modelo económico</dd></div>
  </dl>
  <nav class="toc" aria-label="Secciones">
    <a href="#preguntas">Preguntas</a><a href="#posturas">Posturas</a><a href="#coinciden">En qué coinciden</a><a href="#contrapunto">Contrapunto</a><a href="#falta">Qué falta</a><a href="#fuentes">Fuentes</a>
  </nav>
  <div class="acciones">''' + compartir("Master Plan del Gran Parque Central: qué dice cada uno y qué se puede comprobar, con el minuto exacto de cada cita.", "debate/") + '''</div>
</header>''')

# Preguntas
A('<section id="preguntas" class="sec"><h2>Las preguntas más importantes</h2>')
A('<p class="sec-intro">Cada pregunta indica dónde se hizo. Cada respuesta enlaza al video en el minuto justo. Las citas salen de transcripciones automáticas: escuchá el tramo antes de citarlo.</p>')
for p in PREGUNTAS:
    A(f'<article class="q" id="{p["id"]}"><h3>{html.escape(p["q"])}</h3>')
    A('<div class="asked"><span class="label">Dónde se preguntó</span><ul>')
    for who, txt, r in p["pregunta"]:
        A(f'<li><span class="who">{who}:</span> {html.escape(txt)} {R(r)}</li>')
    A('</ul></div><div class="answers">')
    for who, txt, r in p["resp"]:
        A(f'<div class="ans"><p class="ans-who">{who}</p><p class="ans-txt">{html.escape(txt)}</p><p class="ans-ref">{R(r)}</p></div>')
    A('</div>')
    A(f'<div class="verdict"><div class="chips">{"".join(chip(e) for e in p["estado"])}</div><p>{R(p["lectura"])}</p></div>')
    A(f'<a class="more" href="detalle-{p["id"]}.html">Ver en detalle: qué piensa cada uno, en qué se apoya y análisis</a></article>')
A('</section>')

# Posturas
A('<section id="posturas" class="sec"><h2>Las posturas</h2><div class="posturas">')
for n, rol, txt, r in POSTURAS:
    A(f'<article class="post"><h3>{n}</h3><p class="rol">{rol}</p><p>{html.escape(txt)}</p><p class="ans-ref">{R(r)}</p></article>')
A('</div></section>')

# Coinciden
A('<section id="coinciden" class="sec"><h2>En qué coinciden</h2><p class="sec-intro">En los datos centrales, las dos partes dan cifras iguales o muy cercanas. La discusión es sobre cómo leerlas y cuánto riesgo aceptar.</p><dl class="coin">')
for t, v, r in COINCIDEN:
    A(f'<div><dt>{t}</dt><dd>{html.escape(v)} <span class="refs">{R(r)}</span></dd></div>')
A('</dl></section>')

# Contrapunto
A('<section id="contrapunto" class="sec"><h2>Contrapunto</h2><p class="sec-intro">Estado de cada tema según lo que se puede comprobar hoy. Las definiciones de cada estado están al pie.</p><div class="table-wrap"><table><thead><tr><th scope="col">Tema</th><th scope="col">Estado</th><th scope="col">Detalle</th></tr></thead><tbody>')
for t, e, anchor in FILAS:
    det = R(NOTAS[t]) if t in NOTAS else (f'<a href="{anchor}">Ver la pregunta</a>' if anchor else "")
    A(f'<tr><th scope="row">{t}</th><td>{chip(e)}</td><td>{det}</td></tr>')
A('</tbody></table></div>')
A('''<dl class="legend">
<div><dt>''' + chip("coinciden") + '''</dt><dd>Las dos partes dan la misma cifra.</dd></div>
<div><dt>''' + chip("consistente") + '''</dt><dd>Lo confirma un documento oficial registrado.</dd></div>
<div><dt>''' + chip("mocion") + '''</dt><dd>Lo confirma el texto oficial de la moción.</dd></div>
<div><dt>''' + chip("atribucion") + '''</dt><dd>La fuente original no dice lo que publicó un medio.</dd></div>
<div><dt>''' + chip("distintos") + '''</dt><dd>La misma persona dijo cosas distintas en fechas distintas. No implica que sea falso: la información puede haber cambiado.</dd></div>
<div><dt>''' + chip("cuenta") + '''</dt><dd>La cifra dicha no coincide con sus propios componentes.</dd></div>
<div><dt>''' + chip("parcial") + '''</dt><dd>Una parte coincide con un documento y otra no se puede comprobar.</dd></div>
<div><dt>''' + chip("pendiente") + '''</dt><dd>Falta el documento que lo resuelve.</dd></div>
</dl></section>''')

# Falta
A('<section id="falta" class="sec"><h2>Qué falta para verificar</h2><ul class="falta">')
for d, r in FALTA:
    A(f'<li><strong>{d}</strong><span>{r}</span></li>')
A('</ul></section>')

# Fuentes
A('<section id="fuentes" class="sec"><h2>Fuentes</h2><p class="sec-intro">Cada código (F-0014, etc.) es la ficha de la fuente en el repositorio del proyecto. Los enlaces con minuto abren el video en ese punto.</p><ul class="fuentes">')
for f in FUENTES:
    A(f'<li><span class="code">{f}</span>{src_link(f)}</li>')
A('</ul></section>')

A('''<footer class="foot"><p>Proyecto de verificación del debate sobre el Master Plan del Gran Parque Central, el primer estadio mundialista. Hecho por Santiago Trias, socio de Nacional (n.º 55554), con asistencia de Claude. Método: se separan hechos, estimaciones y opiniones; se aplica la misma vara a todos, incluida la directiva; ninguna cifra se da sin fuente. Fuentes, método e historial de cambios: <a href="https://github.com/strias/masterplan-gpc">repositorio en GitHub</a>.</p></footer></main>''')

os.makedirs("debate", exist_ok=True)
open("debate/index.html", "w").write(documento(TITULO, DESCRIPCION, "\n".join(out), '<style>.back { font-family: var(--f-mono); font-size: .82rem; }</style>', "debate/"))

from detalle import DETALLE
EXTRA = """<style>
.back { font-family: var(--f-mono); font-size: .82rem; }
.lado { background: var(--surface); border: 1px solid var(--line); padding: 18px; display: flex; flex-direction: column; gap: 10px; min-width: 0; }
.lado h3 { font-size: 1.35rem; }
.lado .tesis { font-family: var(--f-display); font-size: 1.2rem; color: var(--red); text-transform: uppercase; letter-spacing: .02em; }
.porque { border-top: 1px dashed var(--line); padding-top: 10px; color: var(--muted); font-size: .95rem; }
.porque b { font-family: var(--f-mono); font-size: .72rem; text-transform: uppercase; letter-spacing: .08em; color: var(--ink); font-weight: 500; margin-right: 6px; }
.lados { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }
.analisis { background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--red); padding: 20px; display: flex; flex-direction: column; gap: 14px; }
.analisis .aviso { font-size: .92rem; color: var(--muted); }
.cg { font-family: var(--f-mono); font-size: .66rem; text-transform: uppercase; letter-spacing: .06em; background: transparent; color: var(--muted); border: 1px dashed currentColor; padding: 0 5px; border-radius: 3px; white-space: nowrap; }
.lectura { font-size: 1.15rem; border-left: 4px solid var(--navy); padding-left: 14px; max-width: 64ch; }
.res { margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 4px; }
.pager { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px; font-family: var(--f-mono); font-size: .82rem; border-top: 1px solid var(--line); padding-top: 16px; }
</style>"""
ids = [p["id"] for p in PREGUNTAS]
for i, p in enumerate(PREGUNTAS):
    d = DETALLE[p["id"]]
    o = []
    o.append('<main class="wrap">')
    o.append(f'<header class="hero"><a class="back" href="index.html">← Volver al debate</a><p class="eyebrow">Master Plan GPC · Pregunta en detalle</p><h1>{html.escape(d["titulo"])}</h1><p class="lede">{R(d["corto"])}</p><div class="chips">{"".join(chip(e) for e in p["estado"])}</div></header>')
    o.append('<section class="sec"><h2>Qué dice cada uno</h2><div class="lados">')
    for who, tesis, txt, porque in d["posturas"]:
        o.append(f'<article class="lado"><h3>{who}</h3><p class="tesis">{html.escape(tesis)}</p><p>{R(txt)}</p><p class="porque"><b>Por qué lo dice</b>{R(porque)}</p></article>')
    o.append('</div></section>')
    o.append('<section class="sec"><h2>Análisis</h2><div class="analisis"><p class="aviso">Este análisis es de Claude, la IA que asiste al proyecto, y es opinión. Se apoya en las fuentes enlazadas y, donde lo indica la etiqueta <span class="cg">conocimiento general</span>, en conocimiento general de finanzas y obras que no sale de una fuente registrada. Las cuentas propias usan solo cifras dichas por las partes.</p>')
    for par in d["analisis"]:
        o.append(f'<p>{R(par)}</p>')
    o.append('</div></section>')
    o.append(f'<section class="sec"><h2>En resumen</h2><p class="lectura">{R(d["lectura"])}</p></section>')
    o.append('<section class="sec"><h2>Qué lo resolvería</h2><ul class="res">' + "".join(f"<li>{html.escape(x)}</li>" for x in d["resolveria"]) + '</ul></section>')
    prev = f'<a href="detalle-{ids[i-1]}.html">← {html.escape(DETALLE[ids[i-1]]["titulo"])}</a>' if i > 0 else '<span></span>'
    nxt = f'<a href="detalle-{ids[i+1]}.html">{html.escape(DETALLE[ids[i+1]]["titulo"])} →</a>' if i + 1 < len(ids) else '<a href="index.html">Volver al debate</a>'
    o.append(f'<div class="acciones">{compartir(d["titulo"] + " Qué dice cada parte y en qué se apoya, con fuentes.", "debate/detalle-" + p["id"] + ".html")}</div>')
    o.append(f'<nav class="pager">{prev}{nxt}</nav>')
    o.append(f'<footer class="foot"><p>Preliminar, al {ACTUALIZADO}. Las citas salen de transcripciones automáticas: escuchá el tramo enlazado antes de citarlo. Los veredictos formales siguen pendientes hasta tener el modelo económico. Fuentes y método: <a href="https://github.com/strias/masterplan-gpc">repositorio en GitHub</a>.</p></footer></main>')
    descripcion = f'{d["titulo"]} Qué dice cada parte, en qué se apoya y análisis, en el debate sobre el Master Plan del Gran Parque Central.'
    open(f"debate/detalle-{p['id']}.html", "w").write(documento(d["titulo"], descripcion, "\n".join(o), EXTRA, f"debate/detalle-{p['id']}.html"))
print("detalles:", len(ids))
print("ok", sum(len(x) for x in out))

# ---------- Portada: la moción ----------
import mocion as M

def chip_resp(k):
    t, c = M.RESPUESTAS[k]
    return f'<span class="chip chip-{c}">{t}</span>'

PORTADA_CSS = """<style>
.cg { font-family: var(--f-mono); font-size: .66rem; text-transform: uppercase; letter-spacing: .06em; background: transparent; color: var(--muted); border: 1px dashed currentColor; padding: 0 5px; border-radius: 3px; white-space: nowrap; }
.obra { margin: 0; padding-left: 26px; display: flex; flex-direction: column; gap: 8px; max-width: 70ch; }
.obra li::marker { font-family: var(--f-mono); color: var(--red); }
.aparte { border: 1px dashed var(--line); padding: 20px; background: var(--surface); }
.aviso-alt { border-left: 4px solid var(--red); padding-left: 12px; max-width: 70ch; }
.corto { margin: 0; padding-left: 22px; display: flex; flex-direction: column; gap: 10px; max-width: 70ch; }
.arts { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; }
.art { display: grid; grid-template-columns: 110px 1fr; gap: 14px; padding: 14px 0; border-bottom: 1px solid var(--line); }
.art .num { font-family: var(--f-display); font-size: 1.3rem; text-transform: uppercase; color: var(--red); line-height: 1.1; }
.art h3 { font-size: 1.25rem; }
.art div { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.art .more { margin-top: 2px; }
.resp { display: flex; flex-direction: column; gap: 12px; }
.resp article { background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--navy); padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; }
.resp h3 { font-size: 1.25rem; }
.resp h3 a { color: inherit; text-decoration-thickness: 1px; }
.analisis { background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--red); padding: 20px; display: flex; flex-direction: column; gap: 14px; }
.analisis .aviso { font-size: .92rem; color: var(--muted); }
.lectura { font-size: 1.15rem; border-left: 4px solid var(--navy); padding-left: 14px; max-width: 64ch; }
.cta { display: inline-block; align-self: flex-start; font-family: var(--f-mono); font-size: .85rem; background: var(--navy); color: var(--bg); padding: 8px 14px; border-radius: 3px; text-decoration: none; }
.cta:hover { text-decoration: underline; }
@media (max-width: 560px) { .art { grid-template-columns: 1fr; gap: 4px; } }
</style>"""

o = []
P = o.append
P('<main class="wrap">')
P('''<header class="hero">
  <p class="eyebrow">Gran Parque Central · Master Plan · Asamblea del 24 de octubre</p>
  <h1>Qué se vota el 24 de octubre</h1>
  <p class="lede">El 29 de septiembre el club publicó la moción que considera la Asamblea General Extraordinaria. Acá está artículo por artículo, con la página de cada cita, qué responde a las preguntas del debate y qué deja abierto.</p>
  <dl class="facts">
    <div><dt>Asamblea</dt><dd>24 de octubre de 2026, 10:00 · Polideportivo</dd></div>
    <div><dt>Moción</dt><dd>''' + R("Publicada el 29/09/2026 · 9 páginas {F-0007}") + '''</dd></div>
    <div><dt>Estado</dt><dd>Preliminar · actualizado el ''' + ACTUALIZADO + '''</dd></div>
  </dl>
  <nav class="toc" aria-label="Secciones">
    <a href="#resumen">En resumen</a><a href="#obra">Para que empiece la obra</a><a href="#articulos">Artículo por artículo</a><a href="#debate">Y el debate</a><a href="#no-dice">Qué no dice</a><a href="#hechos">Datos por verificar</a><a href="#analisis">Análisis</a><a href="#otra-mocion">Aparte: otra moción</a><a href="#fuentes">Fuentes</a>
  </nav>
  <div class="acciones"><a class="cta" href="debate/">El debate: qué dice cada uno →</a><a class="cta" href="anteproyecto/">El anteproyecto: qué se construye y en qué orden →</a>''' + compartir("¿Qué se vota el 24 de octubre? La moción del Master Plan del Gran Parque Central, artículo por artículo y con la fuente de cada dato.") + '''</div>
</header>''')

P('<section id="resumen" class="sec"><h2>En resumen</h2><ul class="corto">')
for x in M.EN_CORTO:
    P(f'<li>{R(x)}</li>')
P('</ul></section>')


P('<section id="obra" class="sec"><h2>Qué tiene que pasar para que empiece la obra</h2><p class="sec-intro">Según la moción, todo esto, y se repite en cada etapa.</p><ol class="obra">')
for t, x in M.OBRA:
    P(f'<li><strong>{html.escape(t)}:</strong> {R(x)}</li>')
P(f'</ol><p class="sec-intro">{R(M.OBRA_PLAZO)}</p>')
P('<h3>¿Vuelve a votar la Asamblea?</h3><p>Solo en estos casos:</p><ul class="falta">')
for t, r in M.VUELVE:
    P(f'<li><strong>{html.escape(t)}</strong><span>{R(r)}</span></li>')
P(f'</ul><p class="sec-intro">{R(M.VUELVE_NOTA)}</p></section>')

P('<section id="articulos" class="sec"><h2>Artículo por artículo</h2><p class="sec-intro">La parte que se vota es la resolución, en diez artículos. Resumen propio; cada enlace abre la página del PDF oficial.</p><ol class="arts">')
for num, tit, txt, pag, deb in M.ARTICULOS:
    link = f'<a class="more" href="debate/detalle-{deb[0]}.html">En el debate: {html.escape(deb[1])}</a>' if deb else ""
    P(f'<li class="art"><span class="num">{num}</span><div><h3>{html.escape(tit)}</h3><p>{R(txt)} {R("{F-0007 " + pag + "}")}</p>{link}</div></li>')
P('</ol></section>')

P('<section id="debate" class="sec"><h2>Qué responde a las preguntas del debate</h2><p class="sec-intro">Las preguntas son las del <a href="debate/">contrapunto</a>. Cada una enlaza a su página de detalle.</p><div class="resp">')
for pid, q, k, txt in M.DEBATE:
    P(f'<article><h3><a href="debate/detalle-{pid}.html">{html.escape(q)}</a></h3><div class="chips">{chip_resp(k)}</div><p>{R(txt)}</p></article>')
P('</div></section>')

P('<section id="no-dice" class="sec"><h2>Qué no dice</h2><ul class="falta">')
for t, x in M.NO_DICE:
    P(f'<li><strong>{html.escape(t)}</strong><span>{R(x)}</span></li>')
P('</ul></section>')

P('<section id="hechos" class="sec"><h2>Datos de la moción, por verificar</h2><p class="sec-intro">Los antecedentes de la moción traen afirmaciones de hecho. Se verifican como cualquier otra, con la misma vara para el club.</p><div class="table-wrap"><table><thead><tr><th scope="col">Dato</th><th scope="col">Estado</th><th scope="col">Contraste</th></tr></thead><tbody>')
for t, r, e, x in M.HECHOS:
    P(f'<tr><th scope="row">{html.escape(t)} <span class="refs">{R(r)}</span></th><td>{chip(e)}</td><td>{R(x)}</td></tr>')
P('</tbody></table></div></section>')

P(f'<section id="analisis" class="sec"><h2>Análisis</h2><div class="analisis"><p class="aviso">{M.AVISO}</p>')
for par in M.ANALISIS:
    P(f'<p>{R(par)}</p>')
P('</div></section>')
P(f'<section class="sec"><h2>Conclusión</h2><p class="lectura">{R(M.LECTURA)}</p><div class="acciones"><a class="cta" href="debate/">Ver el debate completo →</a>{compartir("¿Qué se vota el 24 de octubre? La moción del Master Plan del Gran Parque Central, artículo por artículo y con la fuente de cada dato.")}</div></section>')

P('<section id="otra-mocion" class="sec aparte"><h2>Aparte: la moción de la agrupación Atilio García</h2>')
P(f'<p class="aviso-alt">{R(M.ALT_AVISO)}</p><ul class="corto">')
for x in M.ALT_RESUMEN:
    P(f'<li>{R(x)}</li>')
P('</ul><div class="table-wrap"><table><thead><tr><th scope="col">Tema</th><th scope="col">Moción oficial</th><th scope="col">Moción Atilio García</th></tr></thead><tbody>')
for t, oficial, alt in M.ALT_TABLA:
    P(f'<tr><th scope="row">{html.escape(t)}</th><td>{R(oficial)}</td><td>{R(alt)}</td></tr>')
P('</tbody></table></div><h3>Qué opinan de ella</h3><div class="posturas">')
for quien, rol, citas in M.ALT_OPINIONES:
    P(f'<article class="post"><h3>{html.escape(quien)}</h3><p class="rol">{html.escape(rol)}</p><ul class="corto">' + "".join(f"<li>{R(c)}</li>" for c in citas) + '</ul></article>')
P('</div><h3>Contra lo que se dijo de ella</h3><ul class="corto">')
for x in M.ALT_DICHOS:
    P(f'<li>{R(x)}</li>')
P('</ul></section>')

P('<section id="fuentes" class="sec"><h2>Fuentes</h2><p class="sec-intro">Cada código es la ficha de la fuente en el repositorio del proyecto. Los enlaces con página abren el PDF en esa página; los que tienen minuto abren el video en ese punto.</p><ul class="fuentes">')
for f in M.FUENTES_PORTADA:
    P(f'<li><span class="code">{f}</span>{src_link(f)}</li>')
P('</ul></section>')
P('''<footer class="foot"><p>Proyecto de verificación del debate sobre el Master Plan del Gran Parque Central, el primer estadio mundialista. Hecho por Santiago Trias, socio de Nacional (n.º 55554), con asistencia de Claude. Método: se separan hechos, estimaciones y opiniones; se aplica la misma vara a todos, incluida la directiva; ninguna cifra se da sin fuente. Fuentes, método e historial de cambios: <a href="https://github.com/strias/masterplan-gpc">repositorio en GitHub</a>.</p></footer></main>''')

open("index.html", "w").write(documento(
    "La moción del Master Plan",
    "Qué se vota el 24 de octubre: la moción del Master Plan del Gran Parque Central artículo por artículo, qué responde del debate y qué deja abierto.",
    "\n".join(o), PORTADA_CSS))
print("portada ok", sum(len(x) for x in o))

# ---------- El anteproyecto ----------
import anteproyecto as AP

def chip_tipo(k):
    t, c = AP.TIPOS[k]
    return f'<span class="chip chip-{c}">{t}</span>'

AP_CSS = PORTADA_CSS.replace("</style>", """
.etapas { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; }
.etapa { display: grid; grid-template-columns: 64px 1fr; gap: 14px; padding: 14px 0; border-bottom: 1px solid var(--line); }
.etapa .n { font-family: var(--f-display); font-size: 2rem; line-height: 1; color: var(--red); }
.etapa div { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.etapa .agrega { color: var(--muted); font-size: .95rem; }
.etapa.estadio .n { color: var(--navy); }
.back { font-family: var(--f-mono); font-size: .82rem; }
@media (max-width: 560px) { .etapa { grid-template-columns: 44px 1fr; } }
</style>""")
AP_COMPARTIR = "El anteproyecto del Master Plan del Gran Parque Central, etapa por etapa: qué se construye primero y cuándo llega cada mejora del estadio."

a = []
Q = a.append
Q('<main class="wrap">')
Q('<header class="hero">'
  '<a class="back" href="../">← La moción, artículo por artículo</a>'
  '<p class="eyebrow">Gran Parque Central · Master Plan · El anteproyecto</p>'
  '<h1>Qué se construye y en qué orden</h1>'
  '<p class="lede">El anteproyecto etapa por etapa, con la página de cada dato, y cómo se compara con lo que dijeron las partes y con lo que pide la moción.</p>'
  '<dl class="facts">'
  f'<div><dt>Documento</dt><dd>{R("Memoria del concurso de ideas · 121 páginas {F-0004}")}</dd></div>'
  '<div><dt>Fechas</dt><dd>Junio de 2025 · publicado el 23/09/2026</dd></div>'
  f'<div><dt>Estado</dt><dd>Preliminar · actualizado el {ACTUALIZADO}</dd></div>'
  '</dl>'
  '<nav class="toc" aria-label="Secciones"><a href="#resumen">En resumen</a><a href="#etapas">Las 14 etapas</a><a href="#orden">El orden y la moción</a><a href="#contraste">Contra lo que se dijo</a><a href="#cuentas">Las cuentas</a><a href="#no-trae">Qué no trae</a><a href="#analisis">Análisis</a><a href="#fuentes">Fuentes</a></nav>'
  f'<div class="acciones"><a class="cta" href="../debate/">El debate: qué dice cada uno →</a>{compartir(AP_COMPARTIR, "anteproyecto/")}</div>'
  '</header>')

Q('<section id="resumen" class="sec"><h2>En resumen</h2><ul class="corto">')
for x in AP.EN_CORTO:
    Q(f'<li>{R(x)}</li>')
Q('</ul></section>')

Q(f'<section id="etapas" class="sec"><h2>Las 14 etapas</h2><p class="sec-intro">Resumen propio de la memoria. Cada etapa indica si es del estadio o de unidades de negocio.</p><ol class="etapas">')
for n, obras, agrega, tipo, pag in AP.ETAPAS:
    Q(f'<li class="etapa {tipo}"><span class="n">{n}</span><div><div class="chips">{chip_tipo(tipo)}</div><p>{R(obras)} {R("{F-0004 p." + pag + "}")}</p><p class="agrega"><strong>Agrega:</strong> {R(agrega)}</p></div></li>')
Q('</ol></section>')

Q('<section id="orden" class="sec"><h2>El orden y la moción</h2>')
for x in AP.ORDEN:
    Q(f'<p>{R(x)}</p>')
Q('</section>')

Q('<section id="contraste" class="sec"><h2>Contra lo que se dijo</h2><p class="sec-intro">Afirmaciones del debate que el anteproyecto permite contrastar. Los estados son los del <a href="../debate/#contrapunto">contrapunto</a>.</p><div class="table-wrap"><table><thead><tr><th scope="col">Qué se dijo</th><th scope="col">Estado</th><th scope="col">Qué dice el anteproyecto</th></tr></thead><tbody>')
for tema, quien, dice, e, deb in AP.CONTRASTE:
    link = f' <a href="../{deb}">Ver la pregunta</a>' if deb else ""
    Q(f'<tr><th scope="row">{html.escape(tema)}<br><span class="refs">{R(quien)}</span></th><td>{chip(e)}</td><td>{R(dice)}{link}</td></tr>')
Q('</tbody></table></div></section>')

Q('<section id="cuentas" class="sec"><h2>Las cuentas del documento</h2><p class="sec-intro">Sumas propias de lo que agrega cada etapa, contra los totales de la página 42.</p><div class="table-wrap"><table><thead><tr><th scope="col">Rubro</th><th scope="col">Suma de las etapas</th><th scope="col">Total del documento</th><th scope="col">Estado</th></tr></thead><tbody>')
for t, suma, total, e in AP.CUENTAS:
    Q(f'<tr><th scope="row">{html.escape(t)}</th><td>{html.escape(suma) or "—"}</td><td>{html.escape(total)}</td><td>{chip(e)}</td></tr>')
Q('</tbody></table></div></section>')

Q('<section id="no-trae" class="sec"><h2>Qué no trae</h2><ul class="falta">')
for t, x in AP.NO_TRAE:
    Q(f'<li><strong>{html.escape(t)}</strong><span>{R(x)}</span></li>')
Q('</ul></section>')

Q(f'<section id="analisis" class="sec"><h2>Análisis</h2><div class="analisis"><p class="aviso">{AP.AVISO}</p>')
for par in AP.ANALISIS:
    Q('<p>' + R(par).replace('href="debate/', 'href="../debate/') + '</p>')
Q('</div></section>')
Q(f'<section class="sec"><h2>Conclusión</h2><p class="lectura">{R(AP.LECTURA)}</p><div class="acciones"><a class="cta" href="../">Ver la moción →</a>{compartir(AP_COMPARTIR, "anteproyecto/")}</div></section>')

Q('<section id="fuentes" class="sec"><h2>Fuentes</h2><p class="sec-intro">Los enlaces con página abren el PDF en esa página; los que tienen minuto abren el video en ese punto.</p><ul class="fuentes">')
for f in AP.FUENTES_PAGINA:
    Q(f'<li><span class="code">{f}</span>{src_link(f)}</li>')
Q('</ul></section>')
Q('<footer class="foot"><p>Proyecto de verificación del debate sobre el Master Plan del Gran Parque Central, el primer estadio mundialista. Hecho por Santiago Trias, socio de Nacional (n.º 55554), con asistencia de Claude. Los autores del anteproyecto son el equipo ganador del concurso, parte interesada. Fuentes, método e historial de cambios: <a href="https://github.com/strias/masterplan-gpc">repositorio en GitHub</a>.</p></footer></main>')

os.makedirs("anteproyecto", exist_ok=True)
open("anteproyecto/index.html", "w").write(documento(
    "El anteproyecto, etapa por etapa",
    "Qué se construye en cada una de las 14 etapas del Master Plan del Gran Parque Central, en qué orden, y cómo se compara con lo que dijeron las partes y con la moción.",
    "\n".join(a), AP_CSS, "anteproyecto/"))
print("anteproyecto ok")
