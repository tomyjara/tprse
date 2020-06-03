import unittest

import networkx as nx

from constantes import ESTADO_INCUBANDO, SCALE_FREE, ESTADO_INFECTADO_GRAVE, ESTADO_INFECTADO_MILD, ESTADO_SUSCEPTIBLE
from estados.sism.estado_incubando_sism import EstadoIncubandoSISM
from estados.sism.estado_susceptible_sism import EstadoSusceptibleSISM
from modelos import crear_modelo_SISM


class TestEstadoIncubandoSism(unittest.TestCase):
    grafo = nx.scale_free_graph(10)
    modelo = crear_modelo_SISM(grafo, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                               probabilidad_de_estar_incubando=1, probabilidad_deceso=1, probabilidad_riesgo=0,
                               probabilidad_infecc_grave_riesgo=0, probabilidad_infecc_grave=1,
                               probabilidad_deceso_riesgo=0)

    nodo = 0

    def test_el_estado_se_instancia_correctamente(self):
        estado = EstadoSusceptibleSISM()

        self.assertEqual(estado.__class__.__name__, ESTADO_SUSCEPTIBLE)

    def test_al_transicionar_si_todos_los_vecinos_estan_incubando_el_nodo_se_contagia(self):
        self.grafo.nodes[self.nodo]['estado'] = EstadoSusceptibleSISM()
        estado = self.grafo.nodes[self.nodo]['estado']

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_INCUBANDO)

    def test_al_transicionar_si_ninguno_de_los_vecinos_esta_incubando_el_nodo_no_se_contagia(self):
        self.grafo.nodes[self.nodo]['estado'] = EstadoSusceptibleSISM()
        estado = self.grafo.nodes[self.nodo]['estado']

        for vecino in self.grafo.neighbors(self.nodo):
            self.grafo.nodes[vecino]['estado'] = EstadoSusceptibleSISM()

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_SUSCEPTIBLE)

