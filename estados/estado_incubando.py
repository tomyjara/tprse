import random

from estados.estado_infectado_grave import EstadoInfectadoGrave
from estados.estado_infectado_mild import EstadoInfectadoMild
from estados.estado_nodo import EstadoNodo


class EstadoIncubando(EstadoNodo):

    def __init__(self, tiempo_incubacion):
        self.tiempo_incubacion = tiempo_incubacion

    def transicionar(self, nodo, grafo):
        self.tiempo_incubacion -= 1
        estado_actual = self

        if self.tiempo_incubacion == 0:
            if grafo.nodes[nodo]['riesgo']:
                if random.random() < grafo.graph['prob_infec_grave_riesgo']:
                    estado_actual = EstadoInfectadoGrave(tiempo_inf_grave=grafo.graph['tiempo_inf_grave'])
                else:
                    estado_actual = EstadoInfectadoMild(tiempo_infeccion=grafo.graph['tiempo_inf_mild'])
            else:
                if random.random() < grafo.graph['prob_infec_grave']:
                    estado_actual = EstadoInfectadoGrave(tiempo_inf_grave=grafo.graph['tiempo_inf_grave'])
                else:
                    estado_actual = EstadoInfectadoMild(tiempo_infeccion=grafo.graph['tiempo_inf_mild'])
        return estado_actual
