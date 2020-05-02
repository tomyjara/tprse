import networkx as nx

from modelos import correrModeloSIRM, crearModelo2
import sys


# tipo_de_grafo = sys.argv[1]# cantidad_de_nodos = int(sys.argv[2])
# probabilidad_de_estar_incubando = float(sys.argv[3])
# cantidad_de_iteraciones = int(sys.argv[6])


def main():
    global grafo
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
            cantidadDeNodos = int(input("Cantidad de nodos: "))
            grafo = nx.scale_free_graph(cantidadDeNodos)
            grafo.graph['tipo'] = "Scale Free"
        elif num_grafo == '2':
            cantidadDeNodosX = int(input("Cantidad nodos X: "))
            cantidadDeNodosY = int(input("Cantidad nodos Y: "))
            grafo = nx.grid_graph(dim=[cantidadDeNodosX, cantidadDeNodosY])
            grafo.graph['tipo'] = "Grid " + str(cantidadDeNodosX) + "x" + str(cantidadDeNodosY)
        elif num_grafo == '3':
            cantidadDeNodos = int(input("Cantidad de nodos: "))
            vecinosMasCerca = int(input("Cantidad de vecinos: "))
            probDeRewiringCadaEje = float(input("Probabilidad de rewiring [0,1]: "))

            if probDeRewiringCadaEje > 1 or probDeRewiringCadaEje < 0:
                print("Invalid probability")
                return

            grafo = nx.watts_strogatz_graph(cantidadDeNodos, vecinosMasCerca, probDeRewiringCadaEje)
            grafo.graph['tipo'] = "Small world"
        elif num_grafo == '4':
            gradoDeNodo = int(input("Grado de salida de los nodos: "))
            cantidadDeNodos = int(input("Cantidad de nodos: "))
            seed = int(input("Seed: "))
            grafo = nx.random_regular_graph(gradoDeNodo, cantidadDeNodos, seed)
        elif num_grafo == '5':
            d = int(input("Grado de salida de los nodos: "))
            lamb = int(input("Distancia maxima entre nodos: "))
            grafo = nx.balanced_tree(d, lamb)
            grafo.graph['tipo'] = "Balanced Graph"
        else:
            print("Invalid input.")

        probabilidad_de_estar_incubando = float(input("Probabilidad de estar infectado: "))
        cantidad_de_iteraciones = int(input("Numero de iteraciones: "))

        if probabilidad_de_estar_incubando > 1 or probabilidad_de_estar_incubando < 0:
            print("Invalid probability")
            return

        modelo = crearModelo2(unGrafo=grafo, probabilidad_de_estar_incubando=probabilidad_de_estar_incubando)

        correrModeloSIRM(modelo, cantidad_de_iteraciones)

    except ValueError:
        print("No.. input is invalid.")


if __name__ == "__main__":
    main()
    exit(0)
