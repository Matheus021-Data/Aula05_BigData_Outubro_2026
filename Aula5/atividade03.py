compra = float(input('Valor da compra: '))
fidelidade = input('O cliente é cadastratado de fidelidade [s/n]: ').lower() [0]
frete = 25

if compra > 250 or fidelidade == 's':
    mensagem = f'Frete grátis, atende os requisitos. Valor da compra: {compra}'

else:
    compra = compra + frete
    mensagem = f'Acréscimo de R$ 25,00 de frete. Valor atualizado: {compra}'

print(mensagem)
    