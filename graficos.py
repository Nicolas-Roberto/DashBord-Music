import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import layout_m as lm
from math import log2

# lê o csv
df_inicial = pd.read_csv('new_3.csv')

# cria uma lista de países para os gráficos de calor e scrobbles
lista_p = df_inicial.paises.unique()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
# MAPA ARTISTAS

def mapa():

    df = df_inicial[['paises', 'artistas', 'ouvintes']]       
    df = df.sort_values(by = 'ouvintes', ascending = False)

    # LÊ O CSV, DETERMINA AS COLUNAS A SEREM UTILIZADAS E ORDENA POR OUVINTES

    pais = df['paises']
    artista = df['artistas']
    paises = []
    artistas = []
    for i in range(514853):   
        if pais[i] not in paises and artista[i] not in artistas and type(pais[i]) == str:
            paises.append(pais[i])
            artistas.append(artista[i])

    # EVITA O APARECIMENTO DE NaN E FAZ COM QUE PAISES APAREÇAM APENAS UMA VEZ        

    paises[paises.index('Soviet Union')] = 'Russia' # TROCA O NOME "SOVIET UNION" QUE APARECE NO CSV PARA RUSSIA

    trace = go.Scattergeo(
                        fill = 'toself', # PERMITE QUE A COR DA CAIXA DE TEXTO MUDE
                        fillcolor = '#252e3f', # DETERMINA A COR DA CAIXA DE TEXTO
                        locationmode = 'country names', # DETERMINA O MODO EM QUE VÃO SER ENCONTRADOS 
                                                        # AS LOCALIZAÇÕES QUE APARECEM NA VARIÁVEL "LOCATIONS"
                        locations = paises, # DETERMINA AS LOCALIZAÇÕES QUE APARECEM NO MAPA, NO CASO OS PAÍSES
                        text = artistas, # DETERMINA O TEXTO QUE APARECE NA CAIXA DE TEXTO,
                                        # NESTE CASO, OS ARTISTAS MAIS INFLUENTES NO PAÍS
                        mode = 'none', # DETERMINA O MODO DE COMO VÃO APARECER AS LOCALIZAÇÕES NO MAPA
                        )

    # CRIA O GRÁFICO

    layout = lm.layout_mc('Most Relevant Artist by Country')

    # EDITA O LAYOUT 

    data = [trace]
    fig = go.Figure(data=data, layout=layout)
    return fig

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
# MAPA DE CALOR

def calor(): 
    
    df = df_inicial[['paises', 'scrobbles']]
    df = df.values.tolist()

    # cria uma lista somando os scrobbles por país
    lista_s = list()
    for pais in lista_p:
        scrobbles = 0
        for i in range(len(df)):
            if pais == df[i][0]:
                scrobbles += df[i][1]
        lista_s.append(scrobbles)

    # cria uma lista com os logs dos scrobbles da ultima lista
    lista_o_l = ([log2(i) for i in lista_s])

    # cria o gráfico
    trace = go.Choropleth(
                        locationmode = 'country names', # DETERMINA O MODO QUE MOSTRARÁ OS PONTOS NO MAPA
                        locations = lista_p, # DETERMINA AS LOCALIZAÇÕES QUE APARECEM NO MAPA, NO CASO OS PAÍSES
                        z = lista_o_l, # BASE PARA AS CORES DO MAPA
                        text = lista_s,
                        colorscale = [
                                    'rgb(255, 255, 255)',
                                    'rgb(67, 183, 152)'
                                    ], # ESCALA DE CORES DETERMINADA PARA O GRÁFICO
                        colorbar = {'thickness' : 25,
                                    'tickfont' : {'color' : '#c8d4d3',
                                                'family' : 'Courier New'}} # DETERMINA A COR E FONTE DO TEXTO E A LARGURA DA BARRA DE CORES
                        )
    # cria e muda o layout
    layout = lm.layout_mc('Heat Map of Scrobbles per Country')

    data = [trace]
    fig = go.Figure(data=data, layout=layout)
    return fig

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
# GRÁFICO PAÍS

def pais(pais):
    
    df = df_inicial[['paises', 'estilos', 'ouvintes']]
    df = df.values.tolist()

    # cria uma lista com apenas o país determinado
    x = pais
    df2 = list()
    for i in range(len(df)):
        if df[i][0] == x:
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

    # cria o gráfico
    trace = go.Bar(x = ([lista[i][0] for i in range(11)]),
                y = ([lista[i][1] for i in range(11)]),
                marker = {'color' : '#c8d4d3'})

    # cria e muda o layout                    
    layout = lm.layout_gps('Percentage of Listeners by Genres: ' + x.title(),
                        'listeners percentage',
                        )

    data = [trace]
    fig = go.Figure(data = data, layout = layout)
    return fig

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
# GRÁFICO GêNERO

def genero(estilo):

    df = df_inicial[['paises', 'estilos', 'ouvintes']]
    df = df.values.tolist()

    # cria uma lista com apenas o estilo determinado
    x = estilo
    df2 = list()
    for i in range(len(df)):
        if df[i][1] == x:
            df2.append(df[i])

    # cria uma lista de países
    paises = list()
    for i in range(len(df2)):
        if df2[i][0] not in paises:
            paises.append(df2[i][0])

    # cria uma lista somando os ouvintes por país
    lista_o = list()
    for pais in paises:
        ouvintes = 0
        for i in range(len(df2)):
            if pais == df2[i][0]:
                ouvintes += df2[i][2]
        lista_o.append(ouvintes)


    # calcula a porcentagem de cada estilo
    total_o = sum(lista_o)
    porcentagem = list()
    for i in lista_o:
        porcentagem.append(i/total_o)

    # cria uma lista ordenada dupla com o nome do país e a quantidade de ouvintes
    lista = ([[pais, porc] for pais, porc in zip(paises, porcentagem)])
    lista = sorted(lista, key= lambda x:x[1], reverse= True)

    # retira e joga o 'outro' pro final da lista
    lista_top = lista[:10]
    for i in range(len(lista_top)):
        if 'outro' == lista[i][0]:
            outro = lista[i]
            del(lista[i])
            lista.append(outro)

    # calcula a porcentagem do 'outros' e adiciona à posição 10 da lista
    lista_b = lista[11:]
    outros = 0
    for i in range(len(lista_b)):
        outros += lista_b[i][1]
    lista.insert(10, ['others', outros])

    # cria o gráfico
    trace = go.Bar(x = [lista[i][0] for i in range(11)],
                y = [lista[i][1] for i in range(11)],
                marker = {'color' : '#c8d4d3'}
                )
                    
    # muda o layout do gráfico
    layout = lm.layout_gps('Percentage of Listeners by Countries: ' + x.title(),
                        'listeners percentage',
                        )

    data = [trace]
    fig = go.Figure(data = data, layout = layout)
    return fig

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
# GRÁFICO HISTOGRAMA

def histograma():
    
    # 1º - Definindo a variável "df" (dataframe) que receberá as informações que está no csv
    # 2º - Utilizando a biblioteca pandas (pd) lerá o csv "new_3.csv" e armazenará apenas a coluna "ouvintes" no dataframe
    df = df_inicial['ouvintes']
    # Calcula número de ouvintes no dataframe
    somaouvintes = df.sum()
    # Cria uma lista com a porcentagem do numero de ouvintes de cada artista
    porc = (df)/somaouvintes

    # Plotando o gráfico
    # 1º - Definindo a variável "fig" onde será armazenado o gráfico
    # 2º - Utiliza a função histograma no módulo "px" da biblioteca plotly
    fig = px.histogram( # Informa que a origem dos dados, não especificados, vêm do dataframe "df"
                    x = df, # O eixo x se refere ao número de ouvintes
                    y = porc, # O eixo y se refere à porcentagem de artistas com certo número de ouvintes
                    nbins = 30, # Divide o total de ouvintes em 30 intervalos
                    color_discrete_sequence= ['#c8d4d3']) # Muda a cor das barras do gráfico

    # Modificando o layout do gráfico "fig"
    fig.update_layout(lm.layout_gps('Histogram: Number of Listeners per Artist', 'percentage of artists', 'number of listeners'))
    fig.update_layout(yaxis_tickformat= '.2%',
                      margin = dict(t = 100))
    # Mostra o gráfico construído
    return fig

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
# GRÁFICO SCROBBLES

def scrobbles():
    
    df = df_inicial[['paises', 'scrobbles']]
    df = df.values.tolist()

    # cria uma lista com a quantidade de scrobbles de cada país
    lista_s = list()
    for pais in lista_p:
        scrobbles = 0
        for i in range(len(df)):
            if df[i][0] == pais:
                scrobbles += df[i][1]
        lista_s.append(scrobbles)

    # calcula a porcentagem de cada país com base nos scrobbles
    total_s = sum(lista_s)
    porcentagem = [i/total_s for i in lista_s]

    # cria a lista final com os países e porcentagens e ordena
    lista = [[pais, porcentagem] for pais, porcentagem in zip(lista_p, porcentagem)]
    lista = sorted(lista, key= lambda x:x[1], reverse= True)

    # retira o 'outro' das 10 primeiras posições e coloca no final da lista
    lista_t = lista[:10]
    for i in range(len(lista_t)):
        if lista_t[i][0] == 'outro':
            outro = lista[i]
            del(lista[i])
            lista.append(outro)

    # calcula e coloca o "outros" na lista final
    lista_b = lista[11:]
    outros = 0
    for i in range(len(lista_b)):
        outros += lista_b[i][1]
    lista.insert(10, ['others', outros])

    # cria o gráfico
    trace = go.Bar(x = ([lista[i][0] for i in range(11)]),
                y = ([lista[i][1] for i in range(11)]),
                marker = {'color' : '#c8d4d3'})

    # cria e muda o layout
    layout = lm.layout_gps('Proportion of all Scrobbles by Country',
                        'listeners percentage',
                        'countries')

    data = [trace]
    fig = go.Figure(data=data, layout=layout)
    return fig

