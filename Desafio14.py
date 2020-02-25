print('='*12+'Desafio 14'+'='*12)
celsius = float(input('Digite a temperatura em °C: '))
fahr = (celsius * 9 / 5) +32
print(f'{celsius:.1f} °C correspondem a {fahr:.1f} °F!')
fahr2 = float(input('Digite a temperatura em °F: '))
celsius2 = (fahr2 - 32) * 5 / 9
print(f'{fahr2:.1f} °F correspondem a {celsius2:.1f} °C!')