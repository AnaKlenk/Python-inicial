# Crie um arquivo chamado numeros.txt 
# Escreva os numeros de 1 a 5, um por linha 

from pathlib import Path

num = Path("numeros.txt")
dados = [1, 2, 3, 4, 5]

with num.open(mode='w') as arquivo:
    for numero in dados:
        arquivo.write(f"{numero} \n")

print("numeros salvos!")