print('='*12+'Desafio 35'+'='*12)
l1 = float(input('Digite o comprimento 1: '))
l2 = float(input('Digite o comprimento 2: '))
l3 = float(input('Digite o comprimento 3: '))
if (l1+l2)>l3 and (l1+l3)>l2 and (l2+l3)>l1:
    print(f'As retas de comprimento {l1}, {l2} e {l3} podem formar um triângulo!')
else:
    print(f'As retas de comprimento {l1}, {l2} e {l3} não podem formar um triângulo!')
