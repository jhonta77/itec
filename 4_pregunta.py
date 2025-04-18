import streamlit as st
import pandas as pd

# Título de la app
st.title("🏨 Estadías de los Huéspedes")

# Cargar el archivo
df = pd.read_csv(r'C:\Users\Yenifer\absolute\itec\reservas 27032024 27032025.csv', sep=';', skiprows=1, encoding='utf-8')

# Convertir columnas de fecha
df['Ingreso'] = pd.to_datetime(df['Ingreso'], errors='coerce')
df['Salida'] = pd.to_datetime(df['Salida'], errors='coerce')

# Calcular noches
df['Noches'] = (df['Salida'] - df['Ingreso']).dt.days

# Agrupar por cliente y sumar noches
estadias_por_cliente = df.groupby('Titular')['Noches'].sum().reset_index()
estadias_por_cliente = estadias_por_cliente.sort_values(by='Noches', ascending=False)

# Explicación
st.markdown("""
### 📊 ¿Cuántos días se ha quedado cada cliente?

Aquí puedes ver cuántas noches en total ha pasado cada huésped en el hotel. Esto es útil para identificar clientes frecuentes o de larga estadía.
""")

# Mostrar la tabla
st.dataframe(estadias_por_cliente)

# Mostrar un gráfico de los 10 huéspedes con más noches
top_10 = estadias_por_cliente.head(10)
st.bar_chart(data=top_10, x='Titular', y='Noches')

# Calcular noches promedio por cliente
promedio_noches = estadias_por_cliente['Noches'].mean()

# Mostrar resultado
st.markdown(f"""
### 🛏️ ¿Cuántas noches en promedio se queda un huésped?

En promedio, **cada huésped se queda {promedio_noches:.2f} noches** en el hotel.

Este cálculo se hace sumando todas las noches que han pasado los huéspedes y dividiéndolo entre la cantidad de huéspedes distintos (titulares).
""")

