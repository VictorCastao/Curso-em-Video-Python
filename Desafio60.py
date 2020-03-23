print('=' * 12 + 'Desafio 60' + '=' * 12)

# Forma While
print('=====While=====')
fat = int(input('Digite o número a ser calculado: '))
inicio = fat
resposta = 1
print(f'O Fatorial de {inicio} é: ', end='')
while fat > 1:
    print(f'{fat} x ',end='')
    resposta *= fat
    fat -= 1
print(f'1 = {resposta}')

# Forma For
print('=====For=====')
fat2 = int(input('Digite o número a ser calculado: '))
resposta2 = 1
print(f'O fatorial de {fat2} é: ', end='')
for c in range(fat2, 1, -1):
    print(f'{c} x ', end='')
    resposta2 *= c
print(f'1 = {resposta2}')
