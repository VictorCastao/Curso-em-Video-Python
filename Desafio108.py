from modulos import moeda2

print('=' * 12 + 'Desafio 108' + '=' * 12)
moeda = input('Digite a moeda: ')
numero = float(input(f'Digite o valor em {moeda}: '))
numero = round(numero, 2)
print(f'O dobro de {moeda} {moeda2.moeda(numero)} é {moeda} {moeda2.dobro(numero)}.')
print(f'A metade de {moeda} {moeda2.moeda(numero)} é {moeda} {moeda2.metade(numero)}.')
print(f'Aumentando 10% de {moeda} {moeda2.moeda(numero)}, temos {moeda} {moeda2.aumentar(numero, 10)}.')
print(f'Diminuindo 10% de {moeda} {moeda2.moeda(numero)}, temos {moeda} {moeda2.diminuir(numero, 10)}.')
