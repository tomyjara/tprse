import random

from estados.estado_muerto import EstadoMuerto
from estados.estado_nodo import EstadoNodo
from estados.estado_recuperado import EstadoRecuperado


class EstadoInfectado(EstadoNodo):

    def __init__(self, tiempo_infeccion, tiempo_incubacion):
        self.tiempo_infeccion = tiempo_infeccion
        self.tiempo_incubacion = tiempo_incubacion

    def muereDada(self, una_probabilidad, t_incubacion):
        if not t_incubacion > 0:
            return random.random() < una_probabilidad
        else:
            return False

    def transicionar(self, nodo, grafo):
        self.tiempo_infeccion -= 1
        self.tiempo_incubacion -= 1

        probabilidad_de_deceso = grafo.graph['prob_de_deceso']

        estado_actual = self
        if self.muereDada(probabilidad_de_deceso, self.tiempo_incubacion):
            estado_actual = EstadoMuerto()
        else:
            if self.tiempo_infeccion == 0:
                estado_actual = EstadoRecuperado()

        return estado_actual
