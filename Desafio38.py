print('=' * 12 + 'Desafio 38' + '=' * 12)
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
if a > b:
    print(f'O primeiro número ({a}) é maior que o segundo ({b})!')
elif b > a:
    print(f'O segundo número ({b}) é maior que o primeiro ({a})!')
else:
    print(f'Não existe número maior, pois os dois são iguais ({a})!')
