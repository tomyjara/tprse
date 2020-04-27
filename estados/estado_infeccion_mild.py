from estados.estado_nodo import EstadoNodo
from estados.estado_recuperado import EstadoRecuperado


class EstadoInfeccionMildCase(EstadoNodo):
    def __init__(self, tiempo_infeccion):
        self.tiempo_infeccion = tiempo_infeccion

    def transicionar(self, nodo, grafo):
        self.tiempo_infeccion -= 1

        estado_actual = self

        if self.tiempo_infeccion == 0:
            estado_actual = EstadoRecuperado()

        return estado_actual
