from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("bk", 'hamburger')
bebida_suco = Bebida("Suco de Maracuja", 5.0, "Medio")
bebida_suco.aplicar_desconto()
prato_pao = Prato("Paozinho", 2.0, "ta quentinho")
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()