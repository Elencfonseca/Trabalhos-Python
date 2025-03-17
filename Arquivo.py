import pandas as pd
dadosProdutos = pd.read_csv("compras.csv")
print(dadosProdutos.columns)

dadosProdutos ['preco'].max()
print("Média de preços de produtos", dadosProdutos['preco'].mean()) 


import pandas as pd
import matplotlib.pyplot as plt
# Carregando dados
dados_produtos = pd.read_csv('compras.csv', delimiter=',')
# Criando o gráfico de PREÇO por ANO para cada PRODUTO
plt.figure(figsize=(10, 6))
# Plotando os dados para cada produto 
for produto in dados_produtos['produto'].unique(): # O for serve para buscar o preço e o mundo
    dados_produto = dados_produtos[dados_produtos ['produto']== produto] 
    plt.plot(dados_produto['ano'], dados_produto ['preco'], label=produto, marker='o')
# Adicionando título e rótulos
plt.title('Preço dos produtos ao longo dos anos')
plt.xlabel('ano')
plt.ylabel('preco')
plt.legend(title="produto")
# Exibindo o gráfico
plt.grid(True)
plt.show()
