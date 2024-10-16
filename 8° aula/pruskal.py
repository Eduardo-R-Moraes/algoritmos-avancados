class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adjacencia = [[] for _ in range(num_vertices)]
        self.grafo = []  # Inicializando a lista de arestas

    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.lista_adjacencia[vertice1].append((peso, vertice2))
        self.lista_adjacencia[vertice2].append((peso, vertice1))
        self.grafo.append((vertice1, vertice2, peso))  # Adicionando a aresta à lista de arestas

    def visualizar_grafo(self):
        print("Grafo:")
        for vertice in range(self.num_vertices):
            arestas = ', '.join(f'({vertice_adjacente}, peso:{peso})' for peso, vertice_adjacente in self.lista_adjacencia[vertice])
            print(f'Vertice {vertice}: {arestas}')

    def encontrar(self, parent, i):
        if parent[i] == i:
            return i
        return self.encontrar(parent, parent[i])

    def unir(self, parent, rank, x, y):
        xraiz = self.encontrar(parent, x)
        yraiz = self.encontrar(parent, y)
        if xraiz != yraiz:
            if rank[xraiz] < rank[yraiz]:
                parent[xraiz] = yraiz
            elif rank[xraiz] > rank[yraiz]:
                parent[yraiz] = xraiz
            else:
                parent[yraiz] = xraiz
                rank[xraiz] += 1

    def kruskal(self):
        resultado = []
        i = 0
        e = 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])  # Agora, self.grafo está preenchida
        parent = []
        rank = []

        for nodo in range(self.num_vertices):
            parent.append(nodo)
            rank.append(0)

        while e < self.num_vertices - 1:
            vertice1, vertice2, peso = self.grafo[i]
            i += 1
            x = self.encontrar(parent, vertice1)
            y = self.encontrar(parent, vertice2)

            if x != y:
                e += 1
                resultado.append((vertice1, vertice2, peso))
                self.unir(parent, rank, x, y)

        custo_minimo = sum(peso for _, _, peso in resultado)
        return resultado, custo_minimo

grafo = Grafo(5)
grafo.adicionar_aresta(0, 1, 10)
grafo.adicionar_aresta(0, 2, 5)
grafo.adicionar_aresta(1, 3, 3)
grafo.adicionar_aresta(3, 4, 9)
grafo.adicionar_aresta(3, 2, 8)
grafo.adicionar_aresta(2, 4, 4)

grafo.visualizar_grafo()
print()

arvore_minima_kruskal, custo_minimo_kruskal = grafo.kruskal()
print("Árvore Geradora Mínima:", arvore_minima_kruskal)
print("Custo da Árvore Geradora Mínima:", custo_minimo_kruskal)
