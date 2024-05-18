inputUser = int(input("Digite um número: "))

def fatorial(num):
    fat = 1
    if(num < 0):
        raise ValueError(f" O fatorial não está definido para números negativos.\n Valor digitado: {num}")
    elif (num == 0):
        return 1
    while(num > 1):
        fat = fat * num
        num = num -1
    return fat
    
resultado = fatorial(inputUser)

print(f"O fatorial de {inputUser} é {resultado} ")



print("*" *30 + "\n Cálculo binominal: \n")

def binominal(n, k=2):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))

'''
n é o número total de elementos.
𝑘
k é o número de elementos a serem escolhidos.
!
! denota o fatorial de um número.'''

resultado = binominal(inputUser, 2)
print(f"O coeficiente binomial de {inputUser} sobre 2 é {resultado}")
    

print("*" * 30 + "\n Testes automatizados para função fatorial:\n ")
    
def testaFatorial():
    if (fatorial(1) == 1): 
        print("Funciona para 1")
    else:
        print("Não funciona para 1")

    if (fatorial(2) == 2):
        print("Funciona para 2")
    else:
        print("Não funciona para 2")

    if (fatorial(0) == 1):
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

    if (fatorial(5) == 120):
        print("Funciona para 5")
    else:
        print("Não funciona para 5")     
      


testaFatorial()

print("*" * 30 + "\n Testes automatizados para função binominal:\n ")

testes = [
    (0, 0, 1),
   (5, 2, 10),
   (6, 3, 20),
   (7, 0, 1),
   (7, 7, 1),
   (10, 5, 252),
   (4, 2, 6),
   (10, 3, 120) 
]

for n, k, esperado in testes:
    resultado = binominal(n, k)
    assert resultado == esperado, f"Teste falhou para n={n} e k={k}, resultado esperado {esperado}, mas obteve {resultado}"
    print(f"Teste passou para n={n}, k={k}: {resultado} ")









































