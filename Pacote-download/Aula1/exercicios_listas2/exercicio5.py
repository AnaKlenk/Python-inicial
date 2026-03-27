''' Exercicio 5
Crie uma lista vazia.
Peca nomes ao usuario ate ele digitar "sair".
Depois mostre todos os nomes digitados em ordem crescente.
Dica: use sort()
'''
nomes = []

while True:
    nome = input("Digite um nome (ou 'sair' para parar): ")

    if nome == "sair":
        break

    nomes.append(nome)

nomes.sort()

print("Nomes em ordem crescente:")

for nome in nomes:
    print(nome)
