from time import sleep

print('=' * 12 + 'Desafio 99' + '=' * 12)


def maior(*lista):
    sleep(1)
    print('Analisando...')
    a = len(lista)
    maior = 0
    for i in range(a):
        if i == 0 or lista[i] >= maior:
            maior = lista[i]
    sleep(1)
    print(f'Foram informados {a} valores: {lista}.')
    sleep(1)
    print(f'O maior valor encontrado foi {maior}.')
    print()


maior(1, 2, 3, 4, 5, 6, 7)
maior(23, 43, 12, 65, 3, 43, 21)
maior()
maior(23, 534, 122, 56, 3, 11, 2)
maior(-1, -2, 12, -4, -43)
