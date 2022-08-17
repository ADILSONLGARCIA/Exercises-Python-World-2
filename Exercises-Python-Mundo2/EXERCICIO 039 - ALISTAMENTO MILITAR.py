from datetime import date
data_atual = date.today().year
nascimento = int(input('Digite o ano de nasciento: '))
idade_atual = data_atual - nascimento
print('O rapaz que nasceu em {} tem agora {} anos em {}.'.format(nascimento, idade_atual, data_atual))
if idade_atual == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade_atual < 18:
    falta = 18 - idade_atual
    print('Você deve se alistar em {} ano(s)!'.format(falta))
elif idade_atual > 18:
    passou = idade_atual - 18
    print('Já passou do tempo de se alistar e você está atrasado em {} ano(s)'.format(passou))
