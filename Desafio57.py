print('=' * 12 + 'Desafio 57' + '=' * 12)
sexo = input('Digite o sexo [M/F/O]: ').strip().upper()
while sexo != 'M' and sexo != 'F' and sexo != 'O':
    print('Opção inválida! Digite novamente.')
    sexo = input('Digite o sexo [M/F/O]: ').strip().upper()
if sexo == 'M':
    print('\nSexo: Masculino')
elif sexo == 'F':
    print('\nSexo: Feminino')
else:
    print('\nSexo: Outro / Não especificado')
