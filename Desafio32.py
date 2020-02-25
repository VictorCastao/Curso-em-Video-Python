print('='*12+'Desafio 32'+'='*12)
ano = int(input('Digite o ano: '))
if (ano % 4) == 0:
    if (ano % 100) == 0 and (ano % 400) != 0:
        print(f'O ano de {ano} não é bissexto!')
    else:
        print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')
