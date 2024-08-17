'''
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
'''

while True:
    soma = 0
    produtos = []

    while True:
        valor = float(input('Valor: '))
        if not valor:
            break
        soma += valor
        produtos.append(valor)

    print('\nLoja Tabajara')

    for i in range(len(produtos)):
        print(f'Produto {i + 1}: {produtos[i]}')

    print(f'Valor da compra: {soma}\n')

    while True:
        dinheiro = float(input('Digite o valor em dinheiro: '))
        if dinheiro >= soma:
            break
        print('Dinheiro insuficiente.')

    troco = soma - dinheiro
    print(f'\nTroco: {troco}') 

    condicional = input('\nIniciar outra compra (sim, nao): ')

    if condicional == 'nao':
        break