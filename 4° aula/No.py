class No:
    def __init__(self, valor: int):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def getValor(self):
        return self.valor
    
    def getEsquerda(self):
        return self.esquerda
        
    def getDireita(self):
        return self.direita

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    def setDireita(self, direita):
        self.direita = direita