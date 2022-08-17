cont = dmaior = masc = femi = idade = 0
continuar = sexo =' '
while True:
    idade = int(input('Quantos anos você tem? '))
    if idade >= 18:
        dmaior += 1
    sexo = str ( input ( 'Informe [M/F]: ' ) ).strip ().upper ()[0]
    if sexo in 'Mm':
        masc += 1
    if sexo in 'Ff':
        if idade < 20:
            femi += 1
    continuar = str (input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print(f'Tivemos {dmaior} pessoas maiores de 18 anos.')
print(f'Tivemos {masc} pessoas do sexo nasculino.')
print(f'Tivemos {femi} mulheres menores de 20 anos.')
