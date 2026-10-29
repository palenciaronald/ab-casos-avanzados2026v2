---
marp: true
theme: default
paginate: true
header: "Casos Avanzados · Maestría en Ingeniería Analítica"
footer: "Clase 1 · Jueves 29 de octubre · Bienvenida y cierre"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Casos Avanzados de Machine Learning
## Montamos una startup de ML, de principio a fin

**Clase 1 · Jueves 29 de octubre**

<!--
NOTAS DEL PRESENTADOR
- Esta presentación tiene DOS partes: las diapositivas 1-7 son la Bienvenida (10 min, al inicio del
  día) y las 8-10 son el Cierre (5 min, al final del día). Saltar directo a la 8 al cerrar.
-->

---

# Qué vamos a construir

Cada grupo monta **una startup** y lleva un modelo **de la pregunta de negocio a una app que
alguien puede usar**:

**Caso de negocio** → **datos** → **modelo** → **seguimiento** → **app desplegada** → **reporte** →
**exposición**

> Ya saben entrenar modelos. Este curso trata de **aplicarlos con criterio** y de **entregarlos**.

---

# Qué cambia frente al curso anterior

| Antes | Ahora |
|---|---|
| Aprender una técnica | **Aplicarla** a un caso real |
| Trabajo individual | **Grupo** con roles y un caso propio |
| Un notebook | Un **repositorio modular**, con pruebas |
| Un resultado en pantalla | Un **producto desplegado** que otra persona usa |
| Las métricas del libro | La **métrica del negocio**: cuesta distinto equivocarse en cada lado |
| Programar a mano | Programar **con ayuda de IA** (Claude), entendiendo lo que genera |

---

# El calendario: seis clases

| Semana | Jueves | Viernes | Sábado |
|---|---|---|---|
| **1** | **Clase 1 · 29 oct (hoy):** nivelación, grupos, instalación y caso | **Clase 2 · 30 oct:** montaje, EDA y preprocesamiento → **H1** | **Clase 3 · 31 oct:** variables, torneo y optimización con seguimiento |
| | *5 días de trabajo autónomo del grupo* | | |
| **2** | **Clase 4 · 5 nov:** validación, registro, módulos y esqueleto de la app → **H2** | **Clase 5 · 6 nov:** despliegue de la app y presentación → **H3** | **Clase 6 · 7 nov:** **exposiciones** (10 min por grupo) |

Entre la clase 3 y la clase 4 hay **5 días de trabajo autónomo del grupo**; entre las demás clases,
solo la noche. El reporte técnico final se entrega el **domingo 15 de noviembre** (**H4**), 8 días
después de la última clase.

---

# Qué entrega cada grupo

1. **Repositorio** con código modular (`src/`) y pruebas
2. **Notebooks** de cada etapa
3. **Modelo final**, registrado y exportado
4. **Reporte técnico**, que se construye por secciones, una por hito
5. **Presentación ejecutiva** de **máximo 5 diapositivas**
6. **App desplegada** con enlace público

Y una **exposición de máximo 10 minutos** en la clase 6 (sábado 7 de noviembre): caso de negocio, demo en vivo y
resultados.

---

# Cómo trabajamos en clase

- **Demo corta** del instructor al inicio de cada etapa (máximo 20 minutos), sobre un ejemplo
  completo llamado **CreditSight**.
- **Trabajo de grupo** aplicando esa etapa a su propio caso, con el instructor circulando.
- **Un hito** al cierre de las clases 2, 4 y 5, con criterios que se conocen desde hoy.

> **Una condición:** programan con **Claude**. Todo lo que genere la IA lo deben **entender y poder
> explicar**: habrá una pregunta oral individual.

---

# Los cuatro hitos

| Hito | Cuándo | Qué se entrega |
|---|---|---|
| **H1** | Cierre de la clase 2 (viernes 30 de octubre) | Ficha de caso aprobada, EDA y preprocesamiento reproducible |
| **H2** | Cierre de la clase 4 (jueves 5 de noviembre) | Modelos comparados y registrados, repo modular, app local |
| **H3** | Clase 5 (viernes 6 de noviembre) | App con enlace público y presentación de ≤ 5 diapositivas |
| **H4** | Domingo 15 de noviembre (8 días tras la última clase) | Reporte técnico completo |

Hoy, más adelante, les entregamos la **rúbrica completa**.

<!--
FIN DE LA BIENVENIDA. Continuar con el mapa de lo visto en el curso previo.
-->

---

<!-- _class: lead -->

# Cierre de la clase 1

**Hoy logramos**

☐ Ubicar lo que ya sabíamos y dónde lo vamos a usar
☐ Detectar vacíos (sin nota)
☐ **Formar los grupos**
☐ Entender pipeline, end-to-end, tracking y despliegue
☐ **Instalar el entorno** y probar la conexión
☐ Conocer la **rúbrica** y el **kit** de trabajo con Claude
☐ Escribir una **ficha de caso** en borrador

---

# Tarea para mañana

1. **Terminar y corregir la ficha de caso** de tu grupo.
2. **Crear el repositorio del grupo**: una persona lo crea **vacío** en GitHub, clona la rama `feature/estudiantes` del curso
   (`git clone --branch feature/estudiantes …`) y la apunta a ese repo; **compartir el enlace**.
3. Si quedó algo **pendiente de la instalación**, resolverlo con la guía o pedir apoyo antes de la
   clase.
4. Quien tenga dudas del **diagnóstico**, revisar el material del curso previo del tema señalado.

> Ayuda: `curso/guias/instalacion.md` y `curso/guias/desarrollo-con-ia.md`.

---

# Mañana · Clase 2 (viernes 30 de octubre)

- **Primera media hora:** el instructor **aprueba o devuelve** cada ficha de caso.
- Demo del instructor: **caso, EDA y preprocesamiento** con CreditSight.
- Trabajo de grupos sobre su propio dataset.
- **Cierre:** hito **H1**.

> Sin ficha aprobada **no se avanza** con los datos: si la devuelvo, la corrigen en el momento.

*¡Hasta mañana!*
