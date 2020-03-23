print('=' * 12 + 'Desafio 48' + '=' * 12)
soma = 0
numeros = 0
print('A soma entre os ímpares múltiplos de 3 entre 1 e 500 é:')
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        numeros += 1
print(f'{soma} -> Resultado da soma de {numeros} números!')
