velocidade = int(input("Entre com a velocidade do carro: "))
if (velocidade > 80):
    print("Multa por excesso de velocidade!!!")
    multa = (velocidade - 80) * 5
    print(f"Valor da multa: R${multa:.2f}")
