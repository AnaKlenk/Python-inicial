# Crie um arquivo chamado nomes.txt 
# Escreva 3 nomes, um em cada linha 

from pathlib import Path

nome = Path("nomes.txt")

salvar_nomes = ['ana', 'julia', 'klenk']

with nome.open(mode='w') as arquivo:
    for item in salvar_nomes:
        arquivo.write(f"{item}\n")

print("Nomes salvos!")