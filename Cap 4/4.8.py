n1 = float(input("Entre com um numero: "))
n2 = float(input("Entre com outro numero: "))

op = input("Entre com a operação que deseja realizar [+, -, *, /]: ")

if (op == "+"):
    print(f"{n1} + {n2} = {n1 + n2}")

elif (op == "-"):
    print(f"{n1} - {n2} = {n1 - n2}")

elif (op == "*"):
    print(f"{n1} X {n2} = {n1 * n2}")

elif (op == "/"):
    print(f"{n1} / {n2} = {n1 / n2}")

else:
    print("Operação Inválida! Escolha uma das seguintes operações [+, -, *, /]")
    