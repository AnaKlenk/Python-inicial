# Exercicio 4
# Crie uma lista vazia.
# Use range(5) para pedir 5 numeros ao usuario.
# Mostre a soma apenas dos numeros maiores que 10.

numero = []
soma = 0
for i in range(5):
    num = int(input("Digite 5 numeros: "))

    if num > 10:
        soma += num

print(soma)