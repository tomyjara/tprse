import random

from estados.estado_incubando import EstadoIncubando
from estados.estado_nodo import EstadoNodo


class EstadoSusceptible(EstadoNodo):

    def seContagiaDada(self, una_probabilidad):
        return random.random() < una_probabilidad

    def transicionar(self, nodo, grafo):
        probabilidad_de_contagio = self.calcularProbabilidadDeContagio(grafo, nodo)

        estado_actual = self
        if self.seContagiaDada(probabilidad_de_contagio):
            estado_actual = EstadoIncubando(tiempo_incubacion=grafo.graph['tiempo_incubacion'])

        return estado_actual
