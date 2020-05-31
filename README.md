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


CONSIDERACIONES EXPERIMENTOS:

Experimento 2:

 - Ver que la cantidad de ejes sea constatnte para cada tipo de grafo en base a la cantidad de nodos
 - El tamaño del grafo es igual en todos los modelos(cantidad de nodos)
 - Tomamos un estandar de 1% de nodos incubando inicial
 - Cantidad de nodos totales, 3 medidas
 - Medimos: nuevos infectados por unidad, mortalidad
 - Corremos 10 iteraciones y obtenemos promedio por cada configuracion
 - ver a partir de que momento no se ven cambios relevantes(el virus no progresa)
 - 365 unidades y 50000 nodos y 0.01 probabilidad de estar incubando


TODO
- revisar parametros estandar