import random

from estados.estado_muerto import EstadoMuerto
from estados.estado_nodo import EstadoNodo
from estados.estado_recuperado import EstadoRecuperado


class EstadoInfectadoGrave(EstadoNodo):
    def __init__(self, tiempo_inf_grave):
        self.tiempo_infectado_grave = tiempo_inf_grave

    def muereDada(self, una_probabilidad, t_infeccion):
        return t_infeccion > 0 and (random.random() < una_probabilidad)

    def transicionar(self, nodo, grafo):
        self.tiempo_infectado_grave -= 1
        estado_actual = self

        if self.tiempo_infectado_grave == 0:
            estado_actual = EstadoRecuperado()

        if grafo.nodes[nodo]['riesgo']:
            if self.muereDada(grafo.graph['prob_de_deceso_riesgo'], self.tiempo_infectado_grave):
                estado_actual = EstadoMuerto()
        else:
            if self.muereDada(grafo.graph['prob_de_deceso'], self.tiempo_infectado_grave):
                estado_actual = EstadoMuerto()

        return estado_actual



