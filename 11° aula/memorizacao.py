def fibonacciMemorização(n):
    aux = [-1] * (n+1)
    lookFibo(aux, n)
    return aux[n-1] + aux[n-2]

def lookFibo(aux, n):
    if aux[n] >= 0:
        return aux[n]
    
    if n <= 1:
        aux[n] = n
    
    else: 
        aux[n] = lookFibo(aux, n-1) + lookFibo(aux, n-2)

    return aux[n]

posição = int(input('Digite a posição do fibonacci: '))
print(f'Número fibonacci na posição {posição}: {fibonacciMemorização(posição)}')