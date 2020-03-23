print('=' * 12 + 'Desafio 69' + '=' * 12)
maisde18 = homens = mulheres20 = pessoas = 0
while True:
    print('=====CADASTRE UMA PESSOA=====')
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Informe o sexo [M/F]: ').strip().upper()[0]
    if idade > 18:
        maisde18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    pessoas += 1
    print('=====PESSOA CADASTRADA=====')
    opção = ' '
    while opção not in 'SN':
        opção = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if opção == 'N':
        break
print(f"""
CADASTRAMENTO ENCERRADO!
Foram cadastradas {pessoas} pessoas.
Existem {maisde18} pessoas maiores de 18 anos.
Existem {homens} homens.
Existem {mulheres20} mulheres menores de 20 anos.""")
