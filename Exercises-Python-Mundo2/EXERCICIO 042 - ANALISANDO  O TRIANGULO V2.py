print(' ** ANALISANDO SE AS 3 RETAS PODEM FORMAR UM TRIANGULO E QUAL SEU TIPO **')
lado_a = float(input('Informe o valor da primeira reta:'))
lado_b = float(input('Informe o valor da segunda reta:'))
lado_c = float(input('Informe o valor da terceira reta:'))
if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Os seguimentos acima podem formar um TRIANGULO ', end='')
    if lado_a == lado_b == lado_c:
        print('EQUILATERO!')
    elif lado_a != lado_b != lado_c:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os seguimentos acima NÃO podem formar um TRIANGULO!')
