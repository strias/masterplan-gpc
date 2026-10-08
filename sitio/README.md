# Sitio

Sitio estático con cuatro partes:

- **Portada** (`index.html`): guía para el socio sobre la Asamblea del 24 de octubre. Qué se vota, cómo votar, el proyecto en cifras, qué protege al club (citado del texto de la moción), por qué la apoyan (con las palabras de cada uno), preguntas frecuentes y qué queda abierto. Contenido en `guia.py`.
- **Moción** (`mocion/`): la moción oficial, versión 2 ([F-0026](../fuentes/F-0026-mocion-asamblea-v2.md)), artículo por artículo, qué cambió respecto de la versión 1 ([F-0007](../fuentes/F-0007-mocion-asamblea.md)), qué responde a las preguntas del debate, qué no dice, sus datos por verificar y un análisis marcado como opinión. Contenido en `mocion.py`.
- **Anteproyecto** (`anteproyecto/`): las 14 etapas del anteproyecto ([F-0004](../fuentes/F-0004-anteproyecto.md)), su orden frente a la moción, qué se dijo en el debate contra lo que dice el documento y sus cuentas.
- **Debate** (`debate/`): el "Contrapunto del Master Plan": preguntas clave, respuestas de cada parte con enlace al minuto exacto, en qué coinciden, qué falta verificar y una página de detalle por pregunta. Resume [`analisis/contrapunto-master-plan.md`](../analisis/contrapunto-master-plan.md).

- `build.py`: genera todas las páginas a partir de los datos que tiene adentro y de `detalle.py`. Se corre desde esta carpeta: `python3 build.py`.
- `guia.py`: contenido de la portada (guía para el socio).
- `mocion.py`: contenido de la página de la moción.
- `anteproyecto.py`: contenido de la página del anteproyecto.
- `detalle.py`: contenido de las páginas de detalle de cada pregunta (posturas, por qué lo dicen, análisis, qué lo resolvería).
- `head.html`: fuentes y estilos compartidos.
- `og.html` y `og-AAAA-MM-DD.jpg`: plantilla e imagen de la vista previa que muestran X, WhatsApp y otros al compartir un enlace (1200×630). Si cambia la plantilla, se regenera la imagen con el comando de su comentario y se le da un nombre nuevo, porque X guarda la anterior en caché. El banner del README principal usa la misma imagen: actualizar ahí también el nombre.
- `og-anteproyecto.html` y `og-anteproyecto-AAAA-MM-DD.jpg`: tarjeta propia de la página del anteproyecto, con cuatro láminas recortadas del anteproyecto (`fondo-ap-*.jpg`). Si cambia, se le da un nombre nuevo y se actualiza `OG_ANTEPROYECTO` en `build.py`.
- `robots.txt`: permite a todos los buscadores y bots de vistas previas.
- `index.html`, `debate/index.html` y `debate/detalle-<id>.html`: páginas generadas. Son documentos HTML completos y autónomos. Solo dependen de las fuentes de Google y del script de Cloudflare Web Analytics, que cuenta visitas sin cookies ni datos personales; el contenido no usa JavaScript.

Marcas en los textos: `{F-0014 01:08:44}` enlaza al minuto del video, `{F-0004 p.42}` a la página del documento, `[[#id|texto]]` a una sección de la misma página, `[[>ruta|texto]]` a otra página, y `[[CG]]` marca una afirmación que sale de conocimiento general y no de una fuente registrada.

El análisis de cada detalle es opinión de Claude y está marcado como tal. Ver «Opiniones del modelo» en el [README](../README.md) del repositorio.

Publicación: los HTML se copian tal cual al servidor. La configuración del hosting y del dominio no forma parte de este repositorio.

Estado: preliminar, al 2026-10-08.
