n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
opcao = 0
resultado = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair''')
    opcao = int(input('Informe uma opção: '))
    if opcao == 1:
        resultado = n1 + n2
        print('O valor da soma é: {}'.format(resultado))
    elif opcao == 2:
        resultado = n1 * n2
        print('O valor da multiplicação é: {}'.format(resultado))
    elif opcao == 3:
        if n1 > n2:
            print('O maior valor é {}'.format(n1))
        else:
            print('O maior valor é {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Informe o outro número: '))
        n2 = int(input('Informe o segundo número: '))
    else:
        print('Opção inválida, informe a opção de [1 - 5]')
print('FIM')

