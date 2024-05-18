nome = input("Digite o nome do cliente: ")
diaVencimento = input("Digite o dia de vencimento: ")
mesVencimento = input("Digite o mês de vencimento: ")
valor = input("Digite o valosr da fatura: ")

print("Olá, {}.\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(nome, diaVencimento, mesVencimento, valor))