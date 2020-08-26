I = 'I'
S = 'S'
R = 'R'
M = 'M'

GRID = '2d_grid'
SCALE_FREE = 'scale'
SMALL_WORLD = 'small_world'
RANDOM = 'random'

# La probabilidad de ser de riesgo depende de cada población.
PROBABILIDAD_RIESGO = 0.25

#Parametros COVID Fuente: https://www.who.int/docs/default-source/coronaviruse/who-china-joint-mission-on-covid-19-final-report.pdf

T_INF_MILD = 10
T_INF_GRAVE = 21
T_RECUPERACION = 15
T_INCUBACION = 7

#Parametros COVID Fuente: https://www.statista.com/statistics/1105402/covid-hospitalization-rates-us-by-age-group/
PROB_INFEC_GRAVE_RIESGO = 0.57
PROB_INFEC_GRAVE = 0.2
PROB_DE_DECESO = 0.000971067
PROB_DE_DECESO_RIESGO = 0.00529539


#Parametros Gripe Fuente:

# T_INF_MILD = 5 # fuente: https://www.cdc.gov/flu/professionals/acip/clinical.htm#:~:text=Uncomplicated%20influenza%20signs%20and%20symptoms,those%20with%20chronic%20lung%20disease.
# T_INF_GRAVE = 14 # fuente: https://www.ncbi.nlm.nih.gov/books/NBK63484/#:~:text=The%20mean%20length%20of%20stay,overall%20(%246%2C900%20versus%20%247%2C700).
# T_RECUPERACION = 200
# T_INCUBACION = 2 #fuente: https://medbroadcast.com/condition/getcondition/influenza
#
# #Parametros Gripe Fuente: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0118369
# PROB_INFEC_GRAVE_RIESGO = 0.54
# PROB_INFEC_GRAVE = 0.00074
# PROB_DE_DECESO = 0.000001
# PROB_DE_DECESO_RIESGO = 0.00529539 #falta calcular

# Estados
ESTADO_INCUBANDO = 'EstadoIncubando'
ESTADO_SUSCEPTIBLE = 'EstadoSusceptible'
ESTADO_INFECTADO_MILD = 'EstadoInfectadoMild'
ESTADO_INFECTADO_GRAVE = 'EstadoInfectadoGrave'
ESTADO_MUERTO = 'EstadoMuerto'
ESTADO_RECUPERADO = 'EstadoRecuperado'
