from math import sin, cos, tan, radians

print('='*12+'Desafio 18'+'='*12)
ang = float(input('Digite o ângulo em graus: '))
print(f'Seno = {sin(radians(ang)):.2f} \nCosseno = {cos(radians(ang)):.2f} \nTangente = {tan(radians(ang)):.2f}')
