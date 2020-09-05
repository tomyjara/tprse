import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({'font.size': 15})


def tieneR(df):
    return df['modelo'].iloc[0] != 'SISM'


def graficar_modelo(df, pi, modelo, save_to):
    pal = sns.color_palette("Set1")
    alpha = 0.4
    recuperados = []
    labels = []
    recuperados.append('recuperados')
    labels.append('susceptibles')
    x = range(0, len(df))
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 6.5)
    labels = ['Incubando', 'Inf. leves', 'Inf. graves', 'Susceptibles', 'Recuperados', 'Muertos']

    ax.stackplot(x, df['incubando'], df['i_mild'], df['i_grave'], df['susceptibles'],
                 df['recuperados'], df['muertos'], labels=labels, colors=pal,
                 alpha=alpha)

    ax.legend(loc='right')
    titulo = "Evolución de casos - Modelo: " + modelo + ' - Porcentaje de nodos incubando: ' + str(pi * 100)
    plt.title(titulo)
    plt.xlabel("Unidades de tiempo")
    plt.ylabel("Proporción de la población")
    # plt.show()
    plt.savefig(save_to)
    plt.close()


def graficar_modelosw(df, pi, modelo, save_to, k, p):
    pal = sns.color_palette("Set1")
    alpha = 0.4
    recuperados = []
    labels = []
    recuperados.append('recuperados')
    labels.append('susceptibles')
    x = range(0, len(df))
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 6.5)
    labels = ['Incubando', 'Inf. leves', 'Inf. graves', 'Susceptibles', 'Recuperados', 'Muertos']

    ax.stackplot(x, df['incubando'], df['i_mild'], df['i_grave'], df['susceptibles'],
                 df['recuperados'], df['muertos'], labels=labels, colors=pal,
                 alpha=alpha)

    ax.legend(loc='right')
    titulo = "Evolución de casos - Modelo: " + modelo + ' - K: ' + str(k) + ' P: ' + str(p)
    plt.title(titulo)
    plt.xlabel("Unidades de tiempo")
    plt.ylabel("Proporción de la población")
    # plt.show()
    plt.savefig(save_to)
    plt.close()


def graficar_modelo_tree(df, pi, modelo, save_to, r, h):
    pal = sns.color_palette("Set1")
    alpha = 0.4
    recuperados = []
    labels = []
    recuperados.append('recuperados')
    labels.append('susceptibles')
    x = range(0, len(df))
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 6.5)
    labels = ['Incubando', 'Inf. leves', 'Inf. graves', 'Susceptibles', 'Recuperados', 'Muertos']

    ax.stackplot(x, df['incubando'], df['i_mild'], df['i_grave'], df['susceptibles'],
                 df['recuperados'], df['muertos'], labels=labels, colors=pal,
                 alpha=alpha)

    ax.legend(loc='right')
    titulo = "Evolución de casos - Modelo: " + modelo + ' - R: ' + str(r) + ' H: ' + str(h)
    plt.title(titulo)
    plt.xlabel("Unidades de tiempo")
    plt.ylabel("Proporción de la población")
    # plt.show()
    plt.savefig(save_to)
    plt.close()



grid_0001 = pd.read_csv('../resultados/grid/grid_0.0001')
grid_0005 = pd.read_csv('../resultados/grid/grid_0.0005')
grid_001 = pd.read_csv('../resultados/grid/grid_0.001')
grid_01 = pd.read_csv('../resultados/grid/grid_0.01')

graficar_modelo(grid_0001, 0.0001, "Grid", '../resultados/imagenes/grid/grid_0001.png')
graficar_modelo(grid_0005, 0.0005, "Grid", '../resultados/imagenes/grid/grid_0005.png')
graficar_modelo(grid_001, 0.001, "Grid", '../resultados/imagenes/grid/grid_001.png')
graficar_modelo(grid_01, 0.01, "Grid", '../resultados/imagenes/grid/grid_01.png')

random_01_5 = pd.read_csv('../resultados/random/random_0.01_5')
random_01_2 = pd.read_csv('../resultados/random/random_0.01_2')
random_01_3 = pd.read_csv('../resultados/random/random_0.01_3')
random_001_2 = pd.read_csv('../resultados/random/random_0.001_2')
random_001_3 = pd.read_csv('../resultados/random/random_0.001_3')
random_001_5 = pd.read_csv('../resultados/random/random_0.001_5')
random_0001_5 = pd.read_csv('../resultados/random/random_0.0001_5')
random_0001_3 = pd.read_csv('../resultados/random/random_0.0001_3')
random_0001_2 = pd.read_csv('../resultados/random/random_0.0001_2')

graficar_modelo(random_01_5, 0.01, "Random m = 5", '../resultados/imagenes/random/random_01_5.png')
graficar_modelo(random_01_2, 0.01, "Random m = 2", '../resultados/imagenes/random/random_01_2.png')
graficar_modelo(random_01_3, 0.01, "Random m = 3", '../resultados/imagenes/random/random_01_3.png')
graficar_modelo(random_001_2, 0.001, "Random m = 2", '../resultados/imagenes/random/random_001_2.png')
graficar_modelo(random_001_3, 0.001, "Random m = 3", '../resultados/imagenes/random/random_001_3.png')
graficar_modelo(random_001_5, 0.001, "Random m = 5", '../resultados/imagenes/random/random_001_5.png')
graficar_modelo(random_0001_5, 0.0001, "Random m = 5", '../resultados/imagenes/random/random_0001_5.png')
graficar_modelo(random_0001_3, 0.0001, "Random m = 3", '../resultados/imagenes/random/random_0001_3.png')
graficar_modelo(random_0001_2, 0.0001, "Random m = 2", '../resultados/imagenes/random/random_0001_2.png')

scale_free_01 = pd.read_csv('../resultados/scale_free/scale_free_0.1')
scale_free_001 = pd.read_csv('../resultados/scale_free/scale_free_0.01')
scale_free_0001 = pd.read_csv('../resultados/scale_free/scale_free_0.001')
scale_free_02 = pd.read_csv('../resultados/scale_free/scale_free_0.2')
scale_free_03 = pd.read_csv('../resultados/scale_free/scale_free_0.3')
scale_free_05 = pd.read_csv('../resultados/scale_free/scale_free_0.5')
scale_free_005 = pd.read_csv('../resultados/scale_free/scale_free_0.005')
scale_free_0005 = pd.read_csv('../resultados/scale_free/scale_free_0.0005')
vacunados_1 = pd.read_csv('../resultados/scale_free/vacunados_1')
vacunados_01 = pd.read_csv('../resultados/scale_free/vacunados_01')
vacunados_02 = pd.read_csv('../resultados/scale_free/vacunados_02')
vacunados_05 = pd.read_csv('../resultados/scale_free/vacunados_05')

vacunados_101 = pd.read_csv('../resultados/scale_free/vacunados_101')
vacunados_102 = pd.read_csv('../resultados/scale_free/vacunados_102')
vacunados_103 = pd.read_csv('../resultados/scale_free/vacunados_103')

graficar_modelo(scale_free_01, 0.1, "Scale Free", '../resultados/imagenes/scale_free/scale_free_01.png')
graficar_modelo(scale_free_001, 0.01, "Scale Free", '../resultados/imagenes/scale_free/scale_free_001.png')
graficar_modelo(scale_free_0001, 0.001, "Scale Free", '../resultados/imagenes/scale_free/scale_free_0001.png')
graficar_modelo(scale_free_02, 0.2, "Scale Free", '../resultados/imagenes/scale_free/scale_free_02.png')
graficar_modelo(scale_free_03, 0.3, "Scale Free", '../resultados/imagenes/scale_free/scale_free_03.png')
graficar_modelo(scale_free_05, 0.5, "Scale Free", '../resultados/imagenes/scale_free/scale_free_05.png')
graficar_modelo(scale_free_005, 0.005, "Scale Free", '../resultados/imagenes/scale_free/scale_free_005.png')
graficar_modelo(scale_free_0005, 0.0005, "Scale Free", '../resultados/imagenes/scale_free/scale_free_00005.png')
graficar_modelo(vacunados_1, 0.005, "Scale Free, 1% de nodos vacunados",
                '../resultados/imagenes/scale_free/vacunados_1.png')

graficar_modelo(vacunados_01, 0.005, "Scale Free, 0.1% de nodos vacunados",
                '../resultados/imagenes/scale_free/vacunados_01.png')
graficar_modelo(vacunados_02, 0.005, "Scale Free, 0.2% de nodos vacunados",
                '../resultados/imagenes/scale_free/vacunados_02.png')
graficar_modelo(vacunados_05, 0.005, "Scale Free, 0.5% de nodos vacunados",
                '../resultados/imagenes/scale_free/vacunados_05.png')

graficar_modelo(vacunados_101, 0.01, "Scale Free, 0.1% de nodos vacunados",
                '../resultados/imagenes/scale_free/vacunados_101.png')
graficar_modelo(vacunados_102, 0.01, "Scale Free, 0.2% de nodos vacunados",
                '../resultados/imagenes/scale_free/vacunados_102.png')
graficar_modelo(vacunados_103, 0.01, "Scale Free, 0.3% de nodos vacunados",
                '../resultados/imagenes/scale_free/vacunados_103.png')

small_world_k2_p01_001 = pd.read_csv('../resultados/small_world/sw_k2_p0.1_0.001')
graficar_modelosw(small_world_k2_p01_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k2_p0.1_0.001.png', 2, 0.1)

small_world_k2_p03_001 = pd.read_csv('../resultados/small_world/sw_k2_p0.3_0.001')
graficar_modelosw(small_world_k2_p03_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k2_p0.3_0.001.png', 2, 0.3)

small_world_k2_p05_001 = pd.read_csv('../resultados/small_world/sw_k2_p0.5_0.001')
graficar_modelosw(small_world_k2_p05_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k2_p0.5_0.001.png', 2, 0.5)

small_world_k3_p01_001 = pd.read_csv('../resultados/small_world/sw_k3_p0.1_0.001')
graficar_modelosw(small_world_k3_p01_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k3_p0.1_0.001.png', 3, 0.1)

small_world_k3_p03_001 = pd.read_csv('../resultados/small_world/sw_k3_p0.3_0.001')
graficar_modelosw(small_world_k3_p03_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k3_p0.3_0.001.png', 3, 0.3)

small_world_k3_p05_001 = pd.read_csv('../resultados/small_world/sw_k3_p0.5_0.001')
graficar_modelosw(small_world_k3_p05_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k3_p0.5_0.001.png', 3, 0.5)

small_world_k4_p01_001 = pd.read_csv('../resultados/small_world/sw_k4_p0.1_0.001')
graficar_modelosw(small_world_k4_p01_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k4_p0.1_0.001.png', 4, 0.1)

small_world_k4_p03_001 = pd.read_csv('../resultados/small_world/sw_k4_p0.3_0.001')
graficar_modelosw(small_world_k4_p03_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k4_p0.3_0.001.png', 4, 0.3)

small_world_k4_p05_001 = pd.read_csv('../resultados/small_world/sw_k4_p0.5_0.001')
graficar_modelosw(small_world_k4_p05_001, 0.001, "Small World",
                  '../resultados/imagenes/small_world/sw_k4_p0.5_0.001.png', 4, 0.5)

tree_r2_h15 = pd.read_csv('../resultados/tree/balanced_tree_r2_h15_0.0001')
graficar_modelo_tree(tree_r2_h15, 0.0001, "Balanced Tree", '../resultados/imagenes/balanced_tree/tree_r2_h15.png', 2, 15)

tree_r3_h10 = pd.read_csv('../resultados/tree/balanced_tree_r3_h10_0.0001')
graficar_modelo_tree(tree_r3_h10, 0.0001, "Balanced Tree", '../resultados/imagenes/balanced_tree/tree_r3_h10.png', 3, 10)

tree_r4_h7 = pd.read_csv('../resultados/tree/balanced_tree_r4_h7_0.0001')
graficar_modelo(tree_r4_h7, 0.0001, "Balanced Tree", '../resultados/imagenes/balanced_tree/tree_r4_h7.png')

tree_r7_h5 = pd.read_csv('../resultados/tree/balanced_tree_r7_h5_0.0001')
graficar_modelo(tree_r7_h5, 0.0001, "Balanced Tree", '../resultados/imagenes/balanced_tree/tree_r7_h5.png')

tree_r8_h5 = pd.read_csv('../resultados/tree/balanced_tree_r8_h5_0.0001')
graficar_modelo(tree_r8_h5, 0.0001, "Balanced Tree", '../resultados/imagenes/balanced_tree/tree_r8_h5.png')

tree_r9_h5 = pd.read_csv('../resultados/tree/balanced_tree_r9_h5_0.0001')
graficar_modelo_tree(tree_r9_h5, 0.0001, "Balanced Tree", '../resultados/imagenes/balanced_tree/tree_r9_h5.png', 9, 5)

tree_r10_h5 = pd.read_csv('../resultados/tree/balanced_tree_r10_h5_0.0001')
graficar_modelo_tree(tree_r10_h5, 0.0001, "Balanced Tree", '../resultados/imagenes/balanced_tree/tree_r10_h5.png', 10, 5)

tree_r5_h6 = pd.read_csv('../resultados/tree/balanced_tree_r5_h6_0.0001')
graficar_modelo(tree_r10_h5, 0.0001, "Balanced Tree", '../resultados/imagenes/balanced_tree/tree_r5_h6.png')
