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

print(media_emissão_anual)

media_emissão_anual.plot(subplots=True, figsize=(10,40))

plt.show()