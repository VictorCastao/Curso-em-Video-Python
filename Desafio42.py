print('=' * 12 + 'Desafio 42' + '=' * 12)
a = float(input('Digite o lado 1: '))
b = float(input('Digite o lado 2: '))
c = float(input('Digite o lado 3: '))
if a + b > c and a + c > b and b + c > a:
    print(f'As medidas {a}, {b} e {c} PODEM formar um triângulo!')
    if a == b and b == c:
        print('Esse triângulo é do tipo EQUILÁTERO!')
    elif a == b or b == c or c == a:
        print('Esse triângulo é do tipo ISÓCELES!')
    else:
        print('Esse triângulo é do tipo ESCALENO!')
else:
    print(f'As medidas {a}, {b} e {c} NÃO PODEM formar um triângulo!')
