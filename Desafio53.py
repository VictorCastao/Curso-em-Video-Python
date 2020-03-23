print('=' * 12 + 'Desafio 53' + '=' * 12)
frase = input('Digite sua frase: ')
frase = frase.strip().replace(" ","").upper()
tamanho = len(frase)
contador = 0
igual = 0
for i in range(tamanho - 1, -1, -1):
    if frase[contador] == frase[i]:
        igual += 1
    contador += 1
if contador == tamanho:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
