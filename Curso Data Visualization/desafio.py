import pandas as pd
import matplotlib.pyplot as plt

lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

df = pd.DataFrame(vendas_2022, index=lojas)

print(df)

fig, axs = plt.subplots(2,2, figsize=(14,8))
fig.subplots_adjust(hspace=0.3, wspace=0.4)
fig.suptitle('Imigração dos 4 maiores paises da america do sul para o Canada')

axs[0, 0].plot(df.loc['A'])
axs[0, 0].set_title('Loja A')

axs[0, 1].plot(df.loc['B'])
axs[0, 1].set_title('Loja B')

axs[1, 0].plot(df.loc['C'])
axs[1, 0].set_title('Loja C')

axs[1, 1].plot(df.loc['D'])
axs[1, 1].set_title('Loja D')

for ax in axs.flat:
    ax.set_xlabel('Mês')
    ax.set_ylabel('Número de vendas')

plt.show()