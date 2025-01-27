while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Selecione a operação desejada (*,/,+,-): ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou os dois números são inválidos!")
        continue

    operadores_validos = '*/+-'

    if operador not in operadores_validos:
        print("Operador inválido!")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador!")
        continue
    ##############

    multiplicacao = (f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
    divisao = (f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)
    adicao = (f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)
    subtracao = (f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)

    if operador == '*':
        print (multiplicacao)
    elif operador == '+':
        print (adicao)
    elif operador == '-':
        print (subtracao)
    elif operador == '/':
        print (divisao)

    sair = input('Deseja sair? [S]im:').lower()
    if sair.startswith('s'):
        break


    
