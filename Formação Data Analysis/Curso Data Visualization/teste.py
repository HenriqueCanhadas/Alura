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

'''
#####PLOTAGEM#############
plt.figure(figsize=(10,5))
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'],label= 'Brasil')
plt.plot(dados_argentia['ano'], dados_argentia['imigrantes'],label= 'Argentina')
plt.title('Imigração do Brasil para o Canada')
plt.xlabel('Ano')
plt.ylabel('Número de Imigrantes')
plt.xticks(['1980','1985','1990','1995','2000','2005','2010'])
plt.yticks([500,1000,1500,2000,2500,3000])
plt.legend()
plt.show()
'''
'''
###########FIGURA###############
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'],label= 'Brasil')
ax.set_title('Imigração do Brasil para o Canada\n1980 a 2013')
ax.set_xlabel('Ano')
ax.set_ylabel('Número de Imigrantes')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.legend()
plt.show()
'''
'''
########## BOXPLOTS ##############
fig, axs = plt.subplots(1,2, figsize=(15,5))

axs[0].plot(dados_brasil['ano'], dados_brasil['imigrantes'])
axs[0].set_title('Imigração do Brasil para o Canada\n1980 a 2013')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Número de Imigrantes')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid()

axs[1].boxplot(dados_brasil['imigrantes'])
axs[1].set_title('Boxplot da Imigração do Brasil para o Canada\n1980 a 2013')
axs[1].set_xlabel('Brasil')
axs[1].set_ylabel('Número de Imigrantes')
axs[1].grid()

plt.show()

print(dados_brasil.describe())
'''

fig, axs = plt.subplots(2,2, figsize=(10,6))
fig.subplots_adjust(hspace=0.5, wspace=0.3)
fig.suptitle('Imigração dos 4 maiores paises da america do sul para o Canada')

axs[0, 0].plot(df.loc['Brasil', anos])
axs[0, 0].set_title('Brasil')

axs[0, 1].plot(df.loc['Colômbia', anos])
axs[0, 1].set_title('Colômbia')

axs[1, 0].plot(df.loc['Argentina', anos])
axs[1, 0].set_title('Argentina')

axs[1, 1].plot(df.loc['Peru', anos])
axs[1, 1].set_title('Peru')

for ax in axs.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.set_xlabel('Ano')
    ax.set_ylabel('Número de Imigrantes')
    ax.grid()

ymin = 0
ymax = 7000

for ax in axs.ravel():
    ax.set_ylim(ymin, ymax)

plt.show()
