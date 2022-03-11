preco = float(input("Entre com o preço da mercadoria R$ "))
desconto = int(input("Entre com o percentual de desconto: "))
print(f"O valor do desconto será de R${preco * (desconto/100):.2f}")
print(f"O preço da mercadoria com desconto será de R${preco - preco * (desconto/100):.2f}")

