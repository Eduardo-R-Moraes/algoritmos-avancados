'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
• Comprar apenas latas de 18 litros; 
• Comprar apenas galões de 3,6 litros; 
• Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

def quantidadeTinta(metrosQuadrados):
    metros = metrosQuadrados + metrosQuadrados * 0.1
    lata = 0
    galao = 0

    if metros >= 108:
        lata = metros // 108
        metros -= 108

    if metros >= 21.6 and metros < 108:
        galao = metros // 21.6
        metros -= 21.6

    if metros < 21.6:
        galao += 1

    return f"Quantidade de lata: {lata} \nQuantidade de galões: {galao} \nValor total: {lata * 80 + galao * 25}"

print(quantidadeTinta(150))