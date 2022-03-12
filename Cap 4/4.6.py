from turtle import distance


km = int(input("Entre com a distancia que deseja percorrer em km: "))
if (km <= 200):
    preco = km * 0.5
else:
    preco = km * 0.45
print(f"O preço a ser pago por uma viagem de {km}km é de R${preco:.2f}")

