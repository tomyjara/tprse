import random

import networkx as nx

from constantes import S, I, R, M


def obtenerPorcentajeDeNodosEnEstado(estado, grafo):
    nodos_totales = len(grafo)
    if nodos_totales == 0:
        raise Exception("La cantidad de nodos debe ser mayor a cero")
    nodos_en_estado_estado = 0
    for nodo in grafo:
        estadoNodo = type(grafo.nodes[nodo]['estado']).__name__
        if estadoNodo == estado:
            nodos_en_estado_estado += 1
    return nodos_en_estado_estado * 100 / nodos_totales


def obtenerPorcentajeDeInfectados(grafo):
    return obtenerPorcentajeDeNodosEnEstado('EstadoInfectado', grafo)


def obtenerPorcentajeDeSusceptibles(grafo):
    return obtenerPorcentajeDeNodosEnEstado('EstadoSusceptible', grafo)


def obtenerPorcentajeDeRecuperados(grafo):
    return obtenerPorcentajeDeNodosEnEstado('EstadoRecuperado', grafo)


def obtenerPorcentajeDeMuertos(grafo):
    return obtenerPorcentajeDeNodosEnEstado('EstadoMuerto', grafo)


def mostrarGrafo(G):
    G.graph['colores'] = [colorEstado(G.nodes[n]['estado']) for n in G.nodes]
    nx.draw_kamada_kawai(G, node_color=G.graph['colores'], with_labels=True)


def seContagiaDada(una_probabilidad):
    return random.random() < una_probabilidad


def muereDada(una_probabilidad, t_incubacion):
    if not t_incubacion > 0:
        return random.random() < una_probabilidad
    else:
        return False


def calcularProbabilidadDeContagio(grafo, nodo):
    if len(list(grafo.neighbors(nodo))) == 0:
        return 0
    else:
        return (len([vecino for vecino in grafo.neighbors(nodo) if grafo.nodes[vecino]['estado'] == I]) / len(
            list(grafo.neighbors(nodo))))


def mostrarEstadoInicial(modelo, cantidadDeIteraciones):
    print("\n", "CONFIGURACION INICIAL:")
    print(' - Nodos totales: ', len(modelo))
    print(' - Tipo de grafo: ', modelo.graph['tipo'])
    print(' - Cantidad de iteraciones: ', cantidadDeIteraciones)
    print(' - Porcentaje de nodos infectados: ', obtenerPorcentajeDeInfectados(modelo))
    print(' - Porcentaje de nodos susceptibles: ', obtenerPorcentajeDeSusceptibles(modelo))
    print(' - Porcentaje de nodos recuperados: ', obtenerPorcentajeDeRecuperados(modelo))
    print(' - Porcentaje de nodos muertos: ', obtenerPorcentajeDeMuertos(modelo), "\n")


def mostrarEstadoInicial2(modelo, cantidadDeIteraciones):
    print("\n", "CONFIGURACION INICIAL:")
    print(' - Nodos totales: ', len(modelo))
    print(' - Tipo de grafo: ', modelo.graph['tipo'])
    print(' - Cantidad de iteraciones: ', cantidadDeIteraciones)
    print(' - Porcentaje de nodos infectados: ', obtenerPorcentajeDeInfectados(modelo))
    print(' - Porcentaje de nodos susceptibles: ', obtenerPorcentajeDeSusceptibles(modelo))
    print(' - Porcentaje de nodos recuperados: ', obtenerPorcentajeDeRecuperados(modelo))
    print(' - Porcentaje de nodos muertos: ', obtenerPorcentajeDeMuertos(modelo), "\n")


def mostrarEstadoFinal(modelo):
    print("\n", "\n", "ESTADO FINAL:")
    print(' - Porcentaje de nodos infectados: ', obtenerPorcentajeDeInfectados(modelo))
    print(' - Porcentaje de nodos susceptibles: ', obtenerPorcentajeDeSusceptibles(modelo))
    print(' - Porcentaje de nodos recuperados: ', obtenerPorcentajeDeRecuperados(modelo))
    print(' - Porcentaje de nodos muertos: ', obtenerPorcentajeDeMuertos(modelo), "\n")


def obtenerEstado(modelo):
    return obtenerPorcentajeDeInfectados(modelo),\
           obtenerPorcentajeDeSusceptibles(modelo),\
           obtenerPorcentajeDeRecuperados(modelo),\
           obtenerPorcentajeDeMuertos(modelo)


'''Falta generar bien el random y el small world'''


def generarGrafoDadoUnTipo(tipoDeGrafo, cantidadDeNodos):
    if tipoDeGrafo == "scale":
        grafo = nx.scale_free_graph(cantidadDeNodos)
    elif tipoDeGrafo == "2d_grid":
        grafo = nx.grid_2d_graph(cantidadDeNodos, cantidadDeNodos)
    elif tipoDeGrafo == "small_world":
        grafo = nx.watts_strogatz_graph(cantidadDeNodos)
    elif tipoDeGrafo == "random":
        grafo = nx.gnm_random_graph(cantidadDeNodos, int(cantidadDeNodos / 2))
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
