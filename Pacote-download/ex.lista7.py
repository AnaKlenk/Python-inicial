'''
EXERCÍCIO 01: Sistema de "Lista de Tarefas" (To-Do List)
- Crie um programa que gerencie uma lista de tarefas.
- O programa deve exibir um menu com opções para o usuário:
    1. Adicionar uma tarefa.
    2. Visualizar todas as tarefas (com um número ao lado, ex: "1 - Comprar pão").
    3. Remover uma tarefa pelo número da lista.
    4. Sair.
- Utilize um loop 'while' para manter o programa rodando até que o usuário escolha sair.
'''

# ---------------------------------------------------------
# Digite seu código para o Exercício 01 abaixo:

tarefas = []

while True:
    print("\n--- MENU ---")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == '2':
        print("\n--- SUAS TAREFAS ---")
        if len(tarefas) == 0:
            print("Lista vazia.")
        else:
            # Exibe a lista numerada (simples)
            for i in range(len(tarefas)):
                # i+1 faz a contagem começar de 1 para o usuário
                print(f"{i + 1} - {tarefas[i]}")

    elif opcao == '3':
        # Remove pelo número da lista
        if len(tarefas) == 0:
            print("Lista vazia.")
        else:
            # Mostra as tarefas para o usuário ver o número
            for i in range(len(tarefas)):
                print(f"{i + 1} - {tarefas[i]}")
                
            indice = int(input("Digite o número da tarefa a remover: "))
            
            # Verifica se o número existe (simples)
            if indice > 0 and indice <= len(tarefas):
                # pop remove pelo índice, por isso usamos indice - 1
                removida = tarefas.pop(indice - 1)
                print(f"Tarefa '{removida}' removida!")
            else:
                print("Número inválido.")

    elif opcao == '4':
        print("Voce saiu..")
        break
    
    else:
        print("Opção inválida, tente novamente.")
