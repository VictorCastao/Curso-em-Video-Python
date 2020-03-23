print('=' * 12 + 'Desafio 56' + '=' * 12)
nomehomem = 'Não'
idadetotal = 0
idadevelho = 0
mulheres = 0
for i in range(0, 4):
    print('=' * 28)
    nome = input(f'Digite o nome da pessoa {i + 1}: ').strip()
    idade = int(input(f'Digite a idade da pessoa {i + 1}: '))
    sexo = input(f'Digite o sexo da pessoa {i + 1} (M ou F): ').strip().upper()
    idadetotal += idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M' and idade > idadevelho:
        nomehomem = nome
        idadevelho = idade
print('===Resultado===')
print(f'A média das 4 idades é {idadetotal / 4:.1f} anos.')
if nomehomem == 'Não':
    print('Não há homens.')
else:
    print(f'O nome do homem mais velho é {nomehomem} e ele tem {idadevelho} anos.')
print(f'Existem {mulheres} mulheres com menos de 20 anos.')
