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
