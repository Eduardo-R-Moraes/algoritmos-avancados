dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def aceitavel(x, y):
    return 0 <= x < num and 0 <= y < num and tab[x][y] == 0

def tenta(qtde_visitas_feitas, x, y):
    if qtde_visitas_feitas == numQuad: 
        return True

    for k in range(8):
        u = x + dx[k]
        v = y + dy[k]

        if aceitavel(u, v):
            tab[u][v] = qtde_visitas_feitas

            if tenta(qtde_visitas_feitas + 1, u, v):
                return True 

            tab[u][v] = 0 

    return False 

def printTabuleiro():
    for i in range(num):
        for j in range(num):
            print(f"{tab[i][j]:2}", end="\t")  
        print("")

def passeia(x, y):
    tab[x][y] = 1  
    if tenta(2, x, y):  
        printTabuleiro()
    else:
        print("Não existem passeios possíveis para o tabuleiro informado.")

num = int(input("Informe o tamanho do tabuleiro. Exemplo: 8 para 8x8: "))
numQuad = num * num

tab = [[0] * num for i in range(num)]

passeia(0, 0)
