'''
EXERCÍCIO 03: Contador de Palavras em uma Frase
- Peça ao usuário para digitar uma frase longa.
- Conte quantas palavras existem nessa frase.
- Imprima a quantidade de palavras.
- Dica: Pesquise sobre o método '.split()' em Python para transformar a frase em uma lista de palavras.
'''

# ---------------------------------------------------------
# Digite seu código para o Exercício 03 abaixo:

# 1. Pede a frase ao usuário
frase = input("Digite uma frase longa: ")

# 2. Usa o .split() para separar a frase em uma lista de palavras.
# Por padrão, ele separa pelos espaços em branco.
lista_palavras = frase.split()

# 3. Conta quantos elementos existem na lista
quantidade = len(lista_palavras)

# 4. Imprime o resultado
print("A frase contém", quantidade, "palavras.")

# ---------------------------------------------------------