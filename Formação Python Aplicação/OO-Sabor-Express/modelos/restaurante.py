from modelos.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(this, nome, categoria):
        this._nome = nome.title( )
        this._categoria = categoria.upper()
        this._ativo = False
        this._avaliacao = []
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