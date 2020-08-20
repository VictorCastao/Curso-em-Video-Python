print('=' * 12 + 'Desafio 80' + '=' * 12)
lista = []
for c in range(5):
    var = int(input('Digite um valor: '))
    if len(lista) == 0 or var > lista[len(lista) - 1]:
        lista.append(var)
        print('Valor adicionado no fim da lista.')
    elif var <= lista[0]:
        lista.insert(0, var)
        print('Valor adicionado no início da lista.')
    else:
        for num, val in enumerate(lista):
            if var <= val:
                lista.insert(num, var)
                print(f'Valor adicionado na posição {num}')
                break
print(f'A lista dos valores digitados é: {lista}')

