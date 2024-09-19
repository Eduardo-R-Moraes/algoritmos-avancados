from grafoBusca import Grafo
from random import randint

# números de vértices presentes no grafo
vertices = int(input('Digite um número inteiro positivo para o vértice: '))

# cria grafo não direcionado
grafo = Grafo(vertices)

# gera o grafo de forma aleatória
grafo.gerarGrafo()

while True:
    # escolhe a ação a fazer com o grafo
    decisao = int(input('\n1. Mostrar lista de adjacência \n2. Busca em largura \n3. Busca em profundidade \n0. Encerrar programa \n-> '))

    # se o usuario quiser ver a lista
    if decisao == 1:
        grafo.mostrar()
        input('\n<ENTER>')

    # se o usuario quiser fazer busca em largura
    elif decisao == 2:
        vertice = int(input('Digite o vértice inicial: '))
        print('\n', grafo.getBuscaLargura(vertice))
        input('\n<ENTER>')

    # se o usuario quiser fazer busca em profundidade
    elif decisao == 3:
        vertice = int(input('Digite o vértice inicial: '))
        print('\n', grafo.getBuscaProfundidade(vertice))

        input('\n<ENTER>')

    # se o usuario quiser encerrar o programa
    elif not decisao:
        break

print('\nFim do programa')