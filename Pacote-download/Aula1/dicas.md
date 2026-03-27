# dicas
max() = numero maior da lista
min() = numero menor da lista
.append () = adiciona itens ao final da lista
.remove () = remove determinado item 
len() = significa tamanho. Em listas, ele mostra quantos itens existem
.upper(): Tudo em maiúsculas.
.sort () = odena em ordem crescente/alfabetica
.strip(): Remove espaços inúteis no começo e no fim do texto.
.readLines():le todas as linhas
.capitalize(): Só a primeira letra da frase em maiúscula.
.title(): A primeira letra de cada palavra em maiúscula.
.lower(): transforma as letras em minúsculas.
.pop(i): remove um item da lista pelo indice

write() nao aceita int
path: ajuda a criar, ler e abrir arquivos
.open(mode='w') -> open: abrir o arquivo mode='w': modo escrita (write)
.opne(mode='r') → leitura (read). So permite ler, nao escrever


[::-1] = fatiamento, inverte a lista de tras para frente
    lista[0:3]: Pega do índice 0 até o 2 (o último número é exclusivo).
    lista[2:]: Pega do índice 2 até o final.
    lista[:3]: Pega do começo até o índice 2.
    lista[::-1]: O passo -1 diz ao Python para ler a lista de trás para frente.

adicionar dado sem apagar o anterior
with nome.open('a') as arquivo:
    arquivo.write(nom + "\n")

formata data e tempo:
{<dado>: %Y-%m-%d}
{<dado>: %H-M%-%S}
{<dado>: %Y-%m-%d %H:%M}

#mostra o diretorio que estou usando para executar
diretorio = os.getcwd()
print("o seu diretorio é: ", diretorio)

limpa o terminal
os.system("cls")