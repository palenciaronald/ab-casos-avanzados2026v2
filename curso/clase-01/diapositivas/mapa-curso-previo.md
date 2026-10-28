---
marp: true
theme: default
paginate: true
header: "Casos Avanzados · Maestría en Ingeniería Analítica"
footer: "Clase 1 · Jueves 29 de octubre · Mapa de lo visto en el curso previo (20 min)"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Lo que ya sabes
## Mapa del curso previo → dónde lo usarás en tu proyecto

**Clase 1 · Jueves 29 de octubre**

*No es un repaso: es un mapa. Una diapositiva por tema.*

<!--
NOTAS DEL PRESENTADOR (20 min en total, ~1,5 min por diapositiva)
- Objetivo: que cada estudiante reconozca lo que ya domina y vea dónde lo va a usar.
- Si alguien pregunta "¿puedes explicar X?", la respuesta es: "está en la sesión N del curso previo;
  hoy solo ubicamos dónde reaparece". No se reenseña.
-->

---

# Cómo usar este mapa

Cada diapositiva tiene **tres partes**:

1. **Lo que recuerdas:** la idea central del tema, en una frase.
2. **La trampa:** el error típico que el curso previo quiso evitar.
3. **Aquí lo usarás:** en qué etapa de tu proyecto reaparece.

> Si una diapositiva **no te suena**, no pasa nada: apúntala. El diagnóstico que sigue
> sirve justamente para eso, y el material del curso previo sigue siendo tu referencia.

<!--
Aclarar: los temas del curso previo son fundamentos, preparación de datos, clasificación y métricas,
elegir con honestidad, ensambles, optimización, aprendizaje sin etiqueta y explicar y entregar. Hoy
no los repasamos: los conectamos con el proyecto.
-->

---

# 1 · Fundamentos

**Lo que recuerdas.** Aprender de datos es ajustar un modelo con ejemplos y **juzgarlo con datos
que nunca vio**. Supervisado (hay etiqueta) frente a no supervisado (no la hay). El contrato de
`scikit-learn`: se **ajusta** (`fit`) y luego se **predice** (`predict`).

**La trampa.** Un modelo perfecto con los datos con los que se construyó y malo con datos nuevos:
**sobreajuste**. Por eso siempre hay un conjunto aparte y un **baseline** que vencer.

**Aquí lo usarás.** Etapa 1 y 3: el baseline *"siempre Standard"* (costo esperado 1,05) y la
partición por cliente.

---

# 2 · Preparar los datos sin fuga

**Lo que recuerdas.** Escalar, imputar vacíos, codificar categorías, tratar atípicos. Todo en un
**pipeline** (`Pipeline` + `ColumnTransformer`).

**La trampa.** **Todo transformador se ajusta, así que todo transformador puede filtrar
información.** Ajustarlo con todos los datos antes de partir es fuga.

**Aquí lo usarás.** Etapas 3 y 4. Lo que cambia: ahora los datos llegan **sucios de verdad**
(números como texto, centinelas, valores imposibles) y el pipeline lo pides **sin plantilla**.

---

# 3 · Clasificación y métricas

**Lo que recuerdas.** La salida real de un clasificador es una **probabilidad**; la clase sale de
comparar con un **umbral**. Matriz de confusión, *precision*, *recall*, F1, ROC y precisión-recall.

**La trampa.** La **exactitud esconde qué error se cometió**: un modelo que predice "nadie se va"
puede sacar 0,73 con precision, recall y F1 en cero.

**Aquí lo usarás.** Etapa 1 y 7: en vez de F1, una **matriz de costos** (aprobar a un `Poor` cuesta
10; rechazar a un `Good`, 2) y una **regla de decisión de menor costo esperado**.

---

# 4 · Elegir un modelo con honestidad

**Lo que recuerdas.** Una sola partición es una **lotería**: el mismo modelo cambia de resultado
según la semilla. La **validación cruzada** estima con todos los pliegues y deja la prueba cerrada.
Sesgo y varianza se ven en la distancia entre el error de entrenamiento y el de validación.

**La trampa.** Mirar la prueba para decidir: deja de medir generalización.

**Aquí lo usarás.** Etapa 5 y 7: validación cruzada **por cliente** (cada cliente aparece 8
veces), y la prueba se **abre una sola vez**, en la etapa 7.

---

# 5 · Ensambles

**Lo que recuerdas.** *Bagging* y bosques aleatorios (muchos árboles que se promedian) y *boosting*
(cada modelo corrige lo que el anterior dejó). *Early stopping* elige el número de árboles con un
conjunto de validación. XGBoost.

**La trampa.** Combinar modelos solo ayuda cuando **se equivocan de maneras distintas**. En unos
datos ningún ensamble le ganó a la regresión logística por más que el ruido; en otros, el boosting
ganó con claridad.

**Aquí lo usarás.** Etapa 5: el torneo con bosque, LightGBM y XGBoost. Qué modelo gana **es una
propiedad de los datos**, y se mide pareado, pliegue a pliegue.

---

# 6 · Optimización de hiperparámetros

**Lo que recuerdas.** Buscar con rejilla, al azar o con Optuna. El **espacio de búsqueda** lleva tu
conocimiento del modelo. La puntuación de la búsqueda es **optimista** (es el máximo de muchas
estimaciones con ruido); la **validación cruzada anidada** estima el *procedimiento*.

**La trampa.** Creer que optimizar siempre mejora: la ganancia es la distancia entre los valores de
partida y lo que los datos necesitan, y a veces está dentro del ruido.

**Aquí lo usarás.** Etapa 6, ahora **con seguimiento**: cada ensayo queda registrado en MLflow y la
mejora se comprueba en clientes que la búsqueda no vio.

---

# 7 · Aprender sin etiqueta

**Lo que recuerdas.** PCA y selección de variables, k-means, cuántos grupos (codo y estabilidad),
UMAP para dibujar y detección de anomalías con Isolation Forest. Sin etiqueta no hay puntaje: se
valida por **estabilidad y significado de negocio**.

**La trampa.** Leer el tamaño de los grupos o las distancias en un dibujo de UMAP.

**Aquí lo usarás.** Si tu grupo elige **clusterización**, es tu camino. En CreditSight (clasificación)
no aparece, pero la lección de "validar sin etiqueta" sigue valiendo para el perfilado.

---

# 8 · Explicar y entregar

**Lo que recuerdas.** **Calibración** (un buen AUC no garantiza buenas probabilidades),
**SHAP** (explica al modelo, no al mundo), un modelo entregado es **pipeline + metadatos +
script**, **deriva** de los datos y la **ficha del modelo**.

**La trampa.** Confiar en una probabilidad sin comprobar su calibración, o leer SHAP como si
dijera si el modelo acertó.

**Aquí lo usarás.** Etapas 7 y 9: calibración con clientes reservados, SHAP por cliente y la ficha
del modelo.

---

<!-- _class: lead -->

# Lo que NO vieron

El propio curso previo lo dice al cerrar: **no cubrió**

- **registrar experimentos** (MLflow),
- **servir un modelo** como aplicación,
- **empaquetarlo** y desplegarlo.

**Eso es lo nuevo de este curso.**

<!--
Es el puente hacia la nivelación: pipeline, proyecto end-to-end, tracking y despliegue.
-->

---

# El mapa completo

| Tema previo | Reaparece en CreditSight | Clases |
|---|---|---|
| 1 · Fundamentos | Baseline, partición por cliente | 1–2 |
| 2 · Preparar datos | Limpieza, pipeline | 1–2 |
| 3 · Clasificación y métricas | Matriz de costos, regla de decisión | 2–4 |
| 4 · Elegir con honestidad | CV por cliente, prueba una sola vez | 3–4 |
| 5 · Ensambles | Torneo de modelos | 3 |
| 6 · Optimización | Búsqueda con seguimiento en MLflow | 3 |
| 7 · Sin etiqueta | Solo si tu grupo elige clusterización | 2–4 |
| 8 · Explicar y entregar | SHAP, calibración, ficha, inferencia | 4–5 |
| **Nuevo** | **Tracking, registro, app y despliegue** | **3–5** |

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Siguiente: el diagnóstico

12 preguntas cortas, **sin nota**.
Sirven para saber **dónde apoyar**, no para calificar.
