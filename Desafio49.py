print('=' * 12 + 'Desafio 49' + '=' * 12)
numero = int(input('Digite o número para a tabuada: '))
print('=' * 13)
print(f'Tabuada do {numero}')
print('=' * 13)
for i in range(1,11):
    print(f'{numero} x {i:2} = {numero * i}')
print('=' * 13)