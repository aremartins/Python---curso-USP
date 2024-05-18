
n= int(input("Digite um numero: "))


i = 1
lista = []
while n > 0:    
    if(i % 2 != 0):
        lista.append(i)        
        n -= 1
    i += 1
ordened_list = sorted(lista)

for num in ordened_list:
    print(num)