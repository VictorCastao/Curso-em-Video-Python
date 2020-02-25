print('=' * 12 + 'Desafio 34' + '=' * 12)
sal = float(input('Digite o salário: '))
if sal > 1250:
    print(f'O novo salário será R$ {sal * 1.1:.2f}')
else:
    print(f'O novo salário será R$ {sal * 1.15:.2f}')
