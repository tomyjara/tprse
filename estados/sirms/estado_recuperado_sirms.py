from constantes import ESTADO_RECUPERADO
from estados.estado_nodo import EstadoNodo


class EstadoRecuperadoSIRMS(EstadoNodo):

    def __init__(self, tiempo_recuperacion):
        self.__class__.__name__ = ESTADO_RECUPERADO
        self.tiempo_recuperacion = tiempo_recuperacion

    def transicionar(self, nodo, grafo):
        self.tiempo_recuperacion -= 1
        estado_actual = self

        if self.tiempo_recuperacion == 0:
            from estados.sirms.estado_susceptible_sirms import EstadoSusceptibleSIRMS
            estado_actual = EstadoSusceptibleSIRMS()

        return estado_actual
