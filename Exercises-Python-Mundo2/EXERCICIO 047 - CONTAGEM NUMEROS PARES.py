from time import sleep
for c in range(2, 52, 2):
    sleep(0.5)
    print(c, end='')
    print(',', end='')
sleep(0.5)
print('FIM!')
