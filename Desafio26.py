print('='*12+'Desafio 26'+'='*12)
ent = input('Digite sua frase: ')
frase = ent.strip().upper()
letra = frase.count('A')
primvez = frase.find('A') + 1
ultvez = frase.rfind('A') + 1
print(f'A letra "A" aparece {letra} vezes.')
print(f'Sua primeira aparição é na posição {primvez}.')
print(f'Sua última aparição é na posição {ultvez}.')