num1 = int(input('Informe o peimeiro número:'))
num2 = int(input('Informe o segundo número:'))
if num1 > num2:
    print('O maior número é {}'.format(num1))
elif num1 < num2:
    print('O maior número é {}'.format(num2))
else:
    print('Os números são iguais!')
