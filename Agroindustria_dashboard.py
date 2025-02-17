import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# 1. Configuración inicial de la aplicación
st.set_page_config(
    page_title="Dashboard Agropecuario",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Evaluaciones agropecuarias municipales")
st.sidebar.title("🔍 Opciones de Navegación")

# 2. Generación de Datos Aleatorios
np.random.seed(18)
data = pd.DataFrame({
    "Departamento": np.random.choice(["ANTIOQUIA", "VALLE", "QUINDIO", "CAUCA","META","NARIÑO"], size=150),
    "Municipio": np.random.choice(["Cali", "Medellín", "Buenaventura", "Popayán","Puerto Gaitán","Ipiales"], size=150),
    "Fecha": pd.date_range(start="2024-01-01", periods=150, freq="D"),
    "Hectáreas sembradas": np.random.randint(10, 500, size=150),
    "Hectáreas cosechadas": np.random.randint(10, 500, size=150),
    "Tipo de cultivo": np.random.choice(["Acelga", "Tomate", "Caña de azúcar", "Papa", "Stevia", "Cebolla", "Cítricos", "Aguacate"], size=150),
    "Rendimiento (t/ha)": np.random.uniform(5, 30, size=150),
    "Región": np.random.choice(["Eje cafetero", "Llanos orientales", "Pacífico", "Andes"], size=150)
})

# 3. Implementación de la Barra de Navegación
menu = st.sidebar.radio(
    "Selecciona una opción:",
    ["Inicio", "Datos", "Visualización", "Configuración"]
)

# 4. Mostrar los Datos
if menu == "Datos":
    st.subheader("📂 Datos Generados")
    st.dataframe(data)

# 5. Botón para Reiniciar Filtros
    if st.sidebar.button("Reiniciar Filtros"):
        filtered_data = data
        st.experimental_rerun()

# 6. Implementar Pestañas
    st.subheader("📌 Navegación entre Pestañas")
    tab1, tab2 = st.tabs(["📊 Gráficos", "📂 Datos"])
    with tab1:
        st.subheader("Visualización de Datos")
        fig_plotly = px.scatter(
            filtered_data,
            x="Hectáreas sembradas",
            y="Hectáreas cosechadas",
            color="Región",
            title="Relación entre las hectáreas sembradas y cosechadas por Región",
        )
        st.plotly_chart(fig_plotly)
    with tab2:
        st.subheader("Datos Crudos")
        st.dataframe(filtered_data)

# 10. Mensaje de Confirmación
st.sidebar.success("🎉 Configuración completa")

# 11. Ejecución del Script
if __name__ == "__main__":
    st.sidebar.info("Ejecuta este script con: streamlit run talento-roadmap-app.py")


