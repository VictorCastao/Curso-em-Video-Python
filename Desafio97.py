print('=' * 12 + 'Desafio 97' + '=' * 12)


def escreva(texto):
    a = len(texto)
    print('~' * (a + 8))
    print(f'{texto:^{a + 8}}')
    print('~' * (a + 8))


escreva('Curso em Vídeo')
escreva('Programar em Python')
escreva('Bora programar!!!')
