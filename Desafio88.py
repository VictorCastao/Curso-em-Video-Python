from random import randint
from time import sleep

print('=' * 12 + 'Desafio 88' + '=' * 12)
jogos = int(input('Digite o número de jogos a serem realizados: '))
lista = list()
total = list()
valor = 0
for c in range(jogos):
    while len(lista) != 6:
        valor = randint(1, 60)
        if valor not in lista:
            lista.append(valor)
    lista.sort()
    total.append(lista[:])
    lista.clear()
for c in range(jogos):
    sleep(1)
    print(f'Jogo {c + 1}: {total[c]}')
