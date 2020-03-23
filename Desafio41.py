from datetime import datetime

print('=' * 12 + 'Desafio 41' + '=' * 12)
atual = datetime.now().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nascimento
cor = '\033[32m'
normal = '\033[m'
if idade < 0:
    print('Ano de nascimento inválido!')
elif idade <= 9:
    print(f'Idade: {cor}{idade}{normal} anos')
    print(f'Categoria: {cor}MIRIM{normal}')
elif idade <= 14:
    print(f'Idade: {cor}{idade}{normal} anos')
    print(f'Categoria: {cor}INFANTIL{normal}')
elif idade <= 19:
    print(f'Idade: {cor}{idade}{normal} anos')
    print(f'Categoria: {cor}JÚNIOR{normal}')
elif idade <= 25:
    print(f'Idade: {cor}{idade}{normal} anos')
    print(f'Categoria: {cor}SÊNIOR{normal}')
else:
    print(f'Idade: {cor}{idade}{normal} anos')
    print(f'Categoria: {cor}MASTER{normal}')
