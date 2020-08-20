print('=' * 12 + 'Desafio 83' + '=' * 12)
pilha = []
str = input('Digite a expressão: ')
resposta = True
for char in str:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if len(pilha) == 0:
            resposta = False
            break
        else:
            pilha.pop()
if len(pilha) != 0:
    resposta = False
if resposta:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')
