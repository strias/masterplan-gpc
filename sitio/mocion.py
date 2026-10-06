# Contenido de la portada: análisis de la moción oficial, versión 2 (F-0026), que reemplaza
# a la v1 (F-0007). Mismas marcas que detalle.py: {F-0026 p.5} enlaza a la página,
# {F-0014 01:55:53} al minuto, [[CG]] marca conocimiento general y
# [[>debate/detalle-plata.html|texto]] enlaza a otra página.

FUENTE = "F-0026"

EN_CORTO = [
 "Se aprueba el Master Plan como **marco**, pero sin obligación de construir todas las unidades: se pueden adaptar, postergar o excluir. Eso solo **no habilita** obras, financiamiento, garantías ni contratos definitivos {F-0026 p.2-3}.",
 "**Lo primero es un proyecto ejecutivo** que abarque como mínimo el estadio, **con y sin techo**, y el costo del techo por separado. Cada unidad de negocio se evalúa aparte {F-0026 p.2-3}.",
 "Los fondos del club para el estadio (**palcos, Club Social y aportes extraordinarios de socios**) van a un **fideicomiso propio** y no pueden financiar ni garantizar otras unidades. Las cuotas ordinarias quedan excluidas {F-0026 p.3-4}.",
 "Cuando estén los proyectos ejecutivos, los contratos y el financiamiento de las primeras etapas, la Directiva tiene que **convocar otra Asamblea en 45 días**, que decide el alcance definitivo {F-0026 p.5}.",
 "Ninguna etapa empieza sin proyecto ejecutivo, permisos, modelo validado, **financiamiento suficiente para completarla**, licitación e informe jurídico {F-0026 p.5}.",
 "Si en **30 meses** no empezó ninguna etapa sustancial, caduca la autorización, con una sola prórroga de un año {F-0026 p.6}.",
]

# Qué cambió de la versión 1 (29/09) a la versión 2 (05/10).
CAMBIOS = [
 "**Se saca la unanimidad de los once directivos** que pedía la v1 para las decisiones centrales {F-0007 p.8}. En su lugar hay una **Asamblea posterior obligatoria** {F-0026 p.5}.",
 "**Proyecto ejecutivo del estadio primero**, con y sin techo, y cada unidad evaluada por separado {F-0026 p.2-3}. La v1 solo pedía priorizar las etapas del estadio “en función de los flujos y plazos disponibles” {F-0007 p.6}.",
 "**Fideicomiso propio para los fondos del estadio** {F-0026 p.3}. La v1 los reservaba al estadio dentro del mismo vehículo {F-0007 p.6-7}.",
 "**Las unidades se pueden excluir:** la aprobación “no constituye una obligación de construir todas las unidades” {F-0026 p.2}.",
 "**Se quitan dos garantías de la v1.** La lista de cambios que obligaban a volver a la Asamblea ahora remite solo al Estatuto {F-0026 p.6}; antes nombraba deuda, garantías, ingresos ordinarios y propiedad de los bienes {F-0007 p.9}. Y desaparece la frase que prohibía reducir garantías sin una nueva Asamblea {F-0007 p.9}.",
 "**Más información:** mensual a la Directiva (antes trimestral), con detalle de costos por fase y de los fondos del estadio {F-0026 p.6}.",
 "**El preámbulo es más corto.** Ya no trae el detalle de la encuesta ni menciona el concurso de 1957, el carácter “evolutivo” de las estimaciones de CPA Ferrere ni el Consejo Asesor {F-0026 p.1}.",
 "**Tres referencias internas no cierran.** El artículo 4°, numeral 2, exceptúa la prohibición de transferir bienes con “lo dispuesto en el numeral 7”, que no existe. El 3° remite al numeral 5 por los fondos del estadio, que están en el 4. El 1° remite al 8° para excluir unidades, pero el 8° ya no trata eso {F-0026 p.2-4}.",
 "Según la prensa, la Directiva la votó por unanimidad, 11 a 11, con la conformidad de la agrupación Atilio García. El documento no lo dice y todavía no registramos la fuente.",
]

ARTICULOS = [
 ("Primero", "Aprobación institucional", "Aprueba el Master Plan como marco arquitectónico, estratégico y funcional, con la integración del estadio con arena, Plaza del Hincha, estacionamientos y las demás unidades. No obliga a construirlas todas: se pueden adaptar, postergar o excluir por razones fundadas.", "p.2", None),
 ("Segundo", "Alcance de la autorización", "Autoriza a la Directiva a seguir con estudios, proyectos ejecutivos, permisos y negociaciones no vinculantes, y a priorizar el estadio. La primera etapa es un proyecto ejecutivo que abarca como mínimo el estadio y su infraestructura, “con y sin techo”; para las otras unidades, ejecutivos o cotizaciones de “empresas de plaza”. El techo se costea aparte y se compara el estadio solo con distintas combinaciones de unidades.", "p.2-3", ("orden", "¿Qué se hace primero?")),
 ("Tercero", "Fideicomisos", "Uno o más fideicomisos con patrimonio, cuentas y flujos separados de los del club. Los fondos del club para el estadio van a un fideicomiso independiente y no pueden garantizar otras unidades. Prevé operadores especializados y preservar la actividad de los planteles principales.", "p.3", ("plata", "¿Nacional pone plata?")),
 ("Cuarto", "Protección del patrimonio y de la caja", "Seis límites: sin deuda ni garantías del club, ni capital para sobrecostos o déficits; sin hipotecas ni venta de bienes; derechos de uso temporales y reversibles; para el estadio solo palcos, Club Social y aportes extraordinarios de socios, nunca las cuotas ordinarias; restitución al club de lo que aporte; en las demás unidades, el club aporta solo derechos temporales de uso.", "p.4", ("plata", "¿Nacional pone plata?")),
 ("Quinto", "Condiciones antes de cada etapa", "Proyecto ejecutivo, cronograma y presupuesto; permisos; modelo actualizado y validado por CPA Ferrere u otra firma independiente; financiamiento suficiente para completar la etapa, con compromisos vinculantes; licitación con una Comisión de Licitaciones; contratos, garantías y seguros; informe jurídico.", "p.5", ("sobrecosto", "¿Qué pasa si sale más cara?")),
 ("Sexto", "Asamblea posterior", "Con los estudios de viabilidad, proyectos ejecutivos, contratos, operadores y financiamiento de las primeras etapas aceptados por la Directiva, esta convoca una Asamblea Extraordinaria en 45 días. Esa Asamblea decide el alcance definitivo y sus condiciones.", "p.5", ("voto", "¿Qué se vota y con qué mayoría?")),
 ("Séptimo", "Control y transparencia", "Declaración y abstención ante conflictos de interés, auditoría externa, información mensual a la Directiva e informe a los socios al menos cada seis meses, “sin perjuicio de la reserva exigible durante negociaciones o procesos competitivos”.", "p.6", None),
 ("Octavo", "Modificaciones", "Vuelve a la Asamblea cualquier modificación “que requiera aprobación de esta asamblea de acuerdo al Estatuto vigente”.", "p.6", None),
 ("Noveno", "Plazo y caducidad", "A los 30 meses sin inicio material de una etapa sustancial, la Directiva decide si sigue y puede prorrogar una vez por un año. Si vence, cae la autorización del artículo 2°, no la aprobación del 1°. Demoliciones menores o movimientos hechos para evitar el plazo no cuentan.", "p.6", None),
 ("Décimo", "Reglamentación", "La Directiva reglamenta y formaliza la resolución, “dentro de los límites y condiciones aquí establecidas”.", "p.6", None),
]

RESPUESTAS = {
 "si": ("La moción lo responde", "ok"),
 "parte": ("Lo responde en parte", "soft"),
 "no": ("La moción no lo trata", "pend"),
}

# (id de la pregunta del debate, pregunta, respuesta, qué dice la moción)
DEBATE = [
 ("plata", "¿Nacional pone plata en el proyecto?", "si",
  "Sí, y dice cuál: palcos (venta, renovación, uso y gastos comunes), dividendos o utilidades del Club Social y aportes extraordinarios de socios para estas obras. Solo pueden ir al estadio, en un fideicomiso independiente, y nunca las cuotas ordinarias {F-0026 p.3-4}. El modelo tiene que prever su restitución al club {F-0026 p.4}. Es lo que describían Aldabalde y Decurnex, y el vehículo aparte que pedía Decurnex {F-0022 00:06:40} quedó escrito."),
 ("sobrecosto", "¿Qué pasa si la obra sale más cara?", "parte",
  "El club no pone capital para sobrecostos {F-0026 p.4} y ninguna etapa empieza sin financiamiento suficiente para completarla, con garantías y seguros {F-0026 p.5}. No dice qué pasa si una etapa se queda sin fondos a mitad de camino."),
 ("voto", "¿Qué se vota y con qué mayoría?", "parte",
  "Dice qué se vota: el marco y la autorización para estructurar, no la obra {F-0026 p.2-3}. Los socios vuelven a votar el alcance definitivo cuando estén los ejecutivos y el financiamiento {F-0026 p.5}. No fija con qué mayoría decide la Asamblea: se remite a los Estatutos “sin perjuicio de cualquier exigencia estatutaria más rigurosa que resulte vigente” {F-0026 p.1}."),
 ("solo", "¿Se puede terminar solo el estadio?", "parte",
  "Manda estudiarlo: el estadio “en forma completa”, con el techo costeado aparte, y comparar su desarrollo independiente con combinaciones de unidades {F-0026 p.3}. Las unidades se pueden excluir {F-0026 p.2}. La decisión queda para la Asamblea posterior {F-0026 p.5}."),
 ("orden", "¿Qué se hace primero?", "parte",
  "Lo primero es el proyecto ejecutivo del estadio, con y sin techo {F-0026 p.2}. Prioriza las etapas del estadio, pero permite obras habilitantes o unidades complementarias si se justifican {F-0026 p.2}. No fija el orden de las obras. El anteproyecto empieza por el estacionamiento y el zócalo comercial {F-0004 p.38}."),
 ("cuota", "¿Va a haber una cuota extra? ¿Es obligatoria?", "no",
  "Habla de “aportes extraordinarios de socios destinados específicamente a estas obras” y excluye las cuotas ordinarias {F-0026 p.4}. No dice monto, si son voluntarios ni quién los aprueba."),
 ("costo", "¿Cuánto cuesta la obra?", "no",
  "No da ninguna cifra. Manda hacer el proyecto ejecutivo del estadio y pedir costos a empresas de plaza para tener “costos de mercado” {F-0026 p.3}, y exige un presupuesto por etapa antes de empezarla {F-0026 p.5}."),
 ("570", "¿El proyecto genera 570 millones?", "no",
  "No da cifras de ingresos. Pide actualizar los escenarios financieros y de sensibilidad con el proyecto ejecutivo {F-0026 p.3}."),
 ("parking", "¿El estacionamiento da ganancia?", "no",
  "Lo incluye entre las unidades del marco {F-0026 p.2}, sin números. Cada unidad se analiza por separado y puede excluirse {F-0026 p.2-3}."),
]

NO_DICE = [
 ("Costo, financiamiento e ingresos", "Ninguna cifra. Quedan para el proyecto ejecutivo, el modelo actualizado y la Asamblea posterior {F-0026 p.3} {F-0026 p.5}."),
 ("Quién paga el proyecto ejecutivo", "Cada fase se contrata con presupuesto máximo y fuente de fondos aprobados por la Directiva {F-0026 p.2}. No dice cuánto cuesta ni de dónde sale. Las dos partes hablan de unos 2 M {F-0016 00:21:22} {F-0022 00:02:46}."),
 ("Plazo del proyecto ejecutivo", "Ninguno. La moción alternativa pedía 180 días {F-0023}."),
 ("Aporte de socios", "Ni monto, ni si es voluntario, ni quién lo aprueba {F-0026 p.4}."),
 ("Mayoría de la Asamblea", "Se remite a los Estatutos {F-0026 p.1}."),
 ("Mayoría de la Directiva", "Sin la unanimidad de la v1, no fija ninguna mayoría especial {F-0026 p.5}."),
 ("Fondos que no alcanzan a mitad de una etapa", "Prevé el comienzo, no el medio de la obra {F-0026 p.5}."),
 ("Etapas posteriores", "La Asamblea posterior es para “las etapas propuestas para su ejecución inicial” {F-0026 p.5}. No dice si las siguientes vuelven a los socios."),
 ("Sanciones por incumplir", "Ninguna. Aldabalde dijo que van en el Estatuto {F-0014 01:59:47}."),
 ("Votación de la Directiva", "El documento no dice cómo se aprobó ni lleva firma. La v1 salió 7 a 4, según Gomensoro {F-0021 00:01:58}. De la v2, la prensa informa que salió 11 a 11; falta registrar la fuente."),
]

# Afirmaciones de hecho del preámbulo. Estados del debate (ESTADOS en build.py).
HECHOS = [
 ("La CPO y la Directiva aprobaron el proyecto por unanimidad", "{F-0026 p.1}", "pendiente",
  "La v1 daba fechas: 2/7/2025 y 4/8/2025 {F-0007 p.1}. Coincide con lo que dijo Aldabalde, presidente de la CPO: “agosto” y unanimidad {F-0014 00:53:14}. Falta una fuente independiente, como el acta de la Directiva. Un conductor de Pasión Tricolor habla de una aprobación unánime “en cuanto a la idea” {F-0019 00:13:28}."),
 ("Unas cinco hectáreas", "{F-0026 p.1}", "consistente",
  "El anteproyecto da 48.000 m² de terreno {F-0004 p.15}."),
 ("La v2 se votó 11 a 11, con conformidad de la agrupación Atilio García", "prensa", "pendiente",
  "Lo informa la prensa y nadie lo desmintió, pero ni el PDF ni el sitio del club lo dicen. Falta registrar la fuente."),
]

AVISO = "Este análisis es de Claude, la IA que asiste al proyecto, y es opinión. Se apoya en la moción y en las fuentes enlazadas y, donde lo indica la etiqueta <span class=\"cg\">conocimiento general</span>, en conocimiento general de finanzas y fideicomisos que no sale de una fuente registrada. No es una opinión jurídica."

ANALISIS = [
 "**Es una moción de consenso, y se nota en lo que suma.** Toma lo central de la alternativa de la agrupación Atilio García {F-0023}: proyecto ejecutivo del estadio primero, techo costeado aparte, cada unidad evaluada por separado, fondos del estadio en un vehículo propio y una nueva Asamblea con los números {F-0026 p.2-5}. La distancia entre las dos posturas se achica a una sola cosa: el 24 de octubre se aprueba el Master Plan como marco, y la alternativa no lo aprobaba.",
 "**Cambia un control por otro.** La v1 frenaba cada decisión central si un solo directivo se oponía {F-0007 p.8}. La v2 saca ese veto y pone a los socios a decidir el alcance definitivo, con ejecutivos, contratos y financiamiento a la vista {F-0026 p.5}. Es lo que pedían los críticos, saber qué se aprueba antes de aprobarlo {F-0015 00:11:39}, aunque llega en una segunda votación. La contracara: entre el 24 de octubre y esa Asamblea, la Directiva decide sin mayoría especial.",
 "**Se aflojan dos candados, y quedan atados al Estatuto.** La v1 nombraba qué cambios volvían a la Asamblea (más deuda, garantías del club, ingresos ordinarios, propiedad de los bienes) y prohibía reducir garantías sin una nueva Asamblea {F-0007 p.9}. La v2 remite al Estatuto {F-0026 p.6}, que no tenemos. Si el Estatuto ya exige Asamblea para esos casos, no cambia nada; si no, la protección es menor. Conviene que alguien con el Estatuto en la mano lo aclare antes del 24.",
 "**Las referencias que no cierran no son un detalle.** La prohibición de transferir bienes del club tiene una excepción que remite a un “numeral 7” que no existe {F-0026 p.4}. Parece un resto de un borrador, pero en el texto que se vota es una puerta abierta sin definir. Lo mismo, en menor medida, con la remisión al numeral 5 por los fondos del estadio {F-0026 p.3}. Son errores fáciles de corregir y deberían corregirse antes de votar.",
 "**El aporte de socios sigue siendo el punto más abierto.** La v2 excluye las cuotas ordinarias pero admite “aportes extraordinarios de socios destinados específicamente a estas obras” {F-0026 p.4}. Una sobrecuota con permanencia por defecto, como la que describió Gomensoro {F-0021 00:20:03}, parece entrar en esa categoría. Bardanca sostiene que un financiador pide un aporte propio que no sea voluntario {F-0017 00:54:19}. Ver [[>debate/detalle-cuota.html|la cuota]].",
 "**El proyecto ejecutivo no tiene plazo ni precio.** Es la pieza central de la v2, pero la moción no dice cuánto cuesta ni cuándo tiene que estar {F-0026 p.2-3}. Sin plazo, la Asamblea posterior puede tardar; el único reloj es la caducidad de 30 meses {F-0026 p.6}.",
 "**Sin capital del club para sobrecostos, el riesgo lo toma otro.** Un financiador sin garantía del club suele pedir más contingencia, más tasa o menos alcance [[CG]]. Es probable que el financiamiento real sea más caro o más chico que el modelado; con la v2, al menos, eso se ve en la Asamblea posterior. Ver [[>debate/detalle-sobrecosto.html|el sobrecosto]].",
]

LECTURA = "La versión 2 acerca a las dos partes: el estadio y su techo se estudian primero y por separado, la plata del club para el estadio queda en su propio fideicomiso y los socios vuelven a votar con los números en la mano. A cambio, saca el veto de cada directivo y deja dos garantías en manos del Estatuto. Votar el 24 de octubre es aprobar un rumbo y un procedimiento; la decisión sobre la obra llega después. Antes de votar vale pedir que se corrijan las referencias que no cierran y que se aclare qué exige el Estatuto."

FUENTES_PORTADA = ["F-0026", "F-0007", "F-0003", "F-0004", "F-0014", "F-0015", "F-0016", "F-0017", "F-0019", "F-0021", "F-0022", "F-0023"]

# Qué tiene que pasar para que empiece la obra (arts. 2°, 5°, 6° y 9°).
OBRA = [
 ("Asamblea del 24/10", "los socios aprueban la moción {F-0026 p.2}."),
 ("Proyecto ejecutivo", "como mínimo del estadio, con y sin techo; para las otras unidades, ejecutivos o cotizaciones {F-0026 p.2-3}."),
 ("Modelo y evaluación", "actualizados con el ejecutivo, unidad por unidad y en combinaciones {F-0026 p.3}."),
 ("Contratos y financiamiento", "de las primeras etapas, aceptados técnicamente por la Directiva {F-0026 p.5}."),
 ("Segunda Asamblea", "convocada en 45 días; decide el alcance definitivo {F-0026 p.5}."),
 ("Condiciones de cada etapa", "permisos, modelo validado por CPA Ferrere u otra firma, financiamiento suficiente para terminarla con compromisos firmados, licitación, garantías y seguros, informe jurídico {F-0026 p.5}."),
]
OBRA_PLAZO = "El plazo para empezar es de 30 meses, con una sola prórroga de un año {F-0026 p.6}. Hoy no hay financiamiento comprometido: la v1 decía que los contactos con financiadores “no implican compromisos” {F-0007 p.2}."

# ¿Vuelve a votar la Asamblea? En estos casos.
VUELVE = [
 ("Siempre: con los ejecutivos, contratos y financiamiento de las primeras etapas, para decidir el alcance definitivo", "{F-0026 p.5}"),
 ("Una modificación que el Estatuto obligue a llevar a la Asamblea", "{F-0026 p.6}"),
 ("La autorización caducó y se quiere retomar", "{F-0026 p.6}"),
]
VUELVE_NOTA = "La v1 sumaba dos casos que la v2 ya no tiene: la falta de unanimidad en la Directiva y cualquier intento de reducir una garantía {F-0007 p.8-9}. Queda abierta la reforma del Estatuto que exige 75% para proyectos de más de USD 2 M: no rige todavía, y la moción se aplica “sin perjuicio de cualquier exigencia estatutaria más rigurosa que resulte vigente” {F-0026 p.1}. No tenemos el texto de la reforma para saber qué exigiría. Ver [[>debate/detalle-voto.html|la pregunta del voto]]."

# Apartado: la moción de la agrupación Atilio García (F-0023). No es oficial.
ALT_AVISO = "**No es una moción oficial.** La presentó la agrupación Atilio García, con apoyo de Decurnex, y su texto circula en X {F-0023}. Según la prensa, la versión 2 de la moción oficial se armó tomándola en cuenta y la agrupación está conforme; falta registrar la fuente. Lo que sigue la compara con la v2."
ALT_RESUMEN = [
 "**Aprueba solo un proyecto ejecutivo**, en un máximo de 180 días, con el estadio analizado por separado, el costo del techo aparte y cada área adicional analizada por separado. La v2 adopta el ejecutivo del estadio primero y el techo aparte, sin plazo {F-0026 p.2-3}.",
 "**Vuelve a la Asamblea** dentro de los 60 días de recibido el proyecto ejecutivo. La v2 convoca otra Asamblea en 45 días, cuando estén también los contratos y el financiamiento {F-0026 p.5}.",
 "**Flujos propios del club solo para el estadio:** palcos, gastos comunes, Club Social y sobrecuota. La v2 dice lo mismo, en un fideicomiso propio {F-0026 p.3-4}.",
 "**Garantías y fideicomiso:** repite el texto de la v1 de la moción oficial {F-0007 p.6-7}.",
 "**Comisión Técnico-Financiera** de cuatro miembros, designada por la Directiva, que trabaje con CPA Ferrere. La v2 no la incluye.",
]
# (tema, moción oficial v2, moción Atilio García)
ALT_TABLA = [
 ("Qué se aprueba", "El Master Plan como marco; las unidades se pueden excluir {F-0026 p.2}", "Solo hacer el proyecto ejecutivo"),
 ("Proyecto ejecutivo", "Primera etapa, como mínimo el estadio, con y sin techo; sin plazo {F-0026 p.2-3}", "Primero, en 180 días; no dice cómo se paga"),
 ("Estadio y techo por separado", "Sí {F-0026 p.3}", "Sí"),
 ("Nueva Asamblea", "En 45 días, con ejecutivos, contratos y financiamiento de las primeras etapas {F-0026 p.5}", "En 60 días, con el proyecto ejecutivo"),
 ("Mayoría especial de la Directiva", "No tiene; la v1 pedía unanimidad {F-0007 p.8}", "No la menciona"),
 ("Flujos propios solo para el estadio", "Sí, en un fideicomiso propio {F-0026 p.3-4}", "Sí"),
 ("Aporte del club a los otros negocios", "Solo derechos temporales de uso {F-0026 p.4}", "Solo el usufructo del padrón"),
 ("Plazo y caducidad", "30 meses más un año {F-0026 p.6}", "No tiene"),
 ("Comisión técnica", "Solo la Comisión de Licitaciones {F-0026 p.5}", "Cuatro miembros, con CPA Ferrere"),
]
# Qué opinaron de la moción alternativa, antes de la v2: (quién, rol, [citas])
ALT_OPINIONES = [
 ("José Decurnex", "Vocal de la Directiva · la apoyaba (30/09)", [
  "“A mí esa moción me seduce. Capaz que con algún pequeño cambio, algún agregado.” Se la planteó formalmente al presidente Vairo {F-0022 00:17:02}.",
  "Su prioridad era una moción única de toda la Directiva; si no, la presentaban en la Asamblea como “acorde al riesgo que este proyecto tiene” {F-0022 00:26:08}.",
  "El proyecto ejecutivo “lo vas a tener que hacer sí o sí”; reconoce que la plata no está en la caja, pero dice que propuso soluciones en la Directiva {F-0022 00:28:27}.",
  "Cada etapa “tiene que pasar necesariamente por asamblea” {F-0022 00:20:12}, y propone una comisión técnica de cuatro miembros que trabaje con CPA {F-0022 00:41:29}.",
 ]),
 ("Javier Gomensoro", "Prosecretario de la Directiva · en contra (30/09)", [
  "Exige primero un proyecto ejecutivo de “dos millones de dólares” como mínimo: “es un entierro de lujo para que no haya obras” {F-0021 00:13:37}.",
  "Con la v1, el proyecto ejecutivo se hacía cuando ya hubiera un inversor, y acotado a lo que se fuera a financiar {F-0021 00:13:46}.",
  "“No hay un plan alternativo”: no trae otro proyecto para el estadio {F-0021 00:17:36}. Duda de que quienes la impulsan pongan los 2 M si se aprueba {F-0021 00:47:19}.",
  "Es “mucho más honesto votar en contra” que presentar una moción alternativa {F-0021 01:05:19}. Ve en que la presente una agrupación una señal de que “esto es político” {F-0021 00:12:41}.",
 ]),
]

ALT_DICHOS = [
 "Decurnex dijo que su moción pide el 75% y que cada etapa pase por la Asamblea {F-0022 00:19:41}. **En este texto no aparece el 75%**, y hay una sola Asamblea nueva, no una por etapa. La v2 tampoco incluye ninguna de las dos cosas {F-0026}.",
 "Gomensoro la llamó “un entierro de lujo” porque exige gastar unos 2 M en el proyecto ejecutivo antes de tener un inversor {F-0021 00:13:37}. La v2 pone el proyecto ejecutivo del estadio como primera etapa {F-0026 p.2}. Los 2 M los dan las dos partes {F-0016 00:21:22} {F-0022 00:02:46}.",
 "Gomensoro dijo que tiene “plagio textual” de la oficial {F-0021 00:13:07}. Es un hecho que las garantías y el fideicomiso repiten el texto de la v1; llamarlo plagio es una valoración.",
]
