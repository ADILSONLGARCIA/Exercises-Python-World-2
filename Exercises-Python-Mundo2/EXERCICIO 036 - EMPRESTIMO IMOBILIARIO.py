nome = str(input(' Informe o seu nome:'))
salario = float(input('Qual o salário:'))
imovel = float(input('Valor do imovel:'))
tempofin = int(input('Quantos meses para pagar? Informe:'))
financiamento = (imovel / tempofin)
if (salario /100 * 30) > financiamento:
    print('O financiamento do {} foi aprovado e sua parcela mensal ficará em R$ {}'.format(nome, financiamento))
else:
    print('O seu financiamento não foi aprovado, pois a prestação é maior que 30% do seu salário que é R${:.2f}'.format(financiamento))

