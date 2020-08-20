print('=' * 12 + 'Desafio 86' + '=' * 12)
matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        print(f'Digite o valor da posição ({i+1},{j+1}): ', end='')
        matriz[i].append(int(input()))
print('A matriz informada é:')
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()