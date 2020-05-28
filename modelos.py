import random
import sys

from constantes import PROBABILIDAD_DE_DECESO, T_INCUBACION, PROBABILIDAD_RIESGO, \
    PROB_INFEC_GRAVE_RIESGO, PROB_INFEC_GRAVE, TIEMPO_INF_MILD, PROBABILIDAD_DE_DECESO_RIESGO, T_INF_GRAVE, \
    ESTADO_INCUBANDO, ESTADO_INFECTADO_MILD, ESTADO_SUSCEPTIBLE, ESTADO_INFECTADO_GRAVE, ESTADO_RECUPERADO, \
    ESTADO_MUERTO, T_RECUPERACION
from estados.sirm.estado_incubando_sirm import EstadoIncubandoSIRM
from estados.sirms.estado_incubando_sirms import EstadoIncubandoSIRMS
from estados.sirms.estado_susceptible_sirms import EstadoSusceptibleSIRMS
from estados.sism.estado_incubando_sism import EstadoIncubandoSISM
from estados.sism.estado_susceptible_sism import EstadoSusceptibleSISM
from estados.sirm.estado_susceptible_sirm import EstadoSusceptibleSIRM
from utils import mostrar_estado_inicial, mostrar_estado_final, obtener_estado


def iterar_modelo(G):
    for n in G:
        G.nodes[n]['estado'] = G.nodes[n]['estado'].transicionar(n, G)

    return G


def crear_modelo_SIRM(unGrafo,
                      tiempo_incubacion=T_INCUBACION,
                      tiempo_inf_mild=TIEMPO_INF_MILD,
                      tiempo_inf_grave=T_INF_GRAVE,
                      probabilidad_de_estar_incubando=0,
                      probabilidad_deceso=PROBABILIDAD_DE_DECESO,
                      probabilidad_riesgo=PROBABILIDAD_RIESGO,
                      probabilidad_infecc_grave_riesgo=PROB_INFEC_GRAVE_RIESGO,
                      probabilidad_infecc_grave=PROB_INFEC_GRAVE,
                      probabilidad_deceso_riesgo=PROBABILIDAD_DE_DECESO_RIESGO):
    for n in unGrafo.nodes:
        unGrafo.nodes[n]['estado'] = EstadoIncubandoSIRM(
            tiempo_incubacion) if random.random() < probabilidad_de_estar_incubando else EstadoSusceptibleSIRM()

        unGrafo.nodes[n]['riesgo'] = random.random() < probabilidad_riesgo

    unGrafo.graph['tiempo_inf_mild'] = tiempo_inf_mild
    unGrafo.graph['tiempo_inf_grave'] = tiempo_inf_grave
    unGrafo.graph['tiempo_incubacion'] = tiempo_incubacion
    unGrafo.graph['prob_de_deceso'] = probabilidad_deceso
    unGrafo.graph['prob_de_deceso_riesgo'] = probabilidad_deceso_riesgo
    unGrafo.graph['prob_infec_grave_riesgo'] = probabilidad_infecc_grave_riesgo
    unGrafo.graph['prob_infec_grave'] = probabilidad_infecc_grave

    return unGrafo


def crear_modelo_SIRMS(un_grafo,
                       tiempo_incubacion=T_INCUBACION,
                       tiempo_inf_mild=TIEMPO_INF_MILD,
                       tiempo_inf_grave=T_INF_GRAVE,
                       tiempo_recuperacion=T_RECUPERACION,
                       probabilidad_de_estar_incubando=0,
                       probabilidad_deceso=PROBABILIDAD_DE_DECESO,
                       probabilidad_riesgo=PROBABILIDAD_RIESGO,
                       probabilidad_infecc_grave_riesgo=PROB_INFEC_GRAVE_RIESGO,
                       probabilidad_infecc_grave=PROB_INFEC_GRAVE,
                       probabilidad_deceso_riesgo=PROBABILIDAD_DE_DECESO_RIESGO):
    for n in un_grafo.nodes:
        un_grafo.nodes[n]['estado'] = EstadoIncubandoSIRMS(
            tiempo_incubacion) if random.random() < probabilidad_de_estar_incubando else EstadoSusceptibleSIRMS()

        un_grafo.nodes[n]['riesgo'] = random.random() < probabilidad_riesgo

    un_grafo.graph['tiempo_inf_mild'] = tiempo_inf_mild
    un_grafo.graph['tiempo_inf_grave'] = tiempo_inf_grave
    un_grafo.graph['tiempo_incubacion'] = tiempo_incubacion
    un_grafo.graph['tiempo_recuperacion'] = tiempo_recuperacion
    un_grafo.graph['prob_de_deceso'] = probabilidad_deceso
    un_grafo.graph['prob_de_deceso_riesgo'] = probabilidad_deceso_riesgo
    un_grafo.graph['prob_infec_grave_riesgo'] = probabilidad_infecc_grave_riesgo
    un_grafo.graph['prob_infec_grave'] = probabilidad_infecc_grave

    return un_grafo


def crear_modelo_SISM(unGrafo,
                      tiempo_incubacion=T_INCUBACION,
                      tiempo_inf_mild=TIEMPO_INF_MILD,
                      tiempo_inf_grave=T_INF_GRAVE,
                      probabilidad_de_estar_incubando=0,
                      probabilidad_deceso=PROBABILIDAD_DE_DECESO,
                      probabilidad_riesgo=PROBABILIDAD_RIESGO,
                      probabilidad_infecc_grave_riesgo=PROB_INFEC_GRAVE_RIESGO,
                      probabilidad_infecc_grave=PROB_INFEC_GRAVE,
                      probabilidad_deceso_riesgo=PROBABILIDAD_DE_DECESO_RIESGO):
    for n in unGrafo.nodes:
        unGrafo.nodes[n]['estado'] = EstadoIncubandoSISM(
            tiempo_incubacion) if random.random() < probabilidad_de_estar_incubando else EstadoSusceptibleSISM()

        unGrafo.nodes[n]['riesgo'] = random.random() < probabilidad_riesgo

    unGrafo.graph['tiempo_inf_mild'] = tiempo_inf_mild
    unGrafo.graph['tiempo_inf_grave'] = tiempo_inf_grave
    unGrafo.graph['tiempo_incubacion'] = tiempo_incubacion
    unGrafo.graph['prob_de_deceso'] = probabilidad_deceso
    unGrafo.graph['prob_de_deceso_riesgo'] = probabilidad_deceso_riesgo
    unGrafo.graph['prob_infec_grave_riesgo'] = probabilidad_infecc_grave_riesgo
    unGrafo.graph['prob_infec_grave'] = probabilidad_infecc_grave

    return unGrafo


def correr_modelo_SIRM(modelo, cantidadDeIteraciones):
    correr_modelo(modelo, 'SIRM', cantidadDeIteraciones)

def correr_modelo_SISM(modelo, cantidadDeIteraciones):
    correr_modelo(modelo, 'SISM', cantidadDeIteraciones)


def correr_modelo_SIRMS(modelo, cantidad_de_iteraciones):
    correr_modelo(modelo, 'SIRMS', cantidad_de_iteraciones)


def correr_modelo(modelo, nombre_del_modelo, cantidadDeIteraciones):
    resultados = open('resultados', 'w')
    resultados.write('incubando' + ',' + 'i_mild' + ',' + 'i_grave' + ',' + 'susceptibles' + ',' + 'recuperados' +
                     ',' + 'muertos' + '\n')

    print("\n", "Corriendo modelo " + nombre_del_modelo)

    mostrar_estado_inicial(modelo, cantidadDeIteraciones)

    for i in range(1, cantidadDeIteraciones + 1):
        iterar_modelo(modelo)

        nodos_en_estado = obtener_estado(modelo)

        incubando = nodos_en_estado[ESTADO_INCUBANDO]
        mild = nodos_en_estado[ESTADO_INFECTADO_MILD]
        grave = nodos_en_estado[ESTADO_INFECTADO_GRAVE]
        susceptibles = nodos_en_estado[ESTADO_SUSCEPTIBLE]
        recuperados = nodos_en_estado[ESTADO_RECUPERADO]
        muertos = nodos_en_estado[ESTADO_MUERTO]

        resultados.write(str(incubando) + ',' + str(mild) + ',' + str(grave) + ',' + str(susceptibles) + ',' + str(
            recuperados) + ',' + str(muertos) + '\n')

        sys.stdout.write("\r \x1b[1;32m Progreso %d%%" % (int(i * 100 / cantidadDeIteraciones)))
        sys.stdout.flush()

    sys.stdout.write("\x1b[0m")

    resultados.close()
    mostrar_estado_final(modelo)
