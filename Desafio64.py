print('=' * 12 + 'Desafio 64' + '=' * 12)
soma = 0
numero = int(input('Digite um número [999 para sair]: '))
contador = 0
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um número [999 para sair]: '))
print(f'Você digitou {contador} números e a soma deles é {soma}!')
