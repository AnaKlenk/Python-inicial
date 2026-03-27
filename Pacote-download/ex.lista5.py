'''
EXERCÍCIO 04: Ordem Inversa
- Peça 5 nomes de frutas ao usuário e armazene em uma lista.
- Imprima a lista na ordem normal.
- Imprima a lista na ordem inversa (de trás para frente).
  Dica: use lista.reverse() ou fatiamento [::-1]
'''

frutas = []

for i in range(5):
    nome = input("Digite 5 frutas: ")
    frutas.append(nome)

print("frutas na ordem digitada: ", end="")
print(frutas[::-1])
