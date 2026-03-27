# Leia o arquivo nomes.txt 
# Mostre todo o conteudo na tela 

from pathlib import Path

nome = Path("nomes.txt")
salvar_nomes = ['ana', 'julia', 'klenk']

with nome.open(mode='w') as arquivo:
    for item in salvar_nomes:
        arquivo.write(f"{item}\n")

print("Nomes salvos!")

with nome.open(mode='r') as arquivo:
    dados_lidos = arquivo.readlines()

dados_lidos = [linha.strip() for linha in dados_lidos]

print("dados lidos do arquivo: \n")
for ler in dados_lidos:
    print(ler)