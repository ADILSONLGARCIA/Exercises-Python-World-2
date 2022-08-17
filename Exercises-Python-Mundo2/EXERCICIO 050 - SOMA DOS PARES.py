soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Foi informado {} número(s) par(es) e a sua soma foi {}'.format(cont, soma))
