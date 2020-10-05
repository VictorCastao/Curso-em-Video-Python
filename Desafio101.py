from datetime import datetime


def voto(nascimento):
    global ano
    idade = ano - nascimento
    if idade < 16:
        return f'Com {idade} anos, sua situação de voto é: PROIBIDO'
    elif idade >= 18 and idade <= 65:
        return f'Com {idade} anos, sua situação de voto é: OBRIGATÓRIO'
    else:
        return f'Com {idade} anos, sua situação de voto é: OPCIONAL'


print('=' * 12 + 'Desafio 101' + '=' * 12)
ano = datetime.now().year
data = int(input('Digite o ano de nascimento: '))
resp = voto(data)
print(resp)
