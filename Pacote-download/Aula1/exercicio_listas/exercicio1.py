frutas = []

while True:
    fruta = input("Digite uma fruta ou sair: ")
    
    if fruta.lower() == 'sair':
        break

    frutas.append(fruta)

print("Lista de frutas:")

for fruta in frutas :
   print(fruta)