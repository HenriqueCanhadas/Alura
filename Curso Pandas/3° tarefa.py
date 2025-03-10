import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

url = r"aluguel.csv"  

dados = pd.read_csv(url, sep=";")

#Fazer a media da coluna Valores
dados['Valor'].mean()

#Agrupar a media de valores com a coluna Tipo
dados.groupby("Tipo").mean(numeric_only=True)

#Agrupar a media em grupo tipo e calcular apenas a coluna Valor
dados.groupby("Tipo")["Valor"].mean(numeric_only=True)

#ordenar um novo df ordenado
dados.groupby("Tipo")[["Valor"]].mean(numeric_only=True).sort_values("Valor")

#Criar um DF ja com os valores separados e ordenados
df_preco_tipo = dados.groupby("Tipo")[["Valor"]].mean(numeric_only=True).sort_values("Valor")
#Criar grafico com matplotlib
#df_preco_tipo.plot(kind='barh', figsize=(14, 10), color='purple')

#lista com todos os valores unicos da coluna Tipo
dados.Tipo.unique()

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
dados.query('@imoveis_comerciais in Tipo')

#Consultar apenas os valores opostos da lista
dados.query('@imoveis_comerciais not in Tipo')

#Criar um DF ja com os valores separados em apenas valores que nao serem imoveis comerciais
df = dados.query('@imoveis_comerciais not in Tipo')

df_imoveis_residencial = df.groupby("Tipo")[["Valor"]].mean(numeric_only=True).sort_values("Valor")
#Criar grafico com matplotlib
#df_imoveis_residencial.plot(kind='barh', figsize=(14, 10), color='purple')

#Contar quantos valores tem em cada item da coluna Tipo
df.Tipo.value_counts()

#Fazzer a % de cada valor da coluna Tipo
df.Tipo.value_counts(normalize=True)

#Fazer um frame
df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')

df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')
df_percentual_tipo.plot(kind='bar', figsize=(7, 4), color='green', xlabel="Tipos", ylabel="Percentual")

df.query('Tipo == "Apartamento"')

df_apartamento = df.query('Tipo == "Apartamento"')

df_apartamento.isnull().sum()

df = df_apartamento.fillna(0)

df.isnull().sum()

registro_a_remover = df.query('Valor == 0| Condominio == 0').index

df.drop(registro_a_remover, axis=0, inplace=True)

df.Tipo.unique()

df.drop("Tipo", axis=1, inplace=True)

selecao1 = df['Quartos'] == 1
selecao2 = df['Valor'] < 1200

selecao_final = (selecao1) & (selecao2)

df1 = df[selecao_final]

selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)

df2 = df[selecao]

df_index = df.set_index('Bairro')

#df_index.to_excel('dados_apartamentos.xlsx')

#pd.read_excel('dados_apartamentos.xlsx')

#df.to_excel('dados_apartamentos_index.xlsx', index=False,)

#pd.read_excel('dados_apartamentos_index.xlsx')


dados["Valor_por_mes"] = dados['Valor'] + dados['Condominio']
dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados["IPTU"]

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                                        dados['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'

dados['Possui_suite'] = dados["Suites"].apply(lambda x:' Sim' if x>0 else "Não")

print(dados.head())