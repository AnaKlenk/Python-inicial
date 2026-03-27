from pathlib import Path
#path ajuda a criar, ler e abrir arquivos
#pathlib e uma biblioteca do Python. serve para: trabalhar com arquivos, trabalhar com pastas, lidar com caminhos (paths)

caminho_do_arquivo  = Path("seus_dados.txt")
#Quando eu falar desse nome, estou falando desse arquivo aqui

dados_para_salvar = ['Python', 'C++', 'Java']

#with: garante que o arquivo sera fechado automaticamente
#.open('w') -> open: abrir o arquivo mode='w': modo escrita (write)
#arquivo → nome da variavel que representa o arquivo aberto
with caminho_do_arquivo.open(mode='w') as arquivo:
    for item in dados_para_salvar:

        arquivo.write(f"{item} \n")
        #Escreve o texto dentro do arquivo

print("Dados salvos com sucesso!")

#lendo o arquivo

#mode='r' → leitura (read)
with caminho_do_arquivo.open(mode='r') as arquivo:
    dados_lidos = arquivo.readlines()
    #Le todas as linhas. Retorna uma lista:['Python\n', 'C++\n', 'Java']
    #strip() remove caracteres como espaços

dados_lidos = [linha.strip() for linha in dados_lidos]

print("Ddos lidos do arquivo: ", dados_lidos)