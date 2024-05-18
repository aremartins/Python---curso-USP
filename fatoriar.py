def fatoriar(numero):  
    x= 2
    fatorial = 1

    while x <= numero:    
        fatorial *= x
        x += 1
  
    return fatorial




numero = int(input("Digite um nÃºmero: "))


print(fatoriar(numero))

def testaFatoriar():
    if (fatoriar(1) == 1): 
        print("Funciona para 1")
    else:
        print("Não funciona para 1")

    if (fatoriar(2) == 2):
        print("Funciona para 2")
    else:
        print("Não funciona para 2")

    if (fatoriar(0) == 1):
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

    if (fatoriar(5) == 120):
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
        




testaFatoriar()

