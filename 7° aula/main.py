class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.vertices = len(grafo)

    def BFS(self, source: int, sink: int, pai):
        visitados = [False] * self.vertices
        fila = [source]
        visitados[source] = True

        while fila:
            vertice = fila.pop(0)

            for indice, valor in enumerate(self.grafo[vertice]):
                if not visitados[indice] and valor > 0:
                    fila.append(indice)
                    visitados[indice] = True
                    pai[indice] = vertice

                    if indice == sink:
                        return True
        return False

    def FordFulkerson(self, source: int, sink: int):
        pai = [-1] * self.vertices
        fluxoMaximo = 0

        while self.BFS(source, sink, pai):
            caminho_fluxo = float('Inf')
            s = sink

            while s != source:
                caminho_fluxo = min(caminho_fluxo, self.grafo[pai[s]][s])
                s = pai[s]

            fluxoMaximo += caminho_fluxo
            v = sink

            while v != source:
                vertice = pai[v]
                self.grafo[vertice][v] -= caminho_fluxo
                self.grafo[v][vertice] += caminho_fluxo
                v = pai[v]

        return fluxoMaximo

#grafo = [[0, 30, 0, 50, 0],
         #[0, 0, 60, 0, 0],
         #[0, 0, 0, 0, 80],
         #[0, 0, 0, 0, 15],
         #[0, 0, 0, 0, 0]]

vertices = int(input('Digite o número de vértices pertencentes ao grafo: '))

grafo = [[0 for x in range(vertices)] for x in range(vertices)]

for i in range(len(grafo)):
    for j in range(i + 1, len(grafo)):
       if grafo[i][j] == 0 and grafo[j][i] == 0:
           peso = int(input(f'Digite o peso da aresta entre {i + 1} e {j + 1}: '))
           grafo[i][j] = peso

g = Grafo(grafo)

print()

source = int(input('Digite o source: '))
sink = int(input('Digite o sink: '))

print()

print('Grafo:')
for vertice in grafo:
    print(vertice)

print()

maxflow = g.FordFulkerson(source - 1, sink - 1)
print(f"O fluxo máximo é {maxflow}")
