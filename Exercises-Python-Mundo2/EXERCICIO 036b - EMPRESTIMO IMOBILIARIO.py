casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar um imóvel de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser concedido!')
else:
    print(('Emprestimo NÃO SERÁ concedido').format(), end='')
    print(', devido a prestação atingir o limite de 30% do seu salário.')

