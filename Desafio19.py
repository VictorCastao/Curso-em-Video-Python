from random import choice

print('=' * 12 + 'Desafio 19' + '=' * 12)
nome1 = input('Digite o aluno 1: ')
nome2 = input('Digite o aluno 2: ')
nome3 = input('Digite o aluno 3: ')
nome4 = input('Digite o aluno 4: ')
print(f'O aluno escolhido foi {choice([nome1, nome2, nome3, nome4])}.')
