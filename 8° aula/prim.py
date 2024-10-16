class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adjacencia = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.lista_adjacencia[vertice1].append((peso, vertice2))
        self.lista_adjacencia[vertice2].append((peso, vertice1))

    def visualizar_grafo(self):
        print("Grafo:")
        for vertice in range(self.num_vertices):
            arestas = ', '.join(f'({vertice_adjacente}, peso:{peso})' for peso, vertice_adjacente in self.lista_adjacencia[vertice])
            print(f'Vertice {vertice}: {arestas}')

    def minKey(self, chave, mstSet):
        min_valor = float('inf')
        min_index = -1
        for v in range(self.num_vertices):
            if chave[v] < min_valor and not mstSet[v]:
                min_valor = chave[v]
                min_index = v
        return min_index

    def prim(self):
        chave = [float('inf')] * self.num_vertices
        parent = [None] * self.num_vertices
        chave[0] = 0
        mstSet = [False] * self.num_vertices
        parent[0] = -1

        for cout in range(self.num_vertices):
            u = self.minKey(chave, mstSet)
            mstSet[u] = True

            for peso, vertice_adjacente in self.lista_adjacencia[u]:
                if peso > 0 and not mstSet[vertice_adjacente] and chave[vertice_adjacente] > peso:
                    chave[vertice_adjacente] = peso
                    parent[vertice_adjacente] = u

        arvore_geradora_minima = []
        for i in range(1, self.num_vertices):
            arvore_geradora_minima.append((parent[i], i, chave[i]))

        return arvore_geradora_minima

grafo = Grafo(5)
grafo.adicionar_aresta(0, 1, 10)
grafo.adicionar_aresta(0, 2, 5)
grafo.adicionar_aresta(1, 3, 3)
grafo.adicionar_aresta(3, 4, 9)
grafo.adicionar_aresta(3, 2, 8)
grafo.adicionar_aresta(2, 4, 4)

grafo.visualizar_grafo()
print()

arvore_minima = grafo.prim()
print("Arvore Geradora Minima:", arvore_minima)