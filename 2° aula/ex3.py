'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 
'''

def tabuada(n):
    if n > 10 or n < 1:
        print('O número de entrada deve ser um número entre 1 e 10.')
    else:
        print(f'Tabuada de {n}')
        for i in range(1, 10):
            print(f'{n} x {i} = {i * n}')

tabuada(10)
tabuada(0)
tabuada(11)