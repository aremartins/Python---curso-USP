import math



def delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

def calculoRaizes(a, b, c):
    deltaCalc = delta(a, b, c)
    if(deltaCalc >= 0):
        raiz1 = (-b + math.sqrt(deltaCalc)) / (2 * a)
        raiz2 = (-b - math.sqrt(deltaCalc)) / ( 2 * a)  
        return raiz1, raiz2
    
     
    


def bhaskara():
    a = float(input("Informe o valor para a: "))
    b = float(input("Informe o valor para b: "))
    c = float(input("Informe o valor para c: ")) 
    
    deltaCalc = delta(a, b, c)   
    
    if(deltaCalc >= 0 ):
        raiz1, raiz2 = calculoRaizes( a, b, c)
    if(deltaCalc == 0):       
        print("A raiz quadrada é {}".format(raiz1))
    elif deltaCalc < 0:
        print("Esta equação não possui raízes reais")
    elif deltaCalc > 0:
        if raiz1 != raiz2:
            menor = min(raiz1, raiz2)
            maior =  max(raiz1, raiz2)        
            print("As raízes da equação são {}, {}. Onde {} e {} são os valores da raízes".format(menor, maior, menor, maior))
        else:
            print("As raízes da equação são {}, {}. Onde {} e {} são os valores da raízes".format(raiz1, raiz2, raiz1, raiz2))
        
        

bhaskara()