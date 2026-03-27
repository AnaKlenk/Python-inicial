# Crie uma lista vazia.
# Peca numeros ao usuario ate ele digitar 0.
# Mostre o menor numero digitado.

num = []
menor = 1000
while True:
    numero = int(input("Digite numeros, ou 0 para sair: "))
    if numero == 0:
        break

    if numero < menor:
       menor = numero

print(f"menor numero digitado: {menor}")
    