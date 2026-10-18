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
Se estudia un estanque con 100 L iniciales y caudal neto r(t) = 2t (L/min) en el intervalo [0, 5] min. Se calcula la integral exacta (ΔQ = t²) quedando ΔQ = 25 L y se muestra que el volumen final se obtiene como cantidad inicial (100 L) + cambio acumulado (25 L), quedando como resultado 125 L . Con otra cantidad inicial cómo 40 L la integral es la misma, pero el volumen final es 65 L.

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
| 2 | () | Tasa de cambio: Q′(t) = r(t) y significado del signo (r > 0 aumenta, r < 0 disminuye, r = 0 no cambia) | Lucas |
| 3 | () | Integral y acumulación: aportes r(t)·Δt, suma de los aportes, límite e integral ΔQ = ∫r dt | Renato |
| 4 | () | Q(0) = 100 L y Q(0) = 40 L; cambio acumulado vs. cantidad final: Q(b) = Q(a) + ∫r | Renato |
| 5 | () | Cálculo exacto: antiderivada t²/2, ΔQ = [t²]₀⁵ = 25 L y unidades (L/min · min = L) | Victor |
| 6 | () | Respuesta y cierre | Victor |


## Parámetros matemáticos usados en las escenas

| Parámetro | Valor |
|---|---|
| Función (tasa) | r(t) = 2t, en L/min |
| Intervalo | [0, 5] min |
| Cantidad inicial | Q(0) = 100 L (caso comparativo: Q(0) = 40 L) |
| Resultados | ∫₀⁵ r dt = 25 L · Q(5) = 125 L (o 65 L) |
