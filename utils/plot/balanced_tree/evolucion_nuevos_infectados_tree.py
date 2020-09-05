import pandas as pd
import matplotlib.pylab as plt

tree_2_12 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/tree/balanced_tree_r2_h15_0.001')
tree_3_10 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/tree/balanced_tree_r3_h10_0.0001')
tree_9_5 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/tree/balanced_tree_r9_h5_0.0001')
tree_10_5 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/tree/balanced_tree_r10_h5_0.0001')


def evolucion_nuevos_infectados(dataframe):
    infectados_por_iteracion = list(dataframe['infectados_totales'])
    nuevos_infectados_por_dia = []

    for i in range(1, len(infectados_por_iteracion)):
        nuevos_infectados = infectados_por_iteracion[i] - infectados_por_iteracion[i - 1]
        nuevos_infectados_por_dia.append(nuevos_infectados)

    return nuevos_infectados_por_dia

df1 = pd.DataFrame({
    'infectados_totales': tree_2_12['infectados_totales'],
    'iteracion': tree_2_12.index,
    'inf_totales': (tree_2_12['i_grave'] + tree_2_12['i_mild'] + tree_2_12['incubando']),
    'muertos': tree_2_12['muertos'],
    'inf_graves': tree_2_12['i_grave'] * 5
})

df2 = pd.DataFrame({
    'infectados_totales': tree_3_10['infectados_totales'],

    'iteracion': tree_3_10.index,
    'inf_totales': (tree_3_10['i_grave'] + tree_3_10['i_mild'] + tree_3_10['incubando']),
    'muertos': tree_3_10['muertos'],
    'inf_graves': tree_3_10['i_grave'] * 5
})

df3 = pd.DataFrame({
    'infectados_totales': tree_9_5['infectados_totales'],

    'iteracion': tree_9_5.index,
    'inf_totales': (tree_9_5['i_grave'] + tree_9_5['i_mild'] + tree_9_5['incubando']),
    'muertos': tree_9_5['muertos'],
    'inf_graves': tree_9_5['i_grave'] * 5
})

df4 = pd.DataFrame({
    'infectados_totales': tree_10_5['infectados_totales'],
    'iteracion': tree_10_5.index,
    'inf_totales': (tree_10_5['i_grave'] + tree_10_5['i_mild'] + tree_10_5['incubando']),
    'muertos': tree_10_5['muertos'],
    'inf_graves': tree_10_5['i_grave'] * 5
})

dframes = [df1, df2, df3, df4]

i = 0

evolucion_grid_1 = evolucion_nuevos_infectados(df1)
evolucion_grid_2 = evolucion_nuevos_infectados(df2)
evolucion_grid_3 = evolucion_nuevos_infectados(df3)
evolucion_grid_4 = evolucion_nuevos_infectados(df4)

iteraciones = range(1, 151)
plt.grid(True)
plt.suptitle(u'Evolución de nuevos casos por día modelo Balanced Tree', fontsize=14)  # Subtitulo
plt.legend(fancybox=True, loc=2)
plt.ylabel(u'Nuevos casos reportados')  # Titulo ordenada
plt.xlabel(u'Iteración')  # Titulo abcisa
plt.ylim([0, 4000])
plt.plot(iteraciones, evolucion_grid_1[:150], c='cyan', label=u'1')
plt.plot(iteraciones, evolucion_grid_2[:150], c='magenta', label=u'0.1')
plt.plot(iteraciones, evolucion_grid_3[:150], c='crimson', label=u'0.05')
plt.plot(iteraciones, evolucion_grid_4[:150], c='navy', label=u'0.01')

a = plt.scatter(0, df1.inf_totales[0], marker='o', color='cyan')
b = plt.scatter(0, df2.inf_totales[0], marker='o', color='magenta')
d = plt.scatter(0, df4.inf_totales[0], marker='o', color='crimson')
c = plt.scatter(0, df3.inf_totales[0], marker='o', color='navy')

plt.legend((a, b, d, c),
           ('2 15', '3 10', '9 5', '10 5'),
           scatterpoints=1,
           loc='upper right',
           fontsize=10,
           title='       R H')

plt.savefig('/Users/tomasj/PycharmProjects/tprse/resultados/imagenes/balanced_tree/evolucion_infectados_tree.png')
plt.close()
