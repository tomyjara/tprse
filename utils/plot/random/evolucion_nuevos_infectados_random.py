import pandas as pd
import matplotlib.pylab as plt

rn001_2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/random/random_0.01_2')
rn0001_2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/random/random_0.001_2')
rn00001_2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/random/random_0.0001_2')


def evolucion_nuevos_infectados(dataframe):
    infectados_por_iteracion = list(dataframe['infectados_totales'])
    nuevos_infectados_por_dia = []

    for i in range(1, len(infectados_por_iteracion)):
        nuevos_infectados = infectados_por_iteracion[i] - infectados_por_iteracion[i - 1]
        nuevos_infectados_por_dia.append(nuevos_infectados)

    return nuevos_infectados_por_dia

df1 = pd.DataFrame({
    'infectados_totales': rn001_2['infectados_totales'],
    'iteracion': rn001_2.index,
    'inf_totales': (rn001_2['i_grave'] + rn001_2['i_mild'] + rn001_2['incubando']),
    'muertos': rn001_2['muertos'],
    'inf_graves': rn001_2['i_grave'] * 5
})

df2 = pd.DataFrame({
    'infectados_totales': rn0001_2['infectados_totales'],

    'iteracion': rn0001_2.index,
    'inf_totales': (rn0001_2['i_grave'] + rn0001_2['i_mild'] + rn0001_2['incubando']),
    'muertos': rn0001_2['muertos'],
    'inf_graves': rn0001_2['i_grave'] * 5
})

df3 = pd.DataFrame({
    'infectados_totales': rn00001_2['infectados_totales'],

    'iteracion': rn00001_2.index,
    'inf_totales': (rn00001_2['i_grave'] + rn00001_2['i_mild'] + rn00001_2['incubando']),
    'muertos': rn00001_2['muertos'],
    'inf_graves': rn00001_2['i_grave'] * 5
})


dframes = [df1, df2, df3]

i = 0

evolucion_grid_1 = evolucion_nuevos_infectados(df1)
evolucion_grid_2 = evolucion_nuevos_infectados(df2)
evolucion_grid_3 = evolucion_nuevos_infectados(df3)

iteraciones = range(1, 300)
plt.grid(True)
plt.suptitle(u'Evolución de nuevos casos por día modelo Random grado 2', fontsize=14)  # Subtitulo
plt.legend(fancybox=True, loc=2)
plt.ylabel(u'Nuevos casos reportados')  # Titulo ordenada
plt.xlabel(u'Iteración')  # Titulo abcisa
plt.plot(iteraciones, evolucion_grid_1, c='cyan', label=u'1')
plt.plot(iteraciones, evolucion_grid_2, c='magenta', label=u'0.1')
plt.plot(iteraciones, evolucion_grid_3, c='crimson', label=u'0.05')

a = plt.scatter(0, df1.inf_totales[0], marker='o', color='cyan')
b = plt.scatter(0, df2.inf_totales[0], marker='o', color='magenta')
c = plt.scatter(0, df1.inf_totales[0], marker='o', color='crimson')

plt.legend((a, b, c),
           ('1 ', '0.1', '0.01'),
           scatterpoints=1,
           loc='upper right',
           fontsize=10,
           title='% Inicial')

plt.savefig('/Users/tomasj/PycharmProjects/tprse/resultados/imagenes/random/evolucion_infectados_random.png')
plt.close()
