import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df2 = pd.read_csv('reporte de ingreso año 2024 a la fecha.csv', sep=';', encoding='latin1')

# Contar la cantidad de productos comprados
producto_counts = df2['Producto'].value_counts()
producto_percentages = (producto_counts / producto_counts.sum()) * 100

# Top 5 productos más vendidos
top5 = producto_counts.head(5)
top5_percent = producto_percentages[top5.index]

# Gráfico Top 5
fig1, ax1 = plt.subplots()
top5.plot(kind='bar', ax=ax1, color='green', alpha=0.8)
ax1.set_title('Top 5 productos más vendidos')
ax1.set_xlabel('Producto')
ax1.set_ylabel('Cantidad')
ax1.bar_label(ax1.containers[0], labels=[f'{p:.1f}%' for p in top5_percent])

# Mostrar gráfica en Streamlit
st.pyplot(fig1)

# Tabla Top 5
st.write("### 🟢 Top 5 productos más vendidos")
st.write(pd.DataFrame({
    'Producto': top5.index,
    'Cantidad': top5.values,
    'Porcentaje (%)': top5_percent.round(1).values
}))

# Bottom 5 productos menos vendidos
bottom5 = producto_counts.tail(5)
bottom5_percent = producto_percentages[bottom5.index]

# Gráfico Bottom 5
fig2, ax2 = plt.subplots()
bottom5.plot(kind='bar', ax=ax2, color='orange', alpha=0.8)
ax2.set_title('Bottom 5 productos menos vendidos')
ax2.set_xlabel('Producto')
ax2.set_ylabel('Cantidad')
ax2.bar_label(ax2.containers[0], labels=[f'{p:.1f}%' for p in bottom5_percent])

# Mostrar gráfica en Streamlit
st.pyplot(fig2)

# Tabla Bottom 5
st.write("### 🟠 Bottom 5 productos menos vendidos")
st.write(pd.DataFrame({
    'Producto': bottom5.index,
    'Cantidad': bottom5.values,
    'Porcentaje (%)': bottom5_percent.round(1).values
}))
