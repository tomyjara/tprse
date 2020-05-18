import sys

import networkx as nx

from modelos import crear_modelo_SIRM, correr_modelo_SIRM


def main():
    try:
        tipoDeGrafo = sys.argv[1]

        if tipoDeGrafo == "scale":
            check_parametros(5)
            cantidadDeNodos = int(sys.argv[2])
            nextArg = 3
            grafo = nx.scale_free_graph(cantidadDeNodos)
            grafo.graph['tipo'] = "Scale Free"

        elif tipoDeGrafo == "grid":
            check_parametros(6)
            cantidadDeNodosX = int(sys.argv[2])
            cantidadDeNodosY = int(sys.argv[3])
            nextArg = 4
            grafo = nx.grid_graph(dim=[cantidadDeNodosX, cantidadDeNodosY])
            grafo.graph['tipo'] = "Grid " + str(cantidadDeNodosX) + "x" + str(cantidadDeNodosY)

        elif tipoDeGrafo == "small_world":
            check_parametros(7)
            cantidadDeNodos = int(sys.argv[2])
            vecinosMasCerca = int(sys.argv[3])
            probDeRewiringCadaEje = float(sys.argv[4])
            nextArg = 5
            if (probDeRewiringCadaEje < 0 or probDeRewiringCadaEje > 1):
                raise Exception("Probabilidad inválida")
            grafo = nx.watts_strogatz_graph(cantidadDeNodos, vecinosMasCerca, probDeRewiringCadaEje)
            grafo.graph['tipo'] = "Small world"

        elif tipoDeGrafo == "random":
            check_parametros(7)
            cantidadDeNodos = int(sys.argv[2])
            gradoSalida = int(sys.argv[3])
            seed = int(sys.argv[4])
            nextArg = 5
            grafo = nx.random_regular_graph(gradoSalida, cantidadDeNodos, seed)
            grafo.graph['tipo'] = "Random graph"

        elif tipoDeGrafo == "balanced_tree":
            check_parametros(6)
            d = int(sys.argv[2])  # Grado de salida de los nodos
            lamb = int(sys.argv[3])  # Distancia máxima entre par de nodos
            nextArg = 4
            grafo = nx.balanced_tree(d, lamb)
            grafo.graph['tipo'] = "Balanced Tree"

        else:
            raise Exception("Tipo de grafo invalido")

        probabilidad_de_estar_incubando = float(sys.argv[nextArg])
        nextArg += 1
        cantidad_de_iteraciones = int(sys.argv[nextArg])

    except ValueError:
        raise Exception("Input numerico invalido")

    modelo = crear_modelo_SIRM(unGrafo=grafo, probabilidad_de_estar_incubando=probabilidad_de_estar_incubando)

    correr_modelo_SIRM(modelo, cantidad_de_iteraciones)


def check_parametros(cantParam):
    if sys.argv.__len__() > cantParam:
        raise Exception("Parametros de más")


if __name__ == "__main__":
    main()
