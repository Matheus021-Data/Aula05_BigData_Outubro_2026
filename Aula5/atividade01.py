nome = input('Nome do aluno: ')
nota1 = float(input('Digite a nota da média 1º bi: '))
nota2 = float(input('Digite a nota da média 2º bi: '))
nota3 = float(input('Digite a nota da média 3º bi: '))
nota4 = float(input('Digite a nota da média 4º bi: '))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 7.0:
    print(f'O aluno(a): {nome}\n'
          f'Nota: {media:.2f}\n'
           'Situação: Aprovado')

elif media >= 5.0 and media <= 6.9:
    print(f'O aluno(a): {nome}\n'
          f'Nota: {media:.2f}\n'
           'Situação: Recuperação')

else:
    print(f'O aluno(a): {nome}\n'
          f'Nota: {media:.2f}\n'
           'Situação: Reprovado')
    
    
    