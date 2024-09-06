from No import No

class ArvoreBusca:
    def __init__(self): 
        self.raiz = None

    def getRaiz(self):
        return self.raiz

    def setRaiz(self, raiz: No):
        self.raiz = raiz 

    def insere(self, valor: int):
        no = No(valor)
        if self.raiz == None:
            return self.setRaiz(no)
        
        no_pai = None
        no_atual = self.raiz
        while no_atual != None:
            no_pai = no_atual
            if no.getValor() < no_atual.getValor():
                no_atual = no_atual.getEsquerda()
            else:
                no_atual = no_atual.getDireita() 

        if no.getValor() < no_pai.getValor():
            no_pai.setEsquerda(no)
        else:
            no_pai.setDireita(no)

    def mostraCrescente(self, no_atual: No):
        if no_atual != None:
            self.mostraCrescente(no_atual.getEsquerda())
            print(f'{no_atual.getValor()}', end=' ')
            self.mostraCrescente(no_atual.getDireita())

    def mostraDecrescente(self, no_atual: No):
        if no_atual != None:
            self.mostraDecrescente(no_atual.getDireita())
            print(f'{no_atual.getValor()}', end=' ')
            self.mostraDecrescente(no_atual.getEsquerda())