print('=' * 12 + 'Desafio 55' + '=' * 12)
menor = 0
maior = 0
for i in range(0, 5):
    peso = float(input(f'Digite o peso {i + 1}: '))
    if i == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso é {maior} kg')
print(f'O menor peso é {menor} kg')
