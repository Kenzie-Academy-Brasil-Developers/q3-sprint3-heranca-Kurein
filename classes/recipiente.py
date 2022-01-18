class Recipiente:
    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True):
        self.tamanho = tamanho
        self.conteudo = conteudo
        self.limpo = limpo

    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        else:
            return False

    def lavar(self):
        self.conteudo = 0
        self.limpo = True
    
    def esta_limpo(self):
        return self.limpo

    def estado(self):
        if self.limpo:
            return 'limpo'
        else:
            return 'sujo'
    
    def sujar(self):
        self.limpo = False

    def __str__(self):
        return f'O recipiente esta {self.estado()}'