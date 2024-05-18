num = int(input("Digite um numero com varios digitos: "))

adjacentesIguais = False
listNumeros = list(map(int, str(num)))

anterior = 0
posterior = 1



while not adjacentesIguais and posterior < len(listNumeros):
    if(listNumeros[anterior] == listNumeros[posterior]):
            adjacentesIguais = True
    anterior = anterior + 1
    posterior = posterior +1
    
if adjacentesIguais:
    print("sim")
else:
    print("não")
    
   

    


