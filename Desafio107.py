from modulos import moeda
print('=' * 12 + 'Desafio107' + '=' * 12)
numero = float(input('Digite o valor em R$: '))

print(f'O dobro de R$ {numero} é R$ {moeda.dobro(numero)}.')
print(f'A metade de R$ {numero} é R$ {moeda.metade(numero)}.')
print(f'Aumentando 10% de R$ {numero}, temos R$ {moeda.aumentar(numero,10)}.')
print(f'Diminuindo 10% de R$ {numero}, temos R$ {moeda.diminuir(numero,10)}.')