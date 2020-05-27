import abc


class EstadoNodo(abc.ABC):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def transicionar(self, nodo, grafo):
        """Recibe el estado actual de un nodo y retorna el nuevo estado del nodo luego de transicionar"""
