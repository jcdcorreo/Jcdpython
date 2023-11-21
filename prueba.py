import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
st.title('Titulo del Proyecto de prueba')
df = pd.read_csv('tb_medida_estaciones.csv')
# Convertir las cadenas de texto a datetime
df['FECHA_CORTE'] = pd.to_datetime(df['FECHA_CORTE'], format='%Y%m%d')
df['FECHA_MUESTRA'] = pd.to_datetime(df['FECHA_MUESTRA'], format='%Y%m%d')
df.sort_values(by=['FECHA_CORTE', 'FECHA_MUESTRA'], ascending=[True, True], inplace=True)
# Cambiar el formato a DD/MM/YYYY
df['FECHA_CORTE'] = df['FECHA_CORTE'].dt.strftime('%d/%m/%Y')
df['FECHA_MUESTRA'] = df['FECHA_MUESTRA'].dt.strftime('%d/%m/%Y')
df1 = df[((df['FECHA_CORTE'] =='06/07/2023') & (df['ESTACION'] == 'PTE. SANCHEZ CERRO' ))]
cuenta = df1['CUENTA'].iloc[0]
estacion = df1['ESTACION'].iloc[0]
#departamento = df1['DEPARTAMENTO'].iloc[0]
provincia = df1['PROVINCIA'].iloc[0]
distrito = df1['DISTRITO'].iloc[0]
unidad= df1['UNIDAD_MEDIDA'].iloc[0]
# Creando el gráfico
plt.figure(figsize=(12, 6))
plt.plot(df1['FECHA_MUESTRA'], df1['CAUDAL07H'], label='Caudal 07H')
plt.plot(df1['FECHA_MUESTRA'], df1['PROMEDIO24H'], label='Promedio 24H')
plt.plot(df1['FECHA_MUESTRA'], df1['MAXIMA24H'], label='Máxima 24H')
plt.plot(df1['FECHA_MUESTRA'], df1['PRECIP24H'], label='Precip 24H')

plt.xlabel('Fecha de Muestras')
plt.ylabel(f'Valores en {unidad}')
plt.title(f'Datos Hidrometeorológicos - Estación: {estacion}, Cuenca: {cuenta}, Provincia: {provincia},  Distrito: {distrito}')
plt.legend()

# Configurar el localizador de fechas para 30 ticks en el eje X
locator = mdates.AutoDateLocator(minticks=30, maxticks=40)
plt.gca().xaxis.set_major_locator(locator)
plt.xticks(rotation=90)
plt.tight_layout()

# Mostrar el gráfico
plt.show()