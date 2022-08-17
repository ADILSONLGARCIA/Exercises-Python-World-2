n = soma = cont = 0
n = int(input('Informe um número [999 para sair]: '))
while n != 999:
    cont += 1
    soma += n
    n = int ( input ( 'Informe um número [999 para sair]: ' ) )
print('Foram somados {} entradas de números, onde o total desta soma é {}'.format(cont, soma))
print('CONCLUIDO')