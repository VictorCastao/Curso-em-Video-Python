print('=' * 12 + 'Desafio 23' + '=' * 12)
numero = input('Digite um número entre 0 e 9999: ')
tam = len(numero)
unidade = int(numero[tam-1])
dezena = 0
centena = 0
unimil = 0
if tam > 1 :
    dezena = int(numero[tam-2])

if tam > 2 :
    centena = int(numero[tam-3])

if tam > 3 :
    unimil = int(numero[tam-4])

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Unidade de Milhar: {unimil}')