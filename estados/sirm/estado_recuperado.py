from estados.estado_nodo import EstadoNodo


class EstadoRecuperado(EstadoNodo):

    def transicionar(self, nodo, grafo):
        return self
