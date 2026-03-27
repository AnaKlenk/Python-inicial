#rpg nao terminado
print("bem vindo ao jogo!")

inventario = []

while True:

    print("\n 1. ir para a cabana")
    print("2. ir para a floresta")
    print("3. sair do jogo")
    print("4. Ver inventario")

    escolha = int(input("qual sua escolha: "))

    if escolha == 1:
        print("voce entrou na cabana e encontrou uma espada, o que ira fazer?")
        print("1. pegar a espada")
        print("2. ignora a espada")
        print("3. volta para a floresta\n")

        decidir = int(input("o que voce faz: "))

        if decidir == 1:
            inventario.append("espada")
            print("voce adquiriu um novo objeto")

        elif decidir == 2:
            print("seu inventario esta vazio")

        elif decidir == 3:
            print("voce voltou para a floresta")  

        else:
            print("opcao invalida")

    elif escolha == 2:
        print("voce voltou para a floresta")

    elif escolha == 3:
        print("voce saiu do jogo")

    elif escolha == 4:
        print("Seu inventario")
        for item in inventario:
            print(F"{item}")

    else:
        print("opcao invalida")
    
