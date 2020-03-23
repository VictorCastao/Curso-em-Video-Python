print('=' * 12 + 'Desafio 67' + '=' * 12)
while True:
    n = int(input('Digite o número para ver sua tabuada: '))
    if n < 0:
        break
    else:
        print('=' * 20)
        for i in range(1, 11):
            print(f'{n} x {i:2} = {n * i}')
        print('=' * 20)
print('=====TÉRMINO DO PROGRAMA=====')
