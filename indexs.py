import pandas as pd

df = pd.read_csv('new_3.csv', usecols= ['paises', 'ouvintes', 'estilos'])

# estilos para colocar no dropdown
lista_estilos = df[['ouvintes']].groupby(df['estilos']).sum().sort_values(by = 'ouvintes', ascending = False).index
lista_estilos = lista_estilos[:500]

lista_estilos = lista_estilos.drop('outro')
lista_estilos = lista_estilos.drop('britpop')

for estilo in lista_estilos[80:]:
    df_est = df[df['estilos'] == estilo]
    df_i = df_est.paises.unique()

    if len(df_i) < 11:
        lista_estilos = lista_estilos.drop(estilo)
lista_estilos = sorted(lista_estilos)

# paises para colocar no dropdown
lista_paises = df[['ouvintes']].groupby(df['paises']).sum().sort_values(by = 'ouvintes', ascending = False).index

lista_paises = lista_paises.drop('outro')

for país in lista_paises:
    df_pa = df[df['paises'] == país]
    df_k = df_pa.estilos.unique()

    if len(df_k) < 11:
        lista_paises = lista_paises.drop(país)
lista_paises = sorted(lista_paises)