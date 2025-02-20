import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Ventas de vehículos')
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    # Escribir un mensaje
    st.write('Creación de histograma para el conjunto de datos de anuncios de venta de vehículos')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    # Escribir un mensaje
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncions de venta de vehículos')

    # Crear el gráfico de dispersión
    fig_1 = px.scatter(car_data, x="odometer", y="price")

    # Mostrar un gráfico plotly interactivo
    st.plotly_chart(fig_1)