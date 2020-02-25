from random import randint

print('=' * 12 + 'Desafio 45' + '=' * 12)
print("""As opções são as seguintes:
1 - Pedra
2 - Papel
3 - Tesoura""")
pc = randint(1, 3)
escolha = int(input('Digite sua escolha: '))
if pc == 1 and escolha == 2:
    print('O computador escolheu Pedra -> Você Ganhou!')
elif pc == 1 and escolha == 3:
    print('O computador escolheu Pedra -> Você Perdeu!')
elif pc == 2 and escolha == 1:
    print('O computador escolheu Papel -> Você Perdeu!')
elif pc == 2 and escolha == 3:
    print('O computador escolheu Papel -> Você Ganhou!')
elif pc == 3 and escolha == 1:
    print('O computador escolheu Tesoura -> Você Ganhou!')
elif pc == 3 and escolha == 2:
    print('O computador escolheu Tesoura -> Você Perdeu!')
else:
    print('O computador escolheu a mesma coisa -> Empate!')
