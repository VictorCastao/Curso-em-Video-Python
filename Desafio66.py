print('=' * 12 + 'Desafio 66' + '=' * 12)
soma = numeros = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    else:
        soma += n
        numeros += 1
print(f'Foram digitados {numeros} números, e a soma deles é {soma}.')
