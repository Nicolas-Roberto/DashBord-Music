#%%
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('new_3.csv',  usecols= ['paises', 'ouvintes', 'estilos'])
df = df.sort_values(by = 'ouvintes', ascending = False)

# LÊ O CSV, DETERMINA AS COLUNAS A SEREM UTILIZADAS E ORDENA POR OUVINTES

x = 'Brazil'
uk = df[df['paises'] == x].dropna()
# CRIA UM DATA FRAME COM APENAS OS DADOS DO PAÍS DESEJADO E RETIRA OS NaN

group = uk[['ouvintes']].groupby(uk['estilos']).sum().sort_values(by = 'ouvintes', ascending = False)
group['estilos'] = group.index

# SOMA TODOS OS OUVINTES, SEPARANDO-OS POR ESTILOS

if 'outro' in group['estilos'][:10]:
        y = group[group.index == 'outro']
        group = group.drop('outro')
        group = group.append(y)

# MOVE O ESTILO "OUTRO" PARA O FINAL DO DATAFRAME

total = group['ouvintes'].sum()
group['porcentagem'] = (group['ouvintes'] / total)
# CALCULA A PORCENTAGEM DE CADA ESTILO E CRIA UMA COLUNA COM ESTAS PORCENTAGENS

others = group['porcentagem'][11:].sum()
group['porcentagem'][10] = others

# SOMA A PORCENTAGEM DE TODOS ESTILOS A PARTIR DO 11° RELEVANTE E ADICIONA UMA LINHA COM ESTA PORCENTAGEM

group_top = group.head(n = 11)
group_top['estilos'][10] = 'others'

# PEGA OS PRIMEIROS 10 ESTILOS MAIS RELEVANTES E A SOMA DAS OUTRAS PORCENTAGENS

trace = go.Bar(x = group_top['estilos'],
               y = group_top['porcentagem'],
               marker = {'color' : '#c8d4d3'})

# CRIA O GRÁFICO COM OS ESTILOS E A PORCENTAGEM DE CADA UM E DEFINE SUA COR
                
layout = go.Layout(
        yaxis_tickformat = '%', # COLOCA OS VALORES NO GRÁFICO EM PORCENTAGEM
        title = '<b>Percentage of Listeners by Genres: ' + x, # ADICIONA O TÍTULO DO GRÁFICO
        title_x = 0.5, # CENTRALIZA O T´ÍTULO DO GRÁFICO
        titlefont = {'family' : 'Courier New', 
                      'size' : 20,
                      'color' : '#c8d4d3'}, # MUDA A COR, FONTE E TAMANHO DO TÍTULO
        yaxis = {'color' : '#c8d4d3',
                 'title' : '<b>listeners percentage',
                 'titlefont' : {'family' : 'Courier New',
                                'size' : 18}}, # DETERMINA O NOME DO EIXO Y, MUDA SUA COR E TAMANHO
        xaxis = {'color' : '#c8d4d3',
                  'title' : '<b>music genres',
                  'titlefont' : {'family' : 'Courier New',
                                 'size' : 18}}, # DETERMINA O NOME DO EIXO Y, MUDA SUA COR E TAMANHO
        plot_bgcolor = '#252e3f',
        paper_bgcolor = '#252e3f') # MUDA A COR DO FUNDO DO GRÁFICO E DO PAPEL ONDE O GRÁFICO FICA

# MUDA O LAYOUT DO GRÁFICO

data = [trace]
fig = go.Figure(data = data, layout = layout)
fig.show()

# PLOTA E MOSTRA O GRÁFICO
# %%
