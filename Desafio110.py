from modulos import moeda3 as m

print('=' * 12 + 'Desafio 110' + '=' * 12)
un = input('Digite a unidade monetária: ')
val = float(input(f'Digite o valor, em {un}: '))
ta = float(input('Digite, em %, a taxa de aumento: '))
td = float(input('Digite, em %, a taxa de redução: '))
op = input('Deseja formatar [S/N]: ').strip().upper()
if op[0] == 'S':
    fmt = True
else:
    fmt = False
m.resumo(un, val, ta, td, fmt)
