print('=' * 12 + 'Desafio 40' + '=' * 12)
notaa = float(input('Digite a primeira nota: '))
notab = float(input('Digite a segunda nota: '))
media = (notaa + notab) / 2
if media < 5.0:
    print(f'Sua média foi {media:.1f} e você foi REPROVADO!')
elif media >= 7.0:
    print(f'Sua média foi {media:.1f} e você foi APROVADO!')
else:
    print(f'Sua média foi {media:.1f} e você está de RECUPERAÇÃO!')
