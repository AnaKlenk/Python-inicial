# Crie um arquivo chamado numeros.txt
# Peca 5 numeros ao usuario e salve no arquivo (um por linha)
# Depois leia o arquivo e mostre apenas os numeros pares

from pathlib import Path

num = Path("pares.txt")

with num.open(mode='w') as arquivo:
    for i in range(5):
        number = input("Digite um numero: ")
        arquivo.write(number)

print("numeros salvos!")

with num.open(mode='r') as arquivo:
    numero = number
    if numero % 2 == 0:
        ler = arquivo.readlines()
