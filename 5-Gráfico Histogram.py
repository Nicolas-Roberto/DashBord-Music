#%%

# Importa a biblioteca pandas como "pd"
import pandas as pd
# Importa o módulo express da biblioteca plotly como "px"
import plotly.express as px

# 1º - Definindo a variável "df" (dataframe) que receberá as informações que está no csv
# 2º - Utilizando a biblioteca pandas (pd) lerá o csv "new_3.csv" e armazenará apenas a coluna "ouvintes" no dataframe
df = pd.read_csv('new_3.csv', usecols = ['ouvintes'])
# Calcula número de ouvintes no dataframe
somaouvintes = df['ouvintes'].sum()
# Cria uma lista com a porcentagem do numero de ouvintes de cada artista
porc = (df['ouvintes'])/somaouvintes

# Plotando o gráfico
# 1º - Definindo a variável "fig" onde será armazenado o gráfico
# 2º - Utiliza a função histograma no módulo "px" da biblioteca plotly
fig = px.histogram(df, # Informa que a origem dos dados, não especificados, vêm do dataframe "df"
                   x = 'ouvintes', # O eixo x se refere ao número de ouvintes
                   y = porc, # O eixo y se refere à porcentagem de artistas com certo número de ouvintes
                   nbins = 30, # Divide o total de ouvintes em 30 intervalos
                   color_discrete_sequence = ['#c8d4d3']) # Muda a cor das barras do gráfico

# Modificando o layout do gráfico "fig"
fig.update_layout (yaxis_tickformat = '.2%', # Transforma o eixo y em porcentagem com 2 casas decimais
                   title = '<b>Number of Listeners per Artist Histogram', # Altera o título do gráfico
                   title_x = 0.5, # Centraliza o título do gráfico
                   titlefont = {'family' : 'Courier New', # Altera a fonte do título
                                'size' : 20, # Altera o tamanho da fonte do título
                                'color' : '#c8d4d3'}, # Altera a cor da fonte do título
                   yaxis = {'color' : '#c8d4d3', # Altera a cor da fonte do título do eixo y
                            'title' : '<b>percentage of artists', # Altera o nome do título do eixo y
                            'titlefont' : {'family' : 'Courier New', # Altera a fonte do título do eixo y
                                           'size' : 18}}, # Altera o tamanho da fonte do título do eixo y
                   xaxis = {'color' : '#c8d4d3', # Altera a cor da fonte do título do eixo x
                            'title' : '<b>number of listeners', # Altera o nome do título do eixo x
                            'titlefont' : {'family' : 'Courier New', # Altera a fonte do título do eixo x
                                           'size' : 18}}, # Altera o tamanho da fonte do título do eixo x
                   plot_bgcolor = '#252e3f', # Altera a cor de fundo do gráfico
                   paper_bgcolor = '#252e3f',) # Altera a cor do papel ao redor do gráfico

# Mostra o gráfico construído
fig.show()
# %%