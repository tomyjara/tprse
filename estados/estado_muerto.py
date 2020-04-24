from estados.estado_nodo import EstadoNodo


class EstadoMuerto(EstadoNodo):

    def transicionar(self, nodo, grafo):
        return self
