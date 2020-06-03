import unittest

import networkx as nx

from constantes import ESTADO_SUSCEPTIBLE, ESTADO_INFECTADO_MILD
from estados.sism.estado_infectado_mild_sism import EstadoInfectadoMildSISM
from modelos import crear_modelo_SISM


class TestEstadoIncubandoSism(unittest.TestCase):
    grafo = nx.scale_free_graph(100)
    modelo = crear_modelo_SISM(grafo, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                               probabilidad_de_estar_incubando=1, probabilidad_deceso=1, probabilidad_riesgo=0,
                               probabilidad_infecc_grave_riesgo=0, probabilidad_infecc_grave=1,
                               probabilidad_deceso_riesgo=0)

    nodo = 0

    def test_el_estado_se_instancia_correctamente(self):
        estado = EstadoInfectadoMildSISM(tiempo_infeccion=5)

        self.assertEqual(estado.tiempo_infeccion, 5)
        self.assertEqual(estado.__class__.__name__, ESTADO_INFECTADO_MILD)

    def test_al_transicionar_el_tiempo_de_infeccion_se_reduce_una_unidad(self):
        estado = EstadoInfectadoMildSISM(tiempo_infeccion=5)

        self.grafo.nodes[self.nodo]['riesgo'] = False

        self.grafo.graph['prob_de_deceso'] = 0

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.tiempo_infeccion, 4)

    def test_al_transicionar_si_el_tiempo_de_infeccion_no_es_cero_el_estado_no_cambia(self):
        estado = EstadoInfectadoMildSISM(tiempo_infeccion=5)

        self.grafo.nodes[self.nodo]['riesgo'] = False

        self.grafo.graph['prob_de_deceso'] = 0

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_INFECTADO_MILD)

    def test_cuando_el_tiempo_de_infeccion_llega_a_cero_el_estado_pasa_a_susceptible(self):
        estado = EstadoInfectadoMildSISM(tiempo_infeccion=1)

        self.grafo.nodes[self.nodo]['riesgo'] = False

        self.grafo.graph['prob_de_deceso'] = 0

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_SUSCEPTIBLE)


