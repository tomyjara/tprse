import random

from estados.estado_infeccion_grave import EstadoInfeccionGrave
from estados.estado_infeccion_mild import EstadoInfeccionMildCase
from estados.estado_nodo import EstadoNodo


class EstadoIncubando(EstadoNodo):

    def __init__(self, tiempo_incubacion):
        self.tiempo_incubacion = tiempo_incubacion

    def transicionar(self, nodo, grafo):
        self.tiempo_incubacion -= 1

        if self.tiempo_incubacion == 0:
            if grafo.nodes[nodo]['riesgo']:
                return self.transicion_riesgo(nodo, grafo)
            else:
                return self.transicion_no_riesgo(nodo, grafo)
        return self

    @staticmethod
    def transicion_riesgo(nodo, grafo):
        prob_mildcase_riesgo = grafo.nodes[nodo]['prob_mildcase_riesgo']
        if random.random() < prob_mildcase_riesgo:
            return EstadoInfeccionMildCase(tiempo_infeccion=grafo.graph['tiempo_infeccion_mild'])
        else:
            return EstadoInfeccionGrave(tiempo_infeccion=grafo.graph['tiempo_infeccion_grave'])

    @staticmethod
    def transicion_no_riesgo(nodo, grafo):
        prob_mildcase = grafo.nodes[nodo]['prob_mildcase']
        if random.random() < prob_mildcase:
            return EstadoInfeccionMildCase(tiempo_infeccion=grafo.graph['tiempo_infeccion_mild'])
        else:
            return EstadoInfeccionGrave(tiempo_infeccion=grafo.graph['tiempo_infeccion_grave'])
