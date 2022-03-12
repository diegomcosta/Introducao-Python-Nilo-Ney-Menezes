kWh = int(input("Entre com a quantidade de kWh consumida: "))
print("Entre com o tipo de instalação elétrica:")
print("[ R ] para residencial")
print("[ C ] para comercial")
print("[ I ] para industrial")
print()
tipo = input("tipo: ").upper()

if(tipo == "R"):
    if (kWh <= 500):
        preco = 0.4 * kWh
    else:
        preco = 0.65 * kWh

elif(tipo == "C"):
    if (kWh <= 1000):
        preco = 0.55 * kWh
    else:
        preco = 0.6 * kWh

elif(tipo == "I"):
    if(kWh <= 5000):
        preco = 0.55 * kWh
    else:
        preco = 0.6 * kWh

print(f"Preço a se pagar R${preco:.2f}")

 
