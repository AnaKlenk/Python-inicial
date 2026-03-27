print("bem vindo ao jogo!")
print("1. ir para a cabana")
print("2. ir para a floresta")
print("3. sair do jogo")

escolha = int(input("qual sua escolha: "))

if escolha == 1:
    print("voce entrou na cabana e encontrou uma espada, o que ira fazer?")
    print("1. pegar a espada")
    print("2. ignora a espada")
    print("3. volta para a floresta")

    decidir = int(input("o que voce faz: "))

    if decidir == 1:
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

else:
    print("opcao invalida")
    