import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados com o delimitador correto
i = pd.read_csv('dadosfecundidade.csv', delimiter=';')

# Selecionar as colunas desejadas
dados = i[['estados', '2023']]

# Criar o gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(dados['2023'], labels=dados['estados'], autopct='%.1f%%', startangle=90)
plt.title('Taxa de Fecundidade\n fapespa')
plt.legend(i['estados'].unique(),title="Estados", loc='upper left', bbox_to_anchor=(1,1))
# Mostrar o gráfico
plt.show()
