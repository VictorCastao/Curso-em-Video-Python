print('=' * 12 + 'Desafio 73' + '=' * 12)
tabelabrasileirao = (
    "Flamengo", "Santos", "Palmeiras", "Grêmio", "Athletico-PR", "São Paulo", "Internacional", "Corinthians",
    "Fortaleza", "Goiás", "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Botafogo", "Ceará", "Cruzeiro", "CSA",
    "Chapecoense", "Avaí")
print(f'Os 5 primeiros colocados são: {tabelabrasileirao[:5]}')
print(f'Os 4 últimos colocados são: {tabelabrasileirao[16:]}')
print(f"""A ordem alfabética dos times é:
{sorted(tabelabrasileirao)}""")
print(f'A Chapecoense está na {tabelabrasileirao.index("Chapecoense")+1}ª posição.')
