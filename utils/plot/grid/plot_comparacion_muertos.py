import pandas as pd
import matplotlib.pylab as plt

grid_1 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/grid/grid_0.01')
grid_2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/grid/grid_0.001')
grid_3 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/grid/grid_0.0001')
grid_4 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/grid/grid_0.0005')


df1 = pd.DataFrame({
    'iteracion': grid_1.index,
    'inf_totales': (grid_1['i_grave'] + grid_1['i_mild'] + grid_1['incubando']),
    'muertos': grid_1['muertos'],
    'inf_graves': grid_1['i_grave'] * 5
})

df2 = pd.DataFrame({
    'iteracion': grid_2.index,
    'inf_totales': (grid_2['i_grave'] + grid_2['i_mild'] + grid_2['incubando']),
    'muertos': grid_2['muertos'],
    'inf_graves': grid_2['i_grave'] * 5
})

df3 = pd.DataFrame({
    'iteracion': grid_3.index,
    'inf_totales': (grid_3['i_grave'] + grid_3['i_mild'] + grid_3['incubando']),
    'muertos': grid_3['muertos'],
    'inf_graves': grid_3['i_grave'] * 5
})

df4 = pd.DataFrame({
    'iteracion': grid_4.index,
    'inf_totales': (grid_4['i_grave'] + grid_4['i_mild'] + grid_4['incubando']),
    'muertos': grid_4['muertos'],
    'inf_graves': grid_4['i_grave'] * 5
})

df5 = pd.DataFrame({
    'iteracion': grid_3.index,
    'inf_leve': grid_3['i_mild'],
    'inf_grave': grid_3['i_grave']
})


iteraciones = range(1, 201)
plt.grid(True)
plt.title(u'Comparación segun porcentaje inicial de infectados', fontsize=12)  # Titulo
plt.suptitle(u'Evolución de muertos modelo Grid', fontsize=14)  # Subtitulo
plt.legend(fancybox=True, loc=2)
plt.ylabel(u'Porcentaje de la población muerta')  # Titulo ordenada
plt.xlabel(u'Iteración')  # Titulo abcisa
plt.plot(iteraciones, df1.muertos[:200], c='cyan', label=u'0.01')
plt.plot(iteraciones, df2.muertos[:200], c='magenta', label=u'0.001')
plt.plot(iteraciones, df3.muertos[:200], c='navy', label=u'0.0001')
plt.plot(iteraciones, df4.muertos[:200], c='crimson', label=u'0.0001')

a = plt.scatter(0, df1.muertos[0], marker='o', color='cyan')
b = plt.scatter(0, df2.muertos[0], marker='o', color='magenta')
c = plt.scatter(0, df3.muertos[0], marker='o', color='navy')
d = plt.scatter(0, df4.muertos[0], marker='o', color='crimson')

plt.legend((a, b, d, c),
           ('1', '0.1', '0.05', '0.01'),
           scatterpoints=1,
           fontsize=10,
           title='% Inicial')
plt.savefig('/Users/tomasj/PycharmProjects/tprse/resultados/imagenes/grid/evolucion_muertos.png')
plt.show()
