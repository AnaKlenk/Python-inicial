# Exercicio 1
# Crie um arquivo chamado texto.txt
# Escreva a frase: Ola mundo

from pathlib import Path

frase = Path("texto.txt")
frase_salva = ['Ola Mundo!']

with frase.open(mode='w') as arquivo:
    for item in frase_salva:
        arquivo.write(f"{item}")

print("Frase salva!")

# ou

with frase.open('w') as arquivo:
    arquivo.write("Ola Mundo!")
