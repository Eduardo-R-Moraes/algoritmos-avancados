'''
Faça um programa que leia e valide as seguintes informações: Nome: maior que 3 caracteres; Idade: entre 0 e 150; Salário: maior que zero; Sexo: 'f' ou 'm'; Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
sexo = input('Digite seu sexo (f, m): ')
estadoCivil = input('Digite seu estado civil (s, c, v ou d): ')

if len(nome) > 3 and idade in range(0, 151) and salario > 0 and sexo in ['f', 'm'] and estadoCivil in ['s', 'c', 'v', 'd']:
    print('Pessoa válida!')
else:
    print('Pessoa inválida!')