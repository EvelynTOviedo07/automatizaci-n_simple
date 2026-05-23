import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Cargar los datos desde el archivo CSV descargado
df = pd.read_csv("datos_supervivencia_titanic.csv")

# 1. Crear el conjunto de datos basado en tu gráfica
data = {
    "Clase": [1, 1, 2, 2, 3, 3],
    "Superv": ["No sobrevivió", "Sobrevivió", "No sobrevivió", "Sobrevivió", "No sobrevivió", "Sobrevivió"],
    "Total": [80, 136, 97, 87, 372, 119],
}

df = pd.DataFrame(data)

# 2. Configurar el estilo general de la gráfica
sns.set_theme(style="ticks")
plt.figure(figsize=(10, 6.5))

# Definir una paleta de colores personalizada muy similar a la de tu imagen
# El primero es un morado/negro muy oscuro y el segundo un azul grisáceo
colores_personalizados = ["#1d0d3b", "#3b4d5c"]

# 3. Crear la gráfica de barras agrupadas
ax = sns.barplot(
    x="Clase",
    y="Total",
    hue="Superv",
    data=df,
    palette=colores_personalizados,
    edgecolor="none"  # Sin bordes en las barras para un look limpio
)

# 4. Personalizar títulos y etiquetas de los ejes
plt.title("Tasa de Supervivencia por Clase", fontsize=14, pad=10)
plt.xlabel("Clase", fontsize=11)
plt.ylabel("Total", fontsize=11)

# 5. Ajustar la leyenda para que coincida exactamente
plt.legend(title="Supervivencia", loc="upper right", frameon=True)

# Limitar el eje Y para dar un poco de espacio arriba (opcional)
plt.ylim(0, 400)

# 6. Mostrar la gráfica
plt.tight_layout()
plt.show()