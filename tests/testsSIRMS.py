import unittest

import networkx as nx

from estados.estado_muerto import EstadoMuerto
from estados.sirms.estado_infectado_grave_sirms import EstadoInfectadoGraveSIRMS
from estados.sirms.estado_infectado_mild_sirms import EstadoInfectadoMildSIRMS
from estados.sirms.estado_recuperado_sirms import EstadoRecuperadoSIRMS
from estados.sirms.estado_susceptible_sirms import EstadoSusceptibleSIRMS
from modelos import crear_modelo_SIRMS, iterar_modelo


class TestSIRM(unittest.TestCase):
    cantidad_de_nodos = 1
    grid = nx.grid_graph(dim=[cantidad_de_nodos, cantidad_de_nodos])
    scale_free = nx.scale_free_graph(cantidad_de_nodos)

    def test_creoModeloSIRMSCon1NodoDeRiesgoGRID(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=0, tiempo_inf_mild=0, probabilidad_de_estar_incubando=0,
                                   probabilidad_riesgo=1)

        self.assertSonNodosDeRiesgo(grafo)

    def test_creoModeloSIRMCon1NodoDeRiesgoScaleFree(self):
        grafo = crear_modelo_SIRMS(self.scale_free, tiempo_incubacion=0, tiempo_inf_mild=0, tiempo_recuperacion=3,
                                   probabilidad_de_estar_incubando=0, probabilidad_riesgo=1)

        self.assertSonNodosDeRiesgo(grafo)

    def test_creoModeloSIRMConNingunNodoDeRiesgo(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=0, tiempo_inf_mild=0, tiempo_recuperacion=3,
                                   probabilidad_de_estar_incubando=0, probabilidad_riesgo=0)
        self.assertNoSonNodosDeRiesgo(grafo)

    def test_transicionoIncubandoAInfectadoMildRiesgoYRecupera(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=1, tiempo_inf_mild=1, tiempo_recuperacion=3,
                                   probabilidad_de_estar_incubando=1,
                                   probabilidad_riesgo=1, probabilidad_infecc_grave_riesgo=0,
                                   probabilidad_infecc_grave=0)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_modelo(grafo)
        self.assertEstadoInfeccionMild(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosRecuperados(grafo)

    def test_transicionoIncubandoAInfectadoMildRiesgoRecuperaYPasaASusceptible(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=1, tiempo_inf_mild=1, tiempo_recuperacion=1,
                                   probabilidad_de_estar_incubando=1,
                                   probabilidad_riesgo=1, probabilidad_infecc_grave_riesgo=0,
                                   probabilidad_infecc_grave=0)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_modelo(grafo)
        self.assertEstadoInfeccionMild(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosRecuperados(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosSusceptibles(grafo)

    def test_transicionoIncubandoAInfectadoMildNoRiesgoRecuperaYPasaASusceptible(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=1, tiempo_inf_mild=1, tiempo_recuperacion=1,
                                   probabilidad_de_estar_incubando=1,
                                   probabilidad_riesgo=0, probabilidad_infecc_grave_riesgo=0,
                                   probabilidad_infecc_grave=0)

        self.assertNoSonNodosDeRiesgo(grafo)

        grafo = iterar_modelo(grafo)
        self.assertEstadoInfeccionMild(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosRecuperados(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosSusceptibles(grafo)

    def test_transicionoIncubandoAInfectadoGraveRiesgoYMuere(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                                   tiempo_recuperacion=1, probabilidad_de_estar_incubando=1, probabilidad_riesgo=1,
                                   probabilidad_infecc_grave_riesgo=1,
                                   probabilidad_infecc_grave=0, probabilidad_deceso_riesgo=1)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosMuertos(grafo)

    def test_transicionoIncubandoAInfectadoGraveRiesgoRecuperaYPasaASusceptible(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                                   tiempo_recuperacion=1,
                                   probabilidad_de_estar_incubando=1, probabilidad_riesgo=1,
                                   probabilidad_infecc_grave_riesgo=1,
                                   probabilidad_infecc_grave=0, probabilidad_deceso_riesgo=0)

        self.assertSonNodosDeRiesgo(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_modelo(grafo)
        grafo = iterar_modelo(grafo)
        self.assertNodosRecuperados(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosSusceptibles(grafo)

    def test_transicionoIncubandoAInfectadoGraveYMuere(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                                   tiempo_recuperacion=1,
                                   probabilidad_de_estar_incubando=1, probabilidad_deceso=1, probabilidad_riesgo=0,
                                   probabilidad_infecc_grave_riesgo=0, probabilidad_infecc_grave=1,
                                   probabilidad_deceso_riesgo=0)

        self.assertNoSonNodosDeRiesgo(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_modelo(grafo)
        grafo = iterar_modelo(grafo)

        self.assertNodosMuertos(grafo)

    def test_transicionoIncubandoAInfectadoGraveRecuperaYPasaASusceptible(self):
        grafo = crear_modelo_SIRMS(self.grid, tiempo_incubacion=1, tiempo_inf_mild=0, tiempo_inf_grave=2,
                                   tiempo_recuperacion=1,
                                   probabilidad_de_estar_incubando=1, probabilidad_riesgo=0,
                                   probabilidad_infecc_grave_riesgo=1,
                                   probabilidad_infecc_grave=1, probabilidad_deceso_riesgo=0)

        self.assertNoSonNodosDeRiesgo(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosInfectadosGrave(grafo)

        grafo = iterar_modelo(grafo)
        grafo = iterar_modelo(grafo)
        self.assertNodosRecuperados(grafo)

        grafo = iterar_modelo(grafo)
        self.assertNodosSusceptibles(grafo)

    def assertNodosMuertos(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoMuerto)

    def assertEstadoInfeccionMild(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoInfectadoMildSIRMS)

    def assertNodosRecuperados(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoRecuperadoSIRMS)

    def assertNodosSusceptibles(self, grafo):
        nodos = [n for n in grafo]
        for n in nodos:
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoSusceptibleSIRMS)

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
            self.assertIsInstance(grafo.nodes[n]['estado'], EstadoInfectadoGraveSIRMS)