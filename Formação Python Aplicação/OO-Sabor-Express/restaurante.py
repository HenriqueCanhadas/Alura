class Restaurante:
    restaurantes = []

    def __init__(this, nome, categoria):
        this.nome = nome
        this.categoria = categoria
        this.ativo = False
        Restaurante.restaurantes.append(this)

    def __str__(this):
        return f"{this.nome} | {this.categoria}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante("Praça", "Gourmet")
'''
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet"
restaurante_praca.ativo = True
'''
restaurante_pizza = Restaurante("Pizza", "italiana")

restaurantes = [restaurante_pizza,restaurante_praca]

Restaurante.listar_restaurantes()

#print(dir(restaurante_praca))
#print(vars(restaurante_praca))
#print(restaurante_praca.ativo)