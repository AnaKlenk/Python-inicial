# Leia o arquivo numeros.txt 
# Some todos os numeros do arquivo 

from pathlib import Path

num = Path("numeros.txt")
soma = 0

with num.open(mode='r') as arquivo:
    for linha in arquivo:
        numero = int(linha.strip())
        soma += numero

print("Soma dos numeros:", soma)
