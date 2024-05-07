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
else:    
    print("As raízes da equação são {}, {}".format(raiz1, raiz2))  
   


