print ( 'VAMOS INFORMAR 10 TERMOS DA PA' )
primeiro = int ( input ( 'Digite o primeiro termo da PA: ' ) )
razão = int ( input ( 'Informe a Razão: ' ) )
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM!')

