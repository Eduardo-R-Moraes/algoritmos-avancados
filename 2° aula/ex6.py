'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

def parImpar():
    store = []

    for i in range(20):
        store.append(int(input(f'{i+1}. Número: ')))

    par = []
    impar = []
    for i in store:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)

    return f'Vetor original: {store} \nVetor par: {par} \nVetor impar: {impar}'

print(parImpar())