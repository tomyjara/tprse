import pandas as pd
import matplotlib.pylab as plt

scale1 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/scale_free/vacunados_101')
scale2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/scale_free/vacunados_102')
scale3 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/scale_free/vacunados_103')
scale4 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/scale_free/scale_free_0.01')


def evolucion_nuevos_infectados(dataframe):
    infectados_por_iteracion = list(dataframe['infectados_totales'])
    nuevos_infectados_por_dia = []

    for i in range(1, len(infectados_por_iteracion)):
        nuevos_infectados = infectados_por_iteracion[i] - infectados_por_iteracion[i - 1]
        nuevos_infectados_por_dia.append(nuevos_infectados)

    return nuevos_infectados_por_dia

df1 = pd.DataFrame({
    'infectados_totales': scale1['infectados_totales'],
    'iteracion': scale1.index,
    'inf_totales': (scale1['i_grave'] + scale1['i_mild'] + scale1['incubando']),
    'muertos': scale1['muertos'],
    'inf_graves': scale1['i_grave'] * 5
})

df2 = pd.DataFrame({
    'infectados_totales': scale2['infectados_totales'],

    'iteracion': scale2.index,
    'inf_totales': (scale2['i_grave'] + scale2['i_mild'] + scale2['incubando']),
    'muertos': scale2['muertos'],
    'inf_graves': scale2['i_grave'] * 5
})

df3 = pd.DataFrame({
    'infectados_totales': scale3['infectados_totales'],

    'iteracion': scale3.index,
    'inf_totales': (scale3['i_grave'] + scale3['i_mild'] + scale3['incubando']),
    'muertos': scale3['muertos'],
    'inf_graves': scale3['i_grave'] * 5
})

df4 = pd.DataFrame({
    'infectados_totales': scale4['infectados_totales'],

    'iteracion': scale4.index,
    'inf_totales': (scale4['i_grave'] + scale4['i_mild'] + scale4['incubando']),
    'muertos': scale4['muertos'],
    'inf_graves': scale4['i_grave'] * 5
})


dframes = [df1, df2, df3]

i = 0

evolucion_grid_1 = evolucion_nuevos_infectados(df1)
evolucion_grid_2 = evolucion_nuevos_infectados(df2)
evolucion_grid_3 = evolucion_nuevos_infectados(df3)
evolucion_grid_4 = evolucion_nuevos_infectados(df4)


iteraciones = range(1, 101)
plt.grid(True)
plt.suptitle(u'Evolución de casos modelo Scale Free 1% infectados', fontsize=14)  # Subtitulo
plt.legend(fancybox=True, loc=2)
plt.ylabel(u'Nuevos casos reportados')  # Titulo ordenada
plt.xlabel(u'Iteración')  # Titulo abcisa
plt.plot(iteraciones, evolucion_grid_1[:100], c='cyan', label=u'1')
plt.plot(iteraciones, evolucion_grid_2[:100], c='magenta', label=u'0.1')
plt.plot(iteraciones, evolucion_grid_3[:100], c='crimson', label=u'0.05')
plt.plot(iteraciones, evolucion_grid_4[:100], c='navy', label=u'0.05')


d = plt.scatter(0, df2.inf_totales[0], marker='o', color='navy')
a = plt.scatter(0, df1.inf_totales[0], marker='o', color='cyan')
b = plt.scatter(0, df2.inf_totales[0], marker='o', color='magenta')
c = plt.scatter(0, df1.inf_totales[0], marker='o', color='crimson')

plt.legend((d, a, b, c),
           ('0', '0.1', '0.2', '0.3'),
           scatterpoints=1,
           loc='upper right',
           fontsize=10,
           title='% Vacunados')

plt.savefig('/Users/tomasj/PycharmProjects/tprse/resultados/imagenes/scale_free/evolucion_infectados_scale.png')
plt.close()
