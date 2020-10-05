from modulos import moeda3 as md

print('=' * 12 + 'Desafio 109' + '=' * 12)
moeda = input('Digite a moeda: ')
valor = float(input(f'Digite o valor em {moeda}: '))
print(f'O dobro de {moeda} {md.moeda(valor)} é {moeda} {md.dobro(valor, formatar=True)}.')
print(f'A metade de {moeda} {md.moeda(valor)} é {moeda} {md.metade(valor, formatar=True)}.')
print(f'Aumentando 10% de {moeda} {md.moeda(valor)}, temos {moeda} {md.aumentar(valor, 10, formatar=True)}.')
print(f'Diminuindo 10% de {moeda} {md.moeda(valor)}, temos {moeda} {md.diminuir(valor, 10, formatar=True)}.')
