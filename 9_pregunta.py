import streamlit as st
import pandas as pd

# Título
st.title("💰 Ingreso Neto Mensual (después de gastos operativos)")

# Cargar los datos
df = pd.read_csv("df_completo1.csv")

# Filtrar solo reservas efectivas
df_ok = df[df['Estado'].str.lower() == 'ok'].copy()

# Convertir fechas
df_ok['Ingreso'] = pd.to_datetime(df_ok['Ingreso'], errors='coerce')

# Eliminar filas sin precio
df_ok = df_ok[df_ok['Precio'].notnull()]

# Quitar texto como "COP" y convertir a numérico
df_ok['Precio limpio'] = df_ok['Precio'].str.replace('COP', '').str.replace(',', '').str.strip()
df_ok['Precio limpio'] = pd.to_numeric(df_ok['Precio limpio'], errors='coerce')

# Crear columna de mes (formato "2024-03")
df_ok['Mes'] = df_ok['Ingreso'].dt.to_period('M').astype(str)

# Sumar ingresos por mes
ingresos_mensuales = df_ok.groupby('Mes')['Precio limpio'].sum()

# Suponer un 45% de gastos operativos
gastos_mensuales = ingresos_mensuales * 0.45

# Calcular ingreso neto
ingreso_neto = ingresos_mensuales - gastos_mensuales

# Combinar resultados en una tabla
resultado = pd.DataFrame({
    'Ingreso total (COP)': ingresos_mensuales,
    'Gastos operativos (45%)': gastos_mensuales,
    'Ingreso neto (COP)': ingreso_neto
})

# Mostrar explicación
st.markdown("""
### ✅ ¿Cuál es el ingreso neto mensual después de gastos operativos?

Para conocer la ganancia real del hotel mes a mes, calculamos el ingreso neto, que es lo que queda después de cubrir los gastos de operación.

> **Suposición:** estimamos que los gastos fijos del hotel representan el 45% del ingreso mensual.

A continuación, puedes ver cuánto gana el hotel realmente cada mes:
""")

# Mostrar resultados en tabla
st.dataframe(resultado.style.format({"Ingreso total (COP)": "{:,.0f}",
                                     "Gastos operativos (45%)": "{:,.0f}",
                                     "Ingreso neto (COP)": "{:,.0f}"}))

# Gráfico visual
st.line_chart(resultado['Ingreso neto (COP)'])

