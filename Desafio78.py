print('=' * 12 + 'Desafio 78' + '=' * 12)
lista = []
for i in range(5):
    lista.append(int(input('Digite um número: ')))
print(f'Você digitou os valores: {lista}')
print(f'O menor número é {min(lista)} e ele aparece na(s) posição(ões) ', end='')
for c, o in enumerate(lista):
    if o == min(lista):
        print(f'{c}; ', end='')
print()
print(f'O maior número é {max(lista)} e ele aparece na(s) posição(ões) ', end='')
for c, o in enumerate(lista):
    if o == max(lista):
        print(f'{c}; ', end='')
print()