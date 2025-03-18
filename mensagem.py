import time # Importação da biblioteca time serve para manipular data e hora
import random #Biblioteca random serve para frealizar operações de forma aleatória
listacontatos= [] # Está recebendo uma lista vazia
while True: # Laço de repetição/quando a condição for verdadeira continuará lendo o código
    listacontatos.append(input("Digite os nomes")) # Verificando se o usuário deseja adicion ar mais um nome
    maisnome= input("deseja continuar:").lower() # Verificar se o usuário deseja continuar/ Se sim continua, se Não o código para
    if maisnome == "n": # Essa funçaõ irá 
        break
def msg(lista): # Criando a função para mostrar o código na tela
    # Mostrando a msg na tela e usando o random para sortear o nome
    print(f"Boa noite {random.choice(lista)}") # 
    # Com o time a msg será exibida de 2 en 2 segundos
    time.sleep(2) # tempo de pause para o código imprimir uma nova mensagem
    print("Python") 
    # Chamando a função para mostrar a mensagem na tela com a listacontatos com  parâmetros
msg(listacontatos)


    