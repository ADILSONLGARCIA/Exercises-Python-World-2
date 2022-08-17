from random import randint
from time import sleep
tentativas = 1
sorteio = randint(0, 10)
#faz o computador "pensar"
print('-_-_-_-' * 10)
print('Vou pensar em um número entre 0 e 10, tente advinhar...')
print('-_-_-_-' * 10)
jogador = int(input('Em que número eu pensei? '))
#jogador meio que tenta advinhar
print('Processando ...')
sleep(1)
while sorteio != jogador:
    tentativas = tentativas + 1
    jogador = int(input('Em que número eu estou pensando? '))
    print('Voce ERROU ! ! !')
    print('Tente de novo ! ! !')
print('PARABÉNS você conseguiu advinhar ! ! !')
print('O número que pensei foi {} e o número apontado por você foi {}.'.format(sorteio, jogador))
print('Você levou {} tentativas para acertar'.format(tentativas))
print('-_-_-_-' * 10)

''' if sorteio > jogador:
    print('Está quente! Número pensado é maior...')
    else:
    print('Está frio! Número pensado é menor...')'''