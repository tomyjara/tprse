from modelos import correrModeloSIRM, crearModelo2
import sys

tipo_de_grafo = sys.argv[1]
cantidad_de_nodos = int(sys.argv[2])
probabilidad_de_estar_infectado = float(sys.argv[3])
tiempo_de_infeccion = int(sys.argv[4])
tiempo_de_incubacion = int(sys.argv[5])
cantidad_de_iteraciones = int(sys.argv[6])


modelo = crearModelo2(tipo_de_grafo=tipo_de_grafo, cantidad_de_nodos=cantidad_de_nodos,
                      probabilidad_de_estar_infectado=probabilidad_de_estar_infectado, tiempo_infeccion=tiempo_de_infeccion, ri=0,
                      tiempo_incubacion=tiempo_de_incubacion)

correrModeloSIRM(modelo, cantidad_de_iteraciones)
