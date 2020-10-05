print('=' * 12 + 'Desafio 104' + '=' * 12)


def LeiaInt(texto):
    """A função recebe como parâmetro um texto a ser mostrado na tela. Em seguida, o usuário digita o número.
    Caso seja inválido, o programa entra em um loop e só sai deste quando a entrada for válida"""
    ent = input(texto).strip()
    while not ent.isnumeric():
        print('\033[0;31mERRO! Digite um número válido!\033[m')
        ent = input(texto).strip()
    return int(ent)


n = LeiaInt('Digite um número: ')
print(f'O número digitado foi {n}.')
