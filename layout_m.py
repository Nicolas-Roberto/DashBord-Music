import plotly.graph_objects as go
def layout_gps(title, yaxis_t, xaxis_t= ''):
    layout = go.Layout(
        yaxis_tickformat = '%', # COLOCA OS VALORES NO GRÁFICO EM PORCENTAGEM
        title_x = 0.5, # CENTRALIZA O T´ÍTULO DO GRÁFICO
        title = '<b>' + title,
        titlefont = {'family' : 'Courier New',
                        'color' : '#c8d4d3'}, # MUDA A COR, FONTE E TAMANHO DO TÍTULO
        yaxis = {'color' : '#c8d4d3',
                    'title' : '<b>' + yaxis_t,
                    'titlefont' : {'family' : 'Courier New',
                                }}, # DETERMINA O NOME DO EIXO Y, MUDA SUA COR E TAMANHO
        xaxis = {'color' : '#c8d4d3',
                'title' : '<b>' + xaxis_t,
                'titlefont' : {'family' : 'Courier New',
                               }}, # DETERMINA O NOME DO EIXO Y, MUDA SUA COR E TAMANHO
        plot_bgcolor = '#252e3f',
        paper_bgcolor = '#252e3f')
    return layout

def layout_mc(title):
    layout = go.Layout(
        title = '<b>' + title, # MUDA O TÍTULO DO GRÁFICO
        title_x = 0.5, # CENTRALIZA O TÍTULO
        titlefont = {'family': 'Courier New',
                    'size': 24,
                    'color' : '#c8d4d3'}, # MUDA A COR, FONTE E TAMANHO DO TÍTULO
        paper_bgcolor = '#252e3f', # MUDA A COR DO QUE ESTÁ EM VOLTA DO GRÁFICO
        height = 800,
        geo =  {
                'showcountries': True, # MOSTRA AS FRONTEIRAS DO MAPA
                'showocean' : True, # MOSTRA A COR DETERMINADA PARA OS OCEANOS
                'landcolor': '#c8d4d3', # COR DETERMINADA PARA OS CONTINENTES
                'oceancolor' : '#252e3f', # COR DETERMINADA PARA OS OCEANOS
                'showlakes' : False, # MOSTRA OS LAGOS NO MAPA (NO CASO, DETERMINADO PARA NÃO MOSTRAR)
                'countrycolor' : 'rgb(161, 161, 161)', # COR DETERMINADA PARA AS FRONTEIRAS
                'bgcolor' : '#252e3f' # COR DETERMINADA PARA O FUNDO DO MAPA
                })
    return layout



