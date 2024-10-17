def tarefa(inicial, final):
    _inicial = []
    _final = []
    numero_horas = 0

    ultimo_horario_final = 0
    for index, hora_inicio in enumerate(inicial):
        if hora_inicio >= ultimo_horario_final:
            _inicial.append(hora_inicio)
            _final.append(final[index])

            ultimo_horario_final = final[index]

            numero_horas += final[index] - hora_inicio

    return _inicial, _final, numero_horas

# Inicializa os vetores
inicio = []
fim = []

print('\nCaso queira parar digite 100.')
print('Os valores de termino precisam estar em ordem crescente.\n')

# Povoa vetores
valor_termino = 0
repetir = True
while repetir:
    inicial = int(input('Hora de inicio: '))
    if inicial == 100:
        print('-------------------------------------------------')
        break

    final = int(input('Hora de fim: '))
    if final == 100:
        print('-------------------------------------------------')
        break
    
    if final < valor_termino:
        print('\nValor de termino menor que anterior, operação inválida!')
        print('-------------------------------------------------')
        break

    inicio.append(inicial)
    fim.append(final)

    valor_termino = final

    print('-------------------------------------------------')

# Printa o valor dos vetores passados pelo loop
print('Seus vetores:')
print(f'Início: {inicio}')
print(f'Fim: {fim}')

# valores pré configurado como no exemplo
# inicial_setado = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
# final_setado = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

# Para valor setado como no exemplo:
# start, end, horas = tarefa(inicial_setado, final_setado)

start, end, horas = tarefa(inicio, fim)

print('-------------------------------------------------')
print(f'Total de horas reservadas: {horas}')
print('-------------------------------------------------')
print('Horários reservados:')
for inicio, fim in zip(start, end):
    print(f'Dàs \t{inicio} \tàs \t{fim}')
print('-------------------------------------------------')