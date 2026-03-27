#Crie uma lista vazia e use um for com range(3) para pedir 3 cores ao usuário e guardar na lista.
#Depois, mostre todas as cores.

cor = []

for i in range(3):
    cores = input("digite uma cor")
    cor.append(cores)

print("Cores digitadas:")

for cores in cor:
    print(cores)