listaNotas = []
for i in range(4):
    nota = float(input("Informe a nota: "))
    listaNotas.append(nota)
media = sum(listaNotas) / 4
print("A media aritmetica é {}".format(media))   
