#%%
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('new_3.csv', usecols = ['scrobbles', 'paises'])
df = df.groupby(by = 'paises').sum()

# LÊ O CSV, DETERMINA AS COLUNAS A SEREM UTILIZADAS E 
# SOMA OS SCROBBLES SEPARANDO-OS POR PAISES
df['paises'] = df.index
trace = go.Choropleth(
                    locationmode = 'country names', # DETERMINA O MODO QUE MOSTRARÁ OS PONTOS NO MAPA
                    locations = df['paises'], # DETERMINA AS LOCALIZAÇÕES QUE APARECEM NO MAPA, NO CASO OS PAÍSES
                    z = df['scrobbles'], # BASE PARA AS CORES DO MAPA
                    colorscale = [
                                   'rgb(230, 239, 241)',
                                   'rgb(179, 228, 220)',
                                   'rgb(154, 253, 227)',
                                   'rgb(117, 234, 203)',
                                   'rgb(105, 229, 200)',
                                   'rgb(99, 203, 173)',
                                   'rgb(92, 197, 166)',
                                   'rgb(67, 183, 152)',
                                   'rgb(52, 141, 124)',
                                   'rgb(33, 114, 96)',
                                   'rgb(36, 108, 92)',
                                   ], # ESCALA DE CORES DETERMINADA PARA O GRÁFICO
                    colorbar = {'thickness' : 25,
                                'tickfont' : {'color' : '#c8d4d3',
                                              'family' : 'Courier New'}} # DETERMINA A COR E FONTE DO TEXTO E A LARGURA DA BARRA DE CORES
                    )

# CRIA O GRÁFICO

layout = go.Layout(
    title = '<b>Heat Map of Scrobbles per Country', # MUDA O TÍTULO DO GRÁFICO
    title_x = 0.5, # CENTRALIZA O TÍTULO
    titlefont = {'family': 'Courier New',
                 'size': 24,
                 'color' : '#c8d4d3'}, # MUDA A COR, FONTE E TAMANHO DO TÍTULO
    paper_bgcolor = '#252e3f', # MUDA A COR DO QUE ESTÁ EM VOLTA DO GRÁFICO
    geo =  {
            'showocean' : True, # MOSTRA A COR DETERMINADA PARA OS OCEANOS
            'oceancolor' : '#252e3f', # COR DETERMINADA PARA OS OCEANOS
            'showlakes' : False, # MOSTRA OS LAGOS NO MAPA (NO CASO, DETERMINADO PARA NÃO MOSTRAR)
            'bgcolor' : '#252e3f' # COR DETERMINADA PARA O FUNDO DO MAPA
            })

# EDITA O LAYOUT

data = [trace]
fig = go.Figure(data=data, layout=layout)
fig.show()

# PLOTA E MOSTRA O GRÁFICO
# %%