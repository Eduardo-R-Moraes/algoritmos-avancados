class Fibonacci:
    def __init__(self):
        self.fibonacci = []

    def retornarFibo(self, n):
        if n > len(self.fibonacci):
            for i in range(n + 1):
                self.fibonacci.append(False)

            self.fiboAlonga(n)

        return self.fibonacci[n]

    def fiboAlonga(self, n):
        # Se a opção já foi visitada retorna o valor
        if self.fibonacci[n]:
            return self.fibonacci[n]
        
        # adiciona aos primeiros indices o valor 0 e 1
        if n == 0 or n == 1:
            self.fibonacci[n] = n
        
        else: 
            # Aqui impede que haja repetição caso o resultado seja 0 ou 1
            self.fibonacci[n] = self.fiboAlonga(n-1) + self.fiboAlonga(n-2)

        # é retornado no final de todas as chamadas e retorna primeiro 1 e depois 0
        return self.fibonacci[n]

fibonacci = Fibonacci()

posição = int(input('Digite a posição do fibonacci: '))
print(f'Número fibonacci na posição {posição}: {fibonacci.retornarFibo(posição)}')