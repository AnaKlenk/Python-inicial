# Peca um nome ao usuario 
# Salve esse nome no arquivo usuarios.txt 

from pathlib import Path

nome = Path("usuarios.txt")

with nome.open(mode='a') as arquivo:
    nom = input("Digite um nome: ")
    arquivo.write(nom + "\n")

print("nome salvo com sucesso!")

# Leia o arquivo usuarios.txt 
# Mostra todos os nomes salvos

with nome.open(mode='r') as arquivo:
    ler = arquivo.readlines()

ler = [linha.strip() for linha in ler]

print("Dados salvos: ")

for item in ler:
    print(item)

# Leia o arquivo usuarios.txt 
# Mostra apenas os nomes que comecam com a letra a 

with nome.open(mode='r') as arquivo:
    ler = arquivo.readlines()

print("nomes que começam com a:")

for item in ler:
    item = item.strip()
    if item.lower()[0] == 'a':
        print(item)

        