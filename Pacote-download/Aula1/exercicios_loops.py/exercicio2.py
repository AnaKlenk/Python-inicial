senha_correta = 'ana123'
tentativa = ''

print("Bem vindo!")

while tentativa != senha_correta:
    tentativa = input("digite a senha: ")
    if tentativa != senha_correta:
        print("Senha incorreta.Tente novamente")

print("Senha correta.\n Acesso permitido")