from random import randint
from time import sleep

print('=' * 12 + 'Desafio 45' + '=' * 12)
print("""As opções são as seguintes:
1 - Pedra
2 - Papel
3 - Tesoura""")
pc = randint(1, 3)
escolha = int(input('Digite sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 15)
if escolha < 1 or escolha > 3:
    print('Opção inválida!')

elif pc == 1 and escolha == 2:
    print("""O computador escolheu PEDRA
Você esolheu PAPEL
     
Você GANHOU!""")
elif pc == 1 and escolha == 3:
    print("""O computador escolheu PEDRA
Você escolheu TESOURA
     
Você PERDEU!""")
elif pc == 2 and escolha == 1:
    print("""O computador escolheu PAPEL
Você escolheu PEDRA
     
Você PERDEU!""")
elif pc == 2 and escolha == 3:
    print("""O computador escolheu PAPEL 
Você escolheu TESOURA
    
Você GANHOU!""")
elif pc == 3 and escolha == 1:
    print("""O computador escolheu TESOURA
Você escolheu PEDRA
     
Você GANHOU!""")
elif pc == 3 and escolha == 2:
    print("""O computador escolheu TESOURA
Você escolheu PAPEL
     
Você PERDEU!""")
else:
    a = 'NADA'
    if pc == 1:
        a = 'PEDRA'
    elif pc == 2:
        a = 'PAPEL'
    else:
        a = 'TESOURA'
    print(f"""O computador escolheu {a}
Você escolheu {a}

EMPATE!""")
