from datetime import datetime

print('=' * 12 + 'Desafio 54' + '=' * 12)
maiores = 0
menores = 0
ano = datetime.today().year
for i in range(0, 7):
    nascimento = int(input(f'Digite o ano de nascimento {i + 1}: '))
    if ano - nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print('Após a contagem, o resultado foi:')
print(f'{maiores} pessoas atingiram a maioridade.')
print(f'{menores} pessoas não atingiram a maioridade.')
