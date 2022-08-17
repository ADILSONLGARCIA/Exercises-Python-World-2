total = valor = nprod = valortot = vmil = cont = menor = 0
produto = status = ' '
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    valor = int( input( 'Quanro custa: R$ ' ) )
    cont += 1
    if valor > 1000:
        vmil += 1
    if cont == 1:
        menor = valor
    elif valor < menor:
        menor = valor
    status = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    nprod += 1
    valortot = valor + valortot
    if status in 'Nn':
        break
print(f'Foi comprado {nprod} produtos.')
print(f'O valor total da compra foi R$ {valortot:.2f}')
print(f'{vmil} produtos custaram mais de R$ 1000.00')
print(f'O produto de menor valor custou R$ {menor:.2f}')
