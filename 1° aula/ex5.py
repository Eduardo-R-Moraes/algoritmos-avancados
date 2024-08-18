'''
Escreva um programa em Python que calcule o fatorial de um determinado número informado como parâmetro da sua função. Escreva duas versões desse programa, uma usando um laço e outra usando recursividade. Dica: fatorial de 5 = 5*4*3*2*1.
'''

def fatorial(n):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i

    return resultado

def fatorialRecursivo(n):
    if n == 1:
        return 1
    
    return n * fatorial(n-1)

print(fatorial(10))
print(fatorialRecursivo(10))