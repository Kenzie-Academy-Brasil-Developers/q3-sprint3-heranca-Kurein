# -*- coding: utf-8 -*-

from classes.recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho, conteudo = 0, limpo = True):
        super().__init__(tamanho, conteudo, limpo)

    def encher(self, bebida = 'água'):
        if self.esta_limpo():
            self.sujar()
            self.conteudo = self.tamanho
            self.bebida = bebida
        else:
            return 'Não se pode encher um copo sujo'

    def beber(self, quantidade):
        if quantidade < 0:
            return 'Quantidade deve ser positiva'
        elif quantidade > self.conteudo:
            return 'Não há bebida suficiente no copo'
        else:
            self.conteudo -= quantidade
        

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True
        
    def __repr__(self):
        if self.conteudo == 0:
            return f'Um copo vazio de {self.tamanho:.1f}ml'
        else:
            return f'Um copo de {self.tamanho:.1f}ml contendo {self.conteudo:.1f}ml de {self.bebida}'