import unittest

from constantes import GRID, S, I
from modelos import crearModelo, iterar_SIS, iterar_SIRS, iterar_SIR


class TestModelos(unittest.TestCase):
    tipo_de_grafo = GRID

    probabilidad_de_infeccion = 0

    cantidad_de_nodos = 0

    ti = 0

    ri = 0

    def iterarModeloSIS(self, cantidad_de_itaraciones, modelo):
        for i in range(cantidad_de_itaraciones):
            iterar_SIS(modelo, self.ti)

    def iterarModeloSIR(self, cantidad_de_itaraciones, modelo):
        for i in range(cantidad_de_itaraciones):
            iterar_SIR(modelo, self.ti)

    def iterarModeloSIRS(self, cantidad_de_itaraciones, modelo):
        for i in range(cantidad_de_itaraciones):
            iterar_SIRS(modelo, self.ti, self.ri)

    def instanciarModelo(self):
        return crearModelo(self.tipo_de_grafo, self.cantidad_de_nodos, self.probabilidad_de_infeccion, self.ti, self.ri)

    def test_correr_SIS_sin_nodos_infectados_no_debe_alterar_el_estado_de_ninguno(self):

        self.cantidad_de_nodos = 4
        self.ti = 4
        cantidad_de_iteraciones = 4

        modelo = self.instanciarModelo()
        self.iterarModeloSIS(cantidad_de_iteraciones, modelo)

        for nodo in modelo.nodes:
            self.assertEqual(modelo.nodes[nodo]['estado'], S)

    def test_luego_de_2_iteraciones_de_SIS_con_ti_4_comenzando_con_todos_los_nodos_infectados_deben_seguir_todos_infectados(self):

        self.cantidad_de_nodos = 4
        self.ti = 4
        self.probabilidad_de_infeccion = 1

        cantidad_de_iteraciones = 2

        modelo = self.instanciarModelo()
        self.iterarModeloSIS(cantidad_de_iteraciones, modelo)

        for nodo in modelo.nodes:
            self.assertEqual(modelo.nodes[nodo]['estado'], I)

    def test_luego_de_4_iteraciones_de_SIS_con_ti_4_comenzando_con_todos_los_nodos_infectados_deben_terminar_todos_susceptibles(self):

        self.cantidad_de_nodos = 4
        self.ti = 4
        self.probabilidad_de_infeccion = 1

        cantidad_de_iteraciones = 4

        modelo = self.instanciarModelo()
        self.iterarModeloSIS(cantidad_de_iteraciones, modelo)

        for nodo in modelo.nodes:
            self.assertEqual(modelo.nodes[nodo]['estado'], S)

    def test_correr_SIR_sin_nodos_infectados_no_debe_alterar_el_estado_de_ninguno(self):

        self.cantidad_de_nodos = 4
        self.ti = 4
        cantidad_de_iteraciones = 4

        modelo = self.instanciarModelo()
        self.iterarModeloSIR(cantidad_de_iteraciones, modelo)

        for nodo in modelo.nodes:
            self.assertEqual(modelo.nodes[nodo]['estado'], S)

    def test_luego_de_2_iteraciones_de_SIR_con_ti_4_comenzando_con_todos_los_nodos_infectados_deben_seguir_todos_infectados(self):

        self.cantidad_de_nodos = 4
        self.ti = 4
        self.probabilidad_de_infeccion = 1

        cantidad_de_iteraciones = 2

        modelo = self.instanciarModelo()
        self.iterarModeloSIR(cantidad_de_iteraciones, modelo)

        for nodo in modelo.nodes:
            self.assertEqual(modelo.nodes[nodo]['estado'], I)
