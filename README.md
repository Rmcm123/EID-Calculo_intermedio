# EID Cálculo Intermedio – Grupo 7

**Introducción a la integral con Manim Community**

| Campo | Dato |
|---|---|
| Curso | MAT1188 – Cálculo Intermedio |
| Grupo | 07 |
| Tema | Cambio acumulado versus cantidad final |
| Pregunta central | ¿Por qué integrar una tasa de cambio no entrega necesariamente la cantidad final? |

## Integrantes

| Integrante | Cuenta de GitHub | Responsabilidad principal |
|---|---|---|
| Renato Cáceres | Rmcm123 | Investigación y desarrollo matemático |
| Victor Hidalgo | vhidalgo0 | Implementación y visualización en Manim |
| Lucas Núñez | nunezpinillalucas435-dev | Guion, documentación y organización del video |

## Resumen del proyecto

Se estudia un estanque con 150 L iniciales y caudal neto r(t) = 12 − 2t (L/min) en el intervalo [0, 8] min. Se construyen sumas de Riemann con n = 4, 8, 16 y 32, se calcula la integral exacta (32 L) y se muestra que el volumen final (182 L) se obtiene como **cantidad inicial + cambio acumulado**. Con otra cantidad inicial (40 L) la integral es la misma, pero el volumen final es 72 L.

## Versiones y dependencias

- Python: 3.10 o mayor
- Manim Community: ()
- Otras dependencias: ()
- Para renderizar: ()

## Escenas y ejecución

Archivo principal: (). Los nombres de escena deben coincidir con los del código entregado (Victor confirma):

| # | Escena | Contenido | Voz |
|---|---|---|---|
| 1 | () | Presentación: integrantes, tema y pregunta central | Lucas |
| 2 | () | Teoría: V′ = r, aportes r(t*)·Δt, suma de Riemann, integral y relación V(b) = V(a) + ∫r | Renato |
| 3 | () | Estanque y sumas de Riemann para n = 4, 8, 16, 32 (izquierda y derecha) | Victor |
| 4 | () | Cálculo exacto: F(t) = 12t − t², áreas con signo 36 − 4 = 32 | Renato |
| 5 | () | V(t) con V(0) = 150 y V(0) = 40; cambio acumulado vs. cantidad final | Lucas |
| 6 | () | Respuesta y cierre | Renato, Victor, Lucas |


## Parámetros matemáticos usados en las escenas

| Parámetro | Valor |
|---|---|
| Función (tasa) | r(t) = 12 − 2t, en L/min |
| Intervalo | [0, 8] min |
| Número de subintervalos | n = 4, 8, 16, 32 |
| Ancho | Δt = 8/n |
| Puntos muestra | Extremos izquierdos y derechos |
| Cantidad inicial | V(0) = 150 L (caso comparativo: V(0) = 40 L) |
| Resultados | ∫₀⁸ r dt = 32 L · V(8) = 182 L (o 72 L) |
