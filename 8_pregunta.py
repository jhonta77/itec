import streamlit as st
import pandas as pd

# Título de la sección
st.title("🌎 Nacionalidades más comunes entre los huéspedes")

# Cargar el archivo de datos
df = pd.read_csv("df_completo1.csv")

# Filtrar las reservas efectivas (estado "ok")
df_ok = df[df['Estado'].str.lower() == 'ok'].copy()

# Contar nacionalidades
nacionalidades = df_ok['Nacionalidad'].value_counts().head(10)

# Explicación para el informe (puedes copiar esto directamente si haces un PDF)
st.markdown("""
### ✅ ¿Qué nacionalidades son más comunes entre los huéspedes?

Al analizar los datos de las reservas que realmente se realizaron, encontramos que algunas nacionalidades se repiten con mayor frecuencia entre los huéspedes.

Esto puede ayudar al hotel a entender de dónde vienen los clientes y planear acciones específicas, como:
- Traducir menús o información turística.
- Crear alianzas con agencias en esos países.
- Hacer promociones dirigidas al público extranjero más frecuente.

A continuación, mostramos las 10 nacionalidades más comunes entre los huéspedes:
""")

# Mostrar los datos como tabla
st.dataframe(nacionalidades.rename("Cantidad de huéspedes"))

# Si quieres también un gráfico de barras
st.bar_chart(nacionalidades)
