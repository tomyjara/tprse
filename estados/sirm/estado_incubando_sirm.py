import random

from constantes import ESTADO_INCUBANDO
from estados.sirm.estado_infectado_grave_sirm import EstadoInfectadoGraveSIRM
from estados.sirm.estado_infectado_mild_sirm import EstadoInfectadoMildSIRM
from estados.estado_nodo import EstadoNodo


class EstadoIncubandoSIRM(EstadoNodo):

    def __init__(self, tiempo_incubacion):
        self.__class__.__name__ = ESTADO_INCUBANDO
        self.tiempo_incubacion = tiempo_incubacion

    def transicionar(self, nodo, grafo):
        self.tiempo_incubacion -= 1
        estado_actual = self

        if self.tiempo_incubacion == 0:

            es_persona_de_riesgo = grafo.nodes[nodo]['riesgo']

            prob_de_infeccion_grave = grafo.graph['prob_infec_grave_riesgo'] if es_persona_de_riesgo else grafo.graph[
                'prob_infec_grave']

            if random.random() < prob_de_infeccion_grave:
                estado_actual = EstadoInfectadoGraveSIRM(tiempo_infeccion=grafo.graph['tiempo_inf_grave'])
            else:
                estado_actual = EstadoInfectadoMildSIRM(tiempo_infeccion=grafo.graph['tiempo_inf_mild'])

        return estado_actual
