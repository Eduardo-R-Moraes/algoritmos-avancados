'''
Palíndromo. Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice-versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma sequência de caracteres, mostre-a e diga se é um palíndromo ou não.
'''

def palindromo(palavra):
    palavra_inversa = ''
    for i in range(len(palavra) - 1, -1, -1):
        palavra_inversa += palavra[i]

    if palavra != palavra_inversa:
        return False
    
    return True

print(palindromo('osso'))
print(palindromo('ana'))