print('=' * 12 + 'Desafio 43' + '=' * 12)
peso = float(input('Informe sua massa (em kg): '))
altura = float(input('Digite sua altura (em m): '))
imc = peso / (altura ** 2)
print(f'IMC: {imc:.1f}')
if imc < 18.5:
    print('Categoria: ABAIXO DO PESO')
elif imc < 25.0:
    print('Categoria: PESO IDEAL')
elif imc < 30.0:
    print('Categoria: SOBREPESO')
elif imc < 40.0:
    print('Categoria: OBESIDADE')
else:
    print('Categoria: OBESIDADE MÓRBIDA')
