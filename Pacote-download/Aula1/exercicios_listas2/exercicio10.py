# Crie uma lista vazia.
# Peca numeros ao usuario ate ele digitar -1.
# Mostre a soma de todos os numeros digitados.

numero = []
soma = 0
while True: 
    num = int(input("Digite numeros ou -1 para sair: "))
    if num == -1:
        break

    soma += num

print(f"soma dos numeros digitados: {soma}")
