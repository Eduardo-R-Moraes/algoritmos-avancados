'''
Faça um programa que leia 5 números e informe o maior número.
'''

def maiorNumero(vetor):
    maior = 0
    for numero in vetor:
        if numero > maior:
            maior = numero

    return maior

vetor = [1, 2, 13, 4, 5]

print(f'Maior número: {maiorNumero(vetor)}')