from time import sleep
from random import randint
from operator import itemgetter

print('=' * 12 + 'Desafio 91' + '=' * 12)
valores = dict()
print('Início do Jogo:')
for i in range(4):
    sleep(1)
    c = randint(1, 6)
    print(f'Jogador {i + 1} tirou {c}.')
    nome = 'Jogador ' + str(i + 1)
    valores[nome] = c
valores = sorted(valores.items(), key=itemgetter(1), reverse=True)
sleep(1)
print('\nResultado:')
for i, j in enumerate(valores):
    print(f'{i + 1}° lugar: {j[0]} ({j[1]} pontos)')
