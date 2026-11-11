compra = float(input('Valor da compra: '))
fidelidade = input('O cliente é cadastratado de fidelidade [s/n]: ').lower() [0]
FRETE = 25 #BOA PRÁTICA PARA CONSTANTE QUER DIZER QUE NÃO MUDA NADA

if compra > 250 or fidelidade == 's':
    mensagem = f'Frete grátis. Valor da compra: {compra}'

else:
    compra = compra + FRETE
    mensagem = f'Acréscimo de R$ {FRETE} de frete. Valor atualizado: {compra}'

print(mensagem)
    