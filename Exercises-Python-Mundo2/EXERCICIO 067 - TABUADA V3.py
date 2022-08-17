c = 0
while True:
    tabuada = int(input('Qual tabuada quer ver? Informe: '))
    if tabuada < 0:
      break
    for c in range (1, 11):
        print(f'{tabuada} x {c} = {tabuada * c}' )
print('FIM')
