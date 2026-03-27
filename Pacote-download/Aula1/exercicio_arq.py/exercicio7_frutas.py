# Crie um arquivo chamado frutas.txt 
# Salve 3 frutas digitadas pelo usuario 
# Depois leia e mostre as frutas 

from pathlib import Path

arquivo = Path("numeros.txt")

# 1. Pede 5 numeros e salva no arquivo
with arquivo.open(mode='w') as f:
    for i in range(5):
        numero = input("Digite um numero: ")
        f.write(numero + "\n")

print("Numeros salvos!")

# 2. Le o arquivo e mostra apenas os numeros pares
print("Numeros pares:")

with arquivo.open(mode='r') as f:
    linhas = f.readlines()

for linha in linhas:
    numero = int(linha.strip())
    if numero % 2 == 0:
        print(numero)
