# Leia o arquivo nomes.txt 
# Conte quantas linhas existem no arquivo 

from pathlib import Path

nome = Path("nomes.txt")

with nome.open(mode='r') as arquivo:
    dados_lidos = arquivo.readlines()

quantidade = len(dados_lidos)

print("Quantidade de nomes:", quantidade)
