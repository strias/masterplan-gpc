# Contenido de la página de las cuentas: el resumen ejecutivo financiero (F-0036), que resume el
# estudio de prefactibilidad de CPA Ferrere. Mismas marcas que mocion.py: {F-0036 p.2}, **negrita**,
# [[#id|texto]], [[>ruta|texto]] y [[CG]]. Las páginas son las del PDF.

EN_CORTO = [
 "El 10/10 el club publicó un **resumen ejecutivo financiero** para socios, con acceso público. Es el primer documento con costos, deuda y plazos de repago {F-0036 p.1} {F-0003}.",
 "Resume un estudio de **CPA Ferrere** encargado por la Directiva. El estudio completo y el modelo económico todavía no están publicados {F-0036 p.1} {F-0008}.",
 "Compara **cuatro alternativas**: el Master Plan entero o solo el estadio, cada uno con y sin techo. Según el resumen, las cuatro “presentan viabilidad financiera preliminar” {F-0036 p.1}.",
 "El Master Plan completo cuesta **105 M de dólares** (93,6 M a precios de 2025). El techo son unos **21,5 M** {F-0036 p.2} {F-0036 p.3}.",
 "Los socios y otras iniciativas tendrían que aportar el **25% del costo**: 26,3 M en el plan completo, 8,8 M en el estadio sin techo {F-0036 p.2}.",
 "La moción que se vota no aprueba estas cifras: son preliminares y se actualizan con el proyecto ejecutivo {F-0036 p.6} {F-0026 p.3}.",
]

# (nombre, qué incluye)
ALTERNATIVAS = [
 ("Master Plan integral", "El estadio remodelado y ampliado, con el Arena, los estacionamientos, los espacios comerciales y rentables y el resto del complejo {F-0036 p.1}."),
 ("Integral sin techo", "Las mismas unidades, “excluyendo o postergando la cubierta del estadio” {F-0036 p.2}."),
 ("Estadio GPC", "Solo el estadio, con hospitalidad y un estacionamiento de 430 plazas. Sin Arena, sin espacios comerciales y rentables y sin Plaza del Hincha {F-0036 p.2}."),
 ("Estadio GPC sin techo", "El mismo alcance, sin la cubierta. Es la alternativa con menor inversión y menor aporte {F-0036 p.2}."),
]

# Tabla: (alternativa, costo, aportes, deuda, repago base, +10/−10, +20/−20, retiros tras el repago)
TABLA = [
 ("Master Plan integral", "105,0", "26,3", "90,9", "13 años", "14 años¹", "19 años¹ (reestructurar el plazo)", "17,5 M/año promedio desde 2045"),
 ("Integral sin techo", "83,5", "20,9", "76,5", "10 años", "14 años", "14 años¹", "No reportado"),
 ("Estadio GPC", "56,6", "14,2", "49,4", "15 años¹", "15 años¹ ²", "No repaga con la estructura base³", "8,8 M/año promedio desde 2047"),
 ("Estadio GPC sin techo", "35,1", "8,8", "35,0", "10 años", "13 años", "15 años¹", "No reportado"),
]
TABLA_NOTAS = [
 "¹ Aplica caja acumulada a amortizaciones extraordinarias.",
 "² Cancela en 15 años, pero incumple la cobertura de deuda (1,3 veces) en algunos ejercicios.",
 "³ Hay faltantes de fondos. Con una coinversión del 30% (USD 3,4 M más), el repago se proyecta en 22 años {F-0036 p.5}.",
 "“No reportado”: el resumen no da el dato. No se estimó.",
]

COMO_LEER = [
 ("Costo de obra", "Precios corrientes del cronograma: el plan completo cuesta 93,6 M a precios de 2025 y 105,0 M con la suba de precios durante la obra. No es todo lo que hace falta: el modelo suma honorarios, seguros, costos del financiamiento y caja {F-0036 p.2}."),
 ("Aportes", "Una coinversión del 25% del costo, “a recaudar mediante contribuciones voluntarias y otras iniciativas”: sobrecuota voluntaria, Muro de la Historia y otras. El monto final depende de lo que pidan los financiadores {F-0036 p.2} {F-0036 p.3}."),
 ("Deuda", "La toma un fideicomiso con patrimonio separado. El esquema “busca que Nacional no asuma la deuda del proyecto ni actúe como garante” {F-0036 p.3}. No es el costo menos los aportes: depende de la caja de cada año {F-0036 p.3}."),
 ("Repago", "Años para cancelar la deuda, no años de obra. Tasa de referencia del 7,1% y plazo indicativo de 15 años {F-0036 p.2} {F-0036 p.4}."),
 ("Sensibilidades", "Qué pasa si la obra sale 10% o 20% más cara y los ingresos son 10% o 20% menores. No dicen qué tan probable es cada caso {F-0036 p.4}."),
]

# (alternativa, qué pasa si las cosas salen peor), del texto del resumen
ESTRES = [
 ("Master Plan integral", "Con desvíos del 10% repaga dentro de 15 años. Con obra 20% más cara e ingresos 20% menores, el repago se va a 19 años y “sería necesario reestructurar el plazo de la deuda”, aunque podría cancelarse dentro de la vigencia del fideicomiso {F-0036 p.5}."),
 ("Integral sin techo", "En los dos escenarios combinados, el repago queda dentro de 15 años {F-0036 p.5}."),
 ("Estadio GPC", "Es la que tiene “menor holgura”. Con desvíos del 10% puede repagar usando caja, pero incumple la cobertura exigida en algunos años. Con desvíos del 20%, “la estructura base resulta insuficiente” {F-0036 p.5}."),
 ("Estadio GPC sin techo", "Repaga entre 10 y 15 años. En el escenario del 20% necesita usar caja para pagos extraordinarios {F-0036 p.5}."),
]
ESTRES_NOTA = "En todos los escenarios los aportes siguen siendo el 25% del costo, así que suben si la obra se encarece: en el plan completo, de 26,3 M a 31,5 M con un sobrecosto del 20%. Las cifras de repago suponen que esa plata se consigue {F-0036 p.5}."

RETIROS = [
 "Las proyecciones siguen hasta 2055. Una vez cancelada la deuda, Nacional retiraría en promedio **17,5 M por año desde 2045** con el plan completo, y **8,8 M por año desde 2047** con el estadio solo {F-0036 p.6}.",
 "Son **dólares corrientes futuros**, sin contar retiros extraordinarios de caja. El resumen no da su valor de hoy {F-0036 p.6}.",
 "Para las dos variantes sin techo, el resumen **no da retiros**.",
]

# (tipo de recurso, qué incluye)
RECURSOS = [
 ("Aportes para la inversión", "Sobrecuota voluntaria, Muro de la Historia y otras iniciativas de recaudación."),
 ("Recursos que ya tiene el club", "Renovaciones futuras de palcos y excedentes del Club Social, una vez canceladas sus obligaciones."),
 ("Actividades nuevas del estadio", "Hospitalidad, publicidad digital, espectáculos y derechos de denominación."),
 ("Nuevas unidades del complejo", "Alquiler de locales y superficies rentables, explotación del Arena y del estacionamiento."),
]
RECURSOS_NOTA = ("Los recursos que ya tiene el club “contribuyen al repago, pero no constituyen ingresos creados por la inversión” {F-0036 p.4}. "
                 "Supuestos: casi 20.000 m² rentables alquilados a 20 y 25 dólares el m², con 2,5% de vacancia; los 239 palcos renovados a un promedio de 100.000 dólares por diez años; y 1,25 M por año del Club Social desde 2030 {F-0036 p.4}. "
                 "“Las estimaciones comerciales no han sido confirmadas mediante estudios independientes” {F-0036 p.4}.")

NO_DICE = [
 ("El estudio completo", "El resumen cita tablas y secciones de un estudio de octubre que no está publicado. El modelo sigue con “Carga pendiente”, solo para socios habilitados {F-0003} {F-0008}."),
 ("El techo y los ingresos", "En las variantes sin techo, el modelo supone los mismos ingresos que con techo. El propio resumen dice que eso “deberá contrastarse” {F-0036 p.3}."),
 ("Cómo se calculó el estadio solo", "Las variantes de estadio y sin techo salen de “asignaciones y deducciones del presupuesto integral”, no de un presupuesto propio {F-0036 p.3}."),
 ("El valor de hoy de los retiros", "Los retiros están en dólares de 2045 en adelante, sin valor presente {F-0036 p.6}."),
 ("Probabilidades", "Las sensibilidades no dicen qué tan probable es cada escenario ni cubren todos los riesgos {F-0036 p.4}."),
 ("Dos cifras por contrastar", "Habla de casi 20.000 m² rentables; el anteproyecto da 14.266 m² rentables y 3.080 m² de locales {F-0037 p.42}. Y cuenta 239 palcos; una respuesta oficial del sitio dice 240 {F-0003}."),
]

AVISO = "Este análisis es de Claude, la IA que asiste al proyecto, y es opinión. Se apoya en el resumen financiero y las fuentes enlazadas. Las cuentas propias están marcadas como tales."

ANALISIS = [
 "**En los escenarios malos, lo que más pesa es el techo.** Con obra 20% más cara e ingresos 20% menores, las dos variantes con techo pasan los 15 años o no repagan, y las dos sin techo quedan en 15 años o menos {F-0036 p.5}. Pero esa lectura depende del supuesto de que sacar el techo no cambia los ingresos {F-0036 p.3}: si el techo trae hospitalidad, espectáculos o publicidad, las variantes sin techo se ven mejor de lo que son.",
 "**El plan completo no es más seguro que el estadio solo, pero deja más.** Con desvíos del 20%, el plan completo necesita reestructurar la deuda (19 años) y el estadio con techo no repaga {F-0036 p.5}: ninguno de los dos con techo resiste ese escenario con la estructura base. Después del repago, el plan completo dejaría unas dos veces lo del estadio solo por año (17,5 M contra 8,8 M), con un costo unas 1,9 veces mayor (105,0 contra 56,6) {F-0036 p.2} {F-0036 p.6}. Cuenta propia y gruesa: mezcla años distintos y dólares corrientes.",
 "**El esfuerzo de los socios crece con el alcance.** Los aportes van de 8,8 M a 26,3 M según la alternativa, y suben si la obra se encarece {F-0036 p.2} {F-0036 p.5}. El resumen los describe como voluntarios {F-0036 p.2}; cuánto se recaude es uno de los supuestos de los que dependen todos los plazos.",
 "**Es un buen resumen, con un límite claro.** Declara sus propios límites: estimaciones comerciales sin validar, sensibilidades sin probabilidades y supuestos por contrastar {F-0036 p.3} {F-0036 p.4}. Pero lo escribe el club, que impulsa la moción, sobre un estudio que nadie de afuera puede leer todavía. Hasta que se publique el estudio, sus cifras se pueden citar, no verificar.",
]

LECTURA = ("Según el resumen, las cuatro alternativas se pueden pagar en el escenario base; el plan completo cuesta 105 M y deja más plata después, y las variantes sin techo son las que mejor resisten si las cosas salen peor. "
           "Antes de votar vale preguntar cuánto se espera recaudar entre los socios, si sacar el techo cambia los ingresos y cuándo se publica el estudio completo. "
           "La moción no aprueba estos números: los socios vuelven a votar con el proyecto ejecutivo y el financiamiento a la vista {F-0026 p.5}.")

FUENTES_PAGINA = ["F-0036", "F-0008", "F-0003", "F-0037", "F-0026"]
