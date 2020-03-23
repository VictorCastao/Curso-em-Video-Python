print('=' * 12 + 'Desafio 65' + '=' * 12)
soma = contador = maior = menor = 0
continuar = 'S'
while continuar != 'N':
    numero = int(input('Digite um número: '))
    contador += 1
    soma += numero
    if contador == 1:
        maior = menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    continuar = input('Deseja continuar [S/N]: ').strip().upper()
print(f"""Você digitou {contador} números.
A média deles é {soma / contador:.2f}.
O maior número foi {maior}.
O menor número foi {menor}.""")
