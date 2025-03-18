import sqlalchemy

from sqlalchemy import create_engine, MetaData, table, inspect, text

engine = create_engine('sqlite:///:memory:')

url = (r'clientes_banco.csv')

import pandas as pd

dados = pd.read_csv(url)

dados.to_sql('clientes', engine, index=False)

inspector = inspect(engine)

query = 'SELECT * FROM clientes WHERE Categoria_de_renda="Empregado"'

empregados = pd.read_sql(query, engine)

empregados.to_sql('empregados', con=engine, index=False)

pd.read_sql_table('empregados', engine)

pd.read_sql_table('empregados', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual'])

query = 'SELECT * FROM clientes'

pd.read_sql(query, engine)

query = 'DELETE FROM clientes WHERE ID_Cliente=5008804'
with engine.connect() as conn:
    conn.execute(text(query))
    conn.commit()

print(pd.read_sql_table('clientes', engine))

query = 'UPDATE clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808'
with engine.connect() as conn:
    conn.execute(text(query))
    conn.commit()

print(pd.read_sql_table('clientes', engine))