print('=' * 12 + 'Desafio 102' + '=' * 12)


def fatorial(num, show=False):
    """Função que calcula o fatorial de um número.
    Se n<=0, a função retorna 1.
    Se show=True, os processos de multiplicação são mostrados. Caso contrário, somente o resultado é mostrado.
    O retorno da função, em todos os casos, é em forma de string (simplesmente para padronizar)."""
    resultado = 1
    copia = num
    resp = ""
    if num <= 0:
        return str(1)
    while num != 0:
        resultado *= num
        if show == True:
            if num == copia:
                resp += str(num)
            else:
                resp += f' X {num}'
        num -= 1
    if show == True:
        resp += f' = {resultado}'
    else:
        resp = str(resultado)
    return resp


print(fatorial(10))
