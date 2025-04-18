import streamlit as st
import pandas as pd

# Título de la sección
st.title("📅 Volumen de Reservas por Mes")

# Cargar los datos
df = pd.read_csv("df_completo1.csv")

# Filtrar solo las reservas efectivas (Estado = "ok")
df_ok = df[df['Estado'].str.lower() == 'ok'].copy()

# Convertir la columna 'Ingreso' a fecha
df_ok['Ingreso'] = pd.to_datetime(df_ok['Ingreso'], errors='coerce')

# Crear nueva columna con el mes de ingreso en formato año-mes (ej: "2024-03")
df_ok['Mes reserva'] = df_ok['Ingreso'].dt.to_period('M').astype(str)

# Contar reservas por mes y ordenar por fecha
reservas_por_mes = df_ok['Mes reserva'].value_counts().sort_index()

# Mostrar una explicación clara para el informe
st.markdown("""
### ✅ ¿Qué meses presentan mayor volumen de reservas?

Para conocer los meses con más actividad en el hotel, revisamos la fecha en la que los huéspedes hicieron el check-in.

Agrupamos todas las reservas **efectivas** por mes y contamos cuántas hay en cada uno. Esto nos permite ver:
- En qué épocas del año hay mayor demanda.
- Cuándo se necesita reforzar personal o servicios.
- Cuándo es ideal lanzar promociones para atraer más huéspedes.

A continuación se presenta la cantidad de reservas efectivas por mes:
""")

# Mostrar tabla con los datos
st.dataframe(reservas_por_mes.rename("Cantidad de reservas"))

# Gráfico de barras para mejor visualización
st.bar_chart(reservas_por_mes)
