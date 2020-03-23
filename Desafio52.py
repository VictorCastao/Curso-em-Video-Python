print('=' * 12 + 'Desafio 52' + '=' * 12)
numero = int(input('Digite o número: '))
divisores = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1
if divisores == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')
