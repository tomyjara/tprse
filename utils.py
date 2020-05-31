from constantes import ESTADO_INCUBANDO, ESTADO_INFECTADO_MILD, ESTADO_INFECTADO_GRAVE, ESTADO_SUSCEPTIBLE, \
    ESTADO_RECUPERADO, ESTADO_MUERTO


def obtener_porcentaje_de_nodos_en_estado(estado, grafo):
    nodos_totales = len(grafo)
    if nodos_totales == 0:
        raise Exception("La cantidad de nodos debe ser mayor a cero")
    nodos_en_estado_estado = 0
    for nodo in grafo:
        estadoNodo = type(grafo.nodes[nodo]['estado']).__name__
        if estadoNodo == estado:
            nodos_en_estado_estado += 1
    return nodos_en_estado_estado * 100 / nodos_totales


def obtener_porcentaje_de_infectados_mild(grafo):
    return obtener_porcentaje_de_nodos_en_estado(ESTADO_INFECTADO_MILD, grafo)


def obtener_porcentaje_de_infectados_grave(grafo):
    return obtener_porcentaje_de_nodos_en_estado(ESTADO_INFECTADO_GRAVE, grafo)


def obtener_porcentaje_de_susceptibles(grafo):
    return obtener_porcentaje_de_nodos_en_estado(ESTADO_INCUBANDO, grafo)


def obtener_porcentaje_de_recuperados(grafo):
    return obtener_porcentaje_de_nodos_en_estado(ESTADO_RECUPERADO, grafo)


def obtener_porcentaje_de_incubando(grafo):
    return obtener_porcentaje_de_nodos_en_estado(ESTADO_INCUBANDO, grafo)


def mostrar_estado_inicial(modelo, cantidadDeIteraciones):
    print("\n", "CONFIGURACION INICIAL:")
    print(' - Nodos totales: ', len(modelo))
    print(' - Tipo de grafo: ', modelo.graph['tipo'])
    print(' - Cantidad de iteraciones: ', cantidadDeIteraciones)

    estado = obtener_estado(modelo)

    print(' - Porcentaje de nodos susceptibles: ', round(estado[ESTADO_SUSCEPTIBLE], 2))
    print(' - Porcentaje de nodos incubando: ', round(estado[ESTADO_INCUBANDO], 2), "\n")


def mostrar_estado_final(modelo):
    print("\n", "\n", "ESTADO FINAL:")

    estado = obtener_estado(modelo)

    print(' - Porcentaje de nodos incubando: ', round(estado[ESTADO_INCUBANDO], 2))
    print(' - Porcentaje de nodos infectados mild: ', round(estado[ESTADO_INFECTADO_MILD], 2))
    print(' - Porcentaje de nodos infectados grave: ', round(estado[ESTADO_INFECTADO_GRAVE], 2))
    print(' - Porcentaje de nodos susceptibles: ', round(estado[ESTADO_SUSCEPTIBLE], 2))
    print(' - Porcentaje de nodos recuperados: ', round(estado[ESTADO_RECUPERADO], 2))
    print(' - Porcentaje de nodos muertos: ', round(estado[ESTADO_MUERTO], 2), "\n")


def obtener_estado(grafo):
    nodos_totales = len(grafo)
    cantidad_de_nodos_en_estado = {ESTADO_INCUBANDO: 0,
                                   ESTADO_INFECTADO_MILD: 0,
                                   ESTADO_INFECTADO_GRAVE: 0,
                                   ESTADO_SUSCEPTIBLE: 0,
                                   ESTADO_RECUPERADO: 0,
                                   ESTADO_MUERTO: 0}

    for nodo in grafo:
        estadoNodo = grafo.nodes[nodo]['estado'].__class__.__name__
        cantidad_de_nodos_en_estado[estadoNodo] += 1

    for key in cantidad_de_nodos_en_estado:
        cantidad_de_nodos_en_estado[key] = cantidad_de_nodos_en_estado[key] * 100 / nodos_totales

    return cantidad_de_nodos_en_estado
