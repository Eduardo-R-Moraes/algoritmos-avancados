###
# Funções para tratamento de erros
# ###
 
def pegar_vertice():
    while True:
        try:
            print('Insira um número positivo')
            vertices = int(input('|V|: '))
            if vertices > 0:
                return vertices
            print()
        except ValueError:
            print()

def pegar_origem():
    while True:
        try:
            origem = int(input('\nVértice de origem: '))
            if origem > 0:
                return origem
            print()
        except ValueError:
            print()
            
def pegar_destino():
    while True:
        try:
            destino = int(input('Vértice de destino: '))
            if destino > 0:
                return destino
            print()
        except ValueError:
            print()

def pegar_peso():
    while True:
        try:
            peso = int(input('Peso da aresta (se não tiver pressione 0): '))
            if peso > 0:
                return peso
            print()
            if peso == 0:
                return 1
        except ValueError:
            print()