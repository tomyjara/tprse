import copy
import random
import sys
import os

from constantes import PROB_DE_DECESO, T_INCUBACION, PROBABILIDAD_RIESGO, \
    PROB_INFEC_GRAVE_RIESGO, PROB_INFEC_GRAVE, T_INF_MILD, PROB_DE_DECESO_RIESGO, T_INF_GRAVE, \
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


def crear_modelo_SIRM(un_grafo,
                      tiempo_incubacion=T_INCUBACION,
                      tiempo_inf_mild=T_INF_MILD,
                      tiempo_inf_grave=T_INF_GRAVE,
                      probabilidad_de_estar_incubando=0,
                      probabilidad_deceso=PROB_DE_DECESO,
                      probabilidad_riesgo=PROBABILIDAD_RIESGO,
                      probabilidad_infecc_grave_riesgo=PROB_INFEC_GRAVE_RIESGO,
                      probabilidad_infecc_grave=PROB_INFEC_GRAVE,
                      probabilidad_deceso_riesgo=PROB_DE_DECESO_RIESGO):
    for n in un_grafo.nodes:
        un_grafo.nodes[n]['estado'] = EstadoIncubandoSIRM(
            tiempo_incubacion) if random.random() < probabilidad_de_estar_incubando else EstadoSusceptibleSIRM()

        un_grafo.nodes[n]['riesgo'] = random.random() < probabilidad_riesgo

    un_grafo.graph['tiempo_inf_mild'] = tiempo_inf_mild
    un_grafo.graph['tiempo_inf_grave'] = tiempo_inf_grave
    un_grafo.graph['tiempo_incubacion'] = tiempo_incubacion
    un_grafo.graph['prob_de_deceso'] = probabilidad_deceso
    un_grafo.graph['prob_de_deceso_riesgo'] = probabilidad_deceso_riesgo
    un_grafo.graph['prob_infec_grave_riesgo'] = probabilidad_infecc_grave_riesgo
    un_grafo.graph['prob_infec_grave'] = probabilidad_infecc_grave

    return un_grafo


def crear_modelo_SIRMS(un_grafo,
                       tiempo_incubacion=T_INCUBACION,
                       tiempo_inf_mild=T_INF_MILD,
                       tiempo_inf_grave=T_INF_GRAVE,
                       tiempo_recuperacion=T_RECUPERACION,
                       probabilidad_de_estar_incubando=0,
                       probabilidad_deceso=PROB_DE_DECESO,
                       probabilidad_riesgo=PROBABILIDAD_RIESGO,
                       probabilidad_infecc_grave_riesgo=PROB_INFEC_GRAVE_RIESGO,
                       probabilidad_infecc_grave=PROB_INFEC_GRAVE,
                       probabilidad_deceso_riesgo=PROB_DE_DECESO_RIESGO):
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


def crear_modelo_SISM(un_grafo,
                      tiempo_incubacion=T_INCUBACION,
                      tiempo_inf_mild=T_INF_MILD,
                      tiempo_inf_grave=T_INF_GRAVE,
                      probabilidad_de_estar_incubando=0,
                      probabilidad_deceso=PROB_DE_DECESO,
                      probabilidad_riesgo=PROBABILIDAD_RIESGO,
                      probabilidad_infecc_grave_riesgo=PROB_INFEC_GRAVE_RIESGO,
                      probabilidad_infecc_grave=PROB_INFEC_GRAVE,
                      probabilidad_deceso_riesgo=PROB_DE_DECESO_RIESGO):
    for n in un_grafo.nodes:
        un_grafo.nodes[n]['estado'] = EstadoIncubandoSISM(
            tiempo_incubacion) if random.random() < probabilidad_de_estar_incubando else EstadoSusceptibleSISM()

        un_grafo.nodes[n]['riesgo'] = random.random() < probabilidad_riesgo

    un_grafo.graph['tiempo_inf_mild'] = tiempo_inf_mild
    un_grafo.graph['tiempo_inf_grave'] = tiempo_inf_grave
    un_grafo.graph['tiempo_incubacion'] = tiempo_incubacion
    un_grafo.graph['prob_de_deceso'] = probabilidad_deceso
    un_grafo.graph['prob_de_deceso_riesgo'] = probabilidad_deceso_riesgo
    un_grafo.graph['prob_infec_grave_riesgo'] = probabilidad_infecc_grave_riesgo
    un_grafo.graph['prob_infec_grave'] = probabilidad_infecc_grave

    return un_grafo


def correr_modelo_SIRM(modelo, cantidad_de_iteraciones, repeticiones, nombre_archivo_salida):
    correr_modelo(modelo, 'SIRM', cantidad_de_iteraciones, repeticiones, nombre_archivo_salida)


def correr_modelo_SISM(modelo, cantidad_de_iteraciones, repeticiones, nombre_archivo_salida):
    correr_modelo(modelo, 'SISM', cantidad_de_iteraciones, repeticiones, nombre_archivo_salida)


def correr_modelo_SIRMS(modelo, cantidad_de_iteraciones, repeticiones, nombre_archivo_salida):
    correr_modelo(modelo, 'SIRMS', cantidad_de_iteraciones, repeticiones, nombre_archivo_salida)


def correr_modelo(modelo, nombre_del_modelo, cantidad_de_iteraciones, repeticiones, nombre_archivo_salida):
    resultados = open(nombre_archivo_salida, 'w')

    resultados.write('incubando' + ',' + 'i_mild' + ',' + 'i_grave' + ',' + 'susceptibles' + ',' + 'recuperados' +
                     ',' + 'muertos' + '\n')

    print("\n", "Corriendo modelo " + nombre_del_modelo)

    resultados_memoria = [[0, 0, 0, 0, 0, 0] for i in range(cantidad_de_iteraciones)]

    for j in range(repeticiones):
        modelo_actual = copy.deepcopy(modelo)
        mostrar_estado_inicial(modelo_actual, cantidad_de_iteraciones)

        for i in range(cantidad_de_iteraciones):
            nodos_en_estado = obtener_estado(modelo_actual)

            incubando = nodos_en_estado[ESTADO_INCUBANDO]
            mild = nodos_en_estado[ESTADO_INFECTADO_MILD]
            grave = nodos_en_estado[ESTADO_INFECTADO_GRAVE]
            susceptibles = nodos_en_estado[ESTADO_SUSCEPTIBLE]
            recuperados = nodos_en_estado[ESTADO_RECUPERADO]
            muertos = nodos_en_estado[ESTADO_MUERTO]

            resultado_i_esima_iteracion = [incubando, mild, grave, susceptibles, recuperados, muertos]

            for k in range(6):
                resultados_memoria[i][k] += resultado_i_esima_iteracion[k]

            '''resultados.write(
                str(incubando) + ',' + str(mild) + ',' + str(grave) + ',' + str(susceptibles) + ',' +
                str(recuperados) + ',' + str(muertos))

            if not ((i == cantidad_de_iteraciones - 1) and (j == repeticiones - 1)):
                resultados.write('\n')'''

            iterar_modelo(modelo_actual)

            sys.stdout.write("\r \x1b[1;32m Progreso %d%%" % (int(i * 100 / cantidad_de_iteraciones)))
            sys.stdout.flush()

        sys.stdout.write("\x1b[0m")
        mostrar_estado_final(modelo_actual)

    for i in range(cantidad_de_iteraciones):
        for j in range(6):
            resultados_memoria[i][j] = round(resultados_memoria[i][j] / repeticiones, 2)

    for i in range(len(resultados_memoria)):
        resultados.write(
            str(resultados_memoria[i][0]) + ',' + str(resultados_memoria[i][1]) + ',' + str(
                resultados_memoria[i][2]) + ',' + str(resultados_memoria[i][3]) + ',' +
            str(resultados_memoria[i][4]) + ',' + str(resultados_memoria[i][5]))

        if i != (len(resultados_memoria) - 1):
            resultados.write('\n')

    resultados.close()
