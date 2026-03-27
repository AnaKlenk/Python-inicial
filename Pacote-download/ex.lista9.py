'''Criar o Estoque: Comece com uma lista chamada estoque contendo: "Mario", "Zelda", "Sonic".
Adicionar: O fornecedor chegou! Peça ao usuário para digitar o nome de um novo jogo e adicione-o à lista.
Organizar: Use o método para deixar a lista em ordem alfabética.
Vender (Remover): O primeiro jogo da lista (índice 0) foi vendido! Remova-o da lista.
Relatório Final: Imprima a lista atualizada e mostre quantos jogos sobraram no estoque usando o len().
Dica de ouro: Tente fazer um passo por vez e use o print() entre eles para ver se a lista está ficando do jeito que você quer.'''

estoque = ["Mario", "Zelda", "Sonic"]


novo = input("Adicione um novo nome: ")
estoque.append(novo)

estoque.sort()
print(estoque)

estoque.pop(0)
print(estoque)

print("Jogos restantes: ", end="")
print(len(estoque))