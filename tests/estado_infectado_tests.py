import unittest

from constantes import SCALE_FREE
from estados.estado_infectado import EstadoInfectado
from modelos import crear_modelo_SIRM


class TestEstadoInfectado(unittest.TestCase):
    grafo = crear_modelo_SIRM(SCALE_FREE, 10, 0.5, tiempo_infeccion=14,
                              probabilidad_deceso=0.034, tiempo_incubacion=7)

    nodo = grafo.nodes[0]

    def test_estado_infectado_se_instancia_correctamente(self):
        tiempo_infeccion = 14
        tiempo_incubacion = 5

        estado_infectado = EstadoInfectado(tiempo_incubacion=tiempo_incubacion, tiempo_infeccion=tiempo_infeccion)

        self.assertEqual(estado_infectado.tiempo_infeccion, tiempo_infeccion)
        self.assertEqual(estado_infectado.tiempo_incubacion, tiempo_incubacion)

    def test_el_nodo_no_puede_morir_si_el_tiempo_de_incubacion_es_mayor_a_cero(self):
        tiempo_incubacion = 5

        muere_dada_probabilidad_uno = EstadoInfectado.muere_dada(1, tiempo_incubacion)

        self.assertEqual(muere_dada_probabilidad_uno, False)

    def test_el_nodo_muere_si_la_probabilidad_es_uno_y_tiempo_incubacion_0(self):
        tiempo_incubacion = 0

        muere_dada_probabilidad_uno = EstadoInfectado.muere_dada(1, tiempo_incubacion)

        self.assertEqual(muere_dada_probabilidad_uno, True)

    def test_luego_de_transicionar_ambos_tiempos_valen_una_unidad_menos(self, nodo=nodo, grafo=grafo):
        tiempo_infeccion = 14
        tiempo_incubacion = 5

        estado_infectado = EstadoInfectado(tiempo_incubacion=tiempo_incubacion, tiempo_infeccion=tiempo_infeccion)
        nuevo_estado = estado_infectado.transicionar(nodo, grafo)

        self.assertEqual(nuevo_estado.tiempo_incubacion, tiempo_incubacion - 1)
        self.assertEqual(nuevo_estado.tiempo_infeccion, tiempo_infeccion - 1)

    def test_el_estado_no_transiciona_si_tiempo_de_incubacion_no_es_cero(self, nodo=nodo, grafo=grafo):
        tiempo_infeccion = 14
        tiempo_incubacion = 5

        estado_infectado = EstadoInfectado(tiempo_incubacion=tiempo_incubacion, tiempo_infeccion=tiempo_infeccion)
        nuevo_estado = estado_infectado.transicionar(nodo, grafo)

        self.assertEqual(type(nuevo_estado).__name__, "EstadoInfectado")

    def test_cuando_el_tiempo_de_incubacion_es_cero_y_no_muere_se_preserva_el_estado(self, nodo=nodo, grafo=grafo):
        grafo.graph['prob_de_deceso'] = 0

        tiempo_infeccion = 14
        tiempo_incubacion = 0

        estado_infectado = EstadoInfectado(tiempo_incubacion=tiempo_incubacion, tiempo_infeccion=tiempo_infeccion)
        nuevo_estado = estado_infectado.transicionar(nodo, grafo)

        self.assertEqual(type(nuevo_estado).__name__, "EstadoInfectado")

    def test_cuando_el_tiempo_de_incubacion_es_cero_y_muere_pasa_a_estado_muerto(self, nodo=nodo, grafo=grafo):
        grafo.graph['prob_de_deceso'] = 1

        tiempo_infeccion = 14
        tiempo_incubacion = 0

        estado_infectado = EstadoInfectado(tiempo_incubacion=tiempo_incubacion, tiempo_infeccion=tiempo_infeccion)
        nuevo_estado = estado_infectado.transicionar(nodo, grafo)

        self.assertEqual(type(nuevo_estado).__name__, "EstadoMuerto")

    def test_cuando_el_tiempo_de_incubacion_es_cero_y_no_muere_y_el_tiempo_de_infeccion_pasa_a_cero_pasa_a_estado_recuperado(self, nodo=nodo, grafo=grafo):
        grafo.graph['prob_de_deceso'] = 0

        tiempo_infeccion = 1
        tiempo_incubacion = 0

        estado_infectado = EstadoInfectado(tiempo_incubacion=tiempo_incubacion, tiempo_infeccion=tiempo_infeccion)
        nuevo_estado = estado_infectado.transicionar(nodo, grafo)

        self.assertEqual(type(nuevo_estado).__name__, "EstadoRecuperado")
