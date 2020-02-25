from random import sample

print('='*12+'Desafio 20'+'='*12)
nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')
nome4 = input('Digite o nome do aluno 4: ')
print(f'A ordem escolhida para apresentação é:\n{sample([nome1,nome2,nome3,nome4],k=4)}')