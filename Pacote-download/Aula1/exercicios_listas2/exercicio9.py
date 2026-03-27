# Crie uma lista vazia.
# Peca nomes ao usuario ate ele digitar "fim".
# Mostre quantos nomes foram digitados.

nome = []

while True: 
    nom = input("Digite nomes ou fim para sair: ")
    
    if nom == 'fim':
        break
    nome.append(nom)

print(len(nome))
