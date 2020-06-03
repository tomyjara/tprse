import random

from constantes import ESTADO_INCUBANDO
from estados.estado_nodo import EstadoNodo
from estados.sirms.estado_infectado_grave_sirms import EstadoInfectadoGraveSIRMS
from estados.sirms.estado_infectado_mild_sirms import EstadoInfectadoMildSIRMS


class EstadoIncubandoSIRMS(EstadoNodo):

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
                estado_actual = EstadoInfectadoGraveSIRMS(tiempo_infeccion=grafo.graph['tiempo_inf_grave'])
            else:
                estado_actual = EstadoInfectadoMildSIRMS(tiempo_infeccion=grafo.graph['tiempo_inf_mild'])

        return estado_actual
