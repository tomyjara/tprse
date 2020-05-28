import sys

import networkx as nx

from modelos import crear_modelo_SIRM, correr_modelo_SIRM, crear_modelo_SISM, crear_modelo_SIRMS, correr_modelo_SISM, \
    correr_modelo_SIRMS


def main():
    try:
        input_modelo = sys.argv[1]
        tipo_de_grafo = sys.argv[2]

        if tipo_de_grafo == "scale":
            check_parametros(5)
            cantidad_de_nodos = int(sys.argv[3])
            next_arg = 3
            grafo = nx.scale_free_graph(cantidad_de_nodos)
            grafo.graph['tipo'] = "Scale Free"

        elif tipo_de_grafo == "grid":
            check_parametros(6)
            cantidad_de_nodos_x = int(sys.argv[3])
            cantidad_de_nodos_y = int(sys.argv[4])
            next_arg = 4
            grafo = nx.grid_graph(dim=[cantidad_de_nodos_x, cantidad_de_nodos_y])
            grafo.graph['tipo'] = "Grid " + str(cantidad_de_nodos_x) + "x" + str(cantidad_de_nodos_y)

        elif tipo_de_grafo == "small_world":
            check_parametros(7)
            cantidad_de_nodos = int(sys.argv[3])
            vecinos_mas_cerca = int(sys.argv[4])
            prob_de_rewiring_cada_eje = float(sys.argv[5])
            next_arg = 5
            if prob_de_rewiring_cada_eje < 0 or prob_de_rewiring_cada_eje > 1:
                raise Exception("Probabilidad inválida")
            grafo = nx.watts_strogatz_graph(cantidad_de_nodos, vecinos_mas_cerca, prob_de_rewiring_cada_eje)
            grafo.graph['tipo'] = "Small world"

        elif tipo_de_grafo == "random":
            check_parametros(7)
            cantidad_de_nodos = int(sys.argv[3])
            grado_salida = int(sys.argv[4])
            seed = int(sys.argv[5])
            next_arg = 5
            grafo = nx.random_regular_graph(grado_salida, cantidad_de_nodos, seed)
            grafo.graph['tipo'] = "Random graph"

        elif tipo_de_grafo == "balanced_tree":
            check_parametros(6)
            d = int(sys.argv[3])  # Grado de salida de los nodos
            lamb = int(sys.argv[4])  # Distancia máxima entre par de nodos
            next_arg = 4
            grafo = nx.balanced_tree(d, lamb)
            grafo.graph['tipo'] = "Balanced Tree"

        else:
            raise Exception("Tipo de grafo invalido")

        probabilidad_de_estar_incubando = float(sys.argv[next_arg])
        next_arg += 1
        cantidad_de_iteraciones = int(sys.argv[next_arg])

    except ValueError:
        raise Exception("Input numerico invalido")

    if input_modelo == 'SIS':
        modelo = crear_modelo_SISM(unGrafo=grafo, probabilidad_de_estar_incubando=probabilidad_de_estar_incubando)
        correr_modelo_SISM(modelo, cantidad_de_iteraciones)
    elif input_modelo == 'SIR':
        modelo = crear_modelo_SIRM(unGrafo=grafo, probabilidad_de_estar_incubando=probabilidad_de_estar_incubando)
        correr_modelo_SIRM(modelo, cantidad_de_iteraciones)
    elif input_modelo == 'SIRS':
        modelo = crear_modelo_SIRMS(un_grafo=grafo, probabilidad_de_estar_incubando=probabilidad_de_estar_incubando)
        correr_modelo_SIRMS(modelo, cantidad_de_iteraciones)



def check_parametros(cant_param):
    if sys.argv.__len__() > cant_param:
        raise Exception("Parametros de más")


if __name__ == "__main__":
    main()
