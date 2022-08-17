cond = 'S'
cont = soma = media = maior = 0
menor = 99
while cond != 'N':
    num = int(input('Informe um número: '))
    cond = str(input('Deseja continuar [S/N]: ')).upper().split()[0]
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num <= menor:
        menor = num
media = (soma / cont)
print('A soma dos números foi {} e a média é {}'.format(soma, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
