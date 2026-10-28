# Clase 6 · Sábado 7 de noviembre (semana 2) — Exposiciones

**Duración:** 4 horas · **Cierre del curso presencial.** Se evalúan la **exposición** (criterio C de la rúbrica), la
**app y la presentación** (criterio A3) y, con la pregunta oral, el **aporte individual** (criterio D). El **reporte
técnico final (H4)** se entrega el **domingo 15 de noviembre**.

> **Calendario del curso.** Seis clases de 4 horas en dos semanas de tres días seguidos: clase 1 (jue 29 oct), clase 2
> (vie 30 oct), clase 3 (sáb 31 oct) · **cinco días de trabajo autónomo** · clase 4 (jue 5 nov), clase 5 (vie 6 nov) y
> clase 6 (sáb 7 nov, hoy). H1 se cerró el viernes 30 de octubre, H2 el jueves 5 de noviembre y H3 ayer (clase 5).

## Objetivos

Al terminar la clase:

1. **Cada grupo expuso** su proyecto en **máximo 10 minutos**: caso de negocio, **demo de la app en vivo** y resultados
   con su costo de negocio, y respondió preguntas.
2. **Cada grupo tiene registrado** el nivel de los criterios **C** y **A3**, con el tiempo real de la exposición.
3. **Cada integrante respondió** la pregunta oral sobre un fragmento de código generado con IA (criterio **D**).
4. **Todos saben qué falta para H4**: el informe técnico completo, hasta el **domingo 15 de noviembre**
   (`curso/evaluacion/guia-evaluacion-reporte-h4.md`).

## Cómo se organiza la sesión

El **número de grupos se conoce desde la clase 1**, así que la agenda es **paramétrica**: se fija el esqueleto
(apertura, descanso, cierre) y se reparte el resto entre los grupos. Cada exposición se mide con cronómetro y cada
grupo tiene un **turno de 15 minutos**: 10 de exposición y 5 de preguntas. Las reglas de la presentación están en
`curso/evaluacion/guia-exposicion.md` y los criterios en `curso/evaluacion/rubrica.md`.

## Agenda

| Hora | Min | Bloque | Material |
|---|---|---|---|
| 0:00–0:15 | 15 | **Apertura:** reglas, orden de exposición, cronómetro y prueba técnica de la pantalla | `curso/evaluacion/guia-exposicion.md` |
| 0:15–… | 15 × N | **Exposiciones**, primera mitad (≈ N ÷ 2 grupos) | `lista-de-control.md` (hoja de evaluación) |
| a mitad | 10 | **Descanso** | — |
| … | 15 × N | **Exposiciones**, segunda mitad | `lista-de-control.md` |
| 3:45–4:00 | 15 | **Cierre:** devolución general, H4, entrega de notas y encuesta | `curso/evaluacion/guia-evaluacion-reporte-h4.md` |

El tiempo de las exposiciones es lo que sobra después de apertura, descanso y cierre: **240 − 15 − 15 − 10 = 200 min**.

### ¿Con cuántos grupos cabe?

| Grupos (N) | Turno por grupo | Sobra | Qué hacer |
|---|---|---|---|
| 8 | 10 + 5 = 15 min | 80 min | Margen amplio: se puede dejar tiempo extra de preguntas |
| 10 | 10 + 5 = 15 min | 50 min | Margen para repetir una demo que falle |
| 12 | 10 + 5 = 15 min | 20 min | Es el caso típico: un colchón de 20 min para imprevistos |
| **13** | 10 + 5 = 15 min | 5 min | **Máximo con turnos de 15 min**; no queda margen |
| 14 | 10 + 4 = 14 min | 4 min | Se acortan las preguntas a 4 min |
| 15 | 10 + 3 = 13 min | 5 min | Preguntas de 3 min; la pregunta oral individual (D) se reparte entre los dos cortes |
| 16 | 9 + 3 = 12 min | 8 min | Exposiciones de 9 min (la rúbrica sigue exigiendo ≤ 10) y preguntas de 3 min |
| 17 o más | — | — | **Dos salas en paralelo**, cada una con su evaluador y cronometrador (cada sala ≤ 13 grupos) |

**Fórmula:** `tiempo que sobra = 200 − (minutos por turno × N)`. Si sale negativo, usa la fila de más abajo.

> Anuncia en la clase 1 cuántos turnos habrá. Si cambian los grupos, vuelve a calcular y avisa en la clase 5.

**Ejemplo con 12 grupos.** Apertura 0:00–0:15 · grupos 1 a 6: 0:15–1:45 · descanso 1:45–1:55 · grupos 7 a 12:
1:55–3:25 · colchón 3:25–3:45 · cierre 3:45–4:00.

## Detalle por bloque

### 0:00 · Apertura (15 min)
- **Orden de exposición:** por **sorteo** en la clase 5 o, si prefieres, por **orden de entrega del enlace** de la app.
  Publícalo antes de la sesión; el grupo que no esté presente a su turno pasa al final.
- **Reglas del cronómetro** (coherentes con `guia-exposicion.md` y el criterio C):
  - A los **8 minutos**, aviso.
  - A los **10 minutos**, **llamado de tiempo**: el grupo cierra.
  - Se concede **1 minuto de gracia** para terminar la frase y la conclusión (criterio C: nivel 2 si se pasa hasta 1 minuto).
  - Si el grupo sigue después de ese minuto, el instructor **interrumpe** y anota el tiempo real; si se pasó más de
    2 minutos, la duración cuenta como **nivel 0**. La interrupción es, como máximo, a los **12 minutos**.
- **Quién cuenta el tiempo:** un integrante del **grupo siguiente** (como indica la guía). El evaluador anota además el
  tiempo real de cada parte en la hoja de evaluación.
- **Prueba técnica (5 min):** cada grupo abre su **app desde el enlace público en un navegador distinto al de
  desarrollo** y conecta su portátil a la pantalla. Quien tenga problemas lo resuelve con el apoyo mientras empiezan los demás.
- **Plan B ensayado:** cada grupo tiene lista una **captura o grabación** de la app funcionando (ver «Plan B»).

### 0:15 · Exposiciones (turnos de 15 min)
Estructura de **10 minutos** de `guia-exposicion.md`:

| Parte | Min | Qué debe mostrar |
|---|---|---|
| Caso de negocio | 2 | Quién es el cliente, qué decisión apoya el modelo, cuánto cuesta equivocarse |
| App | 4 | **Demo en vivo** desde el enlace público: un caso normal, uno límite y un dato inválido |
| Resultados | 3 | Métrica principal y por qué, comparación con el punto de partida, límites y riesgos |
| Cierre | 1 | Qué haría el grupo con más tiempo; una decisión que cambiaría |

**Las preguntas (5 min).** La guía y el criterio D se combinan así:

1. **Preguntas de negocio y de resultados (≈ 2 min):** quien presentó, o el integrante que designe el grupo, responde una o
   dos preguntas del evaluador o del público (banco en `lista-de-control.md`).
2. **Pregunta oral individual sobre código (≈ 3 min):** el evaluador elige **un fragmento escrito con ayuda de IA**
   (no el que prefiera el estudiante) y se lo pregunta a un integrante **distinto del que habló**. Son las tres preguntas de
   `curso/evaluacion/aporte-individual.md`: ¿qué hace?, ¿por qué está aquí y no de otra forma?, ¿qué pasaría si cambiara esta línea?

**Mientras tanto,** el grupo siguiente abre su app y deja su presentación lista: así el cambio de turno no gasta tiempo.

El evaluador usa la misma hoja y las mismas reglas para todos los grupos.

### Descanso (10 min)
A la mitad de las exposiciones. Aprovecha para pasar a limpio las hojas de evaluación de la primera mitad.

### 3:45 · Cierre (15 min)
- **Devolución general (5 min):** tres cosas que se vieron bien en muchos proyectos, tres que se repiten como error
  (por ejemplo: métrica que no refleja el costo, partición por fila, app sin validar entradas) y qué hacer con ellas.
- **H4 (3 min):** el informe técnico se entrega **hasta el domingo 15 de noviembre** en `reports/informe_tecnico.md`
  del repositorio del grupo. Qué se evalúa y cómo: `curso/evaluacion/guia-evaluacion-reporte-h4.md`. Regla de retraso del
  criterio A4: hasta 3 días tarde = nivel 1; más de 3 días = nivel 0. La hora límite del domingo la fijas tú en la clase 1
  (propuesta: 23:59).
- **Entrega de notas (3 min):** por el canal que definas (correo o plataforma). Recuerda que la escala de la nota final
  (0–5, 0–10 o 0–100) la define el instructor en la clase 1 y que la nota se calcula como la suma ponderada de la rúbrica
  (porcentaje = Σ peso × nivel ÷ 3).
- **Encuesta del curso (4 min):** [ENLACE A LA ENCUESTA]: qué funcionó, qué fue demasiado pesado, qué cambiarían.

## Plan B si la app falla en vivo

1. **Un intento rápido (máximo 1 minuto):** recargar la página o abrirla en otra pestaña.
2. **Si no responde, el grupo muestra la evidencia local:** la **grabación o captura** que preparó, o la app corriendo en
   su portátil desde el repositorio, y sigue con el resto de la exposición.
3. **Consecuencias en la rúbrica:**
   - **Criterio C:** la demo no fue en vivo desde el enlace público → **nivel 2** como máximo (si cubrió las tres partes y no se pasó de tiempo).
   - **Criterio A3:** el instructor **prueba el enlace público después de la sesión**. Si la app funciona desde su navegador,
     A3 se evalúa con esa prueba; si no funciona, se aplica **A3 nivel 1** (app que corre en local con evidencia).
   Esta es la lectura que se propone de la regla de `guia-exposicion.md`; ajústala si prefieres penalizar siempre la falla en vivo.
4. **No se repite la exposición:** el turno es fijo. Solo se usa el colchón de la agenda para dejar al grupo
   mostrar la evidencia local sin quitar tiempo a los demás.

## Qué se evalúa en cada exposición

| Criterio | Qué se mira | Evidencia |
|---|---|---|
| **C · Exposición** | Duración ≤ 10 min · cubre las tres partes (caso, demo en vivo y resultados con su costo de negocio) · responde las preguntas | cronómetro del evaluador |
| **A3 · App y presentación** | App pública que devuelve predicción con datos válidos y error claro con datos inválidos · presentación de ≤ 5 diapositivas | enlace probado por el evaluador, archivo de la presentación |
| **D · Aporte individual** | Respuesta a la pregunta oral y commits por área, por integrante | historial del repo + pregunta oral |

La hoja de evaluación por grupo y el registro del criterio D están en `lista-de-control.md` (fuera de Git).

## Reglas de la sesión

- **El turno es fijo:** el cronómetro manda y se aplica igual a todos los grupos.
- **La demo es en vivo desde el enlace público.** La evidencia local es solo un plan B.
- **Las preguntas de código las elige el evaluador**, no el estudiante, y se hacen a quien no presentó.
- **Se escribe lo que se observa, no lo que se supone:** si un criterio no se puede decidir con la evidencia, el nivel es el
  inferior (regla de la rúbrica).
- **El público también pregunta,** pero el evaluador regula el tiempo para que ningún turno pase de 5 minutos de preguntas.

## Lo que el instructor debe tener listo

- [ ] El **número de grupos** y la fila de la tabla que corresponde; si hay 17 o más, **dos salas** y un segundo evaluador.
- [ ] El **orden de exposición** publicado en la clase 5.
- [ ] `lista-de-control.md` **impresa**, con una hoja de evaluación por grupo y la hoja de aporte individual.
- [ ] Los **enlaces de las apps** de todos los grupos abiertos en pestañas, ya probados.
- [ ] **Un fragmento de código generado con IA elegido por cada integrante de cada grupo** (revisando los repositorios la víspera).
- [ ] Un **cronómetro visible** y alguien que cuente el tiempo del grupo siguiente.
- [ ] La **hora límite de H4** y la **escala de la nota final** ya anunciadas.
- [ ] El **enlace de la encuesta** y el canal para entregar las notas.
- [ ] Proyector, adaptadores y una **conexión de respaldo** (hotspot) para las demos.
