valor = float(input("Entre com o valor da casa a comprar R$ "))
salario = float(input("Entre com o seu salário R$ "))
ano = int(input("Entre com a quantidade de anos que deseja pagar a casa: "))

prestacao = valor / (ano * 12)
print(f"O valor da prestação de uma casa de R${valor:.2f} será de R${prestacao:.2f}.")

if (prestacao <= salario * 0.3):
    print(f"Empréstimo APROVADO! Pois a prestação é menor que R${salario * 0.3:.2f}.")
else:
    print(f"Empréstimo NEGADO! A prestação não pode ser maior que R${salario * 0.3:.2f}.")

