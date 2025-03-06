import pandas as pd

df = pd.read_csv("imigrantes_canada.csv")

#df.info()

df.set_index('País', inplace=True)

anos = list(map(str, range(1980, 2014)))

brasil = df.loc['Brasil', anos]
argentina = df.loc['Argentina', anos]

brasil_dict = {'ano':brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}
argentina_dict = {'ano':argentina.index.tolist(), 'imigrantes': argentina.values.tolist()}

dados_brasil=pd.DataFrame(brasil_dict)
dados_argentia=pd.DataFrame(argentina_dict)

import matplotlib.pyplot as plt

plt.style.use('dark_background')

'''
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3, marker='o', color='red')
ax.set_title('Imigração do Brasil para o Canada\n1980 a 2013', fontsize = 18, loc='left')
ax.set_xlabel('Ano', fontsize=14)
ax.set_ylabel('Número de Imigrantes', fontsize=14)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
plt.grid(linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.savefig('imigraçã_brasil_cana.png', transparent=True, dpi=300, bbox_inches='tight')
plt.show()
'''





america_sul = df.query('Região=="América do Sul"')

america_sul.head()

america_sul_sorted = america_sul.sort_values("Total", ascending=True)

#cores = ['royalblue', 'orange','forestgreen', 'orchid', 'purple', 'brown', 'slateblue', 'gray', 'olive', 'navy', 'teal', 'tomato']

cores = []

for pais in america_sul_sorted.index:
    if pais == 'Brasil':
        cores.append('green')
    else:
        cores.append('silver')

fig, ax = plt.subplots(figsize=(12,5))

ax.barh(america_sul_sorted.index, america_sul_sorted['Total'], color=cores)
ax.set_title('Brasil foi o 4° pais com mais imigrantes\npara o Canada no periodo de 1980 a 2013', loc="left")
ax.set_xlabel('Número de Imigrantes', fontsize=14)
ax.set_ylabel('')

ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

for i, v in enumerate(america_sul_sorted["Total"]):
    ax.text(v + 20, i, str(v), color='red', fontsize=10, ha='left', va='center')

ax.set_frame_on(False)
ax.get_xaxis().set_visible(False)
ax.tick_params(axis='both', which='both', length=0)
fig.savefig('imigraçã_brasil.png', transparent=False, dpi=300, bbox_inches='tight')
plt.show()
