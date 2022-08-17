sexo = str(input('Por favor, insira o sexo do bebê [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite os dados corretos M para Masculino e F para feminino. Digite o sexo: '))
print('O sexo {} inserido com suxesso.'.format(sexo))
