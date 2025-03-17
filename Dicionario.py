produto = {'Nome':'Feijão','Quantidade': 10}
nome = produto ['Nome']
quantidade = produto ['Quantidade']
print("Nome: ", nome)
print('Quantidade :', quantidade)




#Paula de Souza Ribeiro



produto = {'Nome':'Feijão','Quantidade': 10}
produto['Quantidade'] = 100
nome = produto['Nome']
quantidade = produto ['Quantidade']
print("Nome : ", nome)
print('Quantidade: ', quantidade)



#foi aumentado a quantidade


#peercorrer o dicionario 
 #avançando com dicionario
produto = {'Nome':'Feijão','Quantidade': 10}
for chave, valor in produto.items() :
    print(chave, valor)


    #Atenção
    #Função zip= ela vai combinar dois elementos.
    produto = {'Nome':['Feijão', 'Arroz', 'Farinha'], 'Quantidade': [10, 10, 100]}
    for nome, quantidade in zip (produto['Nome'], produto['Quantidade']) :
        print("Produto:", nome, "Quantidade : ",quantidade)

