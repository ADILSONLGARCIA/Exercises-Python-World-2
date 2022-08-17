print('-_' * 25)
print('CALCULO SEQUÊNCIA DE FIBONACCI')
print('-_' * 25)
cont = 3
n = int(input('Informe a quantidade de sequências que deseja: '))
t1 = 0
t2 = 1
print('-_' * 25)
print('{}->{}->'.format(t1, t2), end = '')
while cont <= n:
    t3 = t1 + t2
    print('{}->'.format(t3), end ='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('FIM')
