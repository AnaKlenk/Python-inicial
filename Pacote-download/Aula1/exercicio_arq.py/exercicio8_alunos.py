# Crie um arquivo chamado alunos.txt
# Peca nomes ao usuario ate ele digitar "fim"
# Salve os nomes no arquivo
# Depois leia o arquivo e mostre quantos nomes foram salvos

from pathlib import Path

aluno = Path("alunos.txt")

with aluno.open(mode='w') as arquivo:
    while True:
        nome = input("Digite nomes ou fim para sair: ")
        if nome == 'fim': 
            break

        arquivo.write(nome +"\n")

print("nomes salvos!")

with aluno.open(mode='r') as arquivo:
    ler = arquivo.readlines()

ler = [linha.strip() for linha in ler]

print("Nomes salvos no arquivo:")

for item in ler:
    print(item)

print("Quantidade de nomes:", len(ler))