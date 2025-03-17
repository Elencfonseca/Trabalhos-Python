import pandas as pd
import matplotlib.pyplot as plt
#Carregando os Dados
dados_produtos = pd.read_csv('produtos.cvs', delimiter=';')
#Criando o gráfico de PRECO POR ANO para cada produto
plt.figure(figsize=('10, 6'))
#Plotando os dados para cada produto
for produto in dados_produtos['produto'].unique():
    Dados_produto = dados_produtos[dados_produtos['produtos']== produto]
    plt.plot(dados_produto['ano'], dados_produto['preco'], label=produto, marker='o')
#Adicionando título e rótulos
plt.title('Preço dos produtos por ano')
plt.xlabel('Ano')
plt.ylabel('Preço')
plt.legend(title='produto')
# Exibindo o gráfico
plt.grid(True)
plt.show()