import pandas as pd

url = r"emissoes_CO2.xlsx"

dados_co2 = pd.read_excel(url)

pd.ExcelFile(url).sheet_names

percapita = pd.read_excel(url, sheet_name='emissoes_percapita')

fontes = pd.read_excel(url, sheet_name='fontes')

intervalo = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D')

intervalo_2 = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D',nrows=10)

percapita.to_excel('co2_percapita.xlsx', index=False)