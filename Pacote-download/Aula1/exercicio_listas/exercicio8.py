#Crie uma lista vazia e: Peça ao usuário para digitar 3 nomes 
#Guarde os nomes na lista Depois mostre todos

nomes = []

for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Nomes digitados: ")

for nome in nomes:
    print(nome)