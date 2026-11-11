print('''
ORIGEM DO PRODUTO

1 - Sul
2 - Norte
3 - Leste
4 - Oeste
5|6 - Nordeste
7|8|9 - Sudeste
10 - Centro-Oeste
11 - Noroeste 
''')

codigo = int(input('Digite a opção válida: '))

match codigo:

    case 1:
        print('Sul')

    case 2:
        print('Norte')

    case 3:
        print('Leste')

    case 4:
        print('Oeste')

    case 5|6:
        print('Nordeste')

    case codigo if 7 <= codigo <= 9:
        print('Sudeste')
    #case codigo if codigo in range(7,10):
        #print('Sudeste')

    case 10:
        print('Centro-Oeste')

    case 11:
        print('Nordeste')