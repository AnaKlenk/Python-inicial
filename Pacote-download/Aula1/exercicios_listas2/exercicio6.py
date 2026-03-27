# Crie uma lista vazia.
# Use range(5) para pedir 5 numeros ao usuario.
# Mostre apenas os numeros impares digitados.

num = []

for i in range(5):
    numeros = int(input("digite 5 numeros: "))

    if numeros % 2 == 1:
        num.append(numeros)

print(f"numeros impares{num}")