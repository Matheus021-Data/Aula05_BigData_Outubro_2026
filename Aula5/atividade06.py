venda = float(input('Escreva a venda: '))

match venda:

    case venda if venda < 100:
        print('Venda Pequena')

    case venda if 100 <= venda < 500:
        print('Venda Média')

    case venda if venda >= 500:
        print('Venda Grande')