print('=' * 12 + 'Desafio 51' + '=' * 12)
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos dessa PA são:')
soma = primeiro
for i in range(0, 10):
    print(f'{soma};', end='')
    soma += razão
