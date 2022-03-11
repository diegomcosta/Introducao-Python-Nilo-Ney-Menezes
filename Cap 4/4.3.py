n1 = int(input("Entre com um numero: "))
n2 = int(input("Entre com outro numero: "))
n3 = int(input("Entre com outro numero: "))

maior = menor = n1

if (n2 > n1) and (n2 > n3):
    maior = n2
elif (n3 > n1) and (n3 > n2):
    maior = n3

if (n2 < n1) and (n2 < n3):
    menor = n2
elif (n3 < n1) and (n3 < n2):
    menor = n3

print(f"Menor: {menor}")
print(f"Maior: {maior}")

