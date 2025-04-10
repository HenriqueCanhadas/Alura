import pandas as pd

dados = r'1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

emissoes_gases = pd.read_excel(dados, sheet_name="GEE Estados")

emissoes_gases["Emissão / Remoção / Bunker"].unique()

(emissoes_gases["Emissão / Remoção / Bunker"] == 'Remoção NCI') | (emissoes_gases["Emissão / Remoção / Bunker"] == 'Remoção')

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max() 

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()

emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']

emissoes_gases = emissoes_gases.drop(columns= 'Emissão / Remoção / Bunker')

emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns 

colunas_info =list(emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns)

emissoes_gases.loc[:,1970:2021].columns

colunas_emissao = list(emissoes_gases.loc[:,1970:2021].columns)
 
emissoes_por_ano = emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano' , value_name = 'Emissão')
 
emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')

emissoes_por_ano.groupby('Gás').sum(numeric_only = True)

emissoes_por_ano.groupby('Gás')[['Emissão']].sum()

emissao_por_gas = emissoes_por_ano.groupby('Gás')[['Emissão']].sum().sort_values('Emissão', ascending = False)

import matplotlib.pyplot as plt

emissao_por_gas.plot(kind = 'barh', figsize = (10,6))

emissao_por_gas.iloc[0:9]

print(f'A emissão de CO2 corresponde a {float((emissao_por_gas.iloc[0:9].sum()/emissao_por_gas.sum()).iloc[0])*100:.2f} % de emissão total de gases estufa no Brasil de 1970 a 2021.')

gas_por_setor = emissoes_por_ano.groupby(['Gás', 'Nível 1 - Setor'])[['Emissão']].sum()

gas_por_setor.xs('CO2 (t)', level=0)

gas_por_setor.xs(('CO2 (t)', 'Mudança de Uso da Terra e Floresta'), level= [0,1])

gas_por_setor.xs('CO2 (t)', level=0).max()

gas_por_setor.xs('CO2 (t)', level=0).idxmax()

gas_por_setor.groupby(level=0).idxmax()

valores_max = gas_por_setor.groupby(level=0).max().values

tabela_sumarizada = gas_por_setor.groupby(level = 0).idxmax()
tabela_sumarizada.insert(1, 'Quantidade de emissão',valores_max)

gas_por_setor.swaplevel(0, 1).groupby(level = 0).idxmax()

emissoes_por_ano.groupby('Ano')[["Emissão"]].mean().plot(figsize=(10,6));

emissoes_por_ano.groupby('Ano')[["Emissão"]].mean().idxmax()

emissoes_por_ano.groupby(['Ano', 'Gás'])[['Emissão']].mean()

media_emissão_anual = emissoes_por_ano.groupby(['Ano', 'Gás'])[['Emissão']].mean().reset_index()

media_emissão_anual = media_emissão_anual.pivot_table(index='Ano', columns='Gás', values='Emissão')

media_emissão_anual.plot(subplots=True, figsize=(10,40))

dados_ibge = r'POP2022_Municipios.xls'

populacao_estados = pd.read_excel(dados_ibge, header=1, skipfooter=34)

populacao_estados.groupby('UF').sum(numeric_only = True)

populacao_estados = populacao_estados[populacao_estados['POPULAÇÃO'].str.contains('\(', na = False)]

populacao_estados = populacao_estados.assign(populacao_sem_parenteses = populacao_estados['POPULAÇÃO'].replace('\(\d{1,2}\)', '', regex = True),
                                             populacao = lambda x : x.loc[:, 'populacao_sem_parenteses'].replace('\.', '', regex = True))

populacao_estados[populacao_estados['POPULAÇÃO'].str.contains('\(', na = False)]

populacao_estados = populacao_estados.astype({'populacao':'int64'})

populacao_estados = populacao_estados.groupby('UF')[['populacao']].sum().reset_index()

emissao_estados = emissoes_por_ano[emissoes_por_ano['Ano'] == 2021].groupby('Estado')[['Emissão']].sum().reset_index()

dados_agrupados = pd.merge(emissao_estados, populacao_estados, left_on='Estado', right_on="UF")
print(dados_agrupados)

dados_agrupados.plot(x='populacao',y='Emissão', kind='scatter',figsize=(8,6));

import plotly.express as px

fig = px.scatter(data_frame=dados_agrupados,x='populacao',y='Emissão', text='Estado', opacity=0)

dados_agrupados = dados_agrupados.assign(emissao_per_capita = dados_agrupados['Emissão']/dados_agrupados['populacao']).sort_values('emissao_per_capita', ascending = False)
print(dados_agrupados)

px.scatter(data_frame = dados_agrupados, x = 'populacao', y = 'Emissão', text = 'Estado', size = 'emissao_per_capita')
