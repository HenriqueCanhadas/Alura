import pandas as pd

df = pd.read_csv("imigrantes_canada.csv")

df.set_index('País', inplace=True)

anos = list(map(str, range(1980, 2014)))

brasil = df.loc['Brasil', anos]

brasil_dict = {'ano':brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}

dados_brasil=pd.DataFrame(brasil_dict)

america_sul = df.query('Região=="América do Sul"')

import matplotlib.pyplot as plt

import plotly.express as px

fig = px.line(dados_brasil, x='ano', y='imigrantes',title='Imigração do Brasil de 1980 á 2013')
fig.update_traces(line_color='green', line_width=4)
fig.update_layout(width=1000, height=500, xaxis={'tickangle':-45},font_family='Arial',font_size=14,font_color='red',title_font_color='black',title_font_size=22, xaxis_title='Ano', yaxis_title="Numero de imigrantes")
fig.show()

df_america_sul_clean = america_sul.drop(['Continente', 'Região', 'Total'], axis=1)
america_sul_final = df_america_sul_clean.T

america_sul_final.head()

fig = px.line(america_sul_final, x=america_sul_final.index, y=america_sul_final.columns, color='País',
              title="Imigração dos países da America do Sul", markers=True)

fig.update_layout(
    xaxis={'tickangle':-45},
    xaxis_title='Anos',
    yaxis_title='Numero de imigrantes'
)

fig.show()

fig.write_html('imigracao_america_sul.html')