import pandas as pd

url = r"alunos.csv"  

#1)
dados_alunos = pd.read_csv(url, sep=";")

print("2)",dados_alunos.head(7),"\n",dados_alunos.tail())
print("3)",dados_alunos.shape)
print("4)",dados_alunos.columns,"\n",dados_alunos.info())
print("extra)",dados_alunos.describe())

#print(type(dados))
#print(dados.shape)
#print(dados.columns)
#print(dados.info())

#print(dados['Tipo'])
#print(dados[['Quartos','Valor']])
