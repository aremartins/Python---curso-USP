numero = int(input("Digite um numero: "))

i = 0
contador = len(str(numero))

lista_digitos = list(map(int, str(numero)))
soma = 0


while i < contador:
    soma += lista_digitos[i]
    i +=1
print(soma)

  
