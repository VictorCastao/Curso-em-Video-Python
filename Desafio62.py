print('=' * 12 + 'Desafio 62' + '=' * 12)
acrescimo = 1
primeiro = int(input('Digite o 1° termo da PA: '))
razão = int(input('Digite a razão da PA: '))
enesimo = 10
termos = 10
termino = ((enesimo - 1) * razão) + primeiro
while primeiro <= termino:
    print(f'{primeiro} -> ', end='')
    primeiro += razão
print('PAUSA')
while acrescimo != 0:
    acrescimo = int(input('Digite o número de termos que você ainda deseja ver: '))
    termino2 = ((acrescimo - 1) * razão) + primeiro
    termos += acrescimo
    while primeiro <= termino2:
        print(f'{primeiro} -> ', end='')
        primeiro += razão
    if acrescimo != 0:
        print('PAUSA')
print(f'Término da sequência com {termos} termos!')
