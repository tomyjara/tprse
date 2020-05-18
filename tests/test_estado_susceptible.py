import unittest

from estados.estado_susceptible import EstadoSusceptible
from modelos import crear_modelo_SIRM


class TestEstadoSusceptible(unittest.TestCase):
    grafo = crear_modelo_SIRM(SCALE_FREE, 10, 0.5, tiempo_infeccion=14,
                              probabilidad_deceso=0.034, tiempo_incubacion=7)

    nodo = grafo.nodes[0]

    def test_estado_susceptible_se_instancia_correctamente(self):
        tiempo_infeccion = 14
        tiempo_incubacion = 5

        estado_infectado = EstadoSusceptible(tiempo_incubacion=tiempo_incubacion, tiempo_infeccion=tiempo_infeccion)

        self.assertEqual(estado_infectado.tiempo_infeccion, tiempo_infeccion)
        self.assertEqual(estado_infectado.tiempo_incubacion, tiempo_incubacion)