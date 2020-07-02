print('=' * 12 + 'Desafio 72' + '=' * 12)
numeros = (
'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while escolha < 0 or escolha > 20:
        escolha = int(input('Número Inválido. Digite outro número: '))
    print(f'O número escolhido foi "{numeros[escolha]}"')
    resp = input("Deseja continuar? [S/N] ").strip().upper()
    while resp[0] not in "SN":
        resp = input("Deseja continuar? [S/N] ").strip().upper()
    if resp == 'N':
        break
