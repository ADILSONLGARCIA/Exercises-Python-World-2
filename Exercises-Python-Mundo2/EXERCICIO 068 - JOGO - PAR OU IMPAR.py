from random import randint
vitoria = 0
while True:
    jogador = int(input('Informe um numero: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo: str = ''
    tipo: str = ( input ( 'Par ou Ímpar? [P/I]: ' ) ).strip ().upper ()[0]
    while tipo not in 'PI':
        '''tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]'''
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 ==0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print ( 'Você Venceu!' )
            vitoria += 1
        else :
            print ( 'Você perdeu!' )
            break
    print('Vamos jogar novamente...')
print(f'FIM DE JOGO! Você venceu {vitoria} vezes.')

