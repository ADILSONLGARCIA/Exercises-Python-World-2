n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1+n2)/2
print('A média entre a nota da primeira avaliação {:.2f} e a nota do provão de {:.2f} é igual a nota da média de {:.2f}'.format(n1, n2, media))
if media > 7:
    print('Aluno foi APROVADO')
elif media >= 5 < 6.9:
    print('Aluno na RECUPERAÇÃO')
    print('Você precisa estudar mais!')
elif media < 5:
    print('Aluno foi reprovado.')

