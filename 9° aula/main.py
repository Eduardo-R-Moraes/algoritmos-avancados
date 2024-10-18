class PasseioCavalo:
    def __init__(self, num):
        self.dx = [2, 1, -1, -2, -2, -1, 1, 2]
        self.dy = [1, 2, 2, 1, -1, -2, -2, -1]
        self.num = num
        self.numeroQuadrados = num ** 2
        self.tab = [[0 for i in range(num)] for i in range(num)]

    def aceitavel(self, x, y):
        return 0 <= x < self.num and 0 <= y < self.num and self.tab[x][y] == 0

    def tenta(self, qtde_visitas_feitas, x, y):
        if qtde_visitas_feitas == self.numeroQuadrados: 
            return True

        for k in range(8):
            u = x + self.dx[k]
            v = y + self.dy[k]

            if self.aceitavel(u, v):
                self.tab[u][v] = qtde_visitas_feitas

                if self.tenta(qtde_visitas_feitas + 1, u, v):
                    return True 

                self.tab[u][v] = 0 

        return False 

    def printTabuleiro(self):
        for i in range(self.num):
            for j in range(self.num):
                print(f"{self.tab[i][j]:2}", end="\t")  
            print("")

    def passeia(self, x, y):
        self.tab[x][y] = 1  
        if self.tenta(2, x, y):  
            self.printTabuleiro()
        else:
            print("Não existem passeios possíveis para o tabuleiro informado.")

num = int(input("Informe o tamanho do tabuleiro. Exemplo: 8 para 8x8: "))

cavalo = PasseioCavalo(num)

cavalo.passeia(0, 0)
