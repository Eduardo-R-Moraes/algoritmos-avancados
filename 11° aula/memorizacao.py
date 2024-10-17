'''
# Esta nada mais é do que uma sequência de fibonacci com recursividade normal
  com a adição da tabela chamada aux.

# Quando se calcula o fibonacci normal, a cada chamada da função ele recalcula
  a sequencia inteira. Com a adição do vetor aux, a sequência precisa ser 
  calculada apenas uma vez, sendo que, a cada iteração é usado os valores pré
  calculados.

# Para fazer a implementação, foi necessário adicionar uma condição a mais

# Ela tem duas condições de paradas, uma para chegar no final do vetor e
  outra pra quando o vetor já estiver populado
'''

def fibonacciMemorização(n):
    visitado = [False] * (n+1)
    return lookFibo(visitado, n)

def lookFibo(visitado, n):
    # Se a opção já foi visitada retorna o valor
    if visitado[n]:
        return visitado[n]
    
    # adiciona aos primeiros indices o valor 0 e 1
    if n == 0 or n == 1:
        visitado[n] = n
    
    else: 
        # Aqui impede que haja repetição caso o resultado seja 0 ou 1
        visitado[n] = lookFibo(visitado, n-1) + lookFibo(visitado, n-2)

    # é retornado no final de todas as chamadas e retorna primeiro 1 e depois 0
    return visitado[n]

posição = int(input('Digite a posição do fibonacci: '))
print(f'Número fibonacci na posição {posição}: {fibonacciMemorização(posição)}')