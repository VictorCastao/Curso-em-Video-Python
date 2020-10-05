print('=' * 12 + 'Desafio 105' + '=' * 12)


def Notas(*valores, sit=False):
    """A função consiste de dois parâmetros:
    -Valores: indica as notas do aluno, cuja quantidade é variada.
    -Sit: indica se a situação deverá ou não ser mostrada (é falsa por padrão).
A função retorna um dicionário contendo a maior e a menor nota, bem como a média e, por fim, a situação (caso seja ativada)."""

    soma = 0
    valores = sorted(valores)
    info = dict()
    info['Total'] = len(valores)
    info['Maior'] = valores[-1]
    info['Menor'] = valores[0]

    for c in valores:
        soma += c

    media = float(soma / len(valores))
    info['Média'] = media

    if sit == True:
        if media < 5:
            info['Situação'] = 'Ruim'
        elif 5 <= media < 7:
            info['Situação'] = 'Razoável'
        else:
            info['Situação'] = 'Boa'

    return info


result = Notas(10, 2, 9, sit=True)
print(result)
help(Notas)