---
marp: true
theme: default
paginate: true
header: "Casos Avanzados · Maestría en Ingeniería Analítica"
footer: "Clase 5 · Viernes 6 de noviembre · Demos 2 y 3: presentación ejecutiva y exposición de 10 min"
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Contar el proyecto en 5 diapositivas
## Y exponerlo en 10 minutos

**Clase 5 · Viernes 6 de noviembre**

<!--
NOTAS DEL PRESENTADOR
- Este archivo cubre DOS demos: la Demo 2 (diap. 1-9, 20 min: la presentación ejecutiva) y la Demo 3 (diap. 10-14, 10 min:
  cómo exponer en 10 minutos). Salta directo a la 10 para la Demo 3.
- Las cifras de CreditSight que aparecen son solo las que ya existen (costo del baseline, 1,05). El costo de la prueba del
  modelo final del ejemplo todavía NO existe: está marcado [COSTO EN PRUEBA]. No lo inventes: se completa cuando se
  ejecute la etapa de validación del ejemplo.
-->

---

# Una presentación ejecutiva no es un informe

Quien la escucha **decide**; no revisa tu código.

| El informe técnico (H4) | La presentación ejecutiva |
|---|---|
| Cómo lo hiciste, con todos los detalles | **Qué decide el cliente y por qué debe confiar** |
| Todas las métricas, todas las pruebas | **Un número de negocio** y su límite |
| Para quien quiere reproducirlo | Para quien tiene **5 minutos** |

> Lo técnico **no se pierde**: va al informe. Aquí solo entra lo que cambia una decisión.

---

# La estructura: 5 diapositivas

| # | Diapositiva | Responde |
|---|---|---|
| 1 | **Problema** | ¿Quién decide, qué decide y cuánto cuesta equivocarse? |
| 2 | **Enfoque** | ¿Con qué datos y cómo se validó, **en una frase por idea**? |
| 3 | **Resultado y costo de negocio** | ¿Cuánto mejora la decisión frente al punto de partida? |
| 4 | **Demo de la app** | ¿Cómo se usa? (un caso normal, uno límite, uno inválido) |
| 5 | **Riesgos y siguientes pasos** | ¿Qué no hace el modelo y qué viene? |

**Máximo 5.** Una sexta diapositiva es una decisión que dejaste de tomar.

---

# Diapositiva 1 · Problema

**Un titular que cualquiera entienda, y el costo de equivocarse.**

> *Ejemplo (CreditSight):* El analista de riesgo de una fintech asigna un **límite de crédito alto, estándar o restringido**
> a cada cliente. **Aprobar a un cliente de riesgo cuesta mucho más que rechazar a uno bueno.**

- ¿Quién usa el resultado? ¿Qué decide con él?
- ¿Qué cuesta cada tipo de error? (En CreditSight: aprobar un `Poor` como `Good` cuesta 10; rechazar un `Good`, 2.)

**Prohibido:** abrir con el nombre del algoritmo.

---

# Diapositiva 2 · Enfoque

**Lo justo para confiar, sin jerga.**

- **Los datos:** de dónde vienen y cuántos (*«100.000 registros de 12.500 clientes»*).
- **Cómo se validó con honestidad:** *«partimos por cliente, para que ninguno apareciera en entrenamiento y prueba»*.
- **Qué se comparó:** *«probamos varios modelos con la misma validación y elegimos el de menor costo»*.
- **Qué se descartó y por qué** (si hubo una idea que no funcionó, dilo: da credibilidad).

> Una frase por idea. Los detalles técnicos van al informe.

---

# Diapositiva 3 · Resultado y costo de negocio

**El número que le cambia la decisión a tu cliente.**

| | Sin el modelo (punto de partida) | Con el modelo |
|---|---|---|
| Costo esperado por decisión | **1,05** *(CreditSight, «siempre `Standard`»)* | **[COSTO EN PRUEBA]** |
| En 100.000 decisiones al mes | **~105.000 unidades** | **[COSTO EN PRUEBA] × 100.000** |

- Di la **mejora** y su **intervalo o límite** (*«entre X e Y con 95 % de confianza»*).
- La métrica técnica (F1, AUC) va en una nota, **no en el titular**.

<!--
[COSTO EN PRUEBA] es un marcador: se completa con la cifra de la prueba de CreditSight cuando se ejecute la etapa de
validación del ejemplo. El 1,05 es real (baseline de la clase 1). Cada grupo pondrá SUS cifras (reports/07_validacion.md).
-->

---

# Diapositiva 4 · Demo de la app

**Tres casos, siempre.**

1. **Un caso normal:** responde algo coherente.
2. **Un caso límite:** uno que **cambia la decisión** y muestra por qué.
3. **Un dato inválido:** (por ejemplo, edad −500) y **la app lo rechaza con un mensaje claro**.

- Desde el **enlace público**, en un navegador distinto al de desarrollo.
- **Abre la app unos minutos antes:** puede estar dormida.
- **Plan B:** captura de pantalla con fecha y la app en local.

> La demo muestra **cómo se usa**, no cómo se construyó.

---

# Diapositiva 5 · Riesgos y siguientes pasos

**La que más credibilidad da si es honesta.**

- **Qué NO hace el modelo** (y qué decisión no debe tomar solo).
- **Límites de los datos** (sintéticos, sesgos, periodos, grupos poco representados).
- **Uso responsable:** variables sensibles o reguladas (por ejemplo, la edad).
- **Siguientes pasos:** una mejora concreta y qué vigilarían en producción.

> *«No hay riesgos»* es la frase que más desconfianza genera.

---

# Hablarle a un ejecutivo: tres reglas

1. **La conclusión primero.** *«Reducimos el costo de decisión en [X]»*, y después el cómo.
2. **Un mensaje por diapositiva.** Si no lo puedes decir en una frase, son dos diapositivas.
3. **Cada número con su unidad de negocio.** No «F1 = 0,68», sino «de cada 100 clientes riesgosos, detectamos 80».

| Técnico | Para decidir |
|---|---|
| Recall de la clase de riesgo = 0,80 | Detecta **8 de cada 10** clientes riesgosos |
| Costo esperado 1,05 → **[COSTO EN PRUEBA]** | Ahorro de **[X] unidades por cada 100.000 decisiones** |

---

<!-- _class: lead -->

# Demo 3
## Cómo exponer en 10 minutos

---

# El reparto: 2 · 4 · 3 · 1

| Parte | Min | Qué debe mostrar |
|---|---|---|
| **Caso de negocio** | 2 | Quién decide, qué decide, cuánto cuesta equivocarse |
| **App** | 4 | **Demo en vivo** desde el enlace público: normal, límite, inválido |
| **Resultados** | 3 | Métrica de negocio, comparación con el punto de partida, límites y riesgos |
| **Cierre** | 1 | Qué haría el grupo con más tiempo; una decisión que cambiarían |

Después: **5 minutos de preguntas**. A los **10 minutos se corta.**

---

# Cómo ensayar

- **Cronometren un ensayo completo** y recorten lo que sobre (siempre sobra).
- Un integrante de otro grupo **toma el tiempo** y avisa a los **8** y **10** minutos.
- **No lean las diapositivas:** cuenten la decisión y el resultado.
- Decidan **quién habla de qué** y **quién responde las preguntas técnicas**. **Todos** deben poder explicar el código que generó la IA: se pregunta a quien **no** habló.
- Tengan lista **la captura de la app funcionando** por si falla la conexión.

---

# Errores típicos

| Error | Cómo evitarlo |
|---|---|
| Más de 5 diapositivas o texto diminuto | Quita detalle técnico: va al informe |
| Abrir con el algoritmo | Abrir con la decisión del cliente |
| Resultado solo en F1 o accuracy | Traducirlo a costo, dinero o casos |
| Demo solo con el caso feliz | Normal, límite e **inválido** |
| La app dormida o sin red | Abrirla antes; plan B con captura y app local |
| Hablar uno solo de todo | Repartir; todos responden preguntas |
| Pasarse de 10 minutos | Ensayar con cronómetro y recortar |

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Puntos de control 2 y 3

**2 · Presentación:** máximo **5 diapositivas**, cifra de negocio, demo con tres casos, `reports/09_despliegue.md` iniciado.
**3 · Ensayo:** **≤ 10 minutos** con el tiempo real anotado y una corrección hecha tras la retroalimentación.

**Ahora: 50 minutos para la presentación y 45 para ensayar.**
