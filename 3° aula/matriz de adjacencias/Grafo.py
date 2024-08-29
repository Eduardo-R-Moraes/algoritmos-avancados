class Grafo:
    def __init__(self, vertices: int, direcional: bool = False):
        self.vertices = vertices
        self.direcional = direcional
        self.grafo = [[0] * self.vertices for i in range(vertices)]

    # adiciona à matriz se origem e destino positivos.
    def adicionarAresta(self, origem: int, destino: int, peso: int = 1):
        self.grafo[origem-1][destino-1] = 1 * peso
        if not self.direcional:
            self.grafo[destino-1][origem-1] = 1 * peso

    def mostrar(self):
        print('Matriz de adjacência: ')
        if self.vertices == 0:
            print('Zero vértices.')
        else:
            for i in range(len(self.grafo)):
                print(self.grafo[i])