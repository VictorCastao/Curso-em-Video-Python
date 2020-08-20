print('=' * 12 + 'Desafio 76' + '=' * 12)
tupla = (
    'Arroz', 9.5, 'Feijão', 4.5, 'Batata', 2.3, 'Café', 7.7, 'Leite', 2.8, 'Rúcula', 3.5, 'Nescau', 11, 'Tomate', 4.5)
tamanho = len(tupla)
preço = 1
produto = 0
print('==========TABELA DE PREÇOS==========')
while preço < tamanho or produto < tamanho:
    print(f'{tupla[produto]:.<25} R$ {tupla[preço]:>6.2f}')
    preço += 2
    produto += 2
print('=' * 36)
