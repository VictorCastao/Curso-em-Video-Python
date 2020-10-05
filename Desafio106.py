from time import sleep


def ajuda(txt):
    escrita(f'Buscando por "{txt}"...', 4)
    sleep(0.5)
    print(cores[6], end='')
    return help(txt)


def escrita(texto, cor=0):
    print(cores[cor], end='')
    print('=' * (len(texto) + 5))
    print(f'{texto:^{len(texto) + 5}}')
    print('=' * (len(texto) + 5))
    print(cores[0], end='')


print('=' * 12 + 'Desafio 106' + '=' * 12)
cores = ('\033[m',  # sem cores
         '\033[0;30;41m',  # vermelho
         '\033[0;30;42m',  # verde
         '\033[0;30;43m',  # amarelo
         '\033[0;30;44m',  # azul
         '\033[0;30;45m',  # roxo
         '\033[7;30m'  # branco
         )
escrita('MENU INTERATIVO', 1)

while True:
    msg = input('Função ou Biblioteca >> ').strip()
    if msg.upper() == 'FIM':
        escrita('FINALIZANDO...', 4)
        sleep(1)
        break
    ajuda(msg)
    print(cores[0], end='')
    sleep(1)
    escrita('MENU INTERATIVO', 1)
