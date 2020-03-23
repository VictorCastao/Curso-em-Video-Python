print('=' * 12 + 'Desafio 61' + '=' * 12)
primeiro = int(input('Digite o 1° termo da sequência: '))
razão = int(input('Digite a razão da sequência: '))
termo10 = (9 * razão) + primeiro
while primeiro <= termo10:
    print(f'{primeiro}, ', end='')
    primeiro += razão
