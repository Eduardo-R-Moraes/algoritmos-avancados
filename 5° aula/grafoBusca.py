from random import randint

class Grafo:
    def __init__(self, vertices: int = 0):
        self.vertices = vertices
        self.grafo = [[] * vertices for i in range(vertices)]

        # Resultado da última busca em profundiade
        self.visitadosProfundidade = []

        # Resultado da última busca em largura
        self.visitadosLargura = []

    def gerarGrafo(self):
        for i in range(len(self.grafo)):
            for j in range(self.vertices - 1):
                num = randint(0, self.vertices - 1)
                if num != 0 and num != i:
                    self.adicionar(i + 1, num + 1) 

    def adicionar(self, origem, final):
        if final not in self.grafo[origem - 1]:
            self.grafo[origem - 1].append(final)
        if origem not in self.grafo[final - 1]:
            self.grafo[final - 1].append(origem)

    def mostrar(self):
        print('\nLista de adjacência: ')
        if self.vertices == 0:
            print('Zero vértices.')
        else:
            for i in range(self.vertices):
                print(f'{i + 1} -> {self.grafo[i]}')

    def getBuscaProfundidade(self, vertice):
        self.visitadosProfundidade.clear()
        self.buscaProfundidade(vertice)
        return self.visitadosProfundidade
        
    def getBuscaLargura(self, vertice):
        self.visitadosLargura.clear()
        self.buscaLargura(vertice)
        return self.visitadosLargura
    
    def verticesAdj(self, vertice):
        adj = []
        for i in range(len(self.grafo[vertice-1])):
            adj.append(self.grafo[vertice-1][i])

        return adj

    def buscaProfundidade(self, vertice):
        if vertice in self.visitadosProfundidade:
            return False

        self.visitadosProfundidade.append(vertice)
        for verticeAdjacente in self.verticesAdj(vertice):
            if verticeAdjacente not in self.visitadosProfundidade:
                return self.buscaProfundidade(verticeAdjacente)
            
    def buscaLargura(self, vertice):
        fila = [vertice]
        self.visitadosLargura.append(vertice)

        while len(fila):
            proximoVerticeFila = fila.pop(0)

            for verticeAdjacente in self.verticesAdj(proximoVerticeFila):
                if not verticeAdjacente in self.visitadosLargura:
                    fila.append(verticeAdjacente)
                    self.visitadosLargura.append(verticeAdjacente)