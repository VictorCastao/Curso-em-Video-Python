print('=' * 12 + 'Desafio 103' + '=' * 12)


def ficha(id='Desconhecido', num=0):
    return f'O jogador {id} fez {num} gols na partida!'


nome = input('Digite o nome do jogador: ').strip()
gols = input('Digite o número de gols na partida: ')
resp = ""

if not gols.isnumeric() and nome == "":
    resp = ficha()
elif nome == "":
    resp = ficha(num=int(gols))
elif not gols.isnumeric():
    resp = ficha(nome)
else:
    resp = ficha(nome, int(gols))

print(resp)
