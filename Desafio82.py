print('=' * 12 + 'Desafio 82' + '=' * 12)
lista = []
pares = []
impares = []
while True:
    var = int(input('Digite um valor: '))
    lista.append(var)
    resp = input('Deseja continuar [S/N]? ').upper().strip()
    if resp[0] == 'N':
        break;
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'A lista original digitada foi: {lista}')
print(f'Os elementos pares são {pares}')
print(f'Os elementos ímpares são {impares}')
