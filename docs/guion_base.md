# GUION

## presentación: lucas

"buenas tardes, somos el grupo 7: Renato Cáceres, Victor Hidalgo y yo, Lucas Núñez. Nuestro tema es cambio acumulado versus cantidad final. Y nuestra pregunta central es: ¿por qué integrar una tasa de cambio no entrega necesariamente la cantidad final? Para responderla vamos a usar un ejemplo con un estanque de agua."

## tasa de cambio: lucas

"Una tasa de cambio indica qué tan rápido aumenta o disminuye una cantidad. Si Q de t es la cantidad de agua en un estanque, su tasa de cambio es la derivada: r de t igual a Q prima de t. Si Q prima vale 5 litros por minuto, el agua aumenta a razón de 5 litros cada minuto. Si vale menos 5, el agua disminuye a esa misma razón. Entonces el signo también informa: si r es positiva la cantidad aumenta, si es negativa disminuye, y si es cero, en ese instante no está cambiando."

## integral y acumulación: renato

"Ahora, ¿qué información entrega una integral? Una integral definida acumula los valores de una función en un intervalo. En un intervalo pequeño de ancho delta t, la cantidad cambia aproximadamente r de t por delta t. Por ejemplo, si la tasa es de 5 litros por minuto y pasa un minuto, el cambio es de 5 litros. Si dividimos el intervalo completo en muchos intervalos pequeños y sumamos todos esos cambios, obtenemos una aproximación del cambio total. La integral es el límite de ese proceso de acumulación: delta Q igual a la integral de a hasta b de r de t dt. Por eso, al integrar una tasa de cambio obtenemos el cambio acumulado, es decir, cuánto aumentó o disminuyó la cantidad, y no directamente su valor final."

## cambio acumulado vs cantidad final: renato

"El cambio acumulado y la cantidad final son conceptos distintos. El cambio acumulado dice cuánto aumentó o disminuyó la cantidad durante el intervalo. La cantidad final es el valor que tiene la cantidad al terminar, y para obtenerla necesitamos conocer también la cantidad inicial. La relación es: Q de b igual a Q de a más la integral de a hasta b de r. Dicho en palabras: cantidad final igual a cantidad inicial más cambio acumulado. Veámoslo con dos estanques que tienen la misma tasa. Supongamos que la integral entrega 25 litros, valor que calcularemos enseguida. Si el estanque parte con 100 litros, termina con 125. Si parte con 40 litros, termina con 65. Misma integral, distinta cantidad final: la tasa informa cómo cambia la cantidad, pero no desde dónde partió."

## calculo de ejercicio: victor

"Calculemos el cambio acumulado de nuestro ejemplo: un estanque con 100 litros iniciales y tasa r de t igual a 2t litros por minuto, con t en minutos. La tasa no es constante, crece con el tiempo: en t igual a 0 vale 0, en 1 vale 2, en 2 vale 4 y en 5 vale 10 litros por minuto. Queremos el cambio entre los minutos 0 y 5, así que integramos: la integral de 0 a 5 de 2t dt. Sacamos el 2, y una antiderivada de t es t al cuadrado sobre 2. El 2 se simplifica con el denominador y queda t al cuadrado evaluado entre 0 y 5. Esto significa sustituir t por 5 y restar el valor obtenido al sustituir t por 0: 5 al cuadrado menos 0 al cuadrado. Así obtenemos 25 menos 0, es decir, 25. Sobre las unidades: r está en litros por minuto y dt en minutos, entonces litros por minuto por minuto da litros. Por eso el cambio acumulado es 25 litros: durante esos cinco minutos el agua aumentó 25 litros, y como partía con 100, la cantidad final es 125 litros."

## cierre: victor

"Respondiendo la pregunta: integrar una tasa de cambio nos da solo el cambio acumulado en el intervalo, porque la tasa no contiene información sobre la cantidad inicial. En el ejemplo, la integral fue 25 litros, pero la cantidad final fue 125 litros si el estanque partía con 100, y 65 litros si partía con 40. Por eso la integral es acumulación: suma de aportes pequeños convertida en límite. Y la cantidad final es siempre la cantidad inicial más el cambio acumulado. Gracias por ver."

