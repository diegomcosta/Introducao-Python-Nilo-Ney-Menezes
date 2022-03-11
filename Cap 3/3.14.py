km = int(input("Entre com a quantidade de km percorridos pelo carro: "))
dia = int(input("Entre com a quantidade de dias alugado: "))

preco = 0.15 * km + 60 * dia

print(f"O preço a ser pago é de R${preco:.2f}")

