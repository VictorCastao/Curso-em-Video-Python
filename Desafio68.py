from random import randint
print('=' * 12 + 'Desafio 68' + '=' * 12)
vitorias = 0
while True:
    numero = int(input('Insira um número: '))
    opção = ' '
    while opção not in 'PI':
        opção = input('Escolha par ou ímpar [P/I]: ').strip().upper()[0]
    computador = randint(0, 10)
    resultado = 'NADA'
    soma = numero + computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print('=' * 70)
    print(f'Você escolheu {numero} e o computador escolheu {computador}. A soma é {soma} e deu {resultado}!')
    if resultado[0] == opção:
        print('Você GANHOU! Jogue novamente')
        vitorias += 1
        print('=' * 70)
    else:
        print('Você PERDEU!')
        break
print('=' * 70)
print(f'Você conseguiu ganhar {vitorias} vezes seguidas!')
