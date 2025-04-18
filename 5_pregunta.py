import pandas as pd
import streamlit as st

# Cargar el archivo
df = pd.read_csv("df_completo1.csv")

# Filtrar reservas efectivas (estado "ok")
df_ok = df[df['Estado'].str.lower() == 'ok'].copy()

# Limpiar la columna 'Precio': quitar " COP", puntos de miles y comas
df_ok['Precio'] = df_ok['Precio'].astype(str)
df_ok['Precio'] = df_ok['Precio'].str.replace(' COP', '', regex=False)
df_ok['Precio'] = df_ok['Precio'].str.replace('.', '', regex=False)
df_ok['Precio'] = df_ok['Precio'].str.replace(',', '.', regex=False)
df_ok['Precio'] = pd.to_numeric(df_ok['Precio'], errors='coerce')

# Asegurarse de que la columna 'Personas' sea numérica
df_ok['Personas'] = pd.to_numeric(df_ok['Personas'], errors='coerce')

# Eliminar filas con datos faltantes
df_ok = df_ok.dropna(subset=['Precio', 'Personas'])

# Calcular el ingreso promedio por huésped
ingreso_total = df_ok['Precio'].sum()
total_personas = df_ok['Personas'].sum()
ingreso_promedio = ingreso_total / total_personas

# Mostrar resultados
st.title("💰 Ingreso promedio por huésped")
st.markdown("Este valor muestra cuánto dinero deja, en promedio, cada persona que se hospedó realmente en el hotel.")

st.subheader(f"✅ Ingreso promedio por huésped: **{ingreso_promedio:,.0f} COP**")
