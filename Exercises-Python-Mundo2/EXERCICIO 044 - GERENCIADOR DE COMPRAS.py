print('{:=^40}'.format(' LOJAS DO GARCIA '))
preço = float(input('Qual o valor das compras: R$ '))
print(''' FORMAS DE PAGAMENTO:
[1] `a vista - dinheiro ou cheque
[2]  à vista - cartão
[3] 2x - cartão
[4] 3x ou mais - cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('O valor da sua compra à vista recebeu um desconto de 10% e saiu por R${:.2f}'.format(total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('O valor da sua compra à vista no CARTÃO recebeu um desconto de 5% e saiu por R${:.2f}'.format(total))
elif opção == 3:
    parcelas = preço / 2
    print('O valor da sua compra {} à vista dividido em 2 vezes de {} '.format(preço, parcelas))
elif opção == 4:
    parcelas = int(input('Informe o número de parceçelas: '))
    parcels_jours = (preço + (preço * 20 / 100))
    preço_div = preço / parcelas
    total = (preço_div + (preço_div * 20 / 100)) * parcelas
    print('O valor da sua compra de R${:.2f} parcelado em {} vezes de R${} sairá por R${:.2f} '.format(preço, parcelas, parcels_jours, total))
