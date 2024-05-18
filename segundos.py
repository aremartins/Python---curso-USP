segundos = int(input("Informe os segundos: " ))
dias = segundos // (24 * 3600)
segundos = segundos % (24 * 3600)
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60
print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))

                 
                       