qtd_cigarro = int(input("Entre com a quantidade de cigarros por dia: "))
ano = int(input("Entre com a quantidade de anos fumando: "))

tot_cigarros = qtd_cigarro * ano * 365
minuto = tot_cigarros * 10

tot_dia = minuto / 1440

print(f"O total de dias perdidos é de {tot_dia} dia(s).")