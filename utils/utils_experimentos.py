import pandas as pd


def obtener_iteracion_con_mas_infectados(dataframe):
    infectados_por_iteracion = list(dataframe['infectados_totales'])

    max_inf = max(infectados_por_iteracion)
    pico = infectados_por_iteracion.index(max_inf)

    return pico, max_inf


def evolucion_nuevos_infectados(dataframe):
    infectados_por_iteracion = list(dataframe['infectados_totales'])
    nuevos_infectados_por_dia = []

    for i in range(1, len(infectados_por_iteracion)):
        nuevos_infectados = infectados_por_iteracion[i] - infectados_por_iteracion[i - 1]
        nuevos_infectados_por_dia.append(nuevos_infectados)

    return nuevos_infectados_por_dia


def obtener_pico(dataframe):
    infectados_por_iteracion = list(dataframe['infectados_totales'])
    diff = 0
    iteracion_pico = 0

    for i in range(1, len(infectados_por_iteracion)):
        nuevos_infectados = infectados_por_iteracion[i] - infectados_por_iteracion[i - 1]
        if nuevos_infectados > diff:
            diff = nuevos_infectados
            iteracion_pico = i

    return iteracion_pico


grid_1 = pd.read_csv('../resultados/grid/grid_0.01')
grid_2 = pd.read_csv('../resultados/grid/grid_0.001')
grid_3 = pd.read_csv('../resultados/grid/grid_0.0005')
grid_4 = pd.read_csv('../resultados/grid/grid_0.0001')

tree_2_12 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/tree/balanced_tree_r2_h15_0.001')
tree_3_10 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/tree/balanced_tree_r3_h10_0.0001')
tree_9_5 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/tree/balanced_tree_r9_h5_0.0001')
tree_10_5 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/tree/balanced_tree_r10_h5_0.0001')

r_001_2 = pd.read_csv('../resultados/random/random_0.01_2')
r_001_3 = pd.read_csv('../resultados/random/random_0.01_3')
r_001_5 = pd.read_csv('../resultados/random/random_0.01_5')

r_0001_2 = pd.read_csv('../resultados/random/random_0.001_2')
r_0001_3 = pd.read_csv('../resultados/random/random_0.001_3')
r_0001_5 = pd.read_csv('../resultados/random/random_0.001_5')

r_00001_2 = pd.read_csv('../resultados/random/random_0.0001_2')
r_00001_3 = pd.read_csv('../resultados/random/random_0.0001_3')
r_00001_5 = pd.read_csv('../resultados/random/random_0.0001_5')

s0 = pd.read_csv('../resultados/scale_free/vacunados_101')
s1 = pd.read_csv('../resultados/scale_free/vacunados_102')
s2 = pd.read_csv('../resultados/scale_free/vacunados_103')
s3 = pd.read_csv('../resultados/scale_free/scale_free_0.01')

sw21 = pd.read_csv('../resultados/small_world/sw_k2_p0.1_0.001')
sw23 = pd.read_csv('../resultados/small_world/sw_k2_p0.3_0.001')
sw25 = pd.read_csv('../resultados/small_world/sw_k2_p0.5_0.001')
sw31 = pd.read_csv('../resultados/small_world/sw_k3_p0.1_0.001')
sw33 = pd.read_csv('../resultados/small_world/sw_k3_p0.3_0.001')
sw35 = pd.read_csv('../resultados/small_world/sw_k3_p0.5_0.001')
sw41 = pd.read_csv('../resultados/small_world/sw_k4_p0.1_0.001')
sw43 = pd.read_csv('../resultados/small_world/sw_k4_p0.3_0.001')
sw45 = pd.read_csv('../resultados/small_world/sw_k4_p0.5_0.001')





sf = pd.read_csv('../resultados/scale_free/scale_free_0.5')

print('| Modelo |', '| Iteracion max acumulado |', '| Nodos Infectados |', '| Pico |')

print('Grid-0.01        ', obtener_iteracion_con_mas_infectados(grid_1)[0], '                       ',
      obtener_iteracion_con_mas_infectados(grid_1)[1],
      '         ', obtener_pico(grid_1))
print('Grid-0.001       ', obtener_iteracion_con_mas_infectados(grid_2)[0], '                       ',
      obtener_iteracion_con_mas_infectados(grid_2)[1],
      '        ', obtener_pico(grid_2))
print('Grid-0.0005      ', obtener_iteracion_con_mas_infectados(grid_3)[0], '                     ',
      obtener_iteracion_con_mas_infectados(grid_3)[1],
      '        ', obtener_pico(grid_3))
print('Grid-0.0001      ', obtener_iteracion_con_mas_infectados(grid_4)[0], '                     ',
      obtener_iteracion_con_mas_infectados(grid_4)[1],
      '         ', obtener_pico(grid_4))

print('Tree R2 H15      ', obtener_iteracion_con_mas_infectados(tree_2_12)[0], '                     ',
      obtener_iteracion_con_mas_infectados(tree_2_12)[1],
      '         ', obtener_pico(tree_2_12))
print('Tree R3 H10      ', obtener_iteracion_con_mas_infectados(tree_3_10)[0], '                     ',
      obtener_iteracion_con_mas_infectados(tree_3_10)[1],
      '         ', obtener_pico(tree_3_10))
print('Tree R9 H5      ', obtener_iteracion_con_mas_infectados(tree_9_5)[0], '                     ',
      obtener_iteracion_con_mas_infectados(tree_9_5)[1],
      '         ', obtener_pico(tree_9_5))
print('Tree R10 H5      ', obtener_iteracion_con_mas_infectados(tree_10_5)[0], '                     ',
      obtener_iteracion_con_mas_infectados(tree_10_5)[1],
      '         ', obtener_pico(tree_10_5))

print('r 0.01 2      ', obtener_iteracion_con_mas_infectados(r_001_2)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_001_2)[1],
      '         ', obtener_pico(r_001_2))
print('r 0.01 3      ', obtener_iteracion_con_mas_infectados(r_001_3)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_001_3)[1],
      '         ', obtener_pico(r_001_3))
print('r 0.01 5      ', obtener_iteracion_con_mas_infectados(r_001_5)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_001_5)[1],
      '         ', obtener_pico(r_001_5))

print('r 0.001 2      ', obtener_iteracion_con_mas_infectados(r_0001_2)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_0001_2)[1],
      '         ', obtener_pico(r_0001_2))
print('r 0.001 3      ', obtener_iteracion_con_mas_infectados(r_0001_3)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_0001_3)[1],
      '         ', obtener_pico(r_0001_3))
print('r 0.001 5      ', obtener_iteracion_con_mas_infectados(r_0001_5)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_0001_5)[1],
      '         ', obtener_pico(r_0001_5))

print('r 0.0001 2      ', obtener_iteracion_con_mas_infectados(r_00001_2)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_00001_2)[1],
      '         ', obtener_pico(r_00001_2))
print('r 0.0001 3      ', obtener_iteracion_con_mas_infectados(r_00001_3)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_00001_3)[1],
      '         ', obtener_pico(r_00001_3))
print('r 0.0001 5      ', obtener_iteracion_con_mas_infectados(r_00001_5)[0], '                     ',
      obtener_iteracion_con_mas_infectados(r_00001_5)[1],
      '         ', obtener_pico(r_00001_5))

print('s0      ', obtener_iteracion_con_mas_infectados(s0)[0], '                     ',
      obtener_iteracion_con_mas_infectados(s0)[1],
      '         ', obtener_pico(s0))
print('s1      ', obtener_iteracion_con_mas_infectados(s1)[0], '                     ',
      obtener_iteracion_con_mas_infectados(s1)[1],
      '         ', obtener_pico(s1))
print('s2      ', obtener_iteracion_con_mas_infectados(s2)[0], '                     ',
      obtener_iteracion_con_mas_infectados(s2)[1],
      '         ', obtener_pico(s2))
print('s3      ', obtener_iteracion_con_mas_infectados(s3)[0], '                     ',
      obtener_iteracion_con_mas_infectados(s3)[1],
      '         ', obtener_pico(s3))

print('s21      ', obtener_iteracion_con_mas_infectados(sw21)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw21)[1],
      '         ', obtener_pico(sw21))
print('s23      ', obtener_iteracion_con_mas_infectados(sw23)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw23)[1],
      '         ', obtener_pico(sw23))
print('s25      ', obtener_iteracion_con_mas_infectados(sw25)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw25)[1],
      '         ', obtener_pico(sw25))


print('s31      ', obtener_iteracion_con_mas_infectados(sw31)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw31)[1],
      '         ', obtener_pico(sw31))
print('s33      ', obtener_iteracion_con_mas_infectados(sw33)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw33)[1],
      '         ', obtener_pico(sw33))
print('s35      ', obtener_iteracion_con_mas_infectados(sw35)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw35)[1],
      '         ', obtener_pico(sw35))

print('s41      ', obtener_iteracion_con_mas_infectados(sw41)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw41)[1],
      '         ', obtener_pico(sw41))
print('s43      ', obtener_iteracion_con_mas_infectados(sw43)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw43)[1],
      '         ', obtener_pico(sw43))
print('s45      ', obtener_iteracion_con_mas_infectados(sw45)[0], '                     ',
      obtener_iteracion_con_mas_infectados(sw45)[1],
      '         ', obtener_pico(sw45))