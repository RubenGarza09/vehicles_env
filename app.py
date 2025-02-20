import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('notebooks\vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    # Escribir un mensaje
    st.write('Creación de histograma para el conjunto de datos de anuncios de venta de vehículos')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
