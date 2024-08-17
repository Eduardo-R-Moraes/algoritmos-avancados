'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo.
'''

def fibonacci(n):
    result = []
    
    for i in range(n):
        if i == 0 or i == 1:
            result.append(1)
        else:
            result.append(result[i-1] + result[i-2])

    return result

print(fibonacci(10))