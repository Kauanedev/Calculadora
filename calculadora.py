while True:
    numero1 = input("Digite um número: ")
    numero2 = input("Digite outro número: ")
    operador = input(
        "Escolha um operador entre soma, subtração, \
                     multiplicação e divisão [+, -, *, /]: "
    )

    numeros_validos = None
    operadores_validos = "+-*/"

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)

        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números são inválidos. Tente novamente")

        continue

    if operador not in operadores_validos:
        print("Operador inválido. Tente novamente")

        continue

    if len(operador) > 1:
        print("Digite apenas 1(um) operador matemático, por favor :)")

        continue

    if operador == "+":
        resultado = num_1_float + num_2_float
        print(f"Resultado = {resultado}")

    elif operador == "-":
        resultado = num_1_float - num_2_float
        print(f"Resultado = {resultado}")

    elif operador == "*":
        resultado = num_1_float * num_2_float
        print(f"Resultado = {resultado}")

    elif operador == "/":
        resultado = num_1_float / num_2_float
        print(f"Resultado = {resultado}")

    continuar = input("Deseja continuar? Digite [s]im ou [n]ão : ").lower()

    if continuar == "n":
        print("Até mais :) ")
        break

    elif continuar == 's':
        continue

    else:
        print("Você digitou algo diferente de 'n' ou 's'. Então, jogue novamente :) ")
