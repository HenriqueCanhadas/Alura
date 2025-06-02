import pandas as pd

dados_hospedagem =r'dados_hospedagem.json'

dados = pd.read_json(dados_hospedagem)

dados_normalizados = pd.json_normalize(dados['info_moveis'])

colunas = list(dados_normalizados.columns)

dados = dados_normalizados.explode(colunas[3:])

dados.reset_index(inplace=True, drop=True)

import numpy as np

dados['max_hospedes'] = dados['max_hospedes'].astype(np.int64)

col_numericas = ['quantidade_banheiros','quantidade_quartos','quantidade_camas']

dados[col_numericas] = dados[col_numericas].astype(np.int64)

dados['avaliacao_geral'] = dados['avaliacao_geral'].astype(np.float64)

dados['preco'] = dados['preco'].apply(lambda x: x.replace('$','').replace(',','').strip())

dados['preco'] = dados['preco'].astype(np.float64)

dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].applymap(lambda x: x.replace('$', '').replace(',','').strip())

dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']]

dados['descricao_local'] = dados['descricao_local'].str.lower()

dados['descricao_local'] = dados['descricao_local'].str.replace(r'[^a-zA-Z0-9\-\' ]', ' ', regex=True)

dados['descricao_local'] = dados['descricao_local'].str.replace(r'(?<!\w)-(?!\w)', ' ', regex=True)

dados['descricao_local'] = dados['descricao_local'].str.split()

dados['comodidades'] = dados['comodidades'].str.replace('\{|}|\"','',regex=True)

dados['comodidades'] = dados['comodidades'].str.split(',')

dt_data = pd.read_json(r'moveis_disponiveis.json')

dt_data['data'] = pd.to_datetime(dt_data['data'])

dt_data['data'].dt.strftime('%Y-%m')

subset = dt_data.groupby(dt_data['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum()
print(subset)