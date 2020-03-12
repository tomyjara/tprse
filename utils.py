import random

import networkx as nx

from constantes import S, I, R


def obtenerPorcentajeDeNodosEnEstado(estado, grafo):
    nodos_totales = len(grafo)
    nodos_en_estado_estado = 0
    for nodo in grafo:
        if grafo.nodes[nodo]['estado'] == estado:
            nodos_en_estado_estado += 1
    return nodos_en_estado_estado * 100 / nodos_totales


def obtenerPorcentajeDeInfectados(grafo):
    return obtenerPorcentajeDeNodosEnEstado(I, grafo)


def obtenerPorcentajeDeSusceptibles(grafo):
    return obtenerPorcentajeDeNodosEnEstado(S, grafo)


def obtenerPorcentajeDeRecuperados(grafo):
    return obtenerPorcentajeDeNodosEnEstado(R, grafo)


def mostrarGrafo(G):
    G.graph['colores'] = [colorEstado(G.nodes[n]['estado']) for n in G.nodes]
    nx.draw_kamada_kawai(G, node_color=G.graph['colores'], with_labels=True)


def seContagiaDada(una_probabilidad):
    return random.random() < una_probabilidad


def calcularProbabilidadDeContagio(grafo, nodo):
    if len(list(grafo.neighbors(nodo))) == 0:
        return 0
    else:
        return len([vecino for vecino in grafo.neighbors(nodo) if grafo.nodes[vecino]['estado'] == I]) / len(
            list(grafo.neighbors(nodo)))


def mostrarEstadoInicial(modelo, cantidadDeIteraciones):
    print("\n", "CONFIGURACION INICIAL:")
    print(' - Nodos totales: ', len(modelo))
    print(' - Tipo de grafo: ', modelo.graph['tipo'])
    print(' - Cantidad de iteraciones: ', cantidadDeIteraciones)
    print(' - Porcentaje de nodos infectados: ', obtenerPorcentajeDeInfectados(modelo))
    print(' - Porcentaje de nodos susceptibles: ', obtenerPorcentajeDeSusceptibles(modelo))
    print(' - Porcentaje de nodos recuperados: ', obtenerPorcentajeDeRecuperados(modelo), "\n")


def mostrarEstadoFinal(modelo):
    print("\n", "\n", "ESTADO FINAL:")
    print(' - Porcentaje de nodos infectados: ', obtenerPorcentajeDeInfectados(modelo))
    print(' - Porcentaje de nodos susceptibles: ', obtenerPorcentajeDeSusceptibles(modelo))
    print(' - Porcentaje de nodos recuperados: ', obtenerPorcentajeDeRecuperados(modelo))


def generarGrafoDadoUnTipo(tipoDeGrafo, cantidadDeNodos):
    if tipoDeGrafo == "scale":
        grafo = nx.scale_free_graph(cantidadDeNodos)
    elif tipoDeGrafo == "2d_grid":
        grafo = nx.grid_2d_graph(cantidadDeNodos, cantidadDeNodos)
    elif tipoDeGrafo == "small_world":
        grafo = nx.watts_strogatz_graph(cantidadDeNodos)
    elif tipoDeGrafo == "random":
        grafo = nx.random(cantidadDeNodos)
    else:
        raise Exception("Tipo de grafo invalido")

    return grafo


def colorEstado(estado):
    if estado == S:
        return 'blue'
    if estado == I:
        return 'red'
    if estado == R:
        return 'green'
