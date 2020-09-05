import pandas as pd
import matplotlib.pylab as plt


def evolucion_nuevos_infectados(dataframe):
    infectados_por_iteracion = list(dataframe['infectados_totales'])
    nuevos_infectados_por_dia = []

    for i in range(1, len(infectados_por_iteracion)):
        nuevos_infectados = infectados_por_iteracion[i] - infectados_por_iteracion[i - 1]
        nuevos_infectados_por_dia.append(nuevos_infectados)

    return nuevos_infectados_por_dia


grid_1 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/grid/grid_0.01')
grid_2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/grid/grid_0.001')
grid_3 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/grid/grid_0.0001')
grid_4 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/grid/grid_0.0005')

df1 = pd.DataFrame({
    'infectados_totales': grid_1['infectados_totales'],
    'iteracion': grid_1.index,
    'inf_totales': (grid_1['i_grave'] + grid_1['i_mild'] + grid_1['incubando']),
    'muertos': grid_1['muertos'],
    'inf_graves': grid_1['i_grave'] * 5
})

df2 = pd.DataFrame({
    'infectados_totales': grid_2['infectados_totales'],

    'iteracion': grid_2.index,
    'inf_totales': (grid_2['i_grave'] + grid_2['i_mild'] + grid_2['incubando']),
    'muertos': grid_2['muertos'],
    'inf_graves': grid_2['i_grave'] * 5
})

df3 = pd.DataFrame({
    'infectados_totales': grid_3['infectados_totales'],

    'iteracion': grid_3.index,
    'inf_totales': (grid_3['i_grave'] + grid_3['i_mild'] + grid_3['incubando']),
    'muertos': grid_3['muertos'],
    'inf_graves': grid_3['i_grave'] * 5
})

df4 = pd.DataFrame({
    'infectados_totales': grid_4['infectados_totales'],
    'iteracion': grid_4.index,
    'inf_totales': (grid_4['i_grave'] + grid_4['i_mild'] + grid_4['incubando']),
    'muertos': grid_4['muertos'],
    'inf_graves': grid_4['i_grave'] * 5
})

dframes = [df1, df2, df3, df4]

i = 0

evolucion_grid_1 = evolucion_nuevos_infectados(df1)
evolucion_grid_2 = evolucion_nuevos_infectados(df2)
evolucion_grid_3 = evolucion_nuevos_infectados(df3)
evolucion_grid_4 = evolucion_nuevos_infectados(df4)

iteraciones = range(1, 201)
plt.grid(True)
plt.suptitle(u'Evolución de nuevos casos por día modelo Grid', fontsize=14)  # Subtitulo
plt.legend(fancybox=True, loc=2)
plt.ylabel(u'Nuevos casos reportados')  # Titulo ordenada
plt.xlabel(u'Iteración')  # Titulo abcisa
plt.ylim([0, 4500])
plt.plot(iteraciones, evolucion_grid_1[:200], c='cyan', label=u'1')
plt.plot(iteraciones, evolucion_grid_2[:200], c='magenta', label=u'0.1')
plt.plot(iteraciones, evolucion_grid_3[:200], c='navy', label=u'0.05')
plt.plot(iteraciones, evolucion_grid_4[:200], c='crimson', label=u'0.01')

a = plt.scatter(0, df1.inf_totales[0], marker='o', color='cyan')
b = plt.scatter(0, df2.inf_totales[0], marker='o', color='magenta')
d = plt.scatter(0, df4.inf_totales[0], marker='o', color='crimson')
c = plt.scatter(0, df3.inf_totales[0], marker='o', color='navy')

plt.legend((a, b, d, c),
           ('1', '0.1', '0.05', '0.01'),
           scatterpoints=1,
           loc='upper right',
           fontsize=10,
           title='% Inicial')

plt.savefig('/Users/tomasj/PycharmProjects/tprse/resultados/imagenes/grid/evolucion_infectados_grid.png')
plt.close()
