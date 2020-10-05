from time import sleep

print('=' * 12 + 'Desafio 98' + '=' * 12)


def contador(inicio, fim, intervalo):
    if intervalo == 0:
        intervalo = 1
    if inicio <= fim:
        intervalo = abs(intervalo)
    else:
        intervalo = abs(intervalo) * -1
    sleep(0.3)
    print(f'Contagem de {inicio} a {fim}, contando de {abs(intervalo)} em {abs(intervalo)}:')
    if inicio >= fim:
        while inicio >= fim:
            sleep(0.5)
            print(inicio, end=' ')
            inicio += intervalo
    else:
        while inicio <= fim:
            sleep(0.5)
            print(inicio, end=' ')
            inicio += intervalo
    sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
print()
contador(10, 0, 2)
print('\nAgora é sua vez! Digite os parâmetros:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print()
contador(i, f, p)
