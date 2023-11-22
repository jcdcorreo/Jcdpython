import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# st.title('Datos Hidrometereológicos Gobierno Regional Piura')
# Usar HTML para centrar el título
st.markdown("<h3 style='text-align: center;color: blue'>Datos Hidrometereológicos Gobierno Regional Piura</h3>", unsafe_allow_html=True)

df = pd.read_csv('tb_medida_estaciones.csv')
# Convertir las cadenas de texto a datetime
df['FECHA_CORTE'] = pd.to_datetime(df['FECHA_CORTE'], format='%Y%m%d')
df['FECHA_MUESTRA'] = pd.to_datetime(df['FECHA_MUESTRA'], format='%Y%m%d')
df.sort_values(by=['FECHA_CORTE', 'FECHA_MUESTRA'], ascending=[True, True], inplace=True)
# Cambiar el formato a DD/MM/YYYY
df['FECHA_CORTE'] = df['FECHA_CORTE'].dt.strftime('%d/%m/%Y')
df['FECHA_MUESTRA'] = df['FECHA_MUESTRA'].dt.strftime('%d/%m/%Y')

# Lista de fechas de corte
fechas_de_corte = ["06/07/2023", "06/06/2023", "06/05/2023", "06/04/2023", "06/03/2023", "06/02/2023", "06/01/2023", "07/12/2022", "06/11/2022", "06/10/2022", "06/09/2022"]

# Lista de estaciones
estaciones = ['ARDILLA','C. DERIVACION','C. HUAYPIRA','C. MIGUEL CHECA','CANAL NORTE','CANAL PRINCIPAL','CHECK(KM 29+900)','COTA EMBALSE','COTA REPRESA','COTE EMBALSE','CURUMUY','EL CIRUELO','EL PAPAYO','ENTRADA','EVAPORACION','INCREMENTO VOL','PARAJE GRANDE','PTE. NACARA','PTE. SANCHEZ CERRO','PUENTE INTERNACIONAL','RIO CHIRA - ALIVIADERO','RIO CHIRA - TUNEL','RIO CHIRA(SULLANA)','TAMBOGRANDE','TOTAL RIO CHIRA','TOTAL SALIDA','VOLUMEN',
]

col1, col2  = st.columns(2)
with col1:
   # Crear un selectbox para las fechas de corte
   fecha_corte_seleccionada = st.selectbox('Seleccione una Fecha de Corte', fechas_de_corte)
with col2:
   estacion_seleccionada = st.selectbox('Seleccione una Estación', estaciones)


# Crear una fila de columnas para los checkboxes
col1, col2, col3, col4 = st.columns(4)
with col1:
    mostrar_caudal07h = st.checkbox('Mostrar Caudal 07H', True)
with col2:
    mostrar_promedio24h = st.checkbox('Mostrar Promedio 24H', True)
with col3:
    mostrar_maxima24h = st.checkbox('Mostrar Máxima 24H', True)
with col4:
    mostrar_precip24h = st.checkbox('Mostrar Precip 24H', True)
# Filtrar el DataFrame
df1 = df[(df['FECHA_CORTE'] == fecha_corte_seleccionada) & (df['ESTACION'] == estacion_seleccionada)]

cuenta = df1['CUENTA'].iloc[0]
tipoestacion = df1['TIPO_ESTACION'].iloc[0]
estacion = df1['ESTACION'].iloc[0]
#departamento = df1['DEPARTAMENTO'].iloc[0]
provincia = df1['PROVINCIA'].iloc[0]
distrito = df1['DISTRITO'].iloc[0]
unidad= df1['UNIDAD_MEDIDA'].iloc[0]
# Creando el gráfico
plt.figure(figsize=(12, 6))

# Mostrar las líneas en el gráfico según los checkboxes
if mostrar_caudal07h:
    plt.plot(df1['FECHA_MUESTRA'], df1['CAUDAL07H'], label='Caudal 07H')
if mostrar_promedio24h:
    plt.plot(df1['FECHA_MUESTRA'], df1['PROMEDIO24H'], label='Promedio 24H')
if mostrar_maxima24h:
    plt.plot(df1['FECHA_MUESTRA'], df1['MAXIMA24H'], label='Máxima 24H')
if mostrar_precip24h:
    plt.plot(df1['FECHA_MUESTRA'], df1['PRECIP24H'], label='Precip 24H')

# Configuración de líneas de cuadrícula
plt.grid(True)  # Activar las líneas de cuadrícula

plt.xlabel('Fecha de Muestras')
plt.ylabel(f'Valores en {unidad}')
plt.title(f'Estación: {estacion}, Tipo de Estación: {tipoestacion}, Cuenca: {cuenta}, Provincia: {provincia},  Distrito: {distrito}')
plt.legend()

# Configurar el localizador de fechas para 30 ticks en el eje X
locator = mdates.AutoDateLocator(minticks=30, maxticks=40)
plt.gca().xaxis.set_major_locator(locator)
plt.xticks(rotation=90)
plt.tight_layout()

# Mostrar el gráfico
st.pyplot(plt.gcf())
