def troco(cedulas, troco):
    resultado = []
    for cedula in cedulas:
        if cedula <= troco:
            quantidade = troco // cedula
            troco = troco % cedula
            for i in range(quantidade):
                resultado.append(cedula)

            if troco == 0:
                break

    return resultado

cedulas = [100, 50, 25, 10, 5, 2, 1]

_troco = int(input('Digite o valor do troco: '))

print(f'Troco para {_troco}: {troco(cedulas, _troco)}')
