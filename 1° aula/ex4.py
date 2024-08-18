'''
Reescreva o programa de média aritmética para receber um parâmetro de quantidade de notas (ex. 5 notas), leia as notas (ex. leia as 5 notas) e retorne a média aritmética delas. Use um vetor para armazenar as notas. Percorra o vetor para fazer a soma.
'''

def mediaVetor(n):
    vetor = []
    soma = 0

    for i in range(n):
        vetor[i] = int(input(f'Nota {i}: '))

    for i in vetor:
        soma += i

    return soma / n