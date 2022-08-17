acumulador = 0
contador = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        acumulador += cont
        contador += 1
print('A soma dos {} número divisiveis por três é {}'.format(contador, acumulador))
print('FIM!')
