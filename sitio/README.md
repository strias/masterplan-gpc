# Sitio

Sitio estático "Contrapunto del Master Plan": preguntas clave, respuestas de cada parte con enlace al minuto exacto, en qué coinciden, qué falta verificar y una página de detalle por pregunta. Resume [`analisis/contrapunto-master-plan.md`](../analisis/contrapunto-master-plan.md).

- `build.py`: genera todas las páginas a partir de los datos que tiene adentro y de `detalle.py`. Se corre desde esta carpeta: `python3 build.py`.
- `detalle.py`: contenido de las páginas de detalle de cada pregunta (posturas, por qué lo dicen, análisis, qué lo resolvería).
- `head.html`: fuentes y estilos compartidos.
- `index.html` y `detalle-<id>.html`: páginas generadas. Son documentos HTML completos y autónomos, sin JavaScript ni dependencias más allá de las fuentes de Google.

Marcas en los textos: `{F-0014 01:08:44}` enlaza al minuto del video, `{F-0004 p.42}` a la página del documento, `[[#id|texto]]` a una pregunta de la portada, y `[[CG]]` marca una afirmación que sale de conocimiento general y no de una fuente registrada.

El análisis de cada detalle es opinión de Claude y está marcado como tal. Ver «Opiniones del modelo» en el [README](../README.md) del repositorio.

Publicación: los HTML se copian tal cual al servidor. La configuración del hosting y del dominio no forma parte de este repositorio.

Estado: preliminar, al 2026-09-28.
