# Sitio

Página "Contrapunto del Master Plan": preguntas clave, respuestas de cada parte con enlace al minuto exacto, en qué coinciden y qué falta verificar. Resume [`analisis/contrapunto-master-plan.md`](../analisis/contrapunto-master-plan.md).

- `build.py`: genera `contrapunto.html` a partir de los datos que tiene adentro. Se corre desde esta carpeta: `python3 build.py`.
- `detalle.py`: contenido de las páginas de detalle de cada pregunta (posturas, por qué lo dicen, análisis, qué lo resolvería).
- `detalle-<id>.html`: páginas de detalle generadas. Son documentos completos y enlazan a la portada como `index.html`.
- `head.html`: título y estilos.
- `contrapunto.html`: la página generada. Es un fragmento (sin `<!doctype>` ni `<head>`), pensado para publicarse como página de claude.ai. Para GitHub Pages habría que envolverlo.

El análisis de cada detalle es opinión de Claude y está marcado como tal; lo que sale de conocimiento general y no de una fuente registrada lleva la etiqueta "conocimiento general".

Estado: preliminar, al 2026-09-28.
