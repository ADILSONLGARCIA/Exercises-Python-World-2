print ( 'VAMOS INFORMAR 10 TERMOS DA PA' )
print ( 10 * '=*' )
primeiro = int ( input ( 'Digite o primeiro termo da PA: ' ) )
razão = int ( input ( 'Informe a Razão: ' ) )
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0 :
    total += mais
    while cont <= total :
        print ( '{} -> '.format ( termo ), end = '' )
        termo += razão
        cont += 1
    print ( 'PAUSADO...' )
    mais = int ( input ( 'Quantos terms mais? Informe: ' ) )
print ( 'Progressão finalizada com sucesso! Foram informados {} termos.'.format ( total ) )
