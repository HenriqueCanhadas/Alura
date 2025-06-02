import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("imigrantes_canada.csv")
df.set_index('País', inplace=True)

top_10 = df.sort_values("Total", ascending=False).head(10)

"""
#sns.barplot(data=top_10, x=top_10.index, y="Total")
sns.barplot(data=top_10, y=top_10.index, x="Total", orient='h')

ax = sns.barplot(data=top_10, y=top_10.index, x="Total", orient='h')
ax.set(title='Países com maior imigração para o Canadá\n 1980 a 2013',
       xlabel='Numero de imigrantes',
       ylabel='')
"""

'''
fig, ax = plt.subplots(figsize=(8,4))
ax = sns.barplot(data=top_10, y=top_10.index, x="Total", orient='h')
ax.set_title('Países com maior imigração para o Canadá\n1980 a 2013', loc="left", fontsize=16)
ax.set_xlabel("Número de imigrantes", fontsize=14)
ax.set_ylabel("")
plt.show()
'''

def gerar_grafico_paleta(palette):
    fig, ax = plt.subplots(figsize=(10,6))
    ax = sns.barplot(data=top_10, y=top_10.index, x="Total", orient='h', palette=palette)
    ax.set_title('Países com maior imigração para o Canadá\n1980 a 2013', loc="left", fontsize=16)
    ax.set_xlabel("Número de imigrantes", fontsize=14)
    ax.set_ylabel("")
    sns.despine()
    plt.show()

sns.set_theme(style='ticks')

gerar_grafico_paleta('tab10')
