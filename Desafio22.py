print('='*12+'Desafio 22'+'='*12)
nome = input('Digite seu nome completo: ')
nome = nome.strip()
maiusculo = nome.upper()
minusculo = nome.lower()
letras = len(nome) - nome.count(' ')
separar = nome.split()
tam = len(separar[0])
print(f'Nome maiúsculo: {maiusculo}')
print(f'Nome minúsculo: {minusculo}')
print(f'Número de letras: {letras}')
print(f'Letras do primeiro nome: {tam}')