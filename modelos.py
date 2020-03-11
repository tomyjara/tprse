import random
import sys

from simulador_de_epidemias.constantes import S, I, R
from simulador_de_epidemias.utils import calcularProbabilidadDeContagio, seContagiaDada, colorEstado, \
    mostrarEstadoInicial, mostrarEstadoFinal, \
    generarGrafoDadoUnTipo


def iterar_SIS(G, ti):
    for n in G:
        if G.nodes[n]['estado'] == S:
            probabilidad_de_contagio = calcularProbabilidadDeContagio(G, n)
            if seContagiaDada(probabilidad_de_contagio):
                G.nodes[n]['estado'] = I
                G.nodes[n]['Ti'] = ti
        else:
            G.nodes[n]['Ti'] -= 1
            if G.nodes[n]['Ti'] == 0:
                G.nodes[n]['estado'] = S
    # mostrarGrafo(G)
    return G


def iterar_SIR(G, ti):
    for n in G:
        if G.nodes[n]['estado'] == S:
            probabilidad_de_contagio = calcularProbabilidadDeContagio(G, n)
            if seContagiaDada(probabilidad_de_contagio):
                G.nodes[n]['estado'] = I
                G.nodes[n]['Ti'] = ti
        else:
            if G.nodes[n]['estado'] == I:
                G.nodes[n]['Ti'] -= 1
                if G.nodes[n]['Ti'] == 0:
                    G.nodes[n]['estado'] = R
            else:
                pass
    # mostrarGrafo(G)
    return G


def iterar_SIRS(G, ti, ri):
    for n in G:
        if G.nodes[n]['estado'] == S:
            probabilidad_de_contagio = calcularProbabilidadDeContagio(G, n)
            if seContagiaDada(probabilidad_de_contagio):
                G.nodes[n]['estado'] = I
                G.nodes[n]['Ti'] = ti

        elif G.nodes[n]['estado'] == I:
            G.nodes[n]['Ti'] -= 1
            if G.nodes[n]['Ti'] == 0:
                G.nodes[n]['estado'] = R
                G.nodes[n]['Ri'] = ri
        else:
            G.nodes[n]['Ri'] -= 1
            if G.nodes[n]['Ri'] == 0:
                G.nodes[n]['estado'] = S
    # mostrarGrafo(G)

    return G


def crearModelo(tipoDeGrafo, cantidadDeNodos, probabilidadDeEstarInfectado, ti=0, ri=0):
    grafo = generarGrafoDadoUnTipo(tipoDeGrafo, cantidadDeNodos)

    for n in grafo.nodes:
        grafo.nodes[n]['estado'] = I if random.random() < probabilidadDeEstarInfectado else S
        grafo.nodes[n]['Ti'] = ti if grafo.nodes[n]['estado'] == I else 0
        grafo.nodes[n]['Ri'] = ri

    grafo.graph['colores'] = [colorEstado(grafo.nodes[n]['estado']) for n in grafo.nodes]
    grafo.graph['ti'] = ti
    grafo.graph['ri'] = ri
    grafo.graph['tipo'] = tipoDeGrafo

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


def correrModeloSIRS(modelo, cantidadDeIteraciones):
    print("\n", "Corriendo modelo SIRS")
    mostrarEstadoInicial(modelo, cantidadDeIteraciones)

    for i in range(1, cantidadDeIteraciones + 1):
        iterar_SIRS(modelo, modelo.graph['ti'], modelo.graph['ri'])

        sys.stdout.write("\r \x1b[1;32m Progreso %d%%" % (int(i * 100 / cantidadDeIteraciones)))
        sys.stdout.flush()
    sys.stdout.write("\x1b[0m")
    mostrarEstadoFinal(modelo)
