import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import graficos as gr

style_L = {'font-family' : 'Dank Mono',
            'font-size' : '150%'}

app = dash.Dash(__name__) 

app.layout = html.Div(style = {'backgroundColor' : '#1f2630',
                                'color' :  '#7fafdf',
                                },
                      children = [
    html.H1(children = 'Trabalho Final APC - Grupo 4',

    ),
    
    html.Div(style = {'backgroundColor' : '#252e3f'},
            children = [
                html.Label(style = style_L,
                    children = '''
                    Maps: Most Relevant Artist by Country & Numbers of Scrobbles Heat Map
                    ''',
                ),

                dcc.Graph(
                    id = 'grafico'
                ),
                html.P(style = {'font-family' : 'Dank Mono',
                                'font-size' : '125%' },
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
                            'color' : '#c8d4d3'}
                )

            ], className = 'box1'),


    html.Br(),

    html.Div(
             style = {'backgroundColor' : '#252e3f'
                      },
             children = [
                html.Label(style = style_L,
                children = '''
                        Bar Graph: Numbers of Scrobbles per Country'''
                ),

                dcc.Graph(
                    id = 'scrobbles',
                    figure = gr.scrobbles()
                )
             ], className = 'box2')
])
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

if __name__ == '__main__':
    app.run_server(debug = True)