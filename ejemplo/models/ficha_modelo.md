# Ficha del modelo — CreditSight

**Qué es.** Clasificador de perfil crediticio (`Poor`, `Standard`, `Good`) con **random forest**
sin calibrar. Apoya la decisión de límite de crédito: **prioriza la revisión
del analista de riesgo, no decide por sí solo.** La decisión final es siempre humana.

**Cómo decide.** Calcula la probabilidad de cada clase y elige la decisión de **menor costo esperado** según la matriz de costos
(aprobar a un cliente `Poor` cuesta 10; rechazar a uno `Good`, 2), no la clase más probable.

**Datos.** `credit_score_classification.csv`: 12 500 clientes × 8 meses (100 000 filas), datos **sintéticos de ejemplo**.
Entrenado con el 80 % de los clientes; la prueba (20 %) se abrió **una sola vez** (2026-10-28T17:25:46).
Se particiona **por cliente**, nunca por fila.

## Rendimiento en la prueba (clientes que el modelo nunca vio)

| Medida | Valor | IC 95 % (remuestrea clientes) |
|---|---|---|
| Costo esperado por cliente-mes (menor es mejor) | 0.476 | 0.456 a 0.498 |
| AUC macro | 0.854 | 0.846 a 0.862 |
| Costo frente al baseline (modelo − baseline) | -0.567 | -0.610 a -0.523 |
| AUC frente al baseline (modelo − baseline) | +0.354 | +0.346 a +0.362 |

Recall por clase con la regla de decisión: `Poor` 84.1% · `Standard` 72.6% · `Good` 6.0%.
Supera al baseline con confianza.
La app marca "revisar" en 41% de los cliente-mes.

## Límites y usos no recomendados

- **Casi nunca decide `Good`.** La regla de costo mínimo penaliza tanto aprobar a un `Poor` que el recall de `Good` es muy bajo:
  el modelo es prudente por diseño. No sirve para encontrar a los mejores clientes.
- **Datos sintéticos de ejemplo.** No usar con clientes reales sin una validación propia con datos reales.
- **Explica al modelo, no al mundo.** Las variables que más pesan (SHAP) muestran de qué se apoya el modelo, no qué *causa*
  el comportamiento de pago.
- **Variables de uso sensible:** Age, Occupation. Revisar con el área legal antes de producción.
- `Credit_Mix` se usa asumiendo que se conoce al momento de decidir.
- El costo depende de la matriz de costos supuesta; con otra matriz, otra decisión óptima.
