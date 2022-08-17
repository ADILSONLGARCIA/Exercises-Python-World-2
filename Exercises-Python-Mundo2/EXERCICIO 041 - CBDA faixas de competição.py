from datetime import date
hoje = date.today().year
nascimento = int(input('Informe ANO de nascimento do competidor: '))
idade = int(hoje - nascimento)
print('O COMPETIDOR tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <=19:
    print('Categoris JÚNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    var = idade >= 26
    print('Categoria MASTER')




