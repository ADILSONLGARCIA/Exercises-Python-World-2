maior = 0
menor = 0
for count in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(count)))
    if count == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso é {} Kg.'.format(menor))
print('O maior peso é {} Kg.'.format(maior))
