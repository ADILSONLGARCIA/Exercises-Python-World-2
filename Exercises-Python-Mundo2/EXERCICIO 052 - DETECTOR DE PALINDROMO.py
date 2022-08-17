frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('O inverso de {} é {}'.format(junto, inverso))
    print('Temos um palindromo!')
else:
    print('O inverso de {} é {}'.format(junto, inverso))
    print('A frase digitada não é um palindromo.')


