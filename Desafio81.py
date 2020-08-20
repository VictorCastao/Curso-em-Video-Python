print('=' * 12 + 'Desafio 81' + '=' * 12)
lista = []
contador = 0
while True:
    var = int(input('Digite um valor: '))
    contador += 1
    lista.append(var)
    resp = input('Deseja continuar [S/N]? ').strip().upper()
    if resp == 'N':
        break
print(f'Foram digitados {contador} valores!')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista!')
else:
    print('O número 5 não foi digitado e não está na lista!')
