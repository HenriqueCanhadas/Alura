import pandas as pd
import matplotlib.pyplot as plt

url = r"aluguel.csv"  

dados = pd.read_csv(url, sep=";")

#Criar um DF ja com os valores separados e ordenados
df_preco_tipo = dados.groupby("Tipo")[["Valor"]].mean(numeric_only=True).sort_values("Valor")
#Criar grafico com matplotlib
#df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')

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

#Criar um DF ja com os valores separados em apenas valores que nao serem imoveis comerciais
df = dados.query('@imoveis_comerciais not in Tipo')

df_imoveis_residencial = df.groupby("Tipo")[["Valor"]].mean(numeric_only=True).sort_values("Valor")
#Criar grafico com matplotlib
#df_imoveis_residencial.plot(kind='barh', figsize=(14, 10), color='purple')

df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')
#df_percentual_tipo.plot(kind='bar', figsize=(7, 4), color='green', xlabel="Tipos", ylabel="Percentual")

df_apartamento = df.query('Tipo == "Apartamento"')

print("1)",df_apartamento["Quartos"].mean())
print("2)",dados.Bairro.nunique())

df_bairro_alugel = dados.groupby("Bairro")[["Valor"]].mean(numeric_only=True).sort_values("Valor", ascending=False).head(5)

print("3)",df_bairro_alugel)
print("4)")
df_bairro_alugel.plot(kind='barh', figsize=(10, 8), color='green')
plt.show()