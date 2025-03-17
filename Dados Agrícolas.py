import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dados = pd.read_csv("Dados Agrícolas.csv")
dados.columns = dados.columns.str.strip()
print(dados.head())
# Tipo de Cultivo e calcuçlar a produtividade media
produtividade_media = dados.groupby("tipo_de_Cultivo")["produtividade"].mean().reset_index
print("\nProdutividade média por tipo de cultivo:")
print(produtividade_média)
# Produto com maior produtividade media
produto_max_produtividade  = produtividade_media.loc[produtividade_media["produtividade"].idmax()]
print("\nProduto com maior produtividade:")
print(produto_max_produtividade)
# Menor uso de água
uso_de_água_medio = dados.groupby("tipo_de_cultivo")["uso_de_água"].mean()
produto_min_uso_agua = uso_agua_medio.idxmin()
print("\nProduto com menor uso médio de água:", produto_min_uso_agua)
plt.figure(figize=(10, 6))
sns.lineplot(data=dados, x="ano", y="produtividade", hue="tipo_de_cultivo", marker='o')
plt.title("Produtividade ao longo dos anos por tipo de cultivo")
plt.xlabel("ano")
plt.ylabel("Produtividade (Toneladas por Hectare)")
plt.legend(title="Tipo de Cultivo")
plt.grid(True)
plt.show()

