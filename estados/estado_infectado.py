import random
from abc import ABC

from estados.estado_nodo import EstadoNodo


class EstadoInfectado(EstadoNodo, ABC):

    @staticmethod
    def muere_dada(una_probabilidad):
        return random.random() < una_probabilidad
