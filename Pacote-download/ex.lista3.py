'''
EXERCÍCIO 03: Localizando o Maior
- Peça números ao usuário até que ele digite 0.
- Armazene tudo em uma lista (exceto o 0).
- Encontre o maior valor.
- Imprima o maior valor e em qual ÍNDICE (posição) ele está.
  Dica: use lista.index(maior_valor)
'''

lista = []

while True: 
    num = int(input("Digite numeros ou zero para sair: "))
    lista.append(num)
    if num == 0:
        lista.remove(0)
        break

maior = max(lista)

print(f"numero maior: {maior}")
print("posição dentro da lista: ", end="")
print((lista.index(maior)))
