print("============Desafio 8============")
entrada = float(input('Digite o valor em metros: '))
decimetro = entrada *10
centimetro = entrada * 100
milimetros = entrada * 1000
decametro = entrada / 10
hectometro = entrada / 100
kilometro = entrada / 1000
print('{0} metros equivalem a: \n{1} decímetros \n{2} centímetros \n{3} milímetros \n{4} decâmetros \n{5} hectômetros \n{6} quilômetros'.format(entrada, decimetro, centimetro, milimetros, decametro, hectometro, kilometro))