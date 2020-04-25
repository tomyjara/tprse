# tprse


COMO CORRER EL SIMULADOR:
Toma 5 parámetros:

tipo_de_grafo,
cantidad_de_nodos,
probabilidad_de_estar_infectado,
tiempo_de_infeccion,
tiempo_de_incubacion

Desde la terminal correr "python simulador.py tipo_de_grafo cantidad_de_nodos probabilidad_de_estar_infectado tiempo_de_infeccion tiempo_de_incubacion"

Donde tipo_de_grafo es un string perteneciente a la siguiente lista: '2d_grid', 'scale', 'small_world', 'random'
Los demás parámetros son enteros salvo probabilidad_de_estar_infectado que es un float entre 0 y 1

Nota, no usar 'small_world' todavía porque faltan parámetros que configurarle(k y p)

Los resultados se guardan en el archivo 'resultados', en la misma carpeta donde estamos corriendo el codigo. Es un csv donde hay que mirar de a 4 valores,
el primero es el porcentaje de infectados, luego sigue el de susceptibles, el de recuperados y el de muertos. Cada lote de 4 valores representa el estado del
modelo en la n-esima iteracion

Tareas Tomi:

-agrager nuevo estado muerto LISTO
-agregar tasa de letalidad y dividir en poblaciones de riesgo(averiguar) //LISTO solo agrego tasa de letalidad
-en cada iteracion se tira una moneda que representa si muere segun su probabilidad(mientras esta infectado post incubacion) LISTO
-mientras lo incubo contagio, tiempo de incubacion 6-14 días(usar promedio), contagia pero no muere LISTO
-no puede morir hasta despues del promedio del tiempo de incubacion ti > 10 LISTO
-medir en unidades


Tareas Juli:

-armar grafos que pidio esteban
-analizar bien random graph
-data en funcion del tiempo
-data en funcion de los infectados
-cantidad de nuevos infectados x dia
-averiguar ti y ri

Preguntas?

Esta bien probar con varios modelos? Es sis es sir?
tiempo de infeccion(incubacion+presenta la patologia)
Consultar de R a S cuanto tiempo debería pasar

Consulta esteban:

Averiguar ti, ri, r0=probabilidad de contagio que ahora la contamos como vecinos infectados/totales
Utilizar sis, sirs, sir o todo

Medimos:

-muertos
-susceptible
-infectado
-recuperado
-incubando?
-nuevos casos en el día
-casos totales x día
-casos nuevos en la última semana según total de infectadosx


