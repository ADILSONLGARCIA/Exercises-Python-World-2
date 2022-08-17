print ( 'VAMOS INFORMAR 10 TERMOS DA PA' )
primeiro = int ( input ( 'Digite o primeiro termo da PA: ' ) )
razão = int( input ( 'Informe a Razão: ' ) )
décimo = primeiro + (10 - 1) * razão
for c in range ( primeiro, décimo + razão, razão ) :
    print ( '{} '.format ( c ), end = '-> ' )
print ( 'Acabou' )
