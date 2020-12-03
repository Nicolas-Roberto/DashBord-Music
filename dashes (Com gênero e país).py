import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import graficos as gr
import pandas as pd

df = pd.read_csv('new_3.csv')
df2 = df[['ouvintes']].groupby(df['estilos']).sum().sort_values(by = 'ouvintes', ascending = False).index
df2 = df2[:480]
if 'outro' in df2:
    df2 = df2.drop('outro')

df3 = df[['ouvintes']].groupby(df['paises']).sum().sort_values(by = 'ouvintes', ascending = False).index
if 'outro' in df3:
    df3 = df3.drop('outro')




style_L = {'font-family' : 'Dank Mono',
            'font-size' : '150%'}

app = dash.Dash(__name__)

app.layout = html.Div(style = {'backgroundColor' : '#252e3f',
                                'color' :  '#252e3f',
                                },
                      children = [
    html.H1(children = 'Trabalho Final APC - Grupo 4',

    ),
    
    html.Div(style = {'backgroundColor' : '#252e3f'}, #Mapa
            children = [
                html.Label(children = '''
                    Maps: Most Relevant Artist by Country & Numbers of Scrobbles Heat Map
                    ''',
                ),

                dcc.Graph(
                    id = 'grafico'
                ),
                html.P(style = {'font-family' : 'Dank Mono',
                                'font-size' : '125%'},
                    children = '''
                    Select Map:'''
                ),

                dcc.Dropdown(        
                    id= 'filtro',
                    options = [{'label' : 'Relevant Artists', 'value' : 1},
                                {'label' : 'Scrobbles Heat Map', 'value' : 2}],
                    searchable = False,
                    clearable = False,
                    placeholder = 'Select a map',
                    style = {'font-family' : 'Dank Mono',
                            'backgroundColor' : '#252e3f'}
                )

            ]),


    html.Div(      #Scrobbles
             style = {'backgroundColor' : '#252e3f'},
             children = [
                html.Label(style = style_L,
                children = '''
                        Bar Graph: Numbers of Scrobbles per Country'''
                ),

                dcc.Graph(
                    id = 'scrobbles',
                    figure = gr.scrobbles()
                )
             ],className = 'box1'),
    

    html.Div(   #Histogram
             style = {'backgroundColor' : '#252e3f'},
             children = [
                html.Label(style = style_L,
                children = '''
                        Bar Graph: Number of Listeners per Artist Histogram'''
                ),

               dcc.Graph(
                   id = 'histograma',
                   figure = gr.histograma()
               )
            ],className = 'box2'),
    
    html.Br(),

    html.Div(   #genero
        style = {'background' : '#252e3f'},
        children = [
            html.Label(children = '''
                    COLOQUE SEU TEXTO AQUI!!'''
            ),

            dcc.Graph(
                id = 'genero'
            ),

            dcc.Dropdown(
                id = 'estilos-drop',
                options = [{'label' : i.title(), 'value' : i} for i in df2],
                
            )
        ], className = 'box1'),


    html.Div(   #pais
        style = {},
        children = [
            html.Label(style = style_L,
            children = '''
                    COLOQUE SEU TEXTO AQUI!!!'''
            ),

            dcc.Graph(
                id = 'pais'
            ),

            dcc.Dropdown(
                id = 'pais-drop',
                options = [{'label' : i.title(), 'value' : i} for i in df3]
            )
        ], className = 'box2')

], className = 'box3')

@app.callback(
    Output('grafico', 'figure'),
    [Input(component_id = 'filtro', component_property = 'value')]
)

def update_output(value):
    if value is None or value == 1:
        return gr.mapa()
    else:
        if value == 2:
            return gr.calor()

@app.callback(
    Output('genero', 'figure'),
    [Input(component_id = 'estilos-drop', component_property = 'value')]
)

def update_genero(value):
    if value == None:
        return gr.genero('pop')
    else:
        return gr.genero(value)

@app.callback(
    Output('pais', 'figure'),
    [Input(component_id = 'pais-drop', component_property = 'value')]
)

def update_pais(value):
    if value == None:
        return gr.pais('Brazil')
    else:
        return gr.pais(value)

if __name__ == '__main__':
    app.run_server(debug = True)