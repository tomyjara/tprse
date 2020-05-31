import unittest

import networkx as nx

from constantes import ESTADO_INCUBANDO, SCALE_FREE, ESTADO_INFECTADO_GRAVE, ESTADO_INFECTADO_MILD
from estados.sism.estado_incubando_sism import EstadoIncubandoSISM
from modelos import crear_modelo_SISM


class TestEstadoIncubandoSism(unittest.TestCase):
    grafo = nx.scale_free_graph(100)
    modelo = crear_modelo_SISM(grafo, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                               probabilidad_de_estar_incubando=1, probabilidad_deceso=1, probabilidad_riesgo=0,
                               probabilidad_infecc_grave_riesgo=0, probabilidad_infecc_grave=1,
                               probabilidad_deceso_riesgo=0)

    nodo = 0

    def test_el_estado_se_instancia_correctamente(self):
        estado = EstadoIncubandoSISM(tiempo_incubacion=5)

        self.assertEqual(estado.tiempo_incubacion, 5)
        self.assertEqual(estado.__class__.__name__, ESTADO_INCUBANDO)

    def test_al_transicionar_el_tiempo_de_incubacion_se_reduce_una_unidad(self):
        estado = EstadoIncubandoSISM(tiempo_incubacion=5)
        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.tiempo_incubacion, 4)

    def test_al_transicionar_si_el_tiempo_de_incubacion_no_es_cero_el_estado_no_cambia(self):
        estado = EstadoIncubandoSISM(tiempo_incubacion=5)
        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_INCUBANDO)

    def test_si_no_es_de_riesgo_y_se_infecta_gravemente_el_nuevo_estado_es_infectado_grave(self):
        estado = EstadoIncubandoSISM(tiempo_incubacion=1)

        self.grafo.nodes[self.nodo]['riesgo'] = False

        self.grafo.graph['prob_infec_grave_riesgo'] = 0
        self.grafo.graph['prob_infec_grave'] = 1

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_INFECTADO_GRAVE)

    def test_si_es_de_riesgo_y_se_infecta_gravemente_el_nuevo_estado_es_infectado_grave(self):
        estado = EstadoIncubandoSISM(tiempo_incubacion=1)

        self.grafo.nodes[self.nodo]['riesgo'] = True

        self.grafo.graph['prob_infec_grave_riesgo'] = 1
        self.grafo.graph['prob_infec_grave'] = 0

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_INFECTADO_GRAVE)

    def test_si_no_es_de_riesgo_y_no_se_infecta_gravemente_el_nuevo_estado_es_infectado_mild(self):
        estado = EstadoIncubandoSISM(tiempo_incubacion=1)

        self.grafo.nodes[self.nodo]['riesgo'] = False

        self.grafo.graph['prob_infec_grave_riesgo'] = 1
        self.grafo.graph['prob_infec_grave'] = 0

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_INFECTADO_MILD)

    def test_si_es_de_riesgo_y_no_se_infecta_gravemente_el_nuevo_estado_es_infectado_mild(self):
        estado = EstadoIncubandoSISM(tiempo_incubacion=1)

        self.grafo.nodes[self.nodo]['riesgo'] = True

        self.grafo.graph['prob_infec_grave_riesgo'] = 0
        self.grafo.graph['prob_infec_grave'] = 1

        nuevo_estado = estado.transicionar(self.nodo, self.grafo)

        self.assertEqual(nuevo_estado.__class__.__name__, ESTADO_INFECTADO_MILD)
