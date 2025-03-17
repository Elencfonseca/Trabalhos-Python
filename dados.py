import pandas as pd
import matplotlib
# Dados extraídos da tavela fao.org
paises = ["Brasil", "México"]
consumo = [21.6, 34.2]  #Percentual de mulheres que consomem ovos
# Criar o gráfico de pizza
plt.figure(figsize=(8,8))
plt.pie(consumo, labels=paises, autopct="%.1f%%", colors=["blue","red"], startangle=90)
# Título do gráfico
plt.title("Consumo de Ovos por Mulheres (%)")
# Mostrar o gráfico
plt.show()
