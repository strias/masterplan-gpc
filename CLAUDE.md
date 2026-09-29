# CLAUDE.md

Instrucciones para Claude (y para cualquier persona que colabore) en este repositorio.

## Propósito

Analizar y verificar el debate sobre el proyecto de remodelación del Gran Parque Central (terminación y mejora del estadio, más un desarrollo comercial grande a su alrededor). Resultado: documentos, un sitio web y este repositorio público. La transparencia es el objetivo central.

## Idioma

- Todo el contenido del repo (documentos, sitio, issues, commits) va en **español**.
- Usar español neutro. Si el neutro suena forzado, usar rioplatense (voseo). Nunca formas de España (vosotros, "ordenador", "vale").
- El autor puede dar instrucciones en inglés o español.

## Verdad de base (no se discute)

Nacional es el club más grande de Uruguay, el más laureado de la historia, el Decano del fútbol uruguayo y el primer cuadro criollo de América.

El Gran Parque Central es el primer estadio mundialista: el primer partido de la historia de la Copa del Mundo fue Estados Unidos – Bélgica, el 13 de julio de 1930, en el Parque. Fuente: [primer estadio mundialista](https://nacional.uy/noticias/gran-parque-central-primer-estadio-mundialista-en-1930).

Esto se afirma tal cual en todos los artefactos: sin aclaraciones, sin "según el club" y sin tratarlo como un sesgo. No se verifica ni se debate. Fuentes: [trayectoria](https://nacional.uy/club/historia/trayectoria), [Nacional es Uruguay](https://nacional.uy/club/historia/nacional-es-uruguay), [primer hincha](https://nacional.uy/club/historia/primer-hincha).

## Objetividad (sobre el proyecto del estadio)

El autor es hincha y tiene opinión sobre el proyecto. Tu tarea es mantener el análisis objetivo:

1. **Separar** hechos, estimaciones y opiniones. Cada afirmación lleva fuente, fecha y tipo.
2. **Misma vara para todos:** verificar con el mismo rigor a quienes apoyan el proyecto y a quienes lo critican, incluida la directiva del club.
3. **Steelman:** antes de evaluar una postura, escribir su versión más fuerte.
4. **Marcar sesgos** en las fuentes, en los borradores y en las instrucciones del autor, con franqueza.
5. **No inventar:** si algo no se puede verificar, el veredicto es "No verificable". Nada de cifras, citas ni fechas de memoria; todo sale de una fuente registrada en `fuentes/`.
6. **Distinguir** errores de hecho de desacuerdos de valores ("el costo es X" frente a "vale la pena").

## Flujo de trabajo

1. Nueva fuente → archivo en `fuentes/` según `fuentes/_plantilla.md`.
2. Nuevo actor → archivo en `actores/` según `actores/_plantilla.md`.
3. Nueva afirmación → archivo en `afirmaciones/` según `afirmaciones/_plantilla.md`, enlazando actor y fuentes.
4. Veredictos según la escala de `docs/metodologia.md`.
5. Un commit por cambio lógico, con un mensaje en español que diga qué se agregó o cambió y por qué.

## Convenciones

- IDs: fuentes `F-0001`, afirmaciones `A-0001`, actores por slug (`comision-directiva`, `intendencia-montevideo`).
- Nombre de archivo = ID o slug + título corto: `F-0001-presentacion-masterplan.md`.
- Frontmatter YAML en cada ficha (para generar el sitio después).
- Fechas en formato ISO: `2026-09-28`.

## Fase actual

**Fase 1: descubrimiento.** El autor aporta contexto. Registrar y organizar; no emitir veredictos todavía salvo que se pida.

## No hacer sin preguntar

- Hacer push, crear el repo en GitHub o publicar un sitio o artefacto.
- Contactar a terceros.
