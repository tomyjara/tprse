import random
import sys

from constantes import S, I, R, PROBABILIDAD_DE_DECESO, M, T_INCUBACION, T_INFECCION_MILD, T_INFECCION_GRAVE, \
    PROBABILIDAD_DE_DECESO_R

from estados.estado_incubando import EstadoIncubando
from estados.estado_susceptible import EstadoSusceptible

from simulador import poblacion_de_riesgo
from utils import calcularProbabilidadDeContagio, seContagiaDada, colorEstado, \
    mostrarEstadoInicial, mostrarEstadoFinal, \
    generarGrafoDadoUnTipo, muereDada, obtenerEstadoBien


def iterar_SIS(G, ti):
    for n in G:
        if G.nodes[n]['estado'] == S:
            probabilidad_de_contagio = calcularProbabilidadDeContagio(G, n)
            if seContagiaDada(probabilidad_de_contagio):
                G.nodes[n]['estado'] = I
                G.nodes[n]['ti'] = ti
        else:
            G.nodes[n]['ti'] -= 1
            if G.nodes[n]['ti'] == 0:
                G.nodes[n]['estado'] = S
    # mostrarGrafo(G)
    return G


def iterar_SIR(G, ti):
    for n in G:
        if G.nodes[n]['estado'] == S:
            probabilidad_de_contagio = calcularProbabilidadDeContagio(G, n)
            if seContagiaDada(probabilidad_de_contagio):
                G.nodes[n]['estado'] = I
                G.nodes[n]['ti'] = ti
        else:
            if G.nodes[n]['estado'] == I:
                G.nodes[n]['ti'] -= 1
                if G.nodes[n]['ti'] == 0:
                    G.nodes[n]['estado'] = R
            else:
                pass
    # mostrarGrafo(G)
    return G


def iterar_SIRM(G, t_infeccion):
    for n in G:
        if G.nodes[n]['estado'] == S:
            probabilidad_de_contagio = calcularProbabilidadDeContagio(G, n)
            if seContagiaDada(probabilidad_de_contagio):
                G.nodes[n]['estado'] = I
                G.nodes[n]['ti'] = t_infeccion
                G.nodes[n]['t_inc'] = G.graph['t_inc']
        else:

            if G.nodes[n]['estado'] == I:
                G.nodes[n]['ti'] -= 1
                G.nodes[n]['t_inc'] -= 1
                probabilidad_de_morir = G.graph['prob_de_deceso']

                if muereDada(probabilidad_de_morir, G.nodes[n]['t_inc']):
                    G.nodes[n]['estado'] = M
                if G.nodes[n]['ti'] == 0:
                    G.nodes[n]['estado'] = R

            else:
                pass
        # mostrarGrafo(G)
    return G


def iterar_SIRM2(G):
    for n in G:
        G.nodes[n]['estado'] = G.nodes[n]['estado'].transicionar(n, G)
    return G


def iterar_SIRS(G, ti, ri):
    for n in G:
        if G.nodes[n]['estado'] == S:
            probabilidad_de_contagio = calcularProbabilidadDeContagio(G, n)
            if seContagiaDada(probabilidad_de_contagio):
                G.nodes[n]['estado'] = I
                G.nodes[n]['ti'] = ti

        elif G.nodes[n]['estado'] == I:
            G.nodes[n]['ti'] -= 1
            if G.nodes[n]['ti'] == 0:
                G.nodes[n]['estado'] = R
                G.nodes[n]['ri'] = ri
        else:
            G.nodes[n]['ri'] -= 1
            if G.nodes[n]['ri'] == 0:
                G.nodes[n]['estado'] = S
    # mostrarGrafo(G)

    return G


def crearModelo(tipoDeGrafo, cantidadDeNodos, probabilidadDeEstarInfectado, ti=0, ri=0,
                probabilidadDeDeceso=PROBABILIDAD_DE_DECESO, tiempoDeIncubacion=T_INCUBACION):
    grafo = generarGrafoDadoUnTipo(tipoDeGrafo, cantidadDeNodos)

    for n in grafo.nodes:
        grafo.nodes[n]['estado'] = I if random.random() < probabilidadDeEstarInfectado else S
        grafo.nodes[n]['ti'] = ti if grafo.nodes[n]['estado'] == I else 0
        grafo.nodes[n]['t_inc'] = tiempoDeIncubacion if grafo.nodes[n]['estado'] == I else 0
        grafo.nodes[n]['ri'] = ri
        grafo.nodes[n]['esta_vivo'] = True

    grafo.graph['colores'] = [colorEstado(grafo.nodes[n]['estado']) for n in grafo.nodes]
    grafo.graph['ti'] = ti
    grafo.graph['ri'] = ri
    grafo.graph['tipo'] = tipoDeGrafo
    grafo.graph['t_inc'] = tiempoDeIncubacion
    grafo.graph['prob_de_deceso'] = probabilidadDeDeceso

    return grafo


def crearModelo2(tipo_de_grafo, cantidad_de_nodos, probabilidad_de_estar_infectado,
                 tiempo_infeccion_mild=T_INFECCION_MILD, tiempo_infecc_g=T_INFECCION_GRAVE, ri=0,
                 probabilidad_deceso=PROBABILIDAD_DE_DECESO, probabilidad_deceso_riesgo=PROBABILIDAD_DE_DECESO_R,
                 tiempo_incubacion=T_INCUBACION, probabilidad_p_riesgo=poblacion_de_riesgo):
    grafo = generarGrafoDadoUnTipo(tipo_de_grafo, cantidad_de_nodos)

    for n in grafo.nodes:
        grafo.nodes[n]['riesgo'] = random.random() < probabilidad_p_riesgo
        grafo.nodes[n]['estado'] = EstadoIncubando(
            tiempo_incubacion) if random.random() < probabilidad_de_estar_infectado else EstadoSusceptible()

    grafo.graph['colores'] = [colorEstado(grafo.nodes[n]['estado']) for n in grafo.nodes]
    grafo.graph['tiempo_incubacion'] = tiempo_incubacion
    grafo.graph['tiempo_infeccion_mild'] = tiempo_infeccion_mild
    grafo.graph['tiempo_infeccion_grave'] = tiempo_infecc_g
    grafo.graph['ri'] = ri
    grafo.graph['tipo'] = tipo_de_grafo
    grafo.graph['prob_de_deceso'] = probabilidad_deceso
    grafo.graph['prob_de_deceso_riesgo'] = probabilidad_deceso_riesgo

    return grafo


def correrModeloSIS(modelo, cantidadDeIteraciones):
    print("\n", "Corriendo modelo SIS")
    mostrarEstadoInicial(modelo, cantidadDeIteraciones)

    for i in range(1, cantidadDeIteraciones + 1):
        iterar_SIS(modelo, modelo.graph['ti'])

        sys.stdout.write("\r \x1b[1;32m Progreso %d%%" % (int(i * 100 / cantidadDeIteraciones)))
        sys.stdout.flush()

    sys.stdout.write("\x1b[0m")
    mostrarEstadoFinal(modelo)


def correrModeloSIR(modelo, cantidadDeIteraciones):
    print("\n", "Corriendo modelo SIR")
    mostrarEstadoInicial(modelo, cantidadDeIteraciones)

    for i in range(1, cantidadDeIteraciones + 1):
        iterar_SIR(modelo, modelo.graph['ti'])

        sys.stdout.write("\r \x1b[1;32m Progreso %d%%" % (int(i * 100 / cantidadDeIteraciones)))
        sys.stdout.flush()

    sys.stdout.write("\x1b[0m")
    mostrarEstadoFinal(modelo)


def correrModeloSIRM(modelo, cantidadDeIteraciones):
    resultados = open('resultados', 'w')
    print("\n", "Corriendo modelo SIRM")
    mostrarEstadoInicial(modelo, cantidadDeIteraciones)

    for i in range(1, cantidadDeIteraciones + 1):
        iterar_SIRM2(modelo)
        # infectados, susceptibles, recuperados, muertos = obtenerEstadoBien(modelo)
        # resultados.write(str(infectados) + ',' + str(susceptibles) + ',' + str(recuperados) + ',' + str(muertos))
        if i < cantidadDeIteraciones:
            resultados.write(',')

        sys.stdout.write("\r \x1b[1;32m Progreso %d%%" % (int(i * 100 / cantidadDeIteraciones)))
        sys.stdout.flush()

    sys.stdout.write("\x1b[0m")

    resultados.close()
    mostrarEstadoFinal(modelo)


def correrModeloSIRS(modelo, cantidadDeIteraciones):
    print("\n", "Corriendo modelo SIRS")
    mostrarEstadoInicial(modelo, cantidadDeIteraciones)

    for i in range(1, cantidadDeIteraciones + 1):
        iterar_SIRS(modelo, modelo.graph['ti'], modelo.graph['ri'])

        sys.stdout.write("\r \x1b[1;32m Progreso %d%%" % (int(i * 100 / cantidadDeIteraciones)))
        sys.stdout.flush()
    sys.stdout.write("\x1b[0m")
    mostrarEstadoFinal(modelo)
