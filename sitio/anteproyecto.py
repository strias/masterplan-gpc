# Contenido de la página del anteproyecto (F-0004): qué se construye en cada etapa y
# cómo se compara con lo que dijeron las partes. Mismas marcas que mocion.py.
# Las páginas son las impresas; build.py suma la portada al enlazar el PDF.

# (etapa, obras, qué agrega, tipo: "estadio" o "negocio", página)
ETAPAS = [
 (1, "Estacionamiento en el nivel −2. Mudanza del estacionamiento existente y reubicación de las canchas de tenis.", "430 plazas de estacionamiento.", "negocio", "38"),
 (2, "Zócalo bajo la Atilio García, con frente a Urquiza, y bajo la Abdón Porte. Mejora de accesos a esas tribunas.", "3.100 m² de museos, 1.852 m² de locales (ampliables al doble con entrepisos), una tienda ancla de 1.228 m², cocina y área para eventos.", "negocio", "38"),
 (3, "Reforma de la cancha, que se baja 75 cm. Mejor visibilidad en la Atilio García, más filas en la Abdón Porte y codo Atilio García–Scarone.", "1.325 butacas nuevas y 3.567 con visibilidad mejorada.", "estadio", "38"),
 (4, "Bajo tribuna Delgado: vestuarios, acceso de delegaciones y servicios para competiciones. Codos del primer anillo.", "768 butacas nuevas y un salón VIP de 500 m².", "estadio", "39"),
 (5, "Bajo tribuna Scarone y restauración de su fachada patrimonial.", "728 butacas nuevas.", "estadio", "39"),
 (6, "Niveles 3 y 4: ampliación del codo Atilio García–Abdón Porte y tribuna con lounge entre la Atilio García y la Scarone.", "1.101 butacas nuevas, 159 en lounge y 1.494 m² para sede o alquiler.", "estadio", "39"),
 (7, "Codos del segundo anillo y superficies para alquilar detrás de la Delgado.", "2.310 butacas nuevas y 805 m² rentables.", "estadio", "39"),
 (8, "Arena polideportiva y nuevas áreas de prensa.", "Arena de 1.940 m² para 4.730 personas, gastronomía y un auditorio de e-sports.", "negocio", "40"),
 (9, "Estacionamiento en los niveles −1 y 0, y Plaza del Hincha.", "550 plazas y una plaza multievento de 3.969 m².", "negocio", "40"),
 (10, "Niveles 2, 3 y 4 alrededor de la Plaza del Hincha.", "11.138 m² rentables y 9.659 m² de terraza multiuso.", "negocio", "40"),
 (11, "Bandeja alta de la tribuna Héctor Scarone.", "2.015 butacas nuevas.", "estadio", "40"),
 (12, "Primera etapa del techo (Delgado y Atilio García), pantallas y cinta multimedia.", "199 m² de pantalla y 346 m de cinta.", "estadio", "41"),
 (13, "Segunda etapa del techo y reubicación de palcos.", "600 m² de muro multimedia.", "estadio", "41"),
 (14, "Tribunas y lounge elevados en las esquinas.", "1.358 butacas en lounge y 4.053 m² de lounge.", "estadio", "41"),
]
TIPOS = {"estadio": ("Estadio", "soft"), "negocio": ("Unidades de negocio", "pend")}

EN_CORTO = [
 "Es la memoria del proyecto ganador del concurso de ideas: 121 páginas de arquitectura, fechadas en junio de 2025 y publicadas a los socios el 23/09/2026 {F-0004} {F-0003}.",
 "Divide la obra en **14 etapas**. El estadio se sigue usando, salvo en las etapas 3 y 4, que se hacen juntas {F-0004 p.38}.",
 "**No trae costos, financiamiento ni plazos en años.** Eso queda para el modelo económico, que todavía no está publicado {F-0003}.",
 "Las dos primeras etapas son de unidades de negocio: estacionamiento y zócalo comercial. **La primera obra en el estadio es la etapa 3**, y el techo va al final, en las etapas 12 y 13 {F-0004 p.38-41}.",
]

ORDEN = [
 "El anteproyecto ordena las etapas para “acompasar en forma equilibrada los egresos y la generación de ingresos de cada etapa” {F-0004 p.38}. Por eso empieza por el estacionamiento y el zócalo comercial, que generan ingresos.",
 "La moción, en cambio, dice que “deberá priorizarse el inicio de aquellas etapas que involucren directamente al Estadio”, aunque “en función de los flujos y plazos disponibles” {F-0007 p.6}.",
 "El anteproyecto es de junio de 2025 y la moción de septiembre de 2026: el orden puede cambiar. Ninguno de los dos documentos dice cuál va a ser.",
]

# (tema, quién y dónde, qué dice el anteproyecto, estado, [enlace al debate])
CONTRASTE = [
 ("980 plazas de estacionamiento", "Singlet {F-0017 00:39:24}",
  "980 lugares: 430 en la etapa 1 y 550 en la 9 {F-0004 p.42}. El texto de la misma página redondea a 1.000.", "consistente", "debate/detalle-parking.html"),
 ("La bajada de la cancha está incluida", "Aldabalde {F-0014 01:29:17}",
  "Etapa 3: “reforma de la cancha, se baja 75 cm” {F-0004 p.38}.", "consistente", None),
 ("“10 mil butacas nuevas”", "Aldabalde {F-0014 01:52:45}",
  "Sumando las etapas salen 10.116 (8.247 generales y 1.869 de hospitalidad), coherente con pasar de unos 34.000 a más de 43.000 lugares {F-0004 p.64}. Pero el total de la misma memoria dice 16.544 butacas nuevas {F-0004 p.42}.", "parcial", None),
 ("Zócalo comercial de 3.500 o 7.000 m²", "Aldabalde {F-0014 01:08:14}",
  "3.080 m² de locales {F-0004 p.42}: 1.852 ampliables al doble con entrepisos más una tienda ancla de 1.228 {F-0004 p.38}. Con entrepisos serían 4.932 m². Los 7.000 m² no aparecen en el documento.", "parcial", None),
 ("El techo cuesta unos 20 M", "Aldabalde {F-0014 00:53:46}; Singlet, 21,5 M {F-0017 01:41:45}",
  "Lo ubica en las etapas 12 y 13, las últimas antes de las esquinas {F-0004 p.41}. No da su costo.", "pendiente", None),
 ("La cotización no incluye césped, mobiliario, audio ni anclajes del techo", "Decurnex {F-0015 00:08:11}; Singlet {F-0017 00:51:51}",
  "El anteproyecto no tiene costos, así que no se puede contrastar con él. La crítica es sobre la cotización y el modelo, que no están publicados.", "pendiente", "debate/detalle-costo.html"),
 ("La obra lleva cuatro o cinco años", "Aldabalde {F-0016 00:07:30}",
  "No da plazos en años.", "pendiente", None),
]

# Cuentas propias con las cifras del documento.
CUENTAS = [
 ("Estacionamiento", "430 + 550 = 980", "980 (p. 42)", "consistente"),
 ("Locales comerciales", "1.852 + 1.228 = 3.080 m²", "3.080 m² (p. 42)", "consistente"),
 ("Superficies rentables", "1.494 + 805 + 11.138 + 500 + 329 = 14.266 m²", "14.266 m² (p. 42)", "consistente"),
 ("Butacas de hospitalidad", "159 + 281 + 71 + 1.358 = 1.869", "1.869 (p. 42)", "consistente"),
 ("Butacas nuevas", "8.247 generales + 1.869 de hospitalidad = 10.116", "16.544 (p. 42)", "cuenta"),
 ("Aforo", "", "“más de 43.000” (p. 64) y “44.000” (p. 42)", "parcial"),
]

NO_TRAE = [
 ("Costos", "Ni de la obra ni de cada etapa."),
 ("Financiamiento y plazos", "Ni cómo se paga ni cuántos años lleva cada etapa."),
 ("Datos sin completar", "En p. 34 el estacionamiento figura como “XXX”, y en p. 42 la Plaza del Hincha y la arena como “XX”, aunque en la misma página están las cifras."),
 ("Un error corregido", "En p. 51 ubica a la hinchada visitante en la Abdón Porte; los autores aclararon que es la Héctor Scarone {F-0006}."),
]

AVISO = "Este análisis es de Claude, la IA que asiste al proyecto, y es opinión. Se apoya en el anteproyecto, la moción y las fuentes enlazadas y, donde lo indica la etiqueta <span class=\"cg\">conocimiento general</span>, en conocimiento general de obras que no sale de una fuente registrada."

ANALISIS = [
 "**Las mejoras del estadio están repartidas en casi toda la obra.** De las 14 etapas, nueve son del estadio, pero las que más cambian la experiencia del hincha van al final: la bandeja alta de la Scarone en la 11 y el techo en la 12 y la 13 {F-0004 p.40-41}. Quien vote pensando en “terminar el Parque” tiene que saber que, en este orden, el techo es de lo último.",
 "**Empezar por el estacionamiento tiene lógica de obra, y también de caja.** La etapa 1 incluye mudar el estacionamiento existente y reubicar las canchas de tenis {F-0004 p.38}, algo que suele hacerse antes para liberar espacio [[CG]]. Y el propio documento dice que el orden busca equilibrar egresos e ingresos {F-0004 p.38}. Que eso choque o no con la prioridad al estadio que pide la moción {F-0007 p.6} depende del orden definitivo, que ninguno de los dos documentos fija.",
 "**Si cada etapa necesita su propio financiamiento, las últimas dependen de las primeras.** La moción exige financiamiento suficiente para completar cada etapa antes de empezarla {F-0007 p.7}. Si los ingresos de las primeras unidades rinden menos de lo previsto, lo que más se atrasa es justo lo que va al final: el techo y la bandeja alta [[CG]]. Ver [[>debate/detalle-sobrecosto.html|el sobrecosto]] y [[>debate/detalle-solo.html|solo el estadio]].",
 "**El documento es sólido en lo que cuenta y deja afuera lo que se discute.** Casi todos sus totales cierran con las etapas; la excepción son las 16.544 butacas nuevas. Pero el debate es sobre plata, y el anteproyecto no tiene ni un número de costo. Por eso la mayoría de las críticas (costo, techo, estacionamiento) no se pueden contrastar con él: hace falta el modelo económico.",
]

LECTURA = "El anteproyecto dice qué se construye y en qué orden, pero no cuánto cuesta. En su orden actual, primero vienen el estacionamiento y el zócalo comercial, y el techo va entre lo último. La moción pide priorizar el estadio sin fijar un orden nuevo. Antes de votar vale preguntar en qué orden se va a hacer y cuándo llega cada mejora del estadio."

FUENTES_PAGINA = ["F-0004", "F-0006", "F-0003", "F-0007", "F-0014", "F-0015", "F-0016", "F-0017"]
