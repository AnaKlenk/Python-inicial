'''
EXERCÍCIO 05: Mini Sistema de Compras
Crie um menu com while True que permita:
1. Adicionar um item (string) à lista.
2. Remover um item específico pelo nome.
3. Ver a lista atualizada.
4. Sair do programa.
'''

lista = []

while True: 
    compra = input("Item para comprar (ou 'sair'): ")
    if compra.lower() == 'sair':
        break
    lista.append(compra)

print(f"Sua lista atual: {lista}")

remo = input("Deseja remover qual item: ")
if remo in lista: 
    lista.remove(remo)
    print(f"Item {remo} removido!")
else:
    print("Esse item não está na lista.")

print(f"Lista final: {lista}")