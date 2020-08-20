print('=' * 12 + 'Desafio 85' + '=' * 12)
numeros = [[],[]]
for i in range (7):
    print(f'Digite o {i+1}° número: ',end='')
    val = int(input())
    if val % 2 == 0:
        numeros[1].append(val)
    else:
        numeros[0].append(val)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares em ordem crescente são: {numeros[0]}.')
print(f'Os números ímpares em ordem crescente são: {numeros[1]}.')