numero = int(input("Informe o numero: "))
numero_str = str(numero)  # Convertendo o número para uma string
res = 0
for i in numero_str:
    if(len(numero_str) >=2):
        res = numero_str[-2]
print('O dígito das dezenas é {}'.format(res))