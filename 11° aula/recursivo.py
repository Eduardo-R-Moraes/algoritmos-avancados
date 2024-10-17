def fibonacci(n):
    if n <= 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

enesimo_numero = int(input('Digite a posição do número de fibonacci que deseja: '))
print(f'Fibonacci na {enesimo_numero} posição: {fibonacci(enesimo_numero)}')