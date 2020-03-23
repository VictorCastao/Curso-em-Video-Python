print('=' * 12 + 'Desafio 63' + '=' * 12)
n1 = 0
n2 = 1
partida = 3
quantidade = int(input('Digite quantos números da Sequência de Fibonacci você deseja ver: '))
if quantidade == 1:
    print(n1)
elif quantidade == 2:
    print(f'{n1} -> {n2}')
else:
    print(f'{n1} -> {n2} ', end='')
    while partida <= quantidade:
        print(f'-> {n1 + n2} ', end='')
        aux = n1 + n2
        n1 = n2
        n2 = aux
        partida += 1
print('\nTérmino da Sequência!')
