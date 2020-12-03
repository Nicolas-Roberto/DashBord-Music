import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objects as go
import graficos as gr



df = pd.read_csv('new_3.csv',  usecols= ['paises', 'ouvintes', 'estilos'], low_memory=False)
df = df.sort_values(by = 'ouvintes', ascending = False)
df2 = df[['ouvintes']].groupby(df['estilos']).sum().sort_values(by = 'ouvintes', ascending = False)
df2 = df2[:30]

'''for i in df2.index:
    if len(df2[i]) > 9:
        estil.append(df2[i])'''

if 'outro' in df2.index:
    df2 = df2.drop('outro')


Dash = dash.Dash(name= __name__, external_stylesheets= None)

estil = df2.index

Dash.layout = html.Div([

   dcc.Dropdown(
       id='estilo-dropdown',
       options=[{'label':i.title(),'value':i} for i in estil]
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
    if value is None:
        return gr.genero('pop')
    else:
        return gr.genero(value)


if __name__ == '__main__':

    Dash.run_server(debug=True)
