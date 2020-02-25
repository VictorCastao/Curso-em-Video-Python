print('=' * 12 + 'Desafio 33' + '=' * 12)
a = float(input('Digite o número 1: '))
b = float(input('Digite o número 2: '))
c = float(input('Digite o número 3: '))
maior = 0
menor = 0
if a >= b and a >= c:
    maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >= b:
    maior = c
if a <= b and a <= c:
    menor = a
if b <= a and b <= c:
    menor = b
if c <= a and c <= b:
    menor = c
print(f'Dentre esses números, o menor é o {menor} e o maior é o {maior}!')
