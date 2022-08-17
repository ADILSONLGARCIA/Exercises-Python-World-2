from random import randint
from time import sleep
print('{:=^40}'.format(' JOGO JOKENPÔ '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print(computador)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 20)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0: #Jogador jogou PEDRA
        sleep(1)
        print('EMPATE')
    elif jogador == 1: #Jogador jogou PAPEL
        sleep(1)
        print('GANHOU')
    elif jogador == 2: # Jogador jogou TESOURA
        sleep(1)
        print('PERDEU')
if computador == 1: #Computador jogou PAPEL
    if jogador == 0: #Jogador jogou PEDRA
        print('PERDEU')
    elif jogador == 1: #Jogador jogou PAPEL
        sleep(1)
        print('EMPATOU')
    elif jogador == 2: # Jogador jogou TESOURA
        sleep(1)
        print('VENCEU')
if computador == 2: #Computador jogou TESOURA
    if jogador == 0: #Jogador jogou PEDRA
        sleep(1)
        print('VENCEU')
    elif jogador == 1: #Jogador jogou PAPEL
        sleep(1)
        print('PERDEU')
    elif jogador == 2: # Jogador jogou TESOURA
        sleep(1)
        print('EMPATOU')
else:
    print('Opção invalida! Tente novamente.')
print('{:=^40}'.format(' F I M '))
