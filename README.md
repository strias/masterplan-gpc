# Masterplan GPC

Un análisis abierto, verificable y transparente del proyecto de remodelación del **Gran Parque Central** y del desarrollo comercial proyectado a su alrededor.

El proyecto genera debate por su escala. Este repositorio reúne las fuentes, registra quién dijo qué y verifica cada afirmación con evidencia, tanto las de quienes apoyan el proyecto como las de quienes lo critican. Todo el proceso es público: cada fuente, cada veredicto y cada cambio quedan registrados en el historial de git.

## Club Nacional de Football

Nacional es el club más grande de Uruguay, el más laureado de la historia, el Decano del fútbol uruguayo y el primer cuadro criollo de América. Fue fundado el 14 de mayo de 1899.

- [Trayectoria](https://nacional.uy/club/historia/trayectoria)
- [Nacional es Uruguay](https://nacional.uy/club/historia/nacional-es-uruguay)
- [El primer hincha](https://nacional.uy/club/historia/primer-hincha)

## Quién hace esto

Este proyecto lo impulsa **Santiago Trias**, hincha de Nacional. Tiene opinión sobre el proyecto y por eso el método está pensado para que el análisis no dependa de esa opinión: las afirmaciones se verifican con fuentes públicas y los veredictos se pueden revisar y discutir en abierto.

El análisis se hace con asistencia de IA (Claude, de Anthropic). Las reglas que sigue están en [`CLAUDE.md`](CLAUDE.md).

## Opiniones del modelo

Además de verificar, en algunas secciones se le pide al modelo una opinión: por ejemplo, el «Análisis» y el «En resumen» de cada pregunta del sitio. Esas secciones están marcadas como opinión, separadas de los hechos y de los veredictos.

La razón para usarlas: en este tema el modelo no tiene interés propio ni historia con el club, así que su lectura es, en general, más imparcial que la del autor. No es neutral por definición: puede arrastrar sesgos de sus datos de entrenamiento o errores de razonamiento. Por eso cada opinión indica en qué fuentes se apoya, marca lo que sale de conocimiento general y no de una fuente registrada, y se puede discutir como cualquier otra afirmación del repositorio.

## Estado

🔵 **Fase 1: descubrimiento.** Estamos reuniendo documentos, actores y afirmaciones. Todavía no hay veredictos publicados. Sí hay análisis preliminares, marcados como opinión del modelo (ver «Opiniones del modelo»).

La Asamblea General Extraordinaria que considera el proyecto es el **24 de octubre de 2026** ([cronología](docs/cronologia.md)).

## Estructura

| Carpeta | Contenido |
|---|---|
| [`fuentes/`](fuentes/) | Registro de documentos, notas de prensa, declaraciones y datos, con fecha y enlace |
| [`actores/`](actores/) | Personas e instituciones que participan en el debate y sus posiciones |
| [`afirmaciones/`](afirmaciones/) | Cada afirmación verificada: quién la dijo, evidencia y veredicto |
| [`transcripciones/`](transcripciones/) | Transcripciones de entrevistas y programas, con marcas de tiempo, para verificar las citas |
| [`scripts/`](scripts/) | Herramientas del repo (por ejemplo, la que genera las transcripciones) |
| [`analisis/`](analisis/) | Análisis temáticos: financiero, urbano, deportivo, legal y social |
| [`docs/`](docs/) | Metodología y criterios |

## Metodología

La escala de veredictos, los tipos de fuente y las reglas de verificación están en [`docs/metodologia.md`](docs/metodologia.md).

## Cómo participar

¿Tenés una fuente, una corrección o una afirmación para verificar? Leé [`CONTRIBUTING.md`](CONTRIBUTING.md) y abrí un issue. Se aceptan aportes de cualquier persona, sea del cuadro que sea, siempre que vengan con fuentes.

## Licencia

- Código: [MIT](LICENSE)
- Contenido (textos, análisis, datos propios): [CC BY 4.0](LICENSE-CONTENIDO.md)

Los documentos de terceros enlazados en `fuentes/` conservan los derechos de sus autores.
