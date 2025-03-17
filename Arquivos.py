# Criando um arquivo - Elen Cristina Silva da Fonseca
arquivo = open('contatos. txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()


arquivo = open('contatos.txt', "a")
arquivo.write('\n JOSE')
arquivo.close()