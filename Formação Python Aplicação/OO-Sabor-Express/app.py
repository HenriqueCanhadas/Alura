from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("bk", 'hamburger')
restaurante_mexicano = Restaurante('Mexicanfood', "mexicana")
restaurante_mac = Restaurante("mcdonalds", "lanche")

restaurante_mac.alternar_estado()

restaurante_praca.receber_avaliacao("Henrique", 10)
restaurante_praca.receber_avaliacao("William", 8)
restaurante_praca.receber_avaliacao("Pele", 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()