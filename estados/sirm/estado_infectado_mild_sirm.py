from constantes import ESTADO_INFECTADO_MILD
from estados.estado_infectado import EstadoInfectado
from estados.sirm.estado_recuperado import EstadoRecuperado

'''Estado de infeccion leve, estos nodos no mueren y pasan de infectados a recuperados'''


class EstadoInfectadoMildSIRM(EstadoInfectado):
    def __init__(self, tiempo_infeccion):
        self.__class__.__name__ = ESTADO_INFECTADO_MILD
        self.tiempo_infeccion = tiempo_infeccion

    def transicionar(self, nodo, grafo):
        self.tiempo_infeccion -= 1
        estado_actual = self

        if self.tiempo_infeccion == 0:
            estado_actual = EstadoRecuperado()

        return estado_actual
