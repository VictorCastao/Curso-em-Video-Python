from random import randint
from time import sleep

print('=' * 12 + 'Desafio 100' + '=' * 12)


def soma_par(lista):
    soma = 0
    qtde = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
            qtde += 1
    sleep(1)
    print(f'Após a análise, foram encontrados {qtde} números, cuja soma é {soma}.')


def sortear():
    lista = list()
    for i in range(5):
        a = randint(0, 100)
        lista.append(a)
    sleep(1)
    print(f'Os números sorteados são: {lista}.')
    soma_par(lista)


sortear()
