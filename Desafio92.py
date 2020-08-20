from datetime import datetime

print('=' * 12 + 'Desafio 92' + '=' * 12)
ano = datetime.today().year
pessoa = dict()
pessoa['Nome'] = input('Digite o nome: ')
pessoa['Idade'] = ano - int(input('Digite o ano de nascimento: '))
pessoa['CTPS'] = int(input('Digite o número da CTPS (digite 0 se não possuir): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['Salário'] = float(input('Digite o salário: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] - (ano - pessoa['Ano de Contratação']) + 35
print('==Informações==')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')