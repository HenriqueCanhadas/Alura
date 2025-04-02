import pandas as pd

dados = r'dataset-telecon.json'

dados_churn = pd.read_json(dados)

pd.json_normalize(dados_churn['conta']).head()

import json

with open(dados) as f:
    json_bruto = json.load(f)

dados_normalizados = pd.json_normalize(json_bruto)

#dados_normalizados['conta.cobranca.Total'] = dados_normalizados['conta.cobranca.Total'].astype('float64')

dados_normalizados[dados_normalizados['conta.cobranca.Total'] == ' '][['cliente.tempo_servico','conta.contrato','conta.cobranca.mensal','conta.cobranca.Total']]

idx = dados_normalizados[dados_normalizados['conta.cobranca.Total'] == ' '].index

dados_normalizados.loc[idx, 'conta.cobranca.Total'] = dados_normalizados.loc[idx, 'conta.cobranca.mensal'] * 24

dados_normalizados.loc[idx, 'cliente.tempo_servico'] = 24

print(dados_normalizados.loc[idx][['cliente.tempo_servico','conta.contrato','conta.cobranca.mensal','conta.cobranca.Total']])

dados_normalizados['conta.cobranca.Total'] = dados_normalizados['conta.cobranca.Total'].astype('float64')

for col in dados_normalizados.columns:
    print(f"Coluna: {col}")
    print(dados_normalizados[col].unique())
    print("-" * 30)


dados_normalizados.query("Churn == ''")
      
dados_normalizados[dados_normalizados['Churn'] != '']

dados_sem_vazio = dados_normalizados[dados_normalizados['Churn'] != ''].copy()

dados_sem_vazio.reset_index(drop=True, inplace=True)

dados_sem_vazio.duplicated().sum()

filtro_duplicadas = dados_sem_vazio.duplicated()

dados_sem_vazio.drop_duplicates(inplace=True)

dados_sem_vazio.duplicated().sum()

dados_sem_vazio.isna().sum().sum()

dados_sem_vazio[dados_sem_vazio.isna().any(axis=1)]

filtro = dados_sem_vazio['cliente.tempo_servico'].isna()

dados_sem_vazio[filtro][['cliente.tempo_servico','conta.cobranca.mensal','conta.cobranca.Total']]

import numpy as np

dados_sem_vazio['cliente.tempo_servico'].fillna(
    np.ceil(
        dados_sem_vazio['conta.cobranca.Total'] / dados_sem_vazio['conta.cobranca.mensal']
    ),inplace=True
)

print(dados_sem_vazio[filtro][['cliente.tempo_servico','conta.cobranca.mensal','conta.cobranca.Total']])