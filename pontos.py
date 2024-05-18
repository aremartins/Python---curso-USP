import math

x_1 = int(input("Digite o valor da coordenada X para o primeiro plano do ponto cartesiano: "))

y_1 = int(input("Digite o valor da coordenada Y para o primeiro plano do ponto cartesiano: "))

x_2 = int(input("Digite o valor da coordenada X para o segundo plano do ponto cartesiano: "))

y_2 = int(input("Digite o valor da coordenada Y para o segundo plano do ponto cartesiano: "))

#fórmula d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}


distancia = math.sqrt((x_1 - y_1) ** 2 + (x_2 - y_2) ** 2)

if(distancia >= 10):
    print("longe")
else:
    print("perto")


