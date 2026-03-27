# Crie uma lista vazia.
# Peca numeros ao usuario ate ele digitar -1.
# Depois mostre quantos numeros pares foram digitados.
# Dica: numero par -> n % 2 == 0

num = []

while True:
    numero = int(input("Digite numeros, ou -1 para sair: "))

    if numero == -1:
        break

    if numero % 2 == 0:
        num.append(numero)

print("Quantidade de numeros pares:", len(num))
