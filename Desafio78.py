print('=' * 12 + 'Desafio 78' + '=' * 12)
lista = []
for i in range(5):
    lista.append(int(input('Digite um número: ')))
print(f'O menor número é {min(lista)} e ele aparece na posição {lista.index(min(lista))}!')
print(f'O maior número é {max(lista)} e ele aparece na posição {lista.index(max(lista))}!')