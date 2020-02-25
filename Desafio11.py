print("============Desafio 11============")
largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
area = largura * altura
tinta = area / 2.0
print('A área de sua parede equivale a {:.2f} m², e para pintá-la, são necessários {:.2f} l de tinta'.format(area, tinta))
