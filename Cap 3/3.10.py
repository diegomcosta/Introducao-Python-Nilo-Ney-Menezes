salario = float(input("Entre com o salario R$ "))
aumento = int(input("Entre com a porcentagem de aumento: "))
print(f"O aumento será de {aumento}%")
print(f"O salário com aumento de R${salario * (aumento/100):.2f} será de R${salario + salario * (aumento/100):.2f}")
