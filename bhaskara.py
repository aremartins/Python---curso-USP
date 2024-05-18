import math

a = float(input("Informe o valor para a: "))
b = float(input("Informe o valor para b: "))
c = float(input("Informe o valor para c: "))




delta = b**2 - 4*a*c


if(delta >= 0 ):
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / ( 2 * a)  
if(delta == 0):       
    print("A raiz quadrada é {}".format(raiz1))
elif delta < 0:
    print("Esta equação não possui raízes reais")
elif delta > 0:
    if raiz1 != raiz2:
        menor = min(raiz1, raiz2)
        maior =  max(raiz1, raiz2)        
        print("As raízes da equação são {}, {}. Onde {} e {} são os valores da raízes".format(menor, maior, menor, maior))
    else:
        print("As raízes da equação são {}, {}. Onde {} e {} são os valores da raízes".format(raiz1, raiz2, raiz1, raiz2))
   


