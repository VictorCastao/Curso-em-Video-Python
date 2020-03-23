print('=' * 12 + 'Desafio 50' + '=' * 12)
print('Digite os números para somar:')
soma = 0
for i in range(1, 7):
    n = int(input(f'Número {i}: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos pares dentre os 6 números é {soma}')
