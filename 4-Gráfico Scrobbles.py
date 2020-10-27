
#%%


import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('new_3.csv', usecols= ['paises', 'scrobbles'])
df = df.groupby(by='paises').sum()
df = df.sort_values(by='scrobbles', ascending=False)

# LÊ O CSV, DETERMINA AS COLUNAS A SEREM UTILIZADAS E  
# SOMA OS VALORES DE SCROBBLES E OUVINTES E ORDENA O DATAFRAME POR SCROBBLES

soma = df['scrobbles'].sum()
df['porcentagem'] = (df['scrobbles']/soma)
df['paises'] = df.index

# CALCULA A PORCENTAFEM DE SCROBBLES POR PAÍS

if 'outro' in df['paises'][:10]:
        y = df[df.index == 'outro']
        df = df.drop('outro')
        df = df.append(y)

# MOVE O PAÍS "OUTRO" PARA O FINAL DO DATAFRAME

others = df['porcentagem'][11:].sum()
df['porcentagem'] = df['porcentagem'][0:11]
df['porcentagem'][10] = others
df['paises'][10] = 'others'
df_top = df.head(n = 11)

# SOMA A PORCENTAGENS DE SCROBBLES A PARTIR DO 11° E ARMAZENA NA POSIÇÃO 11 DA COLUNA "PORCENTAGEM"
# E PEGA APENAS OS 10 PRIMEIROS PAÍSES E A SOMA

trace = go.Bar(
               x =  df_top['paises'],
               y =  df_top['porcentagem'],
               marker = {'color': '#c8d4d3'})

# CRIA O GRÁFICO E DETERMINA SUA COR

layout = go.Layout(
        yaxis_tickformat = '%',
        title = '<b>Proportion of all Scrobbles by Country',
        title_x = 0.5,
        titlefont = {'family' : 'Courier New',
                      'size' : 20,
                      'color' : '#c8d4d3'},
        yaxis = {'color' : '#c8d4d3',
                 'title' : '<b>percentage of scrobbles',
                 'titlefont' : {'family' : 'Courier New',
                                'size' : 18}},
        xaxis = {'color' : '#c8d4d3',
                  'title' : '<b>countries',
                  'titlefont' : {'family' : 'Courier New',
                                 'size' : 18}},
        plot_bgcolor = '#252e3f',
        paper_bgcolor = '#252e3f')

# EDITA O LAYOUT DO GRÁFICO

data = [trace]
fig = go.Figure(data=data, layout=layout)
fig.show()

# PLOTA E MOSTRA O GRÁFICO
# %%
