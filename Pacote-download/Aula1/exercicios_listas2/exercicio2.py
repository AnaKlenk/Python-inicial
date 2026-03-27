# Crie uma lista vazia.
# Peca numeros ao usuario ate ele digitar 0.
# Mostre o maior numero digitado.
# Dica: use uma variavel chamada maior.

lista = []
maior = 0
while True:
    numero = int(input("Digite numeros, ou 0 para sair: "))
    if numero == 0:
        break
    if numero > maior:
        maior = numero

print(F"maior numero digitado {maior}")


