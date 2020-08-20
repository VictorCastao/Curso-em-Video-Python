print('=' * 12 + 'Desafio 79' + '=' * 12)
resp = 'S'
lista = []
while resp == 'S':
    a = int(input("Digite um valor: "))
    if a in lista:
        print("Número não adicionado (já existente na lista)!")
    else:
        lista.append(a)
        print("Número adicionado!")
    resp = input("Deseja continuar[S/N]? ").strip().upper()
lista.sort()
print(f"Os números digitados foram:\n{lista}")
