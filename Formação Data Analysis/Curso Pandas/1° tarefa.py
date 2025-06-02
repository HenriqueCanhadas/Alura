import pandas as pd

url = r"aluguel.csv"  

dados = pd.read_csv(url, sep=";")

#print(dados.head())
#print(type(dados))
#print(dados.shape)
#print(dados.columns)
#print(dados.info())

print(dados['Tipo'])
print(dados[['Quartos','Valor']])
