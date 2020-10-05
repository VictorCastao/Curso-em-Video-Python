from utilidadesCeV import moeda as md

print('=' * 12 + 'Desafio 111' + '=' * 12)
un = input('Digite a moeda: ')
val = float(input(f'Digite a quantidade, em {un}: '))
ta = float(input('Digite a porcentagem de aumento: '))
tr = float(input('Digite a porcentagem de redução: '))
op = input('Desejará a formatação [S/N]: ').strip().upper()
if op[0] == 'S':
    op = True
else:
    op = False
md.resumo(un, val, ta, tr, op)
