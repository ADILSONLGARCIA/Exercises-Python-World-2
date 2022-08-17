resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Informe um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar [S/N]: ')).upper().split()[0]
media = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
