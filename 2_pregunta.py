import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Cargar los datos ya combinados (df_completo1)
df_completo1 = pd.read_csv("df_completo1.csv")  # Asegúrate de tener este archivo guardado

# Título
st.title("📊 Análisis de Check-ins de Reservas")

st.markdown("Este informe muestra cuántas reservas **sí se realizaron** (check-in) y cuántas fueron **canceladas o no llegaron**.")

# Total de reservas
total_reservas = len(df_completo1)

# Filtrar las que se realizaron
realizadas = df_completo1[df_completo1['Estado'].str.lower() == 'ok']
total_realizadas = len(realizadas)

# Calcular porcentajes
porcentaje_realizadas = (total_realizadas / total_reservas) * 100
porcentaje_no_realizadas = 100 - porcentaje_realizadas

# Mostrar resultados con texto simple
st.subheader("📌 Resultados:")
st.write(f"✅ **Reservas realizadas (con check-in):** {porcentaje_realizadas:.2f}%")
st.write(f"❌ **Reservas canceladas o no realizadas:** {porcentaje_no_realizadas:.2f}%")
st.markdown("---")

# Pie chart para visualización
labels = ['Realizadas (Check-in)', 'No realizadas / Canceladas']
sizes = [porcentaje_realizadas, porcentaje_no_realizadas]
colors = ['#2ecc71', '#e74c3c']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
ax.axis('equal')  # Para que sea circular

st.pyplot(fig)
