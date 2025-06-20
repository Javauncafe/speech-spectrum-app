import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter
from scipy.fft import fft

# Funciones auxiliares
def limpiar_texto(texto):
    return re.sub(r'[^\w\s]', '', texto.lower())

def tokenizar(texto):
    return limpiar_texto(texto).split()

# Interfaz de usuario
st.title("📊 Analizador de Frecuencia + Espectro FFT de Palabras")
st.write("Pega un texto y analiza las palabras más repetidas, junto con su espectro de frecuencia.")

# Entrada de texto
texto = st.text_area("📄 Pega aquí el texto a analizar:", height=300)

# Número de palabras a mostrar
top_n = st.slider("📌 ¿Cuántas palabras más frecuentes deseas ver?", 5, 50, 10)

# Botón para procesar
if st.button("🚀 Analizar"):
    if texto.strip() == "":
        st.warning("Por favor, pega un texto primero.")
    else:
        palabras = tokenizar(texto)
        conteo = Counter(palabras)
        palabras_mas_comunes = conteo.most_common(top_n)

        st.subheader(f"🔝 Top {top_n} palabras más repetidas")
        st.table(palabras_mas_comunes)

        # Gráfico de barras
        palabras_labels, frecuencias = zip(*palabras_mas_comunes)
        st.subheader("📊 Frecuencia de Palabras")
        st.bar_chart(data=frecuencias)

        # Espectro FFT
        espectro = np.abs(fft(frecuencias))
        st.subheader("🎼 Espectro FFT")
        st.line_chart(espectro)
