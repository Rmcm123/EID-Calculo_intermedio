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

- Python utilizado: 3.14.
- Manim Community: 0.22.0.
- Dependencias especificadas en `requirements.txt`.

## Ejecución

Archivo principal: `main.py`.

Para renderizar:
```bash
python -m manim -ql main.py Presentacion
```

## Parámetros matemáticos usados en las escenas

| Parámetro | Valor |
|---|---|
| Función (tasa) | r(t) = 2t, en L/min |
| Intervalo | [0, 5] min |
| Cantidad inicial | Q(0) = 100 L (caso comparativo: Q(0) = 40 L) |
| Resultados | ∫₀⁵ r dt = 25 L · Q(5) = 125 L (o 65 L) |
