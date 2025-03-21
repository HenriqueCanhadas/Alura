import pandas as pd

dados = r'1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

emissoes_gases = pd.read_excel(dados, sheet_name="GEE Estados")

emissoes_gases["Emissão / Remoção / Bunker"].unique()

(emissoes_gases["Emissão / Remoção / Bunker"] == 'Remoção NCI') | (emissoes_gases["Emissão / Remoção / Bunker"] == 'Remoção')

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max() 

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()

emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']

emissoes_gases = emissoes_gases.drop(columns= 'Emissão / Remoção / Bunker')

print(emissoes_gases)

'''

emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns 

colunas_info =list(emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns)

emissoes_gases.loc[:,1970:2021].columns

colunas_emissão = list(emissoes_gases.loc[:,1970:2021].columns)

emissoes_por_ano = emissoes_gases.melt(id_vars = colunas_info, value_vars = colunas_emissão, var_name = 'Ano', value_name = 'Emissão')

emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')

emissoes_por_ano.groupby('Gás').sum(numeric_only = True)

emissoes_por_ano.groupby('Gás')[['Emissão']].sum()

emissao_por_gas = emissoes_por_ano.groupby('Gás')[['Emissão']].sum().sort_values('Emissão', ascending = False)


emissao_por_gas.plot(kind = 'barh', figsize = (10,6));

emissao_por_gas.iloc[0:9]'
'''