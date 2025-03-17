
with open("texto.txt", "w", encoding="utf-8") as file:
    for i in range(3):
     frase = input(f"Digite a {i+1}ª frase:")
     file.write(frase+"\n")
print("Frases salvas com sucesso!")

# Escreva um programa que leia e exiba na tela o conteúdo do arquivo
file= open ('texto.text', 'r')
for linha in file:
   print(linha)
   file.close()

   # Agora conte quantas vogais ele possui

arquivo = open('texto.txt', 'r')
def contar(palavra):
   vogais = 'aeiou'
   for vogal in palavra:
   if vogal in vogais:
      conta+=1
return conta
palavra = str(input("Digite sua palavra:"))
print(contar(palavra))
for linha in arquivo:
   print(linha)
   arquivo.close()
              

   
                  