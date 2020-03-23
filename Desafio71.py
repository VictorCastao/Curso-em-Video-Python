print('=' * 12 + 'Desafio 71' + '=' * 12)
nota50 = nota20 = nota10 = nota1 = 0
print('=====BANCO RACKET=====')
valor = int(input('Digite o valor a ser sacado: R$ '))
original = valor
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
nota1 = valor % 10
print(f'O valor R$ {original} será entregue da seguinte forma:')
if nota50 > 0:
    print(f'{nota50} notas de R$ 50')
if nota20 > 0:
    print(f'{nota20} notas de R$ 20')
if nota10 > 0:
    print(f'{nota10} notas de R$ 10')
if nota1 > 0:
    print(f'{nota1} notas de R$ 1')
print('=====FIM DA OPERAÇÃO=====')
