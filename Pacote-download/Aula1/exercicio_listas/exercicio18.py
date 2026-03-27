#Crie uma lista vazia e peça números ao usuário até ele digitar 0. 
#Depois mostre todos os números digitados. 

lista = []

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    lista.append(numero)

print("Números digitados:")

for num in lista:
    print(num)

