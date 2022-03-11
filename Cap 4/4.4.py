salario = float(input("Entre com o salario do funcionário R$ "))
if (salario > 1250):
    salario += salario * 0.1
else:
    salario += salario * 0.15

print(f"O salário com aumento será de R${salario:.2f}")
