from ArvoreBusca import ArvoreBusca

t = ArvoreBusca()

t.insere(8)
t.insere(3)
t.insere(6)
t.insere(10)
t.insere(14)
t.insere(1)
t.insere(7)
t.insere(13)
t.insere(4)

t.mostraCrescente(t.getRaiz())
print()
t.mostraDecrescente(t.getRaiz())
print()