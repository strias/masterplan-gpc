import html, os, re

ACTUALIZADO = "29/09/2026"
TITULO = "Contrapunto del Master Plan"
DESCRIPCION = "Preguntas, respuestas y fuentes del debate sobre el Master Plan del Gran Parque Central."
HEAD = open("head.html").read()  # fuentes y estilos compartidos


def documento(titulo, descripcion, cuerpo, extra=""):
    """Documento HTML completo y autónomo, listo para copiar a cualquier servidor."""
    return (f'<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>{html.escape(titulo)}</title>\n<meta name="description" content="{html.escape(descripcion)}">\n'
            f'{HEAD}{extra}</head>\n<body>\n{cuerpo}\n</body>\n</html>\n')

YT = {"F-0014": "zOnJazksi08", "F-0015": "ErxVag75_mA", "F-0016": "anYgHKGhDWo",
      "F-0017": "dowYxCNXN7k", "F-0018": "PDYIvpms7r4", "F-0019": "-lKaALmO6ao"}
NOMBRE = {
    "F-0003": "Sitio oficial de la Asamblea", "F-0004": "Anteproyecto (PDF oficial)",
    "F-0007": "Moción oficial (PDF)",
    "F-0009": "La Abdón: moción filtrada", "F-0010": "La Abdón: qué se propone",
    "F-0011": "La Abdón: Decurnex y Aldabalde", "F-0012": "La Abdón: Singlet, Bardanca y Aldabalde",
    "F-0014": "Pasión Tricolor, Aldabalde (25/09)", "F-0015": "Territorio Nacional, Decurnex (21/09)",
    "F-0016": "El Espectador, Aldabalde (17/09)", "F-0017": "Pasión Tricolor, Singlet y Bardanca (24/09)",
    "F-0018": "El Espectador, Aldabalde (16/07)", "F-0019": "Pasión Tricolor, reacción a Decurnex (22/09)",
}
URL = {
    "F-0003": "https://asambleagpc.nacional.uy/",
    "F-0004": "https://asambleagpc.nacional.uy/Anteproyecto.pdf",
    "F-0007": "https://asambleagpc.nacional.uy/Moci%C3%B3n%20Asamblea%20General%20Extraordinaria.pdf",
    "F-0009": "https://laabdon.com/noticias/se-filtro-la-mocion-del-master-plan-que-se-propone-votar-el-24-de-octubre",
    "F-0010": "https://laabdon.com/noticias/master-plan-del-gran-parque-central-que-se-propone-y-que-significa-para-nacional",
    "F-0011": "https://laabdon.com/noticias/el-futuro-del-gran-parque-central-que-propone-cada-uno-y-donde-estan-las-diferencias",
    "F-0012": "https://laabdon.com/noticias/master-plan-del-gpc-las-dudas-de-singlet-y-bardanca-y-las-respuestas-de-aldabalde-frente-a-frente",
}

def ref(fid, ts=None, page=None):
    """Enlace a la fuente, al minuto exacto si es video."""
    if ts and fid in YT:
        h, m, s = map(int, ts.split(":"))
        href = f"https://www.youtube.com/watch?v={YT[fid]}&t={h*3600+m*60+s}s"
        label = f"{fid} · {ts}"
    else:
        href = URL.get(fid, "#fuentes")
        label = fid + (f" · p. {page}" if page else "")
        if page and href.endswith(".pdf"):
            href += f"#page={page.split('-')[0]}"
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
SITIO = "https://masterplangpc.com"

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
   ("Decurnex", "“Nacional está poniendo 147 millones de dólares”: 93 M de renovación de palcos en 30 años, 33 M del Club Social y 21 M de gastos comunes. “Se haga el proyecto o no se haga, es plata de Nacional.”", "{F-0015 00:09:37}"),
  ],
  estado=["coinciden", "mocion"],
  lectura="Hablan de los mismos flujos y con casi las mismas cifras (Aldabalde también da 93 M de palcos y unos 30 M del Club Social, {F-0014 01:44:58}). La diferencia es si llamarlos “aporte del club”. La moción oficial asigna al proyecto justamente esos flujos, y dice que los ya existentes de palcos, Club Social o aportes de socios solo pueden ir al estadio y su infraestructura {F-0007 p.7}."),
 dict(id="costo", q="¿Cuánto cuesta la obra?",
  pregunta=[("Conductor de El Espectador", "“El costo total está tasado en 112 millones, con el costo financiero se iría a 140…”", "{F-0016 00:06:27}")],
  resp=[
   ("Aldabalde", "16/07: la cotización original fue de 93 M y CPA la actualizó “en torno a los 100 millones”. 17/09: “con todas las actualizaciones, todo lo que llaman los soft costs […] está en 112 millones de dólares proyectados en los cuatro o cinco años que va a llevar la obra.”", "{F-0018 00:07:58} {F-0016 00:07:30}"),
   ("Decurnex", "Encargó una estimación a RDA: “un costo arriba de los 150 millones de dólares”, porque el preproyecto no cotiza mobiliario, césped, audio, conectividad ni los anclajes del techo.", "{F-0015 00:07:35} {F-0015 00:08:11}"),
   ("Singlet", "El material entregado a la Directiva parte de 93 M y llega a 105 M, y “no incluye césped, equipamiento deportivo, honorarios de arquitectura e ingeniería, seguros de obra ni costos financieros durante la obra”.", "{F-0017 00:51:51}"),
  ],
  estado=["distintos", "pendiente"],
  lectura="Las cifras de Aldabalde cambian con el tiempo por actualizaciones; la vigente es 112 M. El “140 M” que La Abdón le atribuye lo dijo el entrevistador ({F-0016 00:06:27}). El anteproyecto oficial no trae costos ({F-0004}). Falta ver qué incluye hoy el costo de 112 M y el informe de RDA."),
 dict(id="cuota", q="¿Va a haber una cuota extra? ¿Es obligatoria?",
  pregunta=[("Conductor de Territorio Nacional", "“¿Eso es opcional, José, o es obligatorio?”", "{F-0015 00:13:25}"),
            ("Conductor de Pasión Tricolor", "“La cuota o el dinero este que tienen que sacar de los socios, ¿nunca va a ser obligatorio?”", "{F-0014 02:32:26}")],
  resp=[
   ("Aldabalde", "17/09: “Hay cuotas de 40 pesos, de 50 pesos, 100 pesos y que son voluntarias […] ni se habla de 10 dólares.” 25/09: los USD 10 por mes de 20.000 socios eran “una celda de un Excel” de marzo. Obligatoria: “Siempre [optativa] […] Yo creo que no. Esa es una decisión de directiva, no mía.”", "{F-0016 00:09:10} {F-0014 00:59:29} {F-0014 02:32:36}"),
   ("Decurnex", "El modelo supone 26 M de aporte de socios: 22.500 socios con USD 10 por mes durante 5 años y 1.000 socios con bonos de USD 2.000 por año. Para un financiador, un aporte voluntario “es tomado como cero”: “tenés que hacer una suba de cuota inevitable”, de alrededor del 50%.", "{F-0015 00:13:06} {F-0015 00:14:44}"),
   ("Bardanca", "El financiador exige un aporte propio de 15 a 20% y no acepta que sea voluntario.", "{F-0017 00:54:19}"),
  ],
  estado=["distintos", "cuenta", "pendiente"],
  lectura="Los dos lados coinciden en que el modelo pide unos 26 M de aporte de socios; discrepan en si puede ser voluntario. Aldabalde cambió su versión sobre los USD 10 entre el 17 y el 25 de septiembre. Los componentes que da Decurnex suman 23,5 M, no 26; él mismo da 11 M para los bonos, donde 1.000 × 2.000 × 5 son 10 M ({F-0015 00:14:05}). La tercera cifra de cuota del 17/09 (¿100 o 200 pesos?) falta verificarla en el audio; el 25/09 Aldabalde dijo “hablábamos de 40, 50, 200 pesos” ({F-0014 01:52:05}). Se resuelve con el modelo económico, que todavía no está publicado ({F-0003})."),
 dict(id="570", q="¿El proyecto genera 570 millones de dólares?",
  pregunta=[("Conductor de Pasión Tricolor", "“Según Santiago Aldabalde, el proyecto generaría 570 millones de dólares. Pero dentro de esa cifra se incluyen los ingresos de tres renovaciones de palcos…”", "{F-0014 01:43:03}")],
  resp=[
   ("Aldabalde", "El fideicomiso genera 570 M en 30 años, más 150 M que van directo al club. Acepta el valor presente: “si esos 570 millones, sacando los palcos, son 82 hoy, los 94 de los palcos son 22”.", "{F-0016 00:05:03} {F-0014 01:44:58}"),
   ("Bardanca", "Sumar los ingresos de 30 años “es un error financiero grave y básico”. Traídos al presente, “esos 570 millones son 103 millones de dólares”, y además incluyen palcos, gastos comunes y Club Social, que existirían sin el proyecto.", "{F-0017 00:30:29} {F-0017 00:33:40}"),
  ],
  estado=["coinciden"],
  lectura="Coinciden casi exactamente: 82 + 22 = 104 M según Aldabalde, 103 M según Bardanca. El desacuerdo es qué cifra comunicar y qué ingresos son propios del proyecto."),
 dict(id="parking", q="¿El estacionamiento da ganancia?",
  pregunta=[("Conductor de Pasión Tricolor", "“Lo que generó ruido es lo del garage, los estacionamientos. Decime esa.”", "{F-0017 00:37:56}")],
  resp=[
   ("Singlet", "“980 plazas. El supuesto del proyecto es que hay una ocupación del 90% durante los 30 años.”", "{F-0017 00:39:24}"),
   ("Bardanca", "Con el Excel de CPA y sin cambiar sus supuestos, el valor actual neto del estacionamiento da “menos siete millones de dólares”. La arena tampoco genera valor; el zócalo comercial sí.", "{F-0017 00:43:21} {F-0017 00:57:13}"),
   ("Aldabalde", "El 90% “es la curva de lo que le vamos a cobrar al operador”, no la ocupación. Calculado por eventos, da unos 2,5 M de ingresos y 0,5 M de costo: “es un negocio de 2 millones de dólares”.", "{F-0014 01:11:08} {F-0014 01:13:45}"),
  ],
  estado=["pendiente", "cuenta"],
  lectura="Es un desacuerdo sobre qué dice el modelo, y se resuelve leyendo el documento. Además miden cosas distintas: valor actual neto de la inversión contra resultado anual. En la cuenta de Aldabalde, 3 M con un castigo del 30% dan 2,1 M, no 2,5. Los 980 lugares sí están en el anteproyecto ({F-0004 p.42})."),
 dict(id="solo", q="¿Se puede terminar solo el estadio?",
  pregunta=[("Conductor de El Espectador", "“Hay plan B. El plan B, por ejemplo, es terminar exclusivamente el parque.”", "{F-0016 00:16:01}"),
            ("Conductor de Pasión Tricolor", "“¿Con los flujos de Nacional solamente construir el parque sin todos los negocios anexos, eso para vos es inviable?”", "{F-0014 02:14:26}")],
  resp=[
   ("Aldabalde", "“Para hacer el parque solo no dan los números.” Con los palcos hay 17 M en 10 años, unos 13 M a valor presente. “No para mí, para el análisis que hizo [CPA].”", "{F-0016 00:16:13} {F-0014 02:14:43}"),
   ("Decurnex", "“Debiera de haber un estudio y un análisis pormenorizado y detallado del tema parque en exclusividad”, y los demás negocios los debería financiar alguien de afuera.", "{F-0015 00:16:45}"),
   ("Bardanca", "Trabajan sobre el Excel de CPA con cambios, por ejemplo sin techo, y “tenemos indicios de que se podría llegar a estructurar”. No está terminado.", "{F-0017 01:20:05}"),
  ],
  estado=["pendiente"],
  lectura="Falta el análisis de CPA del escenario de solo estadio y la alternativa de Singlet y Bardanca. Hay un dato en común: el techo cuesta unos 20 M según Aldabalde, con cintas digitales y pantallas, y 21,5 M según Singlet, rubros 12 y 13 ({F-0014 00:53:46}, {F-0017 01:41:45})."),
 dict(id="sobrecosto", q="¿Qué pasa si la obra sale más cara?",
  pregunta=[("Conductor de El Espectador", "“El sobrecosto que puede tener, como tuvo el Camp Nou, como tuvo el Real Madrid, como tuvo el Antel Arena […] ¿quién se hace cargo?”", "{F-0016 00:23:57}")],
  resp=[
   ("Aldabalde", "“El fideicomiso es el responsable de toda la financiación.” Si cuesta 130 en vez de 110, no se empieza sin tener ese dinero; en el peor caso, el fideicomiso tarda más en pagar.", "{F-0016 00:24:12}"),
   ("Decurnex", "El Club Social “tuvo entre un 55 y un 60% de sobrecosto”; hay que prever un 20 a 25% de imprevistos.", "{F-0015 00:20:13} {F-0015 00:36:50}"),
   ("Bardanca", "Estadios como el Real Madrid o el Barcelona tuvieron desvíos del 50 o 60%: “Nosotros un desvío de obra del 60% no lo resistimos.”", "{F-0017 01:08:11}"),
  ],
  estado=["mocion", "pendiente"],
  lectura="Según la moción oficial, el club no aporta capital para sobrecostos {F-0007 p.7} y ninguna etapa empieza sin financiamiento suficiente para completarla {F-0007 p.7}. Si eso alcanza para cubrir el riesgo es una cuestión de valoración."),
 dict(id="voto", q="¿Qué se vota el 24 de octubre y con qué mayoría?",
  pregunta=[("Conductor de Territorio Nacional", "“La Asamblea, ¿para qué sirve?”", "{F-0015 00:21:40}"),
            ("Oyente, leído en Pasión Tricolor", "“Si se aprueba por el 75% o por el 50 más 1. Que hay un debate ahí.”", "{F-0014 02:12:06}")],
  resp=[
   ("Aldabalde", "La Asamblea “aprueba el master plan y aprueba un sistema de trabajo”: sin deuda del club, sin hipotecas y sin empezar nada sin financiamiento. Sobre la mayoría: el 75% salió de una reforma del Estatuto votada “hace dos meses”, que no rige hasta que la apruebe el MEC.", "{F-0014 01:56:05} {F-0014 02:16:38}"),
   ("Decurnex", "Según el Estatuto vigente alcanza con mayoría simple, pero “esto tiene que ser aprobado por el 75%”, como votó la Asamblea; va a plantearlo como moción.", "{F-0015 00:25:45}"),
   ("Singlet", "La reforma del 7 de julio fijó el 75% para proyectos de más de USD 2 M. Dos o tres días después, Aldabalde dijo que esta Asamblea se regiría por el Estatuto vigente.", "{F-0017 00:05:19} {F-0017 00:07:23}"),
  ],
  estado=["coinciden", "pendiente"],
  lectura="Todos coinciden en que la reforma existe y no rige. El desacuerdo es jurídico y de valores. La moción oficial no fija la mayoría de la Asamblea; se remite a los Estatutos “sin perjuicio de cualquier exigencia estatutaria más rigurosa que resulte vigente” {F-0007 p.5}. Para las decisiones de la Directiva pide unanimidad de los once {F-0007 p.8}."),
]

# ---------- Contrapunto ----------
FILAS = [
 ("¿Pone plata Nacional?", "coinciden", "#plata"),
 ("570 M: nominal y valor presente", "coinciden", "#570"),
 ("Costo de la obra", "distintos", "#costo"),
 ("“140 M con costo financiero”", "atribucion", "#costo"),
 ("Costo del proyecto ejecutivo: 2,5 M", "atribucion", None),
 ("Proyecto ejecutivo antes de votar", "mocion", None),
 ("Aporte de socios voluntario", "pendiente", "#cuota"),
 ("Los USD 10 por mes", "distintos", "#cuota"),
 ("Cuentas de los 26 M y del estacionamiento", "cuenta", None),
 ("Ocupación y valor del estacionamiento", "pendiente", "#parking"),
 ("Ocupación comercial de 97,5%", "pendiente", None),
 ("Superficie del zócalo comercial", "parcial", None),
 ("Mantenimiento: 3 o 4 M contra 1,2 M", "pendiente", None),
 ("“10 mil butacas nuevas”", "consistente", None),
 ("Solo estadio", "pendiente", "#solo"),
 ("Informe de CPA “lapidario”", "pendiente", None),
 ("Garantías de la moción", "mocion", None),
 ("Mayoría especial de la Directiva", "mocion", None),
 ("Mayoría del 75%", "coinciden", "#voto"),
]
NOTAS = {
 "Costo del proyecto ejecutivo: 2,5 M": "La Abdón publicó 2,5 M; Aldabalde dijo “del entorno de los 2 millones” {F-0016 00:21:22}.",
 "Proyecto ejecutivo antes de votar": "La moción exige ejecutivo antes de cada etapa, no antes de la Asamblea {F-0007 p.7}. Es un desacuerdo de valores sobre qué hay que saber antes de votar.",
 "Ocupación comercial de 97,5%": "Bardanca {F-0017 01:16:57}; Aldabalde: “100% alquilado, con precontratos” {F-0014 01:08:44}. Falta el modelo.",
 "Superficie del zócalo comercial": "Aldabalde habla de modelos de 3.500 y 7.000 m² {F-0014 01:08:14}; el anteproyecto da 3.080 m² de locales comerciales y 14.266 m² de superficies rentables {F-0004 p.42}.",
 "Mantenimiento: 3 o 4 M contra 1,2 M": "Aldabalde {F-0016 00:06:05}; Singlet, último balance: 1,2 M bruto {F-0017 01:31:00}. Falta el balance.",
 "“10 mil butacas nuevas”": "Aldabalde {F-0014 01:52:45}. El aforo pasa de unos 34.000 a más de 43.000 {F-0004 p.64}.",
 "Informe de CPA “lapidario”": "Aldabalde lo anunció así {F-0016 00:16:50}. En un mail leído al aire, un socio de CPA escribe que “no es lapidario ni pretende serlo” {F-0017 00:47:34}. Falta el informe.",
 "Cuentas de los 26 M y del estacionamiento": "Los componentes que da Decurnex suman 23,5 M, no 26 {F-0015 00:13:06}; en el estacionamiento, 3 M con un castigo del 30% dan 2,1 M, no 2,5 {F-0014 01:13:45}. Ver [[#cuota|la cuota]] y [[#parking|el estacionamiento]].",
 "Mayoría especial de la Directiva": "La moción pide el voto unánime de los once directivos {F-0007 p.8}. Si no hay unanimidad y la mayoría simple quiere seguir, decide una nueva Asamblea en 30 días.",
 "Garantías de la moción": "Fideicomiso separado, sin hipoteca ni deuda del club, unanimidad de la Directiva para las decisiones centrales, vuelta a la Asamblea ante cambios sustanciales y plazo de 30 meses {F-0007 p.6-9}. Un conductor de Pasión Tricolor pide sanciones para quien incumpla {F-0014 01:58:43}; Singlet teme que se relegue a las asambleas en las decisiones futuras {F-0017 00:17:46}. Aldabalde acepta las sanciones, pero dice que van en el Estatuto {F-0014 01:59:47}. Qué cubre un sobrecosto: [[#sobrecosto|la pregunta del sobrecosto]].",
}

COINCIDEN = [
 ("Ingresos a valor presente", "unos 104 M según Aldabalde; 103 M según Bardanca", "{F-0014 01:44:58} {F-0017 00:31:30}"),
 ("Palcos en 30 años", "93 M, tres renovaciones", "{F-0015 00:09:37} {F-0014 01:44:58}"),
 ("Techo", "unos 20 M según Aldabalde, con cintas digitales y pantallas; 21,5 M según Singlet, rubros 12 y 13", "{F-0014 00:53:46} {F-0017 01:41:45}"),
 ("Aporte de socios en el modelo", "unos 26 M", "{F-0014 01:06:00} {F-0015 00:12:34}"),
 ("Reforma del Estatuto (75%)", "existe y todavía no rige", "{F-0014 02:16:38} {F-0015 00:25:45}"),
 ("Pasivo del club", "entre 36 y 40 M", "{F-0014 01:48:47} {F-0015 00:33:36}"),
 ("Ingresos de los negocios", "los modeló la CPO; CPA arma el modelo con esos insumos", "{F-0015 00:19:01} {F-0014 01:15:43}"),
 ("Objetivo", "terminar el estadio, con el Mundial 2030 como oportunidad", "{F-0016 00:14:00} {F-0015 00:33:02} {F-0017 01:20:05} {F-0017 01:35:00}"),
]

FALTA = [
 ("Votación de la Directiva sobre la moción", "Con qué resultado se aprobó el texto oficial"),
 ("Modelo económico financiero", "Costo vigente, cuota, aporte voluntario, supuestos comerciales"),
 ("Material entregado a la Directiva el 11/03/2026", "Qué incluye el costo, ocupación del estacionamiento, techo"),
 ("Excel de CPA “evaluación unidad de negocio v3” e informe de CPA", "Valor de cada negocio, solo estadio"),
 ("Informe de RDA", "Costo de más de 150 M"),
 ("Texto de la reforma del Estatuto", "Mayoría del 75%"),
 ("Último balance del club", "Mantenimiento y pasivo"),
]

POSTURAS = [
 ("Santiago Aldabalde", "Presidente de la CPO · postura oficialista",
  "El Master Plan es la única forma de terminar el estadio y cambiar la economía del club. Cinco hectáreas en el centro de Montevideo que hoy rinden casi solo los días de partido pueden pagar la obra con arena, estacionamiento, zócalo comercial y plaza. El riesgo queda en un fideicomiso: sin hipotecas, sin deuda del club y sin empezar ninguna etapa sin financiamiento. “Hacer solo el estadio no da.”",
  "{F-0014 00:50:14} {F-0016 00:02:32}"),
 ("José Decurnex", "Vocal de la Directiva · votó contra convocar la Asamblea",
  "Lo que quieren los socios es el estadio, y ahí deben ir los recursos del club: 147 M en 30 años de palcos, gastos comunes y Club Social, más el aporte de socios. Los negocios complementarios tienen riesgo y los deberían financiar privados. Sin proyecto ejecutivo no hay costo cierto; pide aprobación con el 75%.",
  "{F-0015 00:04:13} {F-0015 00:16:45}"),
 ("Enrique Singlet y Joaquín Bardanca", "Contadores · agrupación Atilio García",
  "Crítica técnica sobre los documentos de CPA: los 570 M son nominales; con los propios supuestos de CPA, el estacionamiento y la arena no generan valor; el costo de 105 M deja rubros afuera; un financiador no acepta un aporte voluntario; falta análisis de sensibilidad. Dicen que no son asesores de Decurnex y trabajan en una alternativa de solo estadio.",
  "{F-0017 00:11:21} {F-0017 01:24:00}"),
 ("Tatiana Villaverde", "Contadora de la Directiva",
  "El dinero genuino del club debe ir al estadio; las unidades de negocio, a inversores externos a su riesgo, con concesiones temporales como la del restaurante o la tienda. (Mensaje leído al aire.)",
  "{F-0014 01:24:49}"),
]

FUENTES = ["F-0003", "F-0004", "F-0007", "F-0011", "F-0012", "F-0014", "F-0015", "F-0016", "F-0017", "F-0018", "F-0019"]

def src_link(fid):
    if fid in YT:
        return f'<a href="https://www.youtube.com/watch?v={YT[fid]}" target="_blank" rel="noopener">{NOMBRE[fid]}</a>'
    return f'<a href="{URL[fid]}" target="_blank" rel="noopener">{NOMBRE[fid]}</a>'

out = []
A = out.append
A('<main class="wrap">')
A('''<header class="hero">
  <a class="back" href="../">← La moción, artículo por artículo</a>
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
open("debate/index.html", "w").write(documento(TITULO, DESCRIPCION, "\n".join(out), '<style>.back { font-family: var(--f-mono); font-size: .82rem; }</style>'))

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
    open(f"debate/detalle-{p['id']}.html", "w").write(documento(d["titulo"], descripcion, "\n".join(o), EXTRA))
print("detalles:", len(ids))
print("ok", sum(len(x) for x in out))

# ---------- Portada: la moción ----------
import mocion as M

def chip_resp(k):
    t, c = M.RESPUESTAS[k]
    return f'<span class="chip chip-{c}">{t}</span>'

PORTADA_CSS = """<style>
.cg { font-family: var(--f-mono); font-size: .66rem; text-transform: uppercase; letter-spacing: .06em; background: transparent; color: var(--muted); border: 1px dashed currentColor; padding: 0 5px; border-radius: 3px; white-space: nowrap; }
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
    <a href="#resumen">En resumen</a><a href="#articulos">Artículo por artículo</a><a href="#debate">Y el debate</a><a href="#no-dice">Qué no dice</a><a href="#hechos">Datos por verificar</a><a href="#analisis">Análisis</a><a href="#fuentes">Fuentes</a>
  </nav>
  <div class="acciones"><a class="cta" href="debate/">El debate: qué dice cada uno →</a>''' + compartir("¿Qué se vota el 24 de octubre? La moción del Master Plan del Gran Parque Central, artículo por artículo y con la fuente de cada dato.") + '''</div>
</header>''')

P('<section id="resumen" class="sec"><h2>En resumen</h2><ul class="corto">')
for x in M.EN_CORTO:
    P(f'<li>{R(x)}</li>')
P('</ul></section>')


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
