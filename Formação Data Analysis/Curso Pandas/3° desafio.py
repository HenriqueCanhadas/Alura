import pandas as pd
import openpyxl

url = r"alunos.csv"  

dados_alunos = pd.read_csv(url, sep=",")

dados_alunos.isnull().sum()
df = dados_alunos.fillna(0)

print("1)", df.isnull())

alunos_a_remover = df.query('Nome == "Alice" & Nome == "Carlos"').index

print("2)", df)

aprovados = (df['Aprovado'] == True)

df1 = df[aprovados]

print("3)",df1)

print("4)",df1.to_csv("alunos_aprovados.csv"))