#%%
import pandas as pd
import plotly.graph_objs as go
df = pd.read_csv('new_3.csv', usecols = ['paises', 'artistas', 'ouvintes'])       
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
                    fill = 'toself',
                    fillcolor = '#252e3f', # DETERMINA A COR DA CAIXA DE TEXTO
                    locationmode = 'country names', # DETERMINA O MODO EM QUE VÃO SER ENCONTRADOS 
                                                     # AS LOCALIZAÇÕES QUE APARECEM NA VARIÁVEL "LOCATIONS"
                    locations = paises, # DETERMINA AS LOCALIZAÇÕES QUE APARECEM NO MAPA, NO CASO OS PAÍSES
                    text = artistas, # DETERMINA O TEXTO QUE APARECE NA CAIXA DE TEXTO,
                                     # NESTE CASO, OS ARTISTAS MAIS INFLUENTES NO PAÍS
                    mode = 'none', # DETERMINA O MODO DE COMO VÃO APARECER AS LOCALIZAÇÕES NO MAPA
                    )

# CRIA O GRÁFICO

layout = go.Layout(
    title = '<b>Most Relevant Artist by Country', # MUDA O TÍTULO DO GRÁFICO
    title_x = 0.5, # CENTRALIZA O TÍTULO
    titlefont = {'family': 'Courier New',
                 'size': 24,
                 'color' : '#c8d4d3'}, # MUDA A COR, FONTE E TAMANHO DO TÍTULO
    paper_bgcolor = '#252e3f', # MUDA A COR DO QUE ESTÁ EM VOLTA DO GRÁFICO
    geo =  {'scope': 'world', # DETERMINA A ÁREA A APARECER NO MAPA
                'projection': {'type': 'equirectangular'}, # DETERMINA O TIPO DE PROJEÇÃO DO MAPA
                'showcountries': True, # MOSTRA AS FRONTEIRAS DO MAPA
                'showocean' : True, # MOSTRA A COR DETERMINADA PARA OS OCEANOS
                'landcolor': '#c8d4d3', # COR DETERMINADA PARA OS CONTINENTES
                'oceancolor' : '#252e3f', # COR DETERMINADA PARA OS OCEANOS
                'showlakes' : False, # MOSTRA OS LAGOS NO MAPA (NO CASO, DETERMINADO PARA NÃO MOSTRAR)
                'countrycolor' : 'rgb(161, 161, 161)', # COR DETERMINADA PARA AS FRONTEIRAS
                'bgcolor' : '#252e3f' # COR DETERMINADA PARA O FUNDO DO MAPA
                })

# EDITA O LAYOUT 

data = [trace]
fig = go.Figure(data=data, layout=layout)
fig.show()

# PLOTA E MOSTRA O GRÁFICO
# %%
