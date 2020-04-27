from random import random

from estados.estado_muerto import EstadoMuerto
from estados.estado_nodo import EstadoNodo
from estados.estado_recuperado import EstadoRecuperado


class EstadoInfeccionGrave(EstadoNodo):
    def __init__(self, tiempo_infeccion):
        self.tiempo_infeccion = tiempo_infeccion

    def muereDada(self, una_probabilidad, t_infeccion):
        return t_infeccion > 0 & random.random() < una_probabilidad

    def transicionar(self, nodo, grafo):
        self.tiempo_infeccion -= 1

        estado_actual = self

        if grafo.nodes[nodo]['riesgo']:
            probabilidad_de_deceso = grafo.graph['prob_de_deceso_riesgo']
        else:
            probabilidad_de_deceso = grafo.graph['prob_de_deceso']

        if self.muereDada(probabilidad_de_deceso, self.tiempo_infeccion):
            estado_actual = EstadoMuerto()
        else:
            if self.tiempo_infeccion == 0:
                estado_actual = EstadoRecuperado()

        return estado_actual
