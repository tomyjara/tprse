from constantes import ESTADO_INFECTADO_GRAVE
from estados.estado_infectado import EstadoInfectado
from estados.estado_muerto import EstadoMuerto
from estados.sirm.estado_recuperado import EstadoRecuperado

'''Estado de infeccion grave, son personas con un alto riesgo de muerte. Al transicionar '''


class EstadoInfectadoGraveSIRM(EstadoInfectado):

    def __init__(self, tiempo_infeccion):
        self.__class__.__name__ = ESTADO_INFECTADO_GRAVE
        self.tiempo_infeccion = tiempo_infeccion

    def transicionar(self, nodo, grafo):
        self.tiempo_infeccion -= 1
        estado_actual = self

        if self.tiempo_infeccion == 0:
            estado_actual = EstadoRecuperado()

        if grafo.nodes[nodo]['riesgo']:
            if self.muere_dada(grafo.graph['prob_de_deceso_riesgo']):
                estado_actual = EstadoMuerto()
        else:
            if self.muere_dada(grafo.graph['prob_de_deceso']):
                estado_actual = EstadoMuerto()

        return estado_actual
