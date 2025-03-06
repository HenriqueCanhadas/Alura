import pandas as pd
import matplotlib.pyplot as plt

url = r"aluguel.csv"  

dados = pd.read_csv(url, sep=";")

print(dados.head())

#Fazer a media da coluna Valores
print(dados['Valor'].mean())

#Agrupar a media de valores com a coluna Tipo
print(dados.groupby("Tipo").mean(numeric_only=True))

#Agrupar a media em grupo tipo e calcular apenas a coluna Valor
print(dados.groupby("Tipo")["Valor"].mean(numeric_only=True))

#ordenar um novo df ordenado
print(dados.groupby("Tipo")[["Valor"]].mean(numeric_only=True).sort_values("Valor"))

#Criar um DF ja com os valores separados e ordenados
df_preco_tipo = dados.groupby("Tipo")[["Valor"]].mean(numeric_only=True).sort_values("Valor")
#Criar grafico com matplotlib
#df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')

#lista com todos os valores unicos da coluna Tipo
print(dados.Tipo.unique())

imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro',
                      'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial',
                      'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem',
                      'Chácara',
                      'Loteamento/Condomínio',
                      'Sítio',
                      'Pousada/Chalé',
                      'Hotel',
                      'Indústria'
]

#Consultar apenas os valores pasados pela lista
print(dados.query('@imoveis_comerciais in Tipo'))

#Consultar apenas os valores opostos da lista
print(dados.query('@imoveis_comerciais not in Tipo'))

#Criar um DF ja com os valores separados em apenas valores que nao serem imoveis comerciais
df = dados.query('@imoveis_comerciais not in Tipo')

print(df.head())
print(df.Tipo.unique())

df_imoveis_residencial = df.groupby("Tipo")[["Valor"]].mean(numeric_only=True).sort_values("Valor")
#Criar grafico com matplotlib
#df_imoveis_residencial.plot(kind='barh', figsize=(14, 10), color='purple')

#Contar quantos valores tem em cada item da coluna Tipo
print(df.Tipo.value_counts())

#Fazzer a % de cada valor da coluna Tipo
print(df.Tipo.value_counts(normalize=True))

#Fazer um frame
print(df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion'))

df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')
df_percentual_tipo.plot(kind='bar', figsize=(7, 4), color='green', xlabel="Tipos", ylabel="Percentual")

print(df.query('Tipo == "Apartamento"'))

df_apartamento = df.query('Tipo == "Apartamento"')

print(df_apartamento.head())