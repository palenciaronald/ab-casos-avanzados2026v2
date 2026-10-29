---
marp: true
theme: default
paginate: true
header: "Casos Avanzados · Maestría en Ingeniería Analítica"
footer: "Clase 1 · Jueves 29 de octubre · Rúbrica y kit (15 min)"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# La rúbrica y el kit de trabajo
## Cómo se evalúa, y con qué herramientas trabajan

**Clase 1 · Jueves 29 de octubre**

<!--
NOTAS DEL PRESENTADOR (15 min: ~7 de rúbrica y ~8 de kit)
- La ponderación de la diapositiva 2 es la definitiva (suma 100 %). Si la cambias, actualiza también
  `curso/evaluacion/rubrica.md` y vuelve a generar la rama `feature/estudiantes`.
- Mostrar el documento completo (rubrica.md) abierto, no solo estas diapositivas.
-->

---

# La rúbrica, de un vistazo

Cuatro grupos de criterios. **Los pesos suman 100 %.** La escala de la nota final se explica hoy.

| Criterio | Qué mide | Peso |
|---|---|---|
| **A1** Ficha y datos (H1) | Caso aprobado, EDA con decisiones justificadas | 10 % |
| **A2** Modelado y seguimiento (H2) | ≥ 3 modelos comparados, ejecuciones y modelo registrado | 20 % |
| **A3** App y presentación (H3) | App pública y presentación de ≤ 5 diapositivas | 10 % |
| **A4** Reporte técnico (H4) | Informe completo, cada decisión con su motivo | 15 % |
| **B1** Repositorio modular | Estructura, pruebas, sin credenciales | 15 % |
| **B2** Modelo final y ficha | Modelo exportado y ficha del modelo | 5 % |
| **C** Exposición | ≤ 10 min: caso, demo en vivo, resultados | 15 % |
| **D** Aporte individual | Evidencia de lo que hizo cada integrante | 10 % |

---

# Cómo se evalúa

- **Niveles de 0 a 3** en cada criterio: 3 cumple por completo, 2 en parte, 1 mínimamente,
  0 no cumple o no hay evidencia.
- **Cada criterio es observable.** Dos evaluadores que lean la misma evidencia deben dar el mismo nivel.
- La **evidencia** es concreta: un archivo del repo, el enlace de la app, el cronómetro de la
  exposición, la fecha de un commit.
- **Si algo no se puede comprobar, el nivel es el inferior.** Por eso conviene dejar rastro.

> La rúbrica completa está en `curso/evaluacion/rubrica.md`. Léanla hoy con calma.

---

# Los hitos que se evalúan

| Hito | Criterios de aceptación |
|---|---|
| **H1** · Cierre de la clase 2 (vie 30 oct) | Ficha aprobada · EDA con ≥ 5 decisiones justificadas · partición por la unidad correcta · limpieza reproducible por script |
| **H2** · Cierre de la clase 4 (jue 5 nov) | ≥ 3 modelos con la misma validación · ≥ 1 ejecución registrada por candidato · modelo final registrado · `src/` con pruebas · app local |
| **H3** · Clase 5 (vie 6 nov) | App con enlace público · presentación de ≤ 5 diapositivas · ensayo de 10 minutos cronometrado |
| **H4** · Domingo 15 nov (8 días después) | Informe técnico con todas las secciones |

---

# Cuatro reglas que pesan mucho

1. **Nada de credenciales ni datos personales en el repositorio.** Si aparecen, el criterio B1 es **0**
   aunque todo lo demás esté perfecto.
2. **App sin desplegar:** si solo corre en local, con evidencia, el máximo del criterio A3 es **1**.
3. **La prueba se abre una sola vez**, al final. Decidir mirándola invalida la evaluación.
4. **Cada integrante debe poder explicar el código que generó la IA.** Habrá una pregunta oral.

---

# Aporte individual (criterio D)

Se trabaja en grupo, **pero se evalúa a cada persona**:

| Evidencia | Qué muestra |
|---|---|
| **Rol** declarado (datos, modelado, app, negocio) | Qué te corresponde |
| **Commits** en el repo del grupo | Qué hiciste realmente |
| **Pregunta oral** sobre una parte del código | Que lo entiendes, aunque lo haya escrito la IA |

> Si un integrante no aporta, **se nota**: no recae en el resto del grupo.

---

<!-- _class: lead -->

# Ahora, el kit
## Lo que cada grupo recibe en su proyecto

---

# Qué trae el kit

`curso/kit-estudiante/`

| Archivo | Para qué sirve |
|---|---|
| **`CLAUDE.md`** | Instrucciones permanentes: Claude las lee antes de generar nada (contexto del curso, estructura del repo, estilo, qué no hacer) |
| **`especificacion-proyecto.md`** | Plantilla que el grupo llena: caso, dataset, métrica, entregables, riesgos |
| **`prompts-por-etapa.md`** | Un prompt probado para cada etapa, con qué esperar y cómo revisarlo |
| **`checklist-revision-ia.md`** | Cómo revisar el código que generó la IA antes de aceptarlo |
| **La raíz de la rama `feature/estudiantes`** | La estructura vacía del repositorio del grupo: todo lo anterior ya viene en ella |

---

# Cómo se usa el kit

1. **Una persona** crea el repositorio del grupo (público y **vacío**) y clona **la rama `feature/estudiantes`**
   del curso apuntándola a ese repo (`git clone --branch feature/estudiantes …` y `git remote set-url origin …`).
2. **Los demás** clonan el repo **del grupo**; la plantilla y el kit ya vienen incluidos.
3. **Llenar** `especificacion-proyecto.md` (la ficha de caso es su base).
4. **Abrir** el proyecto en VS Code con la extensión de Claude Code.
5. **Pedir en pasos pequeños**, y revisar con el checklist antes de aceptar.

> *Pedir bien = el archivo exacto + qué debe hacer + cómo sabré que funcionó + qué no debe tocar.*

Guía completa: `curso/guias/desarrollo-con-ia.md`.

---

# Claude: cuota y plan B

- Claude se usa desde **VS Code con la extensión de Claude Code**. El plan individual de pago incluye
  Claude Code y la **cuota es compartida con el chat**.
- Hay una **ventana de uso** que se renueva y puede haber topes semanales. Verifiquen los números
  vigentes en el centro de ayuda de Anthropic.
- **Gasten poco:** pidan una cosa por vez y con el archivo exacto; abran conversación nueva al
  cambiar de etapa; dejen lo fijo en `CLAUDE.md`.
- **Sin cuota o sin plan:** avisen **hoy** al instructor para acordar una alternativa.

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ¿Preguntas?

Rúbrica: `curso/evaluacion/rubrica.md`
Kit: `curso/kit-estudiante/`
