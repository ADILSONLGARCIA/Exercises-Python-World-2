''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
    No final do programa,mostre: a média de idade do grupo,
    qual é o nome do homem mais velho e
    quantas mulheres têm menos de 20 anos.'''
somaidade = 0
mediaidade = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('------------{}ª PESSOAS ---------------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input(('Sexo [M/F]: '))).strip()
    somaidade += idade
    maioridadehomem: int = 0
    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
medidade = somaidade / 4
print( 'A média da idade do grupo é {} anos'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

