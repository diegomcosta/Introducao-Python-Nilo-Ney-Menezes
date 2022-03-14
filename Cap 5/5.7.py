n = int(input("Tabuada de: "))
inicio = int(input("Digite o inicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

while(inicio <= fim):
    print(f"{inicio:2} X {n} = {inicio * n}")
    inicio +=1
