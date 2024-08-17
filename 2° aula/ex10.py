'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informadas ordenadas.
'''

notas = []

nome = input('Nome do atleta: ')

maior = 0
menor = 10

for i in range(7):
    nota = float(input(f'Nota {i+1}: '))

    if nota > maior:
        maior = nota

    if nota < menor:
        menor = nota

    notas.append(nota)

soma = 0
for nota in notas:
    soma += nota

soma -= maior - menor

media = soma / 5

print(f'\nAtleta: {nome}')
for nota in notas:
    print(f'Nota: {nota}')
    
print(f'\nAtleta: {nome}')
print(f'Melhor nota: {maior}')
print(f'Pior nota: {menor}')
print(f'Média: {media}')
