print('=' * 12 + 'Desafio 44' + '=' * 12)
valor = float(input('Informe o valor do produto: R$ '))
print("""As opções de pagamento são as seguintes:
1 - À vista (dinheiro/cheque)
2 - À vista (cartão)
3 - Parcelado em 2x (cartão)
4 - Parcelado em 3x ou mais (cartão)""")
opcao = int(input('Opção escolhida: '))
if opcao < 1 or opcao > 4:
    print('Opção inválida!')
elif opcao == 1:
    print(f'O produto terá desconto de 10%, passando a custar R$ {0.9 * valor:.2f}')
elif opcao == 2:
    print(f'O produto terá desconto de 5%, passando a custar R$ {0.95 * valor:.2f}')
elif opcao == 3:
    print(f'O valor não terá o preço alterado, custando os mesmos R$ {valor:.2f}')
    print(f'Cada uma das duas parcela custará R$ {valor / 2:.2f}')
else:
    parcela = int(input('Digite o número de parcelas: '))
    if parcela <= 2:
        print('Número de parcelas inválido!')
    else:
        print(f'O produto terá uma taxa de juros de 20%, passando a custar R$ {valor * 1.2:.2f}')
        print(f'Dividido em {parcela} vezes, cada parcela custará R$ {valor * 1.2 / parcela:.2f}')
