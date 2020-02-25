from datetime import datetime

print('=' * 12 + 'Desafio 39' + '=' * 12)
ano = datetime.now().year
nasc = int(input('Informe o ano de nascimento: '))
idade = ano - nasc
if idade == 18:
    print(f'Este ({ano}) é o ano correto para realizar seu alistamento militar. Aliste-se!')
elif idade > 18:
    print(
        f'Seu alistamento militar deveria ser feito {idade - 18} anos atrás (ou seja, em {ano - (idade - 18)}). Se for o caso, regularize sua situação!')
else:
    print(
        f'Você deverá se alistar ao serviço militar daqui a {18 - idade} anos (ou seja, em {18 - idade + ano}). Fique atento a essa data!')
