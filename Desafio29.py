print('=' * 12 + 'Desafio 29' + '=' * 12)
vel = float(input('Digite a sua velocidade (km/h): '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado e deverá pagar R$ {multa:.2f} de multa!')
else:
    print('Tudo certo!')
