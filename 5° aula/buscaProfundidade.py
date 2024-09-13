class Grafo:
    def __init__(self, vertices: int = 0):
        self.vertices = vertices
        self.grafo = [[] * vertices for i in range(vertices)]

        # Resultado da última busca em profundiade
        self.visitadosProfundidade = []

        # Resultado da última busca em largura
        self.visitadosLargura = []

    def adicionar(self, origem: int, destino: int):
        self.grafo[origem - 1].append(destino)
        if not self.direcional:
            self.grafo[destino - 1].append(origem)

    def mostrar(self):
        print('Lista de adjacência: ')
        if self.vertices == 0:
            print('Zero vértices.')
        else:
            for i in range(self.vertices):
                print(f'{i + 1} -> {self.grafo[i]}')
    
    def verticesAdj(self, vertice):
        adj = []
        for i in range(1, len(self.grafo[vertice])):
            adj.append(self.grafo[vertice][i])

        return adj

    def buscaProfundidade(self, vertice):
        if vertice in self.visitadosProfundidade:
            return False

        self.visitadosProfundidade.append(vertice)
        for verticeAdjacente in self.verticesAdj(vertice):
            if verticeAdjacente not in self.visitadosProfundidade:
                return self.buscaProfundidade(verticeAdjacente, self.visitadosProfundidade)
            
    def buscaLargura(self, vertice):
        fila = [vertice]
        self.visitadosLargura.append(vertice)

        while len(fila):
            proximoVerticeFila = fila.pop(0)

            for verticeAdjacente in self.verticesAdj(proximoVerticeFila):
                if not verticeAdjacente in self.visitadosLargura:
                    fila.append(verticeAdjacente)
                    self.visitadosLargura.append(verticeAdjacente)


