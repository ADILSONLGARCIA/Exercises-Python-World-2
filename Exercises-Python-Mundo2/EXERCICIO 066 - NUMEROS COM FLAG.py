num=soma=cont=0
while True:
    num = int(input('informe um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram somados {cont} números.')
print(f'A soma entre os números foi {soma}')
