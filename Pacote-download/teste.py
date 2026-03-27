lista = []

while True:
    num = int(input("Digite numeros inteiros ou 0 para sair: "))
    
    if num == 0:
        break
    
    lista.append(num)


if len(lista) > 0:
    maior = max(lista) 
    menor = min(lista) 
    
    print("Quantidade de elementos na lista: ", end="")
    print(len(lista))
    print(f"Numero maior: {maior}, numero menor: {menor}")

else:
    print("A lista está vazia.")