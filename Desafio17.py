from math import hypot

print('='*12+'Desafio 17'+'='*12)
cateto1 = float(input('Digite o cateto oposto: '))
cateto2 = float(input('Digite o cateto adjacente: '))
print(f'A hipotenusa é {hypot(cateto1,cateto2):.2f}!')
