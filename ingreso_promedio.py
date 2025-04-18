import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame desde CSV
df_completo1 = pd.read_csv('df_completo1.csv')

# Copia del DataFrame original
df = df_completo1.copy()

# 1. Filtrar solo reservas efectivas (Estado == 'ok')
df_efectivas = df[df['Estado'].str.lower() == 'ok'].copy()

# 2. Convertir 'Ingreso' a datetime
df_efectivas['Ingreso'] = pd.to_datetime(df_efectivas['Ingreso'], errors='coerce')

# 3. Crear columna 'Mes'
df_efectivas['Mes'] = df_efectivas['Ingreso'].dt.to_period('M')

# 4. Asegurarse de que 'Total alojamiento' sea numérico
df_efectivas['Total alojamiento'] = pd.to_numeric(df_efectivas['Total alojamiento'], errors='coerce')

# 5. Agrupar por mes y sumar ingresos
ingresos_mensuales = df_efectivas.groupby('Mes')['Total alojamiento'].sum()

# 6. Calcular el promedio mensual
promedio_mensual = ingresos_mensuales.mean()

# 7. Obtener fecha mínima y máxima del período
fecha_min = df_efectivas['Ingreso'].min()
fecha_max = df_efectivas['Ingreso'].max()

# --- SECCIÓN STREAMLIT ---
st.title("📈 Informe de ingresos mensuales por reservas efectivas")

st.markdown("""
### 💡 ¿Qué estamos analizando?
Este informe presenta el **ingreso mensual promedio** generado por las **reservas efectivas**, es decir, aquellas reservas que realmente se concretaron (estado = 'ok').

Usamos la fecha de **Ingreso** para agrupar los datos mensualmente, sumamos los valores de la columna **"Total alojamiento"**, y luego calculamos el promedio mensual de ingresos.

### 📌 ¿De dónde sale este promedio?
Se sumaron todos los ingresos mensuales y luego se dividieron entre la cantidad de meses únicos que hubo en los datos.
""")

# Mostrar rango de fechas
st.info(f"📅 El archivo contiene ingresos desde **{fecha_min.date()}** hasta **{fecha_max.date()}**.")

# Mostrar resultado del promedio
st.success(f"✅ El ingreso mensual promedio por reservas efectivas es de **${promedio_mensual:,.2f}**")

# Mostrar tabla con ingresos mensuales
st.write("### 🧾 Ingresos mensuales por reservas efectivas")
st.dataframe(ingresos_mensuales.reset_index().rename(columns={
    "Mes": "Mes",
    "Total alojamiento": "Ingreso mensual ($)"
}))

# Mostrar gráfico de barras
st.write("### 📊 Gráfico de ingresos mensuales")
fig, ax = plt.subplots()
ingresos_mensuales.plot(kind='bar', ax=ax, color='lightgreen', edgecolor='black')
ax.set_ylabel('Ingreso ($)')
ax.set_xlabel('Mes')
ax.set_title('Ingresos mensuales por reservas efectivas')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)
