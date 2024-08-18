'''
Faça um programa em Python que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''

def triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return 'Triangulo equilátero.'
    
    if (lado1 + lado2) < lado3 or (lado2 + lado3) <= lado1 or (lado3 + lado1) < lado2:
        return 'Não é um triangulo'
    
    if lado1 != lado2 != lado3:
        return 'Triangulo escaleno'
    
    return 'Triangulo isósceles'

print(triangulo(3,3,3)) 
print(triangulo(5,5,6)) 
print(triangulo(4,5,6)) 
print(triangulo(1,2,10)) 
