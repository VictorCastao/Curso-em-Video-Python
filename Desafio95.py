print('=' * 12 + 'Desafio 95' + '=' * 12)
jogador = dict()
cadastros = list()
while True:
    jogador['Nome'] = input('Digite o nome do jogador: ')
    jogador['Gols'] = []
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    total = 0
    for c in range(partidas):
        qtde = int(input(f'Gols na partida {c + 1}: '))
        total += qtde
        jogador['Gols'].append(qtde)
    jogador['Total'] = total
    cadastros.append(jogador.copy())
    resposta = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if resposta == 'N':
        break
print('\nInformações do dicionário:')
codigo = 0
print(f'{"COD":<3} {"NOME":<15} {"GOLS":<30} {"TOTAL":<5}')
for valor in cadastros:
    print(f'{codigo:>3} {valor["Nome"]:<15} {str(valor["Gols"]):<30}{valor["Total"]:>5}')
    codigo += 1
while True:
    resp = int(input('Digite o jogador a ser consultado [999 para sair]: '))
    if resp == 999:
        break
    if resp >= len(cadastros):
        print('Número Inválido!')
    else:
        for c, v in cadastros[resp].items():
            print(f'{c}: {v}')
        print('\nDetalhes:')
        print(f'O jogador {jogador["Nome"]} disputou {partidas} partidas:')
        for c, v in enumerate(jogador['Gols']):
            print(f'   Partida {c + 1} => {v} gols')
        print(f'O total de gols marcados por {jogador["Nome"]} foi {jogador["Total"]}.')
