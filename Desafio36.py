print('=' * 12 + 'Desafio 36' + '=' * 12)
varcasa = float(input('Digite o valor da casa: R$ '))
salcomp = float(input('Informe o salário do comprador: R$ '))
anos = float(input('Digite o número de anos em que a casa será paga: '))
meses = anos * 12
parcela = varcasa / meses
aprovado = parcela / salcomp
if aprovado > 0.3:
    print('Infelizmente, seu empréstimo foi negado!!!')
else:
    print(f"""Parabéns!!! Seu empréstimo foi aprovado.
A casa, de valor R$ {varcasa:.2f}, será paga em {meses:.0f} meses, com parcela mensal de R$ {parcela:.2f}!""")
