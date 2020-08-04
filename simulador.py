import networkx as nx

from modelos import crear_modelo_SIRM, crear_modelo_SISM, crear_modelo_SIRMS, correr_modelo_SISM, \
    correr_modelo_SIRM, correr_modelo_SIRMS


def main():
    global grafo, grado_de_nodo

    nombre_archivo_salida = input("Ingrese el nombre del archivo en el que quiere los resultados \n")

    print("Cantidad de veces que corre: ")

    repeticiones = int(input("Numero: "))

    print("Elegí el modelo:\n"
          "[1] SIS\n"
          "[2] SIR\n"
          "[3] SIRS\n")

    input_modelo = input("Numero: ")

    print("Elegí el grafo:\n"
          "[1] Scale\n"
          "[2] Grid\n"
          "[3] Small World\n"
          "[4] Random\n"
          "[5] Tree Balanceado\n")
    num_grafo = input("Numero: ")

    # TODO: Random graph
    # TODO: No balanced tree
    try:
        if num_grafo == '1':
            cantidad_de_nodos = int(input("Cantidad de nodos: "))
            grafo = nx.scale_free_graph(cantidad_de_nodos)
            grafo.graph['tipo'] = "Scale Free"
        elif num_grafo == '2':
            cantidad_de_nodos_x = int(input("Cantidad nodos X: "))
            cantidad_de_nodos_y = int(input("Cantidad nodos Y: "))
            grafo = nx.grid_graph(dim=[cantidad_de_nodos_x, cantidad_de_nodos_y])
            grafo.graph['tipo'] = "Grid " + str(cantidad_de_nodos_x) + "x" + str(cantidad_de_nodos_y)
        elif num_grafo == '3':
            cantidad_de_nodos = int(input("Cantidad de nodos: "))
            vecinos_mas_cerca = int(input("Cantidad de vecinos: "))
            prob_de_rewiring_cada_eje = float(input("Probabilidad de rewiring [0,1]: "))

            if prob_de_rewiring_cada_eje > 1 or prob_de_rewiring_cada_eje < 0:
                print("Invalid probability")
                return

            grafo = nx.watts_strogatz_graph(cantidad_de_nodos, vecinos_mas_cerca, prob_de_rewiring_cada_eje)
            grafo.graph['tipo'] = "Small world"
        elif num_grafo == '4':
            grado_de_nodo = int(input("Grado de salida de los nodos: "))
            cantidad_de_nodos = int(input("Cantidad de nodos: "))
            seed = int(input("Seed: "))
            grafo = nx.random_regular_graph(grado_de_nodo, cantidad_de_nodos, seed)
            grafo.graph['tipo'] = "Random graph"
        elif num_grafo == '5':
            d = int(input("Grado de salida de los nodos: "))
            lamb = int(input("Distancia maxima entre nodos: "))
            grafo = nx.balanced_tree(d, lamb)
            grafo.graph['tipo'] = "Balanced Tree"
        else:
            raise Exception("Tipo de grafo invalido")

        probabilidad_de_estar_incubando = float(input("Probabilidad de estar infectado: "))
        cantidad_de_iteraciones = int(input("Numero de iteraciones: "))

        if probabilidad_de_estar_incubando > 1 or probabilidad_de_estar_incubando < 0:
            raise Exception("Probabilidad inválida")

        if input_modelo == '1':
            modelo = crear_modelo_SISM(un_grafo=grafo, probabilidad_de_estar_incubando=probabilidad_de_estar_incubando)
            correr_modelo_SISM(modelo, cantidad_de_iteraciones, repeticiones, nombre_archivo_salida, grado_de_nodo,
                               probabilidad_de_estar_incubando)
        elif input_modelo == '2':
            modelo = crear_modelo_SIRM(un_grafo=grafo, probabilidad_de_estar_incubando=probabilidad_de_estar_incubando)
            correr_modelo_SIRM(modelo, cantidad_de_iteraciones, repeticiones, nombre_archivo_salida, grado_de_nodo,
                               probabilidad_de_estar_incubando)
        elif input_modelo == '3':
            modelo = crear_modelo_SIRMS(un_grafo=grafo, probabilidad_de_estar_incubando=probabilidad_de_estar_incubando)
            correr_modelo_SIRMS(modelo, cantidad_de_iteraciones, repeticiones, nombre_archivo_salida, grado_de_nodo,
                                probabilidad_de_estar_incubando)
    except ValueError:
        raise Exception("Input numerico invalido")


if __name__ == "__main__":
    main()
    exit(0)
