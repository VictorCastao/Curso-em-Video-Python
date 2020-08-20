print('=' * 12 + 'Desafio 94' + '=' * 12)
pessoa = dict()
cadastros = list()
while True:
    pessoa['Nome'] = input('Digite o nome: ')
    pessoa['Idade'] = int(input('Digite a idade: '))
    pessoa['Sexo'] = input('Digite o sexo [M/F/O]: ').strip().upper()[0]
    while pessoa['Sexo'] not in 'MFO':
        pessoa['Sexo'] = input('Caractere inválido! Digite o sexo novamente[M/F/O]: ').strip().upper()[0]
    cadastros.append(pessoa.copy())
    resposta = input('Pessoa cadstrada! Deseja continuar [S/N]? ').strip().upper()[0]
    while resposta not in 'SN':
        resposta = input('Caractere inválido! Digite novamente se deseja continuar [S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break
print('\nRespostas:')
print(f'A) Foram cadastradas {len(cadastros)} pessoas.')
soma = 0
media = 0.0
for c in cadastros:
    soma += c['Idade']
media = soma / len(cadastros)
print(f'B) A média de idade é {media:.1f} anos.')
mulheres = list()
for c in cadastros:
    if c['Sexo'] == 'F':
        mulheres.append(c['Nome'])
print(f'C) Existem {len(mulheres)} mulheres no cadastro, que são: ', end='')
for c in mulheres:
    print(c, end=' | ')
print()
acima = list()
for c in cadastros:
    if c['Idade'] > media:
        acima.append(c['Nome'])
print(f'D) Existem {len(acima)} pessoas com idade acima da média, que são: ', end='')
for c in acima:
    print(c, end=' | ')
print()
