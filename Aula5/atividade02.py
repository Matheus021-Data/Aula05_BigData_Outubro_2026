nota = float(input('Digite a nota: '))
frequencia = int(input('Digite a frequencia: '))
mensalidade = float(input('Valor da mensalidade: R$ '))
desconto = 0.20

if nota >= 7 and frequencia >= 75:
    mensalidade_desconto = mensalidade * desconto
    mensalidade = mensalidade - mensalidade_desconto
    mensagem = f'O aluno(a) cumpriu os requisitos o novo valor da mensalidade: {mensalidade}'

else:
    mensagem = f'O aluno não cumpriu os requisitos mínimos para ter desconto na mensalidade'

print(mensagem)
               

