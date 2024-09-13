class Grafo:
    def __init__(self, vertices: int, direcional: bool = False):
        self.vertices = vertices
        self.direcional = direcional
        self.lista = [[] * vertices for i in range(vertices)]
        self.matriz = [[0] * self.vertices for i in range(vertices)]

    # adiciona à lista e à matriz
    def adicionar(self, origem: int, destino: int, peso: int = 1):
        self.lista[origem - 1].append(f'{destino} (peso:{peso})')
        if not self.direcional:
            self.lista[destino - 1].append(f'{origem} (peso:{peso})')

        self.matriz[origem-1][destino-1] = 1 * peso
        if not self.direcional:
            self.matriz[destino-1][origem-1] = 1 * peso

    def mostrarLista(self):
        print('\nLista de adjacência: ')
        if self.vertices == 0:
            print('Zero vértices.')
        else:
            for i in range(self.vertices):
                print(f'{i + 1} -> {self.lista[i]}')

    def mostrarMatriz(self):
        print('\nMatriz de adjacência: ')
        if self.vertices == 0:
            print('Zero vértices.')
        else:
            for i in range(len(self.matriz)):
                print(self.matriz[i])