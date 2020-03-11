from simulador_de_epidemias.modelos import crearModelo, correrModeloSIS

CANTIDAD_DE_NODOS = 50
PROBABILIDAD_DE_ESTAR_INFECTADO = 0.4
CANTIDAD_DE_ITERACIONES = 10
TI = 7
RI = 0

modelo = crearModelo(tipoDeGrafo="2d_grid", cantidadDeNodos=CANTIDAD_DE_NODOS,
                     probabilidadDeEstarInfectado=PROBABILIDAD_DE_ESTAR_INFECTADO, ti=TI, ri=RI)

correrModeloSIS(modelo, 500)
