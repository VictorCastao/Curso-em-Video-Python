print('=' * 12 + 'Desafio 87' + '=' * 12)
matriz = [[], [], []]
somapar = somaterceiro = maiorsegundo = val = 0
for i in range(3):
    for j in range(3):
        print(f'Digite o valor da posição ({i + 1},{j + 1}): ', end='')
        val = int(input())
        matriz[i].append(val)
        if val % 2 == 0:
            somapar += val
        if i == 1 and (maiorsegundo == 0 or val > maiorsegundo):
            maiorsegundo = val
        if j == 2:
            somaterceiro += val
print('A matriz informada é:')
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma da terceira coluna é {somaterceiro}.')
print(f'O maior valor da segunda linha é {maiorsegundo}.')
