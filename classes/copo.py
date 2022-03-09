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
            print('Não se pode encher um copo sujo!')

    def beber(self, quantidade):
        if quantidade < 0:
            print('Quantidade deve ser positiva')
        elif quantidade > self.conteudo:
            print('Não há bebida suficiente no copo')
        else:
            self.conteudo -= quantidade
        

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True
        
    def __str__(self):
        if self.conteudo == 0:
            return f'Um copo vazio de {self.tamanho}mL.'
        else:
            return f'Um copo de {self.tamanho}mL contendo {self.conteudo}mL de {self.bebida}.'