import unittest

import networkx as nx

from estados.estado_infectado_grave import EstadoInfectadoGrave
from estados.estado_infectado_mild import EstadoInfectadoMild
from estados.estado_muerto import EstadoMuerto
from estados.estado_recuperado import EstadoRecuperado
from modelos import crearModelo2, iterar_SIRM2


class TestSIRM(unittest.TestCase):

    cantidad_de_nodos = 1

    grid = nx.grid_graph(dim=[cantidad_de_nodos, cantidad_de_nodos])
    scale_free = nx.scale_free_graph(cantidad_de_nodos)


    def test_creoModeloSIRMCon1NodoDeRiesgoGRID(self):
        grafo = crearModelo2(self.grid, ri=0, tiempo_incubacion=0, tiempo_inf_mild=0, probabilidad_de_estar_incubando=0,
                             probabilidad_riesgo=1)

        self.assertSonNodosDeRiesgo(grafo)

    def test_creoModeloSIRMCon1NodoDeRiesgoScaleFree(self):
        grafo = crearModelo2(self.scale_free, ri=0, tiempo_incubacion=0, tiempo_inf_mild=0,
                             probabilidad_de_estar_incubando=0, probabilidad_riesgo=1)

        self.assertSonNodosDeRiesgo(grafo)

    # def test_creoModeloSIRMCon1NodoDeRiesgoSmallWorld(self):
    #     grafo = crearModelo2(SMALL_WORLD, self.cantidad_de_nodos, probabilidad_de_estar_incubando=0,
    #                          tiempo_inf_mild=0, ri=0, tiempo_incubacion=0, probabilidad_riesgo=1)
    #
    #     self.assertSonNodosDeRiesgo(grafo)

    def test_creoModeloSIRMConNingunNodoDeRiesgo(self):
        grafo = crearModelo2(self.grid, ri=0, tiempo_incubacion=0, tiempo_inf_mild=0, probabilidad_de_estar_incubando=0,
                             probabilidad_riesgo=0)
        self.assertNoSonNodosDeRiesgo(grafo)

    def test_transicionoIncubandoAInfectadoMildRiesgoYRecupera(self):
        grafo = crearModelo2(self.grid, ri=0, tiempo_incubacion=1, tiempo_inf_mild=1, probabilidad_de_estar_incubando=1,
                             probabilidad_riesgo=1, prob_infecc_grave_riesgo=0, prob_infecc_grave=0)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertEstadoInfeccionMild(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosRecuperados(grafo)

    def test_transicionoIncubandoAInfectadoMildNoRiesgoYRecupera(self):
        grafo = crearModelo2(self.grid, ri=0, tiempo_incubacion=1, tiempo_inf_mild=1, probabilidad_de_estar_incubando=1,
                             probabilidad_riesgo=0, prob_infecc_grave_riesgo=0, prob_infecc_grave=0)

        self.assertNoSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertEstadoInfeccionMild(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosRecuperados(grafo)

    def test_transicionoIncubandoAInfectadoGraveRiesgoYMuere(self):
        grafo = crearModelo2(self.grid, ri=0, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                             probabilidad_de_estar_incubando=1, probabilidad_riesgo=1, prob_infecc_grave_riesgo=1,
                             prob_infecc_grave=0, prob_deceso_riesgo=1)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_SIRM2(grafo)
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoMuerto)

    def test_transicionoIncubandoAInfectadoGraveRiesgoYRecupera(self):
        grafo = crearModelo2(self.grid, ri=0, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                             probabilidad_de_estar_incubando=1, probabilidad_riesgo=1, prob_infecc_grave_riesgo=1,
                             prob_infecc_grave=0, prob_deceso_riesgo=0)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_SIRM2(grafo)
        grafo = iterar_SIRM2(grafo)

        self.assertNodosRecuperados(grafo)

    def test_transicionoIncubandoAInfectadoGraveYMuere(self):
        grafo = crearModelo2(self.grid, ri=0, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                             probabilidad_de_estar_incubando=1, probabilidad_deceso=1, probabilidad_riesgo=0,
                             prob_infecc_grave_riesgo=0, prob_infecc_grave=1, prob_deceso_riesgo=0)

        self.assertNoSonNodosDeRiesgo(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_SIRM2(grafo)
        self.assertNodosMuertos(grafo)

    def test_transicionoIncubandoAInfectadoGraveYRecupera(self):
        grafo = crearModelo2(self.grid, ri=0, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                             probabilidad_de_estar_incubando=1, probabilidad_riesgo=0, prob_infecc_grave_riesgo=1,
                             prob_infecc_grave=1, prob_deceso_riesgo=0)

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
