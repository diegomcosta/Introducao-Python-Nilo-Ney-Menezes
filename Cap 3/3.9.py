dia = int(input("Entre com a quantidade de dias: "))
hora = int(input("Entre com a quantidade de horas: "))
minuto = int(input("Entre com a quantidade de minutos: "))
segundo = int(input("Entre com a quantidade de segundos: "))

tot_segundos = dia * 86400 + hora * 3600 + minuto * 60 + segundo

print(f"Total de segundos: {tot_segundos} segundo(s).")