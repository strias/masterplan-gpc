# Contenido de la portada: análisis de la moción oficial (F-0007). Mismas marcas que
# detalle.py: {F-0007 p.6} enlaza a la página, {F-0014 01:55:53} al minuto, [[CG]]
# marca conocimiento general y [[>debate/detalle-plata.html|texto]] enlaza a otra página.

EN_CORTO = [
 "Se aprueba el Master Plan como **marco** y se autoriza a la Directiva a seguir estructurándolo. Eso solo **no habilita** obras, financiamiento, garantías ni contratos definitivos {F-0007 p.6}.",
 "El proyecto va a un **fideicomiso** con patrimonio y cuentas separadas. El club no es garante, no hipoteca el Parque y no pone capital para sobrecostos ni déficits {F-0007 p.6-7}.",
 "Al proyecto pueden ir los flujos de **palcos y Club Social**, los ingresos nuevos del Master Plan y aportes extraordinarios. Los flujos que ya existen solo pueden ir al estadio {F-0007 p.7}.",
 "Ninguna etapa empieza sin proyecto ejecutivo, permisos, modelo validado, **financiamiento suficiente para completarla**, licitación e informe jurídico {F-0007 p.7-8}.",
 "Las decisiones centrales necesitan el voto **unánime de los once** directivos. Si no lo hay, decide una nueva Asamblea {F-0007 p.8}.",
 "Si en **30 meses** no empezó ninguna etapa sustancial, caduca la autorización, con una sola prórroga de un año {F-0007 p.9}.",
]

ARTICULOS = [
 ("Primero", "Aprobación institucional", "Aprueba el Master Plan como marco arquitectónico, estratégico y funcional, con ejecución por etapas y la integración del estadio con arena, Plaza del Hincha, estacionamientos y las demás unidades del proyecto.", "p.6", None),
 ("Segundo", "Alcance de la autorización", "Autoriza a la Directiva, con la CPO y asesores, a seguir con estudios, proyectos ejecutivos, permisos, licitaciones y negociaciones. “Deberá priorizarse el inicio de aquellas etapas que involucren directamente al Estadio.” No habilita obras, financiamiento, garantías ni afectación de activos o ingresos.", "p.6", ("solo", "¿Se puede terminar solo el estadio?")),
 ("Tercero", "Fideicomiso", "Fideicomiso de propósito específico con patrimonio, contabilidad, cuentas y flujos separados, administración profesional y controles independientes. La operación del complejo debe preservar la actividad de los planteles principales.", "p.6", None),
 ("Cuarto", "Protección del patrimonio y de la caja", "Seis límites acumulativos: sin deuda ni garantías del club; sin capital para sobrecostos o déficits; sin hipotecas ni venta de bienes; derechos de uso temporales y reversibles; solo se asignan palcos, Club Social, ingresos nuevos y aportes extraordinarios; los flujos existentes solo van al estadio; restitución al club de lo que aporte.", "p.6-7", ("plata", "¿Nacional pone plata?")),
 ("Quinto", "Condiciones antes de cada etapa", "Proyecto ejecutivo, cronograma y presupuesto; permisos; modelo actualizado y validado por CPA Ferrere u otra firma independiente; financiamiento suficiente para completar la etapa, con compromisos vinculantes; licitación con una Comisión de Licitaciones; contratos, garantías y seguros; informe jurídico.", "p.7-8", ("sobrecosto", "¿Qué pasa si sale más cara?")),
 ("Sexto", "Mayoría especial de la Directiva", "Unanimidad de los once para el fideicomiso, el modelo definitivo, las contrapartes, los contratos de financiamiento, el presupuesto e inicio de cada etapa y las adjudicaciones. Sin unanimidad, si la mayoría simple quiere seguir, se convoca una Asamblea en 30 días.", "p.8", ("voto", "¿Qué se vota y con qué mayoría?")),
 ("Séptimo", "Control y transparencia", "Declaración y abstención ante conflictos de interés, auditoría externa, informes trimestrales a la Directiva e informe a los socios al menos cada seis meses, “sin perjuicio de la reserva exigible durante negociaciones o procesos competitivos”.", "p.8", None),
 ("Octavo", "Cambios sustanciales", "Vuelven a la Asamblea los cambios que alteren la esencia del Master Plan, comprometan más ingresos ordinarios, agreguen deuda o garantías del club, afecten la propiedad de sus bienes o quiten garantías.", "p.9", None),
 ("Noveno", "Plazo y caducidad", "A los 30 meses sin inicio material de una etapa sustancial, la Directiva decide si sigue y puede prorrogar una vez por un año. Si vence, cae la autorización del artículo 2°, no la aprobación del 1°. Demoliciones menores o movimientos hechos para evitar el plazo no cuentan.", "p.9", None),
 ("Décimo", "Reglamentación", "La Directiva reglamenta la resolución. Ningún acto posterior puede reducir las garantías sin una nueva Asamblea Extraordinaria.", "p.9", None),
]

RESPUESTAS = {
 "si": ("La moción lo responde", "ok"),
 "parte": ("Lo responde en parte", "soft"),
 "no": ("La moción no lo trata", "pend"),
}

# (id de la pregunta del debate, pregunta, respuesta, qué dice la moción)
DEBATE = [
 ("plata", "¿Nacional pone plata en el proyecto?", "si",
  "Sí, y dice cuál: palcos (venta, renovación, uso y gastos comunes), dividendos del Club Social y aportes extraordinarios. Esos flujos, cuando ya existen, solo pueden ir al estadio, y el modelo debe prever su restitución al club {F-0007 p.7}. Es lo que describían tanto Aldabalde como Decurnex."),
 ("sobrecosto", "¿Qué pasa si la obra sale más cara?", "parte",
  "El club no pone capital para sobrecostos y ninguna etapa empieza sin financiamiento suficiente para completarla, con garantías y seguros {F-0007 p.7-8}. No dice qué pasa si una etapa se queda sin fondos a mitad de camino."),
 ("voto", "¿Qué se vota y con qué mayoría?", "parte",
  "Dice qué se vota: el marco y la autorización para estructurar, no la obra {F-0007 p.6}. No fija con qué mayoría decide la Asamblea: se remite a los Estatutos “sin perjuicio de cualquier exigencia estatutaria más rigurosa que resulte vigente” {F-0007 p.5}."),
 ("solo", "¿Se puede terminar solo el estadio?", "parte",
  "Pide priorizar las etapas del estadio {F-0007 p.6}, pero aprueba el conjunto con arena, estacionamiento y zócalo comercial {F-0007 p.6}. No evalúa la alternativa de solo estadio. Pasar a ella parece un cambio de la “esencia” del Master Plan, que vuelve a la Asamblea {F-0007 p.9}."),
 ("cuota", "¿Va a haber una cuota extra? ¿Es obligatoria?", "no",
  "Solo menciona “aportes extraordinarios que se generen para estos fines” {F-0007 p.7}. No dice monto, si son voluntarios ni quién los aprueba."),
 ("costo", "¿Cuánto cuesta la obra?", "no",
  "No da ninguna cifra. Exige un presupuesto por etapa antes de empezarla {F-0007 p.7} y dice que las estimaciones de CPA Ferrere “mantienen carácter evolutivo” {F-0007 p.2}."),
 ("570", "¿El proyecto genera 570 millones?", "no",
  "No da cifras de ingresos. Dice que el repago debería salir “de los nuevos flujos creados o potenciados por el propio Máster Plan” {F-0007 p.3}."),
 ("parking", "¿El estacionamiento da ganancia?", "no",
  "Lo incluye entre las unidades aprobadas {F-0007 p.6}, sin números."),
]

NO_DICE = [
 ("Costo, financiamiento e ingresos", "Ninguna cifra. Quedan para el modelo definitivo, que aprueba la Directiva por unanimidad {F-0007 p.8}."),
 ("Aporte de socios", "Ni monto, ni si es voluntario, ni quién lo aprueba {F-0007 p.7}."),
 ("Mayoría de la Asamblea", "Se remite a los Estatutos {F-0007 p.5}."),
 ("Fondos que no alcanzan a mitad de una etapa", "Prevé el comienzo, no el medio de la obra {F-0007 p.7-8}."),
 ("Sanciones por incumplir", "Ninguna. Aldabalde dijo que van en el Estatuto {F-0014 01:59:47}."),
 ("Conclusiones del Consejo Asesor", "Las presentará “oportunamente” a la Directiva {F-0007 p.2}; no dice si antes de la Asamblea."),
 ("Votación de la Directiva", "El documento no dice cómo se aprobó el texto ni lleva firma."),
]

# Afirmaciones de hecho de los antecedentes. Estados del debate (ESTADOS en build.py).
HECHOS = [
 ("Aprobación unánime de la CPO (2/7/2025) y de la Directiva (4/8/2025)", "{F-0007 p.1}", "pendiente",
  "Coincide con lo que dijo Aldabalde, presidente de la CPO: “agosto” y unanimidad {F-0014 00:53:14}. Falta una fuente independiente del club, como el acta de la Directiva. Un conductor de Pasión Tricolor habla de una aprobación unánime “en cuanto a la idea” {F-0019 00:13:28}."),
 ("Unas cinco hectáreas, unos 50.000 m²", "{F-0007 p.1} {F-0007 p.3}", "consistente",
  "El anteproyecto da 48.000 m² de terreno {F-0004 p.15}."),
 ("Encuesta de 2025 con casi 14.000 respuestas", "{F-0007 p.1}", "pendiente",
  "No hay fuente registrada con los resultados."),
 ("Primer concurso de arquitectura del club desde 1957", "{F-0007 p.1}", "pendiente",
  "No hay fuente registrada."),
 ("Consejo Asesor externo que examinó el modelo", "{F-0007 p.2}", "pendiente",
  "No se sabe quiénes lo integran ni qué concluyó."),
]

AVISO = "Este análisis es de Claude, la IA que asiste al proyecto, y es opinión. Se apoya en la moción y en las fuentes enlazadas y, donde lo indica la etiqueta <span class=\"cg\">conocimiento general</span>, en conocimiento general de finanzas y fideicomisos que no sale de una fuente registrada. No es una opinión jurídica."

ANALISIS = [
 "**Es una moción de garantías más que de proyecto.** De los diez artículos, los dos primeros aprueban y autorizan; los otros ocho ponen límites a la Directiva. Responde con claridad la preocupación que compartían las dos partes, que el club no se endeude ni hipoteque el Parque {F-0007 p.6-7}. En eso, lo que decía Aldabalde {F-0014 01:56:05} queda escrito.",
 "**La unanimidad cambia el equilibrio.** La Directiva votó 7 a 4 convocar la Asamblea {F-0015 00:05:51}. Con unanimidad, cualquiera de los once puede frenar cada decisión central. La salida es convocar otra Asamblea en 30 días {F-0007 p.8}. En la práctica, si el desacuerdo sigue, las decisiones grandes vuelven a los socios. Eso contesta en parte el temor de Singlet de que se relegue a las asambleas {F-0017 00:17:46}. El costo posible: más asambleas y más demora.",
 "**El 24 de octubre se decide el rumbo, no los números.** Costo, cuota, ingresos y estacionamiento, que son casi todo el debate, no están en la moción. Los va a decidir la Directiva después, por unanimidad y con el modelo actualizado {F-0007 p.7-8}. Hoy el modelo no está publicado {F-0003} y la propia moción llama “evolutivas” sus estimaciones {F-0007 p.2}; el Consejo Asesor presentará sus conclusiones “oportunamente”, sin fecha {F-0007 p.2}. Si eso está bien es un desacuerdo de valores: Decurnex quiere el ejecutivo antes de votar {F-0015 00:11:39}; Aldabalde, no gastar 2 M sin respaldo {F-0016 00:21:22}. Ver [[>debate/#voto|la pregunta del voto]].",
 "**Lo que sí queda fijado pesa.** El artículo 1° adopta este Master Plan, con arena, estacionamiento y zócalo comercial, y sobrevive aunque caduque la autorización {F-0007 p.9}. Una alternativa de solo estadio, como la que estudian Singlet y Bardanca {F-0017 01:20:05}, tendría que volver a la Asamblea como cambio sustancial {F-0007 p.9}.",
 "**El aporte de socios es el punto más abierto.** La moción permite asignar “aportes extraordinarios” sin decir si son voluntarios {F-0007 p.7}. Bardanca sostiene que un financiador pide un aporte propio que no sea voluntario {F-0017 00:54:19}. Si eso termina en una suba de cuota, no queda claro si cuenta como “comprometer ingresos ordinarios adicionales”, que obligaría a volver a la Asamblea {F-0007 p.9}. Convendría que la reglamentación lo aclare. Ver [[>debate/detalle-cuota.html|la cuota]].",
 "**Sin capital del club para sobrecostos, el riesgo lo toma otro.** Un financiador sin garantía del club suele pedir más contingencia, más tasa o menos alcance [[CG]]. Es probable que el financiamiento real sea más caro o más chico que el modelado, y eso no se ve hasta la etapa de contratos. Ver [[>debate/detalle-sobrecosto.html|el sobrecosto]].",
 "**Las garantías dependen de quien las haga cumplir.** El artículo 10° impide que la Directiva las reduzca sin una Asamblea {F-0007 p.9}, pero no hay sanciones. La información a los socios es semestral y admite reserva durante las negociaciones {F-0007 p.8}. Tampoco se definen “etapa sustancial” ni “inicio material” más allá de lo que no cuenta {F-0007 p.9}. Son puntos para la reglamentación.",
]

LECTURA = "La moción protege bien la caja y el patrimonio del club, y suma un control fuerte: unanimidad en la Directiva o vuelta a los socios. No contesta las preguntas de números del debate, que quedan para decisiones posteriores bajo esas reglas. Votar el 24 de octubre es aprobar un rumbo y un sistema de garantías. Si alcanza con eso, sin conocer todavía el modelo, es la pregunta que cada socio tiene que responder."

FUENTES_PORTADA = ["F-0007", "F-0003", "F-0004", "F-0014", "F-0015", "F-0016", "F-0017", "F-0019"]
