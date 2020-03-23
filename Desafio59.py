print('=' * 12 + 'Desafio 59' + '=' * 12)
print('=====Início do Programa=====')
opção = 0
n1 = float(input('Digite o número 1: '))
n2 = float(input('Digite o número 2: '))
while opção != 5:
    if opção == 4:
        n1 = float(input('Digite o número 1: '))
        n2 = float(input('Digite o número 2: '))
    print("""Digite uma das opções:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa""")
    opção = int(input('Opção: '))
    if opção < 1 or opção > 5:
        print('Opção inválida! Digite novamente.')
    if opção == 1:
        print(f'Você escolheu Soma: {n1} + {n2} = {n1 + n2}')
    elif opção == 2:
        print(f'Você escolheu Multiplicar: {n1} * {n2} = {n1 * n2}')
    elif opção == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'Você escolheu Maior: {maior} é o maior')
    elif opção == 4:
        print('Digite novos números')
print('=====Fim do Programa=====')
