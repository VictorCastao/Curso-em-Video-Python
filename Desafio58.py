from random import randint

print('=' * 12 + 'Desafio 58' + '=' * 12)
pc = randint(0, 10)
tentativas = 1
adv = int(input('O computador pensou em qual número? '))
while adv != pc:
    tentativas += 1
    if adv < pc:
        print('Maior, tente novamente!')
    else:
        print('Menor, tente novamente!')
    adv = int(input('O computador pensou em qual número? '))
if tentativas == 1:
    print('Você acertou de primeira!')
else:
    print(f'Você acertou em {tentativas} tentativas!')
