# Dada a lista:
# nomes = ["ana", "joao", "alice", "bruno", "amanda"]
# Mostre apenas os nomes que comecam com a letra "a".
# Dica: nome[0] == "a"

nomes = ['ana', 'joao', 'alice', 'bruno', 'amanda']

for nom in nomes:
    if nom[0] == 'a':
        print(F"{nom}")