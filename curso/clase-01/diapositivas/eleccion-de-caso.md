---
marp: true
theme: default
paginate: true
header: "Casos Avanzados · Maestría en Ingeniería Analítica"
footer: "Clase 1 · Jueves 29 de octubre · Grupos y elección del caso"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Grupos y elección del caso
## Tu proyecto empieza aquí

**Clase 1 · Jueves 29 de octubre**

*Al terminar: un grupo, un dataset candidato y una ficha de caso en borrador.*

<!--
NOTAS DEL PRESENTADOR (dos momentos: la diapositiva "Los grupos" tras el diagnóstico, y el resto en el bloque final de 35 min)
- Proyectar hasta la diapositiva "La ficha de caso"; luego los grupos trabajan con la plantilla de la ficha.
- Tener abierto el ejemplo de CreditSight (ejemplo/reports/00_caso.md) para mostrarlo.
-->

---

# Cómo se reparte el día

| Cuándo | Qué |
|---|---|
| **Tras el diagnóstico** (15 min) | **Formar grupos** y repartir roles |
| **Al final del día** (35 min) | **5 min** de criterios del dataset y **30 min** para elegir el caso y escribir la **ficha** (en borrador) |

**Mañana, en la primera media hora, el instructor aprueba o devuelve cada ficha.**
Solo con la ficha aprobada se sigue con los datos.

---

# 1 · Los grupos

- El **tamaño y el número de grupos** los define el instructor hoy, según quién esté.
- Cada grupo reparte **cuatro roles**. Una persona puede tener más de uno, pero cada rol debe
  tener responsable:

| Rol | Se encarga de |
|---|---|
| **Datos** | Conseguir, limpiar y entender los datos |
| **Modelado** | Comparar y optimizar modelos |
| **App** | La aplicación y el despliegue |
| **Negocio** | La pregunta, el costo de equivocarse y la presentación |

> **Regla del curso:** cada integrante debe poder explicar el código que la IA generó. Habrá una
> pregunta oral individual.

<!--
Sugerencia: que cada grupo tenga al menos una persona fuerte en cada tema que apareció como vacío
frecuente en el diagnóstico.
-->

---

# 2 · Qué es un "caso de negocio"

Un caso responde cuatro preguntas:

1. **¿Quién decide?** (una persona real con un cargo)
2. **¿Qué decide?** (una acción concreta)
3. **¿Con qué información?** (los datos que tendrás)
4. **¿Cuánto cuesta equivocarse?** (y si cuesta lo mismo en las dos direcciones)

**Ejemplo, CreditSight:** *El analista de riesgo (1) decide qué límite de crédito asignar (2) a partir
del perfil financiero y el historial de pagos del cliente (3). Aprobar a un cliente de alto riesgo
cuesta mucho más que rechazar a uno bueno (4).*

> Si no puedes responder la 4, todavía no tienes un caso: tienes un dataset.

---

# 3 · Tres tipos de problema

| Tipo | Pregunta | Ejemplo de decisión |
|---|---|---|
| **Clasificación** | ¿A qué clase pertenece? | ¿Este cliente abandonará? ¿Esta transacción es fraude? |
| **Regresión** | ¿Cuánto valdrá? | ¿Cuánto tardará este envío? ¿Cuál será el consumo? |
| **Clusterización** | ¿Qué grupos hay? | ¿Qué segmentos de clientes merecen campañas distintas? |

⚠️ **Clusterización:** no hay etiqueta con qué validar. Tu grupo tendrá que justificar los grupos
con **estabilidad y significado de negocio**, y mostrar qué acción distinta tomaría la empresa en
cada grupo.

<!--
Los ejemplos de decisión son ilustrativos: ninguno es un dataset concreto ni uno de los prohibidos.
-->

---

# 4 · ¿De dónde saco los datos?

Eres libre de elegir. Estas son las opciones:

| Fuente | Cuándo |
|---|---|
| **Kaggle** · *la recomendación del instructor* | El camino más rápido: miles de datasets tabulares con comentarios y código |
| **UCI Machine Learning Repository** | Datasets clásicos y bien documentados |
| **Datos abiertos de tu gobierno** | Casos reales y locales; suelen venir sucios, lo cual es bueno |
| **Hugging Face Datasets** | Tablas de muchos dominios |
| **Tu trabajo** | **Solo** con permiso explícito por escrito y anonimizado, porque el repo es público |

---

# 5 · Cómo buscar en Kaggle

1. Entra a **kaggle.com/datasets** y busca por **tema de negocio**, no por algoritmo
   (por ejemplo: riesgo, seguros, retail, salud, energía, logística).
2. Filtra por datos **tabulares**, **tamaño mediano** y **usabilidad alta**.
3. Abre cada candidato y mira **tres pestañas**:
   - **Datos:** columnas, tipos y cuántas filas hay.
   - **Discusión:** ahí aparecen los problemas conocidos (fugas, errores, basura).
   - **Licencia:** ¿se puede redistribuir? (el repo es público)
4. Descarga el archivo (botón de descarga) y ábrelo con `pandas`.

> Prueba **tres o cuatro candidatos** antes de decidir. El primero que ves casi nunca es el mejor.

---

# 6 · Los criterios (1/2): los datos

| Criterio | Qué se revisa |
|---|---|
| **Volumen suficiente** | **Mínimo 50.000 filas; lo recomendado es 100.000 o más**, y ~10 columnas útiles. Sin pasarse mucho: el cómputo del taller no aguanta datasets enormes |
| **Mezcla de tipos** | Numéricas **y** categóricas (idealmente alguna de alta cardinalidad, fecha o texto corto) |
| **Suciedad real** | Vacíos, formatos inconsistentes, atípicos. Un dataset ya limpio no ejercita nada |
| **Unidad de análisis clara** | Qué es una fila. Si un cliente aparece varias veces, hay que partir **por cliente** |
| **Sin fuga evidente** | Ninguna columna contiene la respuesta ni se conoce solo después del hecho |

---

# 6 · Los criterios (2/2): el caso y las reglas

| Criterio | Qué se revisa |
|---|---|
| **Objetivo definido** | En una frase: qué predices o agrupas y quién usa el resultado |
| **Decisión con costo** | Una acción real y un costo de equivocarse |
| **No repetido** | No está en la lista prohibida (siguiente diapositiva) |
| **Sin datos personales** | Nombres, documentos o contactos se eliminan al inicio |
| **Sin información confidencial** | Si viene de tu trabajo, permiso **por escrito** para un repo público |
| **Licencia revisada** | Puedes redistribuirlo, o el repo explica cómo descargarlo |

---

# 7 · Lo que NO se puede usar

**De este curso:** German Credit, **Credit Score Classification** (es el del ejemplo), Mall
Customers, Credit Card, Financial Statements, Taiwan Bankruptcy y los de sentimientos financieros.

**Del curso previo:** seguro médico (insurance), iris, telco churn, reservas de hotel, Ames Housing,
wine, dígitos, auto MPG y turistas de invierno.

> ¿Dudas de si un dataset es "el mismo" con otro nombre? **Pregunta al instructor antes de
> invertirle tiempo.**

---

# 8 · Ejemplos de rechazo

| Propuesta | Por qué se rechaza |
|---|---|
| Titanic | Demasiado conocido, ~900 filas y ya limpio |
| Una encuesta de 5.000 filas | Por debajo del mínimo de 50.000 filas |
| Varios millones de filas | Demasiado grande para portátiles y la cuota gratuita: usa una muestra de ~100.000 |
| Base de clientes de mi empresa con nombres | Datos personales y confidenciales en un repo público |
| Una columna que dice el "resultado final" del caso que predigo | Fuga del objetivo |
| Precio de una acción para "predecir mañana" | Serie de tiempo: el curso no cubre su validación |
| Imágenes o audio | El curso es de datos tabulares |

---

# 9 · Chequeo rápido: ¿sirve este dataset? (5 min)

Antes de proponerlo, ábrelo y mira:

```python
import pandas as pd

df = pd.read_csv("mi_dataset.csv")
print(df.shape)                       # ¿al menos 50.000 filas y ~10 columnas útiles?
print(df.dtypes.value_counts())       # ¿mezcla de tipos?
print(df.isna().mean().sort_values().tail())   # ¿hay vacíos reales?
print(df.nunique().sort_values().head(8))      # ¿qué columna parece el objetivo?
# ¿alguna columna se repite por cliente?  df["id_cliente"].value_counts().head()
```

También puedes pedirle a **Claude**: *"Revisa este dataset con los criterios de
`criterios-dataset.md` y dime qué problemas ves."*

---

# 10 · La ficha de caso

Cada grupo entrega **una ficha**. Son 11 campos:

`case_id` · `business_question` · `dataset_source` · `dataset_rows` · `dataset_columns` · `target` ·
`problem_type` · `primary_metric` · `business_cost_note` · `status` · `reviewer_notes`

- Estados: **borrador** → *(devuelta → borrador)* → **aprobada**.
- Hoy la dejan en **borrador**. El instructor completa `reviewer_notes`.
- La plantilla está en `curso/evaluacion/ficha-de-caso.md`.

> **Modelo a imitar:** la ficha de CreditSight (`ejemplo/reports/00_caso.md`). Fíjate en cómo
> convierte "equivocarse cuesta más en un lado" en una **matriz de costos** concreta.

---

# Lista rápida antes de presentar

- [ ] Puedo decir la **pregunta de negocio** en una frase.
- [ ] Tiene **al menos 50.000 filas** (lo ideal: 100.000 o más).
- [ ] Sé **qué es una fila** y si hay filas del mismo cliente repetidas.
- [ ] Hay **suciedad real** y mezcla de tipos de variable.
- [ ] Hay un **costo asimétrico** de equivocarme.
- [ ] **No está** en la lista prohibida.
- [ ] No tiene datos personales ni confidenciales; **revisé la licencia**.
- [ ] **Ninguna columna** contiene la respuesta.

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Ahora, a trabajar

**30 minutos** para elegir y escribir la ficha.
El instructor pasa por cada grupo.

*Tarea de hoy:* completar la ficha y crear el repositorio del grupo (una persona lo crea vacío, clona la
rama `feature/estudiantes` del curso y la apunta a ese repo) y compartir el enlace.
