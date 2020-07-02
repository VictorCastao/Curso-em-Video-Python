print('=' * 12 + 'Desafio 75' + '=' * 12)
num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
num3 = int(input('Digite o número 3: '))
num4 = int(input('Digite o número 4: '))
tupla = (num1, num2, num3, num4)
contagem9 = tupla.count(9)
print(f'O número 9 apareceu {contagem9} vez(es).')
if tupla.count(3) == 0:
    print('O número 3 não aparece na tupla.')
else:
    resp = tupla.index(3)
    print(f'O número 3 aparece pela primeira vez na posição {resp}.')
pares = 0
print('Os números pares da tupla são:')
for i in tupla:
    if i % 2 == 0:
        pares += 1
        print(f'{i} ', end='')
if pares == 0:
    print('Nenhum')
