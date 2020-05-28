import random

from constantes import ESTADO_INFECTADO_GRAVE, ESTADO_INFECTADO_MILD, ESTADO_INCUBANDO, ESTADO_SUSCEPTIBLE
from estados.estado_nodo import EstadoNodo
from estados.sirms.estado_incubando_sirms import EstadoIncubandoSIRMS


class EstadoSusceptibleSIRMS(EstadoNodo):

    def __init__(self):
        self.__class__.__name__ = ESTADO_SUSCEPTIBLE

    def calcular_probabilidad_de_contagio(self, grafo, nodo):
        vecinos = list(grafo.neighbors(nodo))
        if len(vecinos) == 0:
            return 0
        else:
            return len(
                [vecino for vecino in vecinos if
                 type(grafo.nodes[vecino]['estado']).__name__ in [ESTADO_INFECTADO_GRAVE, ESTADO_INFECTADO_MILD,
                                                                  ESTADO_INCUBANDO]]) \
                   / len(vecinos)

    def se_contagia_dada(self, una_probabilidad):
        return random.random() < una_probabilidad

    def transicionar(self, nodo, grafo):
        probabilidad_de_contagio = self.calcular_probabilidad_de_contagio(grafo, nodo)

        estado_actual = self
        if self.se_contagia_dada(probabilidad_de_contagio):
            estado_actual = EstadoIncubandoSIRMS(tiempo_incubacion=grafo.graph['tiempo_incubacion'])

        return estado_actual
