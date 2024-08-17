'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

def ordenacaoInversa(vetor):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[i] < vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]

    return vetor

print(ordenacaoInversa([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))