import pandas as pd


url= r"superstore_data.csv"
dados_mercado =pd.read_csv(url, delimiter=',')
dados_mercado.head()

url2 = r'superstore_data_ponto_virgula.csv'
dados_ponto_virgula = pd.read_csv(url2, sep=';')
dados_ponto_virgula.head()

dados_primeiras_linhas = pd.read_csv(url,nrows=5)
dados_primeiras_linhas

dados_coluna_selecao = pd.read_csv(url, usecols=['Id','Year_Birth','Income'])
dados_coluna_selecao

dados_selecao = pd.read_csv(url, usecols=[0,1,4])
dados_selecao

dados_selecao.to_csv('clientes_mercado.csv')
clientes_mercado = pd.read_csv(r"clientes_mercado.csv")
print(clientes_mercado)

dados_selecao.to_csv('dados_mercado.csv', index=False)
print(pd.read_csv(r"dados_mercado.csv"))
