def adicionar(arvore, inicial, final, peso):
    arvore[inicial].append([final, peso])

def verticeAdj(grafo, vertice):
    vertices = []
    for i in range(1, len(grafo[vertice])):
        vertices.append(grafo[vertice][i])
        
    return vertices

grafo = [
    [[0,-1],[1,-1],[3,-1]],
    [[1,-1],[3,-1],[4,-1]],
    [[2,-1],[0,-1],[5,-1]],
    [[3,-1],[2,-1],[4,-1],[5,-1],[6,-1]],
    [[4,-1],[6,-1]],
    [[5,-1]],
    [[6,-1],[5,-1]]
]

# vertice sem pesos
def menorCaminho(grafo, inicial):
    # define a distancia de todos os vértices para None
    for vertice in grafo:
        for i in range(1, len(vertice)):
            vertice[i][1] = None
            
    inicial[1] = 0
    fila = [inicial]
    distancias = [inicial]
    visitados = [inicial[0]]
    
    while len(fila):
        vertice = fila.pop(0)
        for vizinho in verticeAdj(grafo, vertice[0]):
            if not vizinho[0] in visitados:
                vizinho[1] = vertice[1] + 1
                fila.append(vizinho)
                distancias.append(vizinho)
                visitados.append(vizinho[0])

    return distancias

print('Menor caminho com aresta sem peso: ', end='')
print(menorCaminho(grafo, grafo[2][0]))

grafo_naodirecionado = [
    [[0, 0], [1, 5], [2, 6], [3, 10]],
    [[1, 0], [4, 13], [0, 5]],
    [[2, 0], [3, 3], [4, 11], [5, 6]],
    [[3, 0], [4, 6], [5, 4], [0, 10], [2, 3]],
    [[4, 0], [6, 3], [1, 13], [2, 11], [3, 6]],
    [[5, 0], [6, 8], [2, 6], [3, 4]],
    [[6, 0], [4, 3], [5, 8]]
]

def dijkstra(grafo:list, inicial:int, final:int = None):
    distancias = [9999] * len(grafo)
    anterior = [None] * len(grafo)
    
    distancias[inicial] = 0
    fechados = []
    abertos = [inicial]
    
    while len(abertos):
        aux = 9999
        
        for a in abertos:
            if distancias[a] < aux:
                aux = distancias[a]
                v = a

        if v == final:
            break

        for vizinho in verticeAdj(grafo, v):
            if not vizinho[0] in fechados:
                abertos.append(vizinho[0])

            if distancias[vizinho[0]] > distancias[v] + vizinho[1]:
                distancias[vizinho[0]] = distancias [v] + vizinho[1]
                anterior[vizinho[0]] = v

        fechados.append(v)
        abertos.remove(v)

    return distancias, anterior

distancias, anterior = dijkstra(grafo_naodirecionado, 0, 6)

print(f'\nMenor caminho com pesos: {distancias}')

arvore = [[] for i in range(len(distancias))]

for i in range(len(distancias)):
    if anterior[i] == None:
        continue
    else:
        adicionar(arvore, anterior[i], i, distancias[i])

print('\nno_pai -> no_filho1:distancia_acumulada, no_filho2:distancia_acumulada')
for i, vertice in enumerate(arvore):
    if vertice != []:
        print(f'{i} -> ', end='')
        for j in range(len(vertice)):
            print(f'{vertice[j][0]}:{vertice[j][1]}', end=' ')
        print()