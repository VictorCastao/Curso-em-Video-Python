from random import randint
print('='*12+'Desafio 28'+'='*12)
aleatorio = randint(0,5)
adv = int(input('Digite o possível número: '))
if adv == aleatorio:
    print('Você Ganhou!')
else:
    print(f'Você Perdeu! O número certo seria o {aleatorio}.')
