print('=' * 12 + 'Desafio 96' + '=' * 12)


def area(largura, comprimento):
    print(f'A área do terreno é {largura * comprimento:.1f} m².')


print('CÁLCULO DE ÁREA')
a = float(input('Digite a largura (m): '))
b = float(input('Digite o comprimento (m): '))
area(a, b)
