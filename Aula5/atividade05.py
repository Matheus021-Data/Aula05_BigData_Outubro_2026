numero = float(input('Digite um número: '))

match numero:

    case 0:
        print('Digitou zero')

    case numero if numero < 0:
        print('Número negativo')

    case numero if numero > 0:
        print('Número positivo')
        