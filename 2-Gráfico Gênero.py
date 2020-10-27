import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.express as px



df = pd.read_csv('new_3.csv',  usecols= ['paises', 'ouvintes', 'estilos'], low_memory=False)
df = df.sort_values(by = 'ouvintes', ascending = False)
df2 = df[:30]

Dash = dash.Dash(name=__name__,external_stylesheets=None)

estil = df2.estilos.unique()

Dash.layout = html.Div([

   dcc.Dropdown(
       id='estilo-dropdown',
       options=[{'label':i,'value':i} for i in estil]
       

   ),

   html.Div([
       dcc.Graph(
            id='meu-grafico-aqui'
            
       )
       
   ])
 
])

@Dash.callback(
   Output('meu-grafico-aqui','figure'),
   [Input('estilo-dropdown','value')])

def update_output(value):

    x = value
    df_estilos = df[df['estilos'] == x].dropna()

    group = df_estilos[['ouvintes']].groupby(df_estilos['paises']).sum().sort_values(by = 'ouvintes', ascending = False)
    group['paises'] = group.index


    if 'outro' in group['paises'][:10]:
            y = group[group.index == 'outro']
            group = group.drop('outro')
            group = group.append(y)


    total = group['ouvintes'].sum()
    group['porcentagem'] = (group['ouvintes'] / total)

    others = group['porcentagem'][11:].sum()
    group['porcentagem'][10] = others

    group_top = group.head(n = 11)
    group_top['paises'][10] = 'others'
    Fig = px.bar(df_estilos,x=group_top['paises'], y=group_top['porcentagem'])

    Fig.update_layout(
        yaxis_tickformat = '%', # COLOCA OS VALORES NO GRÁFICO EM PORCENTAGEM
        title = '<b>Percentage of Listeners by Country: ' + x.capitalize(), # ADICIONA O TÍTULO DO GRÁFICO
        title_x = 0.5, # CENTRALIZA O T´ÍTULO DO GRÁFICO
        titlefont = {'family' : 'Courier New', 
                    'size' : 20,
                    'color' : '#c8d4d3'}, # MUDA A COR, FONTE E TAMANHO DO TÍTULO
        yaxis = {'color' : '#c8d4d3',
                'title' : '<b>listeners percentage',
                'titlefont' : {'family' : 'Courier New',
                            'size' : 18}}, # DETERMINA O NOME DO EIXO Y, MUDA SUA COR E TAMANHO
        xaxis = {'color' : '#c8d4d3',
                'title' : '<b>countries',
                'titlefont' : {'family' : 'Courier New',
                                'size' : 18}}, # DETERMINA O NOME DO EIXO Y, MUDA SUA COR E TAMANHO
        plot_bgcolor = '#252e3f',
        paper_bgcolor = '#252e3f') # MUDA A COR DO FUNDO DO GRÁFICO E DO PAPEL ONDE O GRÁFICO FICA
    
    return   Fig


if __name__ == '__main__':

    Dash.run_server(debug=True)