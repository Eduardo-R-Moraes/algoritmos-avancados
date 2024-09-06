from tratamento_erros import pegar_vertice, pegar_origem, pegar_destino, pegar_peso
from Grafo import Grafo

# números de vértices presentes no grafo
vertices = pegar_vertice()

# define se o grafo é direcionado ou não
direcionado = input('\nÉ direcionado (sim ou nao): ')

# repete até receber a resposta 'sim' ou 'não'
while direcionado == '' or direcionado != 'sim' and direcionado != 'nao':
    direcionado = input('\nÉ direcionado (sim ou nao): ')

# se for direcionado
if direcionado.lower() == 'sim':
    grafo = Grafo(vertices, True)

# se não for direcionado
if direcionado.lower() == 'nao':
    grafo = Grafo(vertices)

while True:
    # escolhe a ação a fazer com o grafo
    decisao = int(input('\n1. Adicionar \n2. Mostrar matriz \n0. Encerrar programa \n-> '))

    # se escolher adicionar uma aresta
    if decisao == 1:
        origem = pegar_origem()
        destino = pegar_destino()
        peso = pegar_peso()

        if peso:
            grafo.adicionar(origem, destino, peso)

        else:
            grafo.adicionar(origem, destino)

        print('Adicionado com sucesso!\n')

    # se o usuario quiser ver a lista
    elif decisao == 2:
        grafo.mostrar()

    # se o usuario quiser encerrar o programa
    elif not decisao:
        break

print('\nFim do programa')