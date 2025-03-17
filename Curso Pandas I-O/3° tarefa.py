import pandas as pd 

url = r"pacientes.json"

dados_pacientes = pd.read_json(url)


url2 = r"pacientes_2.json"

dados_pacientes2 = pd.read_json(url)

print(dados_pacientes2)

dados_pacientes2.to_json('historico_pacientes_normalizado.json')