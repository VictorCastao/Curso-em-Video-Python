print('=' * 12 + 'Desafio 89' + '=' * 12)
info = list()
aluno = list()
while True:
    aluno.append(input('Digite o nome: '))
    aluno.append(float(input('Digite a nota 1: ')))
    aluno.append(float(input('Digite a nota 2: ')))
    info.append(aluno[:])
    aluno.clear()
    resp = input('Deseja continuar [S/N]? ')
    if resp in 'Nn':
        break
print(f'{"N°":<3}{"Nome":<14}{"Média":>4}')
i = 0
for c in info:
    print(f'{i:<3}{c[0]:<14}{(c[1] + c[2]) / 2:>4.1f}')
    i += 1
while True:
    num = int(input('Deseja saber as notas de qual aluno [999 para sair]? '))
    if num == 999:
        break
    if num >= len(info):
        print('Número Inválido!')
        continue
    print(f'Nome: {info[num][0]}')
    print(f'Nota 1: {info[num][1]}')
    print(f'Nota 2: {info[num][2]}')
