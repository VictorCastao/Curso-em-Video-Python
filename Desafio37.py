print('=' * 12 + 'Desafio 37' + '=' * 12)
num = int(input('Digite o número inteiro: '))
print("""As suas opções de conversão são:
1 - Binário
2 - Octal
3- Hexadecimal""")
option = int(input('Digite a opção escolhida: '))
if option == 1:
    resp = str(bin(num))
    print(f'O número \033[32m{num}\033[m, convertido para binário, corresponde a \033[32m{resp[2:]}\033[m!')
elif option == 2:
    resp = str(oct(num))
    print(f'O número \033[32m{num}\033[m, convertido para octal, corresponde a \033[32m{resp[2:]}\033[m!')
else:
    resp = str(hex(num))
    print(f'O número \033[32m{num}\033[m, convertido para hexadecimal, corresponde a \033[32m{resp[2:]}\033[m!')
