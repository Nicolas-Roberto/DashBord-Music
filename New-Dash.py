#%%
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import layout_m as lm
import math
from math import log2

df = pd.read_csv('new_3.csv', usecols= ['paises', 'estilos', 'ouvintes'])
df = df.values.tolist()

    # cria uma lista com apenas o país determinado
pais = 'United Kingdown'
df2 = list()
for i in range(len(df)):
    if df[i][0] == pais:
        df2.append(df[i])

    # cria uma lista com os estilos
lista_e = list()
for i in range(len(df2)):
    if df2[i][1] not in lista_e:
        lista_e.append(df2[i][1])

    # cria uma lista com os ouvintes de cada estilo
lista_o = list()
for estilo in lista_e:
    ouvintes = 0
    for i in range(len(df2)):
        if df2[i][1] == estilo:
            ouvintes += df2[i][2]
    lista_o.append(ouvintes)

    # calcula a porcentagem de cada estilo
total_o = sum(lista_o)
porcentagem = list()
for i in lista_o:
    porcentagem.append(i/total_o)

    # cria uma lista com os estilos e ouvintes
lista = list()
for estilo, porc in zip(lista_e, porcentagem):
    lista.append([estilo, porc])
lista = sorted(lista, key= lambda x:x[1], reverse= True)

    # retira o 'outro' das 10 primeiras posições e coloca no final da lista
lista_t = lista[:10]
for i in range(len(lista_t)):
    if lista_t[i][0] == 'outro':
        outro = lista[i]
        del(lista[i])
        lista.append(outro)

    # calcular e colocar o "outros" na lista final
lista_b = lista[11:]
outros = 0
for i in range(len(lista_b)):
    outros += lista_b[i][1]
lista.insert(10, ['others', outros])

trace = go.Bar(x = ([lista[i][0] for i in range(11)]),
                y = ([lista[i][1] for i in range(11)]))

    # CRIA O GRÁFICO COM OS ESTILOS E A PORCENTAGEM DE CADA UM E DEFINE SUA COR
                    
layout = lm.layout_gps('Percentage of Listeners by Genres: ' + pais.title(),
                        'listeners percentage',
                        '')
    # MUDA O LAYOUT DO GRÁFICO

data = [trace]
fig = go.Figure(data = data, layout = layout)
fig.show()

#%%