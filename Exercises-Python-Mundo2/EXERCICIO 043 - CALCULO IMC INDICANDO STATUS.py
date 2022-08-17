peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)
print('Sua altura é {} com {:.1f} Kilos sendo assim seu IMC é {:.0f}'.format(altura, peso, imc))
if imc < 18.5:
    print('Você está ABAIXO do peso.')
elif imc > 18.5 and imc < 25:
    print('Você esta no seu peso IDEAL.')
elif imc > 25 and imc < 30:
    print('Você está com SOBREPESO.')
elif imc > 30 and imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está com OBESIDADE MORBIDA.')

