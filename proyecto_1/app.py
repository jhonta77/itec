import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df2 = pd.read_csv('reporte de ingreso año 2024 a la fecha.csv', sep=';', encoding='latin1')

# Convertir columna de fecha
df2['Fecha'] = pd.to_datetime(df2['Fecha'], errors='coerce')

# Crear columnas de Año y Mes
df2['Año'] = df2['Fecha'].dt.year
df2['Mes'] = df2['Fecha'].dt.month
df2['Nombre_Mes'] = df2['Fecha'].dt.month_name()

# Diccionario para ordenar los meses de enero a diciembre
meses_ordenados = {
    'January': 'Enero', 'February': 'Febrero', 'March': 'Marzo',
    'April': 'Abril', 'May': 'Mayo', 'June': 'Junio',
    'July': 'Julio', 'August': 'Agosto', 'September': 'Septiembre',
    'October': 'Octubre', 'November': 'Noviembre', 'December': 'Diciembre'
}
df2['Nombre_Mes'] = df2['Nombre_Mes'].map(meses_ordenados)

# Lista de meses ordenada
lista_meses = list(meses_ordenados.values())
meses_disponibles = ['Todos los meses'] + lista_meses
años_disponibles = sorted(df2['Año'].dropna().unique(), reverse=True)

# --- Selectores ---
año_seleccionado = st.sidebar.selectbox("📅 Año", años_disponibles)
mes_seleccionado = st.sidebar.selectbox("🗓️ Mes", meses_disponibles)

# --- Filtro de datos ---
if mes_seleccionado == 'Todos los meses':
    df_filtrado = df2[df2['Año'] == año_seleccionado]
    subtitulo = f"Año {año_seleccionado}"
else:
    df_filtrado = df2[(df2['Año'] == año_seleccionado) & (df2['Nombre_Mes'] == mes_seleccionado)]
    subtitulo = f"{mes_seleccionado} {año_seleccionado}"

# Si no hay datos, mostrar mensaje
if df_filtrado.empty:
    st.warning(f"❌ No hay datos disponibles para **{subtitulo}**.")
else:
    # --- Análisis de productos ---
    producto_counts = df_filtrado['Producto'].value_counts()
    producto_percentages = (producto_counts / producto_counts.sum()) * 100

    # Top 5 sin alojamiento
    producto_counts_sin_alojamiento = producto_counts[producto_counts.index.str.lower() != 'alojamiento']
    top5_sin_alojamiento = producto_counts_sin_alojamiento.head(5)
    top5_percent = (top5_sin_alojamiento / producto_counts.sum()) * 100

    # Siguientes 5
    next_top5 = producto_counts.iloc[5:10]
    next_top5_percent = producto_percentages[next_top5.index]

    # Bottom 5
    bottom5 = producto_counts.tail(5)
    bottom5_percent = producto_percentages[bottom5.index]

    # --- Gráfico Top 5 sin alojamiento ---
    fig1, ax1 = plt.subplots()
    top5_sin_alojamiento.plot(kind='bar', ax=ax1, color='green', alpha=0.8)
    ax1.set_title(f'Top 5 productos más vendidos (sin Alojamiento) - {subtitulo}')
    ax1.set_xlabel('Producto')
    ax1.set_ylabel('Cantidad')
    ax1.bar_label(ax1.containers[0], labels=[f'{p:.1f}%' for p in top5_percent])
    st.pyplot(fig1)

    st.write(f"### 🟢 Top 5 productos más vendidos (sin Alojamiento) - {subtitulo}")
    st.write(pd.DataFrame({
        'Producto': top5_sin_alojamiento.index,
        'Cantidad': top5_sin_alojamiento.values,
        'Porcentaje (%)': top5_percent.round(1).values
    }))

    # --- Gráfico siguientes 5 ---
    fig2, ax2 = plt.subplots()
    next_top5.plot(kind='bar', ax=ax2, color='blue', alpha=0.8)
    ax2.set_title(f'Siguientes 5 productos más vendidos (puestos 6-10) - {subtitulo}')
    ax2.set_xlabel('Producto')
    ax2.set_ylabel('Cantidad')
    ax2.bar_label(ax2.containers[0], labels=[f'{p:.1f}%' for p in next_top5_percent])
    st.pyplot(fig2)

    st.write(f"### 🔵 Siguientes 5 productos más vendidos (puestos 6-10) - {subtitulo}")
    st.write(pd.DataFrame({
        'Producto': next_top5.index,
        'Cantidad': next_top5.values,
        'Porcentaje (%)': next_top5_percent.round(1).values
    }))

    # --- Gráfico Bottom 5 ---
    fig3, ax3 = plt.subplots()
    bottom5.plot(kind='bar', ax=ax3, color='orange', alpha=0.8)
    ax3.set_title(f'Bottom 5 productos menos vendidos - {subtitulo}')
    ax3.set_xlabel('Producto')
    ax3.set_ylabel('Cantidad')
    ax3.bar_label(ax3.containers[0], labels=[f'{p:.1f}%' for p in bottom5_percent])
    st.pyplot(fig3)

    st.write(f"### 🟠 Bottom 5 productos menos vendidos - {subtitulo}")
    st.write(pd.DataFrame({
        'Producto': bottom5.index,
        'Cantidad': bottom5.values,
        'Porcentaje (%)': bottom5_percent.round(1).values
    }))
