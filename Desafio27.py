print('=' * 12 + 'Desafio 27' + '=' * 12)
var = input('Digite o nome: ')
nome = var.strip().split()
print(f"""Muito prazer em te conhecer!
Primeiro nome: {nome[0]}.
Último nome: {nome[len(nome)-1]}.""")
