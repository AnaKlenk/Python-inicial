'''
EXERCÍCIO 02: Filtro de Pares e Ímpares
- Leia 10 números inteiros e armazene-os em uma lista.
- Crie duas listas adicionais: 'pares' e 'impares'.
- Percorra a lista original e separe os números nas listas corretas.
- Imprima as três listas no final.
'''

lista = []
par = []
impar = []

for i in range(10):
    num = int(input("Digite um numero: "))
    lista.append(num)

    if num % 2 == 0:
        par.append(num)

    if num % 2 != 0:
        impar.append(num)

print(lista)
print(par)
print(impar)