class Grafo:
    def __init__(self, vertices: int = 0, direcional: bool = False):
        self.vertices = vertices
        self.direcional = direcional
        self.grafo = [[] * vertices for i in range(vertices)]

    def adicionar(self, origem: int, destino: int, peso: int = 1):
        self.grafo[origem - 1].append(f'{destino * peso}, ({peso})')
        if not self.direcional:
            self.grafo[destino - 1].append(f'{destino * peso}, ({peso})')

    def mostrar(self):
        print('Lista de adjacência: ')
        if self.vertices == 0:
            print('Zero vértices.')
        else:
            for i in range(self.vertices):
                print(f'{i + 1} -> {self.grafo[i]}')