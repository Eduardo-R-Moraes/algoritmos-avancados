class Fibonacci:
    def __init__(self):
        self.fibonacci = [0, 1]

    def add_number(self, fim):
        inicio = len(self.fibonacci)
        fim += 1

        for i in range(inicio, fim):
            self.fibonacci.append(self.fibonacci[i-1] + self.fibonacci[i-2]) 

    def retorna_numero(self, n):
        if len(self.fibonacci) < n:
            self.add_number(n)

        return self.fibonacci[n]

fibonacci = Fibonacci()

while True:
    print('1 -> Ver número pela posição')
    print('2 -> Ver os números de fibonacci até a última posição')
    opções = input('-> ')

    if opções == '1':
        print('-----------------------------------')
        posição = int(input('Digite a posição: '))
        print('-----------------------------------')
        print(f'Número fibonacci na {posição} posição: {fibonacci.retorna_numero(posição)}')
        print('-----------------------------------')

    if opções == '2':
        print('-----------------------------------')
        print(f'Números até agora: {len(fibonacci.fibonacci)}')
        print(f'Sequência: {fibonacci.fibonacci}')
        print('-----------------------------------')

    if opções == '':
        break
