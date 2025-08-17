# Criando um arquivo com conteúdo

# -- com a função "open" vai abrir como arquivo "exemplo.txt" e será aberto para
# escrita"r" (no caso seria o objeto que nomeei) e o .write diz quando ele deve ser escrito
# e escrever no arquivo "Hello World"
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Hello World!!!")


    with open("exemplo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)


# Lendo linha por linha
with open("exemplo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())