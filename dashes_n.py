import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import graficos as gr
import indexs as i

app = dash.Dash(__name__)

app.layout = html.Div( # Divisão Geral
                      children = [
    
    html.Br(),
    
    html.Div([
    
        html.Img(src = app.get_asset_url("logo.jpeg"),
                className = "imagem"),



        html.H1(
                children = 'Music Analytics Around the World'
        ),

    ], className = "título"),

    html.Br(),
    
    html.Div( # Divisão do Mapa
            children = [
                html.Label(
                    children = '''
                    Maps: Most Relevant Artist by Country & Numbers of Scrobbles Heat Map
                    ''',
                ),

                dcc.Graph(
                    id = 'grafico'
                ),
                html.P(
                    'Select Map:'
                ),

                dcc.Dropdown(        
                    id= 'filtro',
                    options = [{'label' : 'Relevant Artists', 'value' : 1},
                                {'label' : 'Scrobbles Heat Map', 'value' : 2}],
                    searchable = False,
                    clearable = False,
                    placeholder = 'Select a map',
                    className = 'dropdown'
                )

            ], className = 'mapa'),


    html.Div( # Divisão dos gráficos de país e gênero
            children = [

        html.Div(   # Divisão do gráfico de genero
            children = [

                dcc.Graph(
                    id = 'genero'
                ),

                dcc.Dropdown(
                    id = 'estilos-drop',
                    options = [{'label' : i.title(), 'value' : i} for i in i.lista_estilos],
                    clearable = False,
                    className = 'dropdown',
                    placeholder = 'Select a Genre'
                    
                )
            ], className = 'box1'),


        html.Div(   # Divisão do gráfico de pais
            children = [

                dcc.Graph(
                    id = 'pais'
                ),

                dcc.Dropdown(
                    id = 'pais-drop',
                    options = [{'label' : i.title(), 'value' : i} for i in i.lista_paises],
                    clearable = False,
                    className = 'dropdown',
                    placeholder = 'Select a Country'
                )
            ], className = 'box2')

            ], className = 'divs'),
    

    html.Br(),

    html.Div( #Divisão dos gráficos de scrobbles e histograma
            children = [
    

        html.Div(      # Divisão do gráfico de scrobbles
                children = [

                    dcc.Graph(
                        id = 'scrobbles',
                        figure = gr.scrobbles()
                    )
                ],className = 'box1'),
    

        html.Div(   # Divisão do gráfico histograma
                children = [

                dcc.Graph(
                    id = 'histograma',
                    figure = gr.histograma(),
                )
                ],className = 'box2'),
    
            ], className = 'divs'),

    html.Br()

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