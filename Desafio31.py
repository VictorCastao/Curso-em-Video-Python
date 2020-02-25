print('=' * 12 + 'Desafio 31' + '=' * 12)
km = float(input('Digite a distância da viagem (km): '))
if km > 200:
    print(f'O valor da passagem é R$ {km * 0.45:.2f}!')
else:
    print(f'O valor da passagem é R$ {0.5 * km:.2f}!')
