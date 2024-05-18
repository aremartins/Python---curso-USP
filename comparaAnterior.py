firstNum = int(input("número: "))

numeroIgual = False
listNum =[]

listNum.append(firstNum)

i = 0

while not numeroIgual:
    num = int(input("número: "))
    listNum.append(num)
    i +=1
    if(listNum[i] == listNum[i-1]):        
        numeroIgual = True
    

