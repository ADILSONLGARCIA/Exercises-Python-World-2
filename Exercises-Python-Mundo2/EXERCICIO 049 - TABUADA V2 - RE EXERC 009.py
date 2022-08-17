Num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} X {} = {:2}'.format(Num, c, Num * c))
