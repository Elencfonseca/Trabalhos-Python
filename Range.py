for i in range(5): 
    print("liberdade...")



for i in range(5): 
    print("por que ele vive...")


#Paula de Souza Ribeiro


contador = 1 

while contador <= 6: 
    print("Executando", contador, "vez")
    contador += 1


quantidadeImpares = 0

quantidadePares = 0

for i in range(5):
    numero = int(input("Informe um numero: \n"))
    if numero % 2 == 0: # Numero é par
        quantidadePares  +=1
    else:
        quantidadeImpares +=1
print(f"Quantidade de pares: {quantidadePares}")
print(f"Quantidade de impares: {quantidadeImpares}")


#Paula de Souza Ribeiro
#Foram criadas duas variaveis. quantidadePares e quantidadeImpares. O laço de repetição vai pedir 5x para informar um número. Para cada número, o programa vai verificar se o mesmo é par. Sebo número é par é adicionado 1 à variavel quantidadesPares. Se o número não é par, ele só pode ser ímpar, Nesse caso é adicionado 1 à variavel quantidadeImpares. Ao final é mostrado os valores.
