from Grafo import Grafo

# números de vértices presentes no grafo
vertices = int(input('Digite um número inteiro positivo para o vértice: '))

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
    decisao = int(input('\n1. Adicionar \n2. Mostrar lista de adjacência \n3. Mostrar matriz de adjacência \n0. Encerrar programa \n-> '))

    # se escolher adicionar uma aresta
    if decisao == 1:
        origem = int(input('\nDigite o valor do vértice de origem: '))
        destino = int(input('Digite o valor do vértice de destino: '))
        peso = input('Digite o valor do peso da aresta (opcional): ')

        if peso:
            peso = int(peso)
            grafo.adicionar(origem, destino, peso)

        else:
            grafo.adicionar(origem, destino)

        print('Adicionado com sucesso!')
        input('<ENTER>')

    # se o usuario quiser ver a lista
    elif decisao == 2:
        grafo.mostrarLista()
        input('<ENTER>')

    # se o usuario quiser ver a matriz
    elif decisao == 3:
        grafo.mostrarMatriz()
        input('<ENTER>')

    # se o usuario quiser encerrar o programa
    elif not decisao:
        break

print('\nFim do programa')