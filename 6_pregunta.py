import pandas as pd
import streamlit as st

# Cargar los datos
df = pd.read_csv("df_completo1.csv")

# Filtrar reservas efectivas
df_ok = df[df['Estado'].str.lower() == 'ok'].copy()

# Convertir fecha de ingreso
df_ok['Ingreso'] = pd.to_datetime(df_ok['Ingreso'], errors='coerce')

# Crear columna con el día de la semana (en español)
dias_semana = {
    0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves',
    4: 'Viernes', 5: 'Sábado', 6: 'Domingo'
}
df_ok['Día semana'] = df_ok['Ingreso'].dt.dayofweek.map(dias_semana)

# Contar reservas por día
reservas_por_dia = df_ok['Día semana'].value_counts().sort_index()

# Mostrar resultados
st.title("📅 Reservas por día de la semana")
st.bar_chart(reservas_por_dia)
st.markdown("Este gráfico muestra cuántas reservas empiezan cada día de la semana.")
