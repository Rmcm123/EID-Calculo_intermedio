# Investigación por Renato Cáceres

## 1. Cambio acumulado versus cantidad final

### Pregunta central

**¿Por qué integrar una tasa de cambio no entrega necesariamente la cantidad final?**

Para comenzar, debemos responder tres preguntas:

1. ¿Qué es una tasa de cambio?
2. ¿Qué información nos entrega una integral?
3. ¿Cuál es la diferencia entre un cambio acumulado y una cantidad final?

---

## 2. ¿Qué es una tasa de cambio?

Una tasa de cambio indica qué tan rápido aumenta o disminuye una cantidad con respecto a otra variable.

Si una cantidad se representa mediante una función $Q(t)$, entonces su tasa de cambio se puede representar mediante su derivada:

$$
r(t)=Q'(t)
$$

donde:

- $Q(t)$ representa la cantidad que estamos estudiando.
- $t$ representa el tiempo.
- $r(t)$ representa la tasa de cambio de esa cantidad.

Por ejemplo, si $Q(t)$ representa la cantidad de agua que existe en un estanque en un instante específico, entonces $Q'(t)$ indica qué tan rápido está aumentando o disminuyendo la cantidad de agua.

Si:

$$
Q'(t)=5\text{ L/min}
$$

significa que la cantidad de agua está aumentando a una razón de 5 litros por minuto.

En cambio, si:

$$
Q'(t)=-5\text{ L/min}
$$

significa que la cantidad de agua está disminuyendo a una razón de 5 litros por minuto.

Por lo tanto, el signo de la tasa de cambio también nos entrega información:

- Si $r(t)>0$, la cantidad aumenta.
- Si $r(t)<0$, la cantidad disminuye.
- Si $r(t)=0$, en ese instante la cantidad no está cambiando.

---------------------------------------------------------------------------------------------

## 2)¿Qué información nos entrega una integral?

Una integral definida nos permite acumular los valores de una funcion a lo largo de un intervalo.

En este caso como estamos trabajando con una tasa de cambio de  $r(t)$, la integral nos permite conocer cuanto cambió en total la catidad estudiada entre un instante iniciar $a$ y un instante
final $b$.

Este cambio se puede representar como:

$$
\Delta Q = \int_a^b r(t)\,dt
$$

Donde:

- $a$ representa el instante inicial.
- $b$ representa el instante final.
- $r(t)$ representa la tasa de cambio.
- $\Delta Q$ representa el cambio acumulado de la cantidad.

  por lo que al integrar una tasa de cambio, no estamos obteniendo directamente el valor final de la cantidad, si no cuanto aumentó o disminuyó durante el intervalo.

  ### ¿Por qué hablamos de "acumulación"?

durante pequeños intervalos de tiempo $\Delta t$ ocurre un pequeño cambio en la cantidad, este pequeño cambio se puede aproximar con:

$$
r(t)\Delta t
$$

Por ejemplo, si durante un pequeño intervalo la tasa es aproximadamente: 

$$
r(t)=5\text{ L/min}
$$

y pasa un minuto, el cambio producido seria aproximadamente:

$$
5\frac{\text{L}}{\text{min}}\cdot1\text{ min}=5\text{ L}
$$

Si dividimos un intervalo completo en muchos intervalos pequeños y sumamos todos estos cambios, obtenemos una aproximación del cambio total.


La integral representa el limite de este proceso de acumulación:

$$
\Delta Q=\int_a^b r(t)\,dt
$$

Por eso, cuando integramos una tasa de cambio, obtenemos el cambio acumulado durante el intervalo

## 3) ¿Cuál es la diferencia entre un cambio acumulado y una cantidad final?

El cambio acumulado y la cantidad final son conceptos distintos.

El **cambio acumulado** indica cuanto aumentó o disminuyó una cantidad durante un intervalo.

Se calcula mediante:

$$
\Delta Q=\int_a^b r(t)\,dt
$$

En cambio la **cantidad final** representa el valor que tiene la cantidad estudiada al terminar el intervalo.

para obtenerla necesitamos conocer tambien la cantidad inicial.

la relación es 

$$
\boxed{Q(b)=Q(a)+\int_a^b r(t)\,dt}
$$

donde :

- $Q(a)$ es la cantidad inicial.
- $\int_a^b r(t)\,dt$ es el cambio acumulado.
- $Q(b)$ es la cantidad final.

o tambien

$$
\boxed{\text{Cantidad final}=\text{Cantidad inicial}+\text{Cambio acumulado}}
$$

Esta diferencia es justamente la idea principal de la investigación.

La integral de la tasa nos indica cuanto cambió la cantidad, pero no necesariamente cuanto vale al final, ya que para conocer el valor final tambien necesitaríamos saber con que cantidad comenzamos.

### ejemplo

supongamos que un estanque comienza con: 

$$
100\text{ L}
$$

y durante cierto intervalo la integral de su tasa de cambio entrega:

$$
\int_a^b r(t)\,dt=20\text{ L}
$$

Estos $20$ listros representan el **cambio acumulado**, no la cantidad final.

Como inicialmente existian 100 litros

$$
Q(b)=100+20
$$

por lo tanto

$$
Q(b)=120\text{ L}
$$

Entonces tenemos:

- Cantidad inicial: $100\text{ L}$
- Cambio acumulado: $+20\text{ L}$
- Cantidad final: $120\text{ L}$

Esto demuestra que integrar la tasa de cambio no necesariamente entrega la cantidad final.

## 4) Ejemplo de desarrollo


Supongamos que un estanque contiene inicialmente:

$$
Q(0)=100\text{ L}
$$

La cantidad de agua del estanque cambia con el tiempo. Su tasa de cambio está dada por:

$$
r(t)=Q'(t)=2t
$$

donde $t$ representa el tiempo medido en minutos.

Esto significa que la tasa de cambio no es constante, sino que aumenta con el tiempo.

Por ejemplo:

- En $t=0$, la tasa es $r(0)=0$ L/min.
- En $t=1$, la tasa es $r(1)=2$ L/min.
- En $t=2$, la tasa es $r(2)=4$ L/min.
- En $t=5$, la tasa es $r(5)=10$ L/min.

Queremos saber cuánto cambió la cantidad de agua entre los minutos 0 y 5.

### Supuestos del ejemplo

Para desarrollar el ejemplo del estanque se consideran los siguientes supuestos:

- El tiempo $t$ se mide en minutos.
- La cantidad de agua $Q(t)$ se mide en litros.
- El estanque contiene inicialmente:

$$
Q(0)=100\text{ L}
$$

- La tasa de cambio del agua está dada por:

$$
r(t)=2t
$$

y se mide en litros por minuto.

- El intervalo de tiempo estudiado es:

$$
0\leq t\leq5
$$

- Se considera que todos los cambios de agua que ocurren en el estanque están representados por la tasa $r(t)$.
- No se consideran otros ingresos o pérdidas de agua externos a los representados por la función.

### Continuidad de la tasa de cambio

La función utilizada como tasa de cambio es:

$$
r(t)=2t
$$

Esta función es continua en todo el intervalo:

$$
[0,5]
$$

Esto significa que la tasa de cambio no presenta saltos ni interrupciones durante el intervalo estudiado.

Al ser continua en el intervalo, podemos calcular el cambio acumulado mediante la integral:

$$
\Delta Q=\int_0^5 r(t)\,dt
$$

### Cálculo del cambio acumulado

Para obtener el cambio acumulado entre $t=0$ y $t=5$, integramos la tasa de cambio:

$$
\Delta Q=\int_0^5 2t\,dt
$$

Sacamos la constante 2:

$$
\Delta Q=2\int_0^5 t\,dt
$$

Calculamos una antiderivada de $t$:

$$
\int t\,dt=\frac{t^2}{2}
$$

Por lo tanto:

$$
\Delta Q=
2\left[\frac{t^2}{2}\right]_0^5
$$

El 2 se simplifica con el denominador:

$$
\Delta Q=
[t^2]_0^5
$$

Ahora evaluamos en los extremos:

$$
\Delta Q=5^2-0^2
$$

$$
\Delta Q=25
$$

Por lo tanto:

$$
\boxed{\Delta Q=25\text{ L}}
$$

### Unidades

La función $r(t)$ representa una tasa de cambio, por lo que sus unidades son litros por minuto:

$$
\frac{\text{L}}{\text{min}}
$$

Al integrar respecto del tiempo, $dt$ tiene unidades de minutos.

Por lo que:

$$
\frac{\mathrm{L}}{\mathrm{min}}\cdot \mathrm{min}=\mathrm{L}
$$

Por esta razón, el resultado de la integral está expresado en litros.

Entonces:

$$
\int_0^5 r(t)\,dt=25\mathrm{L}
$$

significa que durante esos cinco minutos la cantidad de agua aumentó en 25 litros.

### Caso especial: cantidad inicial igual a cero

Normalmente, el cambio acumulado y la cantidad final no son iguales, debido a que para calcular la cantidad final también debemos considerar la cantidad inicial.

La relación utilizada es:

$$
Q(b)=Q(a)+\int_a^b r(t)\,dt
$$

Sin embargo, existe un caso especial en el que la cantidad inicial es igual a cero.

Si:

$$
Q(a)=0
$$

entonces:

$$
Q(b)=0+\int_a^b r(t)\,dt
$$

Por lo tanto:

$$
\boxed{Q(b)=\int_a^b r(t)\,dt}
$$

En este caso particular, el valor del cambio acumulado y la cantidad final coinciden.

Por ejemplo, si el mismo estanque comenzara completamente vacío:

$$
Q(0)=0\text{ L}
$$

y mantuviéramos la misma tasa de cambio:

$$
r(t)=2t
$$

durante el intervalo de 0 a 5 minutos, tendríamos:

$$
\int_0^5 2t\,dt=25\text{ L}
$$

Como la cantidad inicial es cero:

$$
Q(5)=0+25
$$

por lo tanto:

$$
Q(5)=25\text{ L}
$$

Entonces tenemos:

- Cantidad inicial: $0\text{ L}$
- Cambio acumulado: $25\text{ L}$
- Cantidad final: $25\text{ L}$

En este caso, la integral y la cantidad final coinciden numéricamente debido a que la cantidad inicial es igual a cero.

## 5) Fuentes utilizadas

Para desarrollar los conceptos relacionados con tasa de cambio, derivadas, integrales y acumulación se utilizaron textos de cálculo como fuentes matemáticas de apoyo.

Ron Larson se utilizó principalmente para respaldar los conceptos relacionados con derivadas, tasas de cambio e integración.

James Stewart se utilizó como fuente complementaria para los conceptos relacionados con integral definida, acumulación y la relación existente entre derivación e integración.

## Bibliografía

1. Larson, R., Hostetler, R. P., & Edwards, B. H. (2006).  
   *Cálculo I* (8.ª ed.).  
   McGraw-Hill Interamericana.

2. Stewart, J. (2018).  
   *Cálculo: Trascendentes tempranas* (8.ª ed.).  
   Cengage Learning.
