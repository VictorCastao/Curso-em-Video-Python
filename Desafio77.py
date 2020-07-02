print('=' * 12 + 'Desafio 77' + '=' * 12)
tupla = ('UM', 'PRATO', 'DE', 'TRIGO', 'PARA', 'TRES', 'TIGRES', 'TRISTES')
tamanho = len(tupla)
for c in range(tamanho):
    print(f'A palavra {tupla[c]} tem as seguintes vogais: ', end='')
    tamanho2 = len(tupla[c])
    for i in range(tamanho2):
        if tupla[c][i] in "AEIOU":
            print(f'{tupla[c][i]} ', end='')
    print('\n', end='')
