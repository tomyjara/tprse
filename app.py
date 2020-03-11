import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import random
import time

I = 'I'
S = 'S'
R = 'R'

def color_estado(estado):
    if estado == S:
         return 'blue'
    if estado == I:
         return 'red'
    if estado == R:
         return 'green'

G = nx.binomial_tree(5)
for n in G.nodes:
    G.nodes[n]['probabilidad'] = 0
    G.nodes[n]['estado'] = S if random.random() < 0.5 else I
    G.nodes[n]['Ti'] = 4 if G.nodes[n]['estado'] == I else 0
    G.nodes[n]['Ri'] = 0
G.graph['colores'] = [color_estado(G.nodes[n]['estado']) for n in G.nodes]
#nx.draw_circular(G, node_color=G.graph['colores'], with_labels=True)
plt.show()


def contagiarse(probabilidad):
    return random.random() < probabilidad


def calcularProbabilidad(grafo, nodo):
    return len([vecino for vecino in grafo.neighbors(nodo) if grafo.nodes[vecino]['estado'] == I]) / len(
        list(grafo.neighbors(nodo)))


def iterar_SIS(G, ti):
    for n in G:
        G.nodes[n]['probabilidad'] = calcularProbabilidad(G, n)
    for n in G:
        if G.nodes[n]['estado'] == S:
            if contagiarse(G.nodes[n]['probabilidad']):
                G.nodes[n]['estado'] = I
                G.nodes[n]['Ti'] = ti
        else:
            G.nodes[n]['Ti'] -= 1
            if G.nodes[n]['Ti'] == 0:
                G.nodes[n]['estado'] = S

    colores = ['red' if G.nodes[n]['estado'] == I else 'blue' for n in G.nodes]
    nx.draw(G, node_color=colores, with_labels=True)
    plt.show()
    return G

def iterar_SIR(G, ti):
    for n in G:
        G.nodes[n]['probabilidad'] = calcularProbabilidad(G, n)
    for n in G:
        if G.nodes[n]['estado'] == S:
            if contagiarse(G.nodes[n]['probabilidad']):
                G.nodes[n]['estado'] = I
                G.nodes[n]['Ti'] = ti
        else:
            if G.nodes[n]['estado'] == I:
                G.nodes[n]['Ti'] -= 1
                if G.nodes[n]['Ti'] == 0:
                    G.nodes[n]['estado'] = R
            else:
                pass

    G.graph['colores'] = [color_estado(G.nodes[n]['estado']) for n in G.nodes]
    return G


def iterar_SIRS(G, ti, ri):
    for n in G:
        G.nodes[n]['probabilidad'] = calcularProbabilidad(G, n)
    for n in G:
        if G.nodes[n]['estado'] == S:
            if contagiarse(G.nodes[n]['probabilidad']):
                G.nodes[n]['estado'] = I
                G.nodes[n]['Ti'] = ti
        else:
            if G.nodes[n]['estado'] == I:
                G.nodes[n]['Ti'] -= 1
                if G.nodes[n]['Ti'] == 0:
                    G.nodes[n]['estado'] = R
                    G.nodes[n]['Ri'] = ri
            else:
                G.nodes[n]['Ri'] -= 1
                if G.nodes[n]['Ri'] == 0:
                    G.nodes[n]['estado'] = S


    G.graph['colores'] = [color_estado(G.nodes[n]['estado']) for n in G.nodes]
    nx.draw_kamada_kawai(G, node_color=G.graph['colores'], with_labels=True)
    return G

# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()
plt.close()

# Animation funciton
def animate(i):
    iterar_SIRS(G, 4, 2)


nx.draw_kamada_kawai(G)
fig = plt.gcf()

# Animator call
anim = animation.FuncAnimation(fig, animate, frames=20, interval=20)

# Note: below is the part which makes it work on Colab
rc('animation', html='jshtml')
anim

