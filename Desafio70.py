print('=' * 12 + 'Desafio 70' + '=' * 12)
barato = total = maisde1000 = produtos = 0
nomebarato = 'Nada'
while True:
    print('=====CADASTRAR PRODUTO=====')
    produto = input('Digite o nome do produto: ').strip()
    preço = float(input('Digite o preço do produto: R$ '))
    if nomebarato == 'Nada':
        nomebarato = produto
        barato = preço
    else:
        if preço < barato:
            barato = preço
            nomebarato = produto
        if preço > 1000:
            maisde1000 += 1
        produtos += 1
        total += preço
    print('=====PRODUTO CADASTRADO=====')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break
print('=====CADASTRAMENTO ENCERRADO=====')
print(f"""Foram cadastrados {produtos} produtos.
O total gasto foi R$ {total:.2f}.
O produto mais barato é {nomebarato} e custa R$ {barato:.2f}.
{maisde1000} produtos custaram mais de R$ 1000.00.""")
