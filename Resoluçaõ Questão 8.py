palavra = str(input("Insira uma palavra")) #Declaração da variável
if palavra == palavra[::-1]:
    print(f"palavra '{palavra}' é um palindromo") #Verificação da palavra escrita normalmente é igual == a palavra invertida [::-1]
else:
    print(f"palavra '{palavra}' não é um palindromo")

