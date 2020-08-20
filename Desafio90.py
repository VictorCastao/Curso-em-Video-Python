print('=' * 12 + 'Desafio 90' + '=' * 12)
pessoa = dict()
pessoa['Nome'] = input('Digite o nome do aluno: ')
print(f'Digite a média do(a) {pessoa["Nome"]}: ', end='')
pessoa['Média'] = float(input())
if pessoa['Média'] >= 7:
    pessoa['Situação'] = 'Aprovado(a)'
elif pessoa['Média'] < 5:
    pessoa['Situação'] = 'Reprovado(a)'
else:
    pessoa['Situação'] = 'Recuperação'
print('Resultado:')
print(f'Nome: {pessoa["Nome"]}')
print(f'Média: {pessoa["Média"]}')
print(f'Situação: {pessoa["Situação"]}')
