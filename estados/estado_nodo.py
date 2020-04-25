import abc


class EstadoNodo:
    __metaclass__ = abc.ABCMeta

    def calcularProbabilidadDeContagio(self, grafo, nodo):
        vecinos = list(grafo.neighbors(nodo))
        if len(vecinos) == 0:
            return 0
        else:
            return len([vecino for vecino in vecinos if type(grafo.nodes[vecino]['estado']).__name__ == 'EstadoInfectado']) \
                   / len(vecinos)

    @abc.abstractmethod
    def transicionar(self, nodo, grafo):
        """Recibe el estado actual de un nodo y retorna el nuevo estado del nodo luego de transicionar"""
