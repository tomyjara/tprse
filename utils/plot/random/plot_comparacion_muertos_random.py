import pandas as pd
import matplotlib.pylab as plt

rn001_2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/random/random_0.01_2')
rn0001_2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/random/random_0.001_2')
rn00001_2 = pd.read_csv('/Users/tomasj/PycharmProjects/tprse/resultados/random/random_0.0001_2')


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


iteraciones = range(1, 301)
plt.grid(True)
plt.title(u'Comparación segun porcentaje inicial de infectados', fontsize=12)  # Titulo
plt.suptitle(u'Evolución de muertos modelo Random grado 2', fontsize=14)  # Subtitulo
plt.legend(fancybox=True, loc=2)
plt.ylabel(u'Porcentaje de la población muerta')  # Titulo ordenada
plt.xlabel(u'Iteración')  # Titulo abcisa
plt.plot(iteraciones, df1.muertos, c='cyan', label=u'0.01')
plt.plot(iteraciones, df2.muertos, c='magenta', label=u'0.001')
plt.plot(iteraciones, df3.muertos, c='navy', label=u'0.0001')

a = plt.scatter(0, df1.muertos[0], marker='o', color='cyan')
b = plt.scatter(0, df2.muertos[0], marker='o', color='magenta')
c = plt.scatter(0, df3.muertos[0], marker='o', color='navy')

plt.legend((a, b, c),
           ('1', '0.1', '0.01'),
           scatterpoints=1,
           fontsize=10,
           title='% Inicial')
plt.savefig('/Users/tomasj/PycharmProjects/tprse/resultados/imagenes/random/evolucion_muertos_random.png')
plt.show()
