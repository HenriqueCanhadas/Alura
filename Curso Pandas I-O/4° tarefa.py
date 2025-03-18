import pandas as pd

dados_html = pd.read_html(r"filmes_wikipedia.html") 

type(dados_html)
len(dados_html)

top_filmes = dados_html[1]

top_filmes.to_html('top_filmes.html')
top_filmes.to_csv('top_filmes_1998.csv', index=False)

dados_imdb = pd.read_xml(r"imdb_top_1000.xml")

print(dados_imdb.head(5))

dados_imdb.to_xml('filmes_imdb.xml')