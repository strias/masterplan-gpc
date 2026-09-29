# Metodología

## Tipos de fuente

| Tipo | Ejemplos | Peso |
|---|---|---|
| **Primaria oficial** | Documentos del club, resoluciones de la Intendencia, expedientes, actas, estados contables | Alto |
| **Primaria técnica** | Estudios de impacto, informes de arquitectos o consultoras, planos | Alto (se evalúan sus supuestos) |
| **Datos públicos** | INE, catastro, registros públicos | Alto |
| **Prensa** | Notas periodísticas, entrevistas | Medio (se sigue hasta la fuente primaria) |
| **Declaración** | Dichos de actores en medios, redes o asambleas | Registra *qué se dijo*, no prueba *que sea cierto* |
| **Análisis propio** | Cálculos y comparaciones de este repo | Siempre con el método y los datos a la vista |

## Tipos de afirmación

- **Hecho verificable:** "El proyecto prevé X m² comerciales".
- **Estimación o proyección:** "Va a generar X empleos". Se evalúan los supuestos y el método, no solo el número.
- **Opinión o valoración:** "Es un mal negocio para el club". No recibe veredicto de verdad; se identifican los hechos en los que se apoya y se verifican esos.

## Escala de veredictos

| Veredicto | Significado |
|---|---|
| ✅ **Verdadero** | La evidencia la respalda sin reparos relevantes |
| 🟢 **Mayormente verdadero** | Correcta en lo esencial, con matices o imprecisiones menores |
| 🟡 **Engañoso** | Tiene datos ciertos pero omite contexto clave o lleva a una conclusión equivocada |
| 🟠 **Mayormente falso** | Tiene algún elemento cierto, pero lo esencial no se sostiene |
| 🔴 **Falso** | La evidencia la contradice |
| ⚪ **No verificable** | No hay información pública suficiente para evaluarla |
| 💬 **Opinión** | Es una valoración y no admite veredicto de verdad |

## Vigencia de la información

El proyecto se discute públicamente desde hace casi dos años y sus datos cambiaron: costos, etapas, plazos y alcance.

- Toda fuente lleva su **fecha de publicación**. Sin fecha no se usa como evidencia de un dato del proyecto.
- Cuando un dato cambia, **vale el más reciente**. El anterior no se borra: queda registrado como reemplazado, con la fecha y la fuente del cambio.
- Una afirmación se evalúa contra lo que se sabía **a su fecha**. Si era correcta entonces y después el dato cambió, no es falsa: queda como **desactualizada** y se enlaza el dato vigente.

## Cómo citar

- Cada dato lleva el ID de su fuente y, si es un documento, la página: `F-0004, p. 42`.
- `p. N` es el número impreso en la página, no el del visor del PDF. Si difieren, la ficha de la fuente lo aclara.
- Los videos se citan con marca de tiempo (`F-0005, 03:15`).
- Las transcripciones de audio y video se publican en `transcripciones/`, con los nombres propios corregidos y la lista de correcciones al final. Son automáticas: sirven para ubicar el minuto, pero la cita se verifica contra el video. Cuando hay una transcripción con separación de voces y también subtítulos de YouTube, se combinan: la base es la de voces y, donde las cifras no coinciden, se muestra también la versión de YouTube. Se generan con `scripts/transcripciones.py`. Si no hay separación de voces, se pueden asignar a mano según el contenido, en `scripts/voces/<ID>.tsv`; la transcripción lo aclara como interpretación.
- Las fichas de documentos registran versión, fecha de carga y hash SHA-256, para saber exactamente qué versión se citó.

## Reglas

1. Toda afirmación se registra con su cita textual, autor, fecha y fuente original.
2. Antes de evaluar, se redacta la **versión más fuerte** de la postura.
3. El veredicto explica el razonamiento y enlaza cada pieza de evidencia.
4. Los veredictos pueden cambiar ante nueva evidencia. El cambio se registra en la ficha y queda en el historial de git.
5. Mismo estándar para todos los actores, estén a favor o en contra.
6. Las opiniones del modelo van solo en secciones marcadas como tal, separadas de los hechos, y no cuentan como veredicto. Ver «Opiniones del modelo» en el [README](../README.md).
