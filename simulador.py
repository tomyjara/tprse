from modelos import correrModeloSIRM, crearModelo2
import sys

tipo_de_grafo = sys.argv[1]
cantidad_de_nodos = int(sys.argv[2])
probabilidad_de_estar_infectado = float(sys.argv[3])
tiempo_de_infeccion = int(sys.argv[4])
cantidad_de_iteraciones = int(sys.argv[5])
poblacion_de_riesgo = int(sys.argv[6])

modelo = crearModelo2(tipo_de_grafo=tipo_de_grafo, cantidad_de_nodos=cantidad_de_nodos,
                      probabilidad_de_estar_infectado=probabilidad_de_estar_infectado, ri=0,
                      probabilidad_p_riesgo=poblacion_de_riesgo)

correrModeloSIRM(modelo, cantidad_de_iteraciones)
