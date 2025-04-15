from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(this, nome, categoria):
        this._nome = nome.title( )
        this._categoria = categoria.upper()
        this._ativo = False
        this._avaliacao = []
        this._cardapio = []
        Restaurante.restaurantes.append(this)

    def __str__(this):
        return f"{this._nome} | {this._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property    
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        somas_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qunatidade_de_notas = len(self._avaliacao)
        media = round(somas_das_notas / qunatidade_de_notas, 1)
        return media
    
    #def adicionar_bebida_no_cardapio(self,bebida):
    #    self._cardapio.append(bebida)

    #def adicionar_prato_no_cardapio(self,prato):
    #    self._cardapio.append(prato)

    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardpaio do restaurante{self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
                if hasattr(item,'_descricao'):
                        mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}'
                        print(mensagem_prato)
                elif hasattr(item,'_tamanho'):
                        mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                        print(mensagem_bebida)


        












'''
restaurante_praca = Restaurante("praça", "gourmet")
'''
#restaurante_praca.nome = "Praça"
#restaurante_praca.categoria = "Gourmet"
#restaurante_praca.ativo = True
'''
restaurante_pizza = Restaurante("Pizza", "italiana")
restaurantes = [restaurante_pizza,restaurante_praca]
Restaurante.alternar_estado(restaurante_praca)
Restaurante.listar_restaurantes()
#print(dir(restaurante_praca))
#print(vars(restaurante_praca))
#print(restaurante_praca.ativo)
'''