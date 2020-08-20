print('=' * 12 + 'Desafio 93' + '=' * 12)
jogador = dict()
jogador['Nome'] = input('Digite o nome do jogador: ')
jogador['Gols'] = list()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
total = 0
for c in range(partidas):
    qtde = int(input(f'Gols na partida {c + 1}: '))
    total += qtde
    jogador['Gols'].append(qtde)
jogador['Total'] = total
print('\nInformações do dicionário:')
for c, v in jogador.items():
    print(f'{c}: {v}')
print('\nDetalhes:')
print(f'O jogador {jogador["Nome"]} disputou {partidas} partidas:')
for c, v in enumerate(jogador['Gols']):
    print(f'   Partida {c + 1} => {v} gols')
print(f'O total de gols marcados por {jogador["Nome"]} foi {jogador["Total"]}.')
