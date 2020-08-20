print('=' * 12 + 'Desafio 84' + '=' * 12)
info = []
temp = []
resp = 'S'
menor = -1
maior = -1
contador = 0
while resp in 'sS':
    temp.append(input('Digite o nome: '))
    temp.append(float(input('Digite o peso: ')))
    info.append(temp[:])
    if menor == -1:
        menor = temp[1]
        maior = temp[1]
    if temp[1] < menor:
        menor = temp[1]
    if temp[1] > maior:
        maior = temp[1]
    temp.clear()
    contador+=1
    resp = input('Deseja continuar [S/N]? ')
print(f'Foram cadastradas {contador} pessoas.')
print(f'O maior peso encontrado foi {maior} kg, que é o peso de: ', end='')
for c in info:
    if c[1] == maior:
        print(f'{c[0]}, ', end='')
print()
print(f'O menor peso encontrado foi {menor} kg, que é o peso de:  ', end='')
for c in info:
    if c[1] == menor:
        print(f'{c[0]}, ', end='')
print()