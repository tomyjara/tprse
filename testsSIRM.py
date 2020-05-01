import unittest

from constantes import GRID
from estados.estado_infectado_grave import EstadoInfectadoGrave
from estados.estado_infectado_mild import EstadoInfectadoMild
from estados.estado_muerto import EstadoMuerto
from estados.estado_recuperado import EstadoRecuperado
from modelos import crearModelo2, iterar_SIRM2


class TestSIRM(unittest.TestCase):
    tipo_de_grafo = GRID

    cantidad_de_nodos = 1

    def test_creoModeloSIRMCon1NodoDeRiesgo(self):
        grafo = crearModelo2(self.tipo_de_grafo, self.cantidad_de_nodos, probabilidad_de_estar_incubando=0,
                             tiempo_inf_mild=0, ri=0, tiempo_incubacion=0, probabilidad_riesgo=1)

        self.assertSonNodosDeRiesgo(grafo)

    def test_creoModeloSIRMConNingunNodoDeRiesgo(self):
        grafo = crearModelo2(self.tipo_de_grafo, self.cantidad_de_nodos, probabilidad_de_estar_incubando=0,
                             tiempo_inf_mild=0, ri=0, tiempo_incubacion=0, probabilidad_riesgo=0)
        self.assertNoSonNodosDeRiesgo(grafo)

    def test_transicionoIncubandoAInfectadoMildRiesgoYRecupera(self):
        grafo = crearModelo2(self.tipo_de_grafo, self.cantidad_de_nodos, probabilidad_de_estar_incubando=1,
                             tiempo_inf_mild=1, ri=0, tiempo_incubacion=1, probabilidad_riesgo=1,
                             prob_infecc_grave_riesgo=0, prob_infecc_grave=0)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertEstadoInfeccionMild(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosRecuperados(grafo)

    def test_transicionoIncubandoAInfectadoMildNoRiesgoYRecupera(self):
        grafo = crearModelo2(self.tipo_de_grafo, self.cantidad_de_nodos, probabilidad_de_estar_incubando=1,
                             tiempo_inf_mild=1, ri=0, tiempo_incubacion=1, probabilidad_riesgo=0,
                             prob_infecc_grave_riesgo=0, prob_infecc_grave=0)

        self.assertNoSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertEstadoInfeccionMild(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosRecuperados(grafo)

    def test_transicionoIncubandoAInfectadoGraveRiesgoYMuere(self):
        grafo = crearModelo2(self.tipo_de_grafo, self.cantidad_de_nodos, probabilidad_de_estar_incubando=1,
                             tiempo_inf_mild=0, prob_deceso_riesgo=1, tiempo_inf_grave=2, ri=0, tiempo_incubacion=1,
                             probabilidad_riesgo=1, prob_infecc_grave_riesgo=1, prob_infecc_grave=0)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_SIRM2(grafo)
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoMuerto)

    def test_transicionoIncubandoAInfectadoGraveRiesgoYRecupera(self):
        grafo = crearModelo2(self.tipo_de_grafo, self.cantidad_de_nodos, probabilidad_de_estar_incubando=1,
                             tiempo_inf_mild=0, prob_deceso_riesgo=0, tiempo_inf_grave=2, ri=0, tiempo_incubacion=1,
                             probabilidad_riesgo=1, prob_infecc_grave_riesgo=1, prob_infecc_grave=0)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_SIRM2(grafo)
        grafo = iterar_SIRM2(grafo)

        self.assertNodosRecuperados(grafo)

    def test_transicionoIncubandoAInfectadoGraveYMuere(self):
        grafo = crearModelo2(self.tipo_de_grafo, self.cantidad_de_nodos, probabilidad_de_estar_incubando=1,
                             tiempo_inf_mild=0, probabilidad_deceso=1, prob_deceso_riesgo=0, tiempo_inf_grave=2, ri=0,
                             tiempo_incubacion=1, probabilidad_riesgo=0, prob_infecc_grave_riesgo=0,
                             prob_infecc_grave=1)

        self.assertNoSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosMuertos(grafo)

    def test_transicionoIncubandoAInfectadoGraveYRecupera(self):
        grafo = crearModelo2(self.tipo_de_grafo, self.cantidad_de_nodos, probabilidad_de_estar_incubando=1,
                             tiempo_inf_mild=0, prob_deceso_riesgo=0, tiempo_inf_grave=2, ri=0, tiempo_incubacion=1,
                             probabilidad_riesgo=0, prob_infecc_grave_riesgo=1, prob_infecc_grave=1)

        self.assertNoSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_SIRM2(grafo)
        grafo = iterar_SIRM2(grafo)

        self.assertNodosRecuperados(grafo)

    def assertNodosMuertos(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoMuerto)

    def assertEstadoInfeccionMild(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoInfectadoMild)

    def assertNodosRecuperados(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoRecuperado)

    def assertSonNodosDeRiesgo(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertTrue(grafo.nodes[n]['riesgo'])

    def assertNoSonNodosDeRiesgo(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertFalse(grafo.nodes[n]['riesgo'])

    def assertNodosInfectadosGrave(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoInfectadoGrave)
