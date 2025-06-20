import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import re

# Funciones auxiliares
def limpiar_texto(texto):
    return re.sub(r'[^\w\s]', '', texto.lower())

def tokenizar(texto):
    return limpiar_texto(texto).split()

def bloques_palabras(palabras, tamaño=20):
    return [palabras[i:i+tamaño] for i in range(0, len(palabras), tamaño)]

def frecuencia_por_bloques(palabras, palabra_objetivo, tamaño=20):
    bloques = bloques_palabras(palabras, tamaño)
    return [bloque.count(palabra_objetivo) for bloque in bloques]

# Interfaz de usuario
st.title("📊 Speech Spectrum Analyzer")
st.write("Analiza la frecuencia y el espectro FFT de una palabra en un texto.")

# Entrada de texto (copiar y pegar)
texto = st.text_area("📄 Pega aquí el texto a analizar:", height=300)

# Entrada de palabra clave
palabra_objetivo = st.text_input("🔍 Palabra a analizar:", value="loneliness")

# Tamaño del bloque
bloque_size = st.slider("📏 Tamaño del bloque (número de palabras):", 5, 100, 20)

# Botón para analizar
if st.button("🚀 Analizar"):
    if texto.strip() == "":
        st.warning("Por favor, pega un texto primero.")
    else:
        palabras = tokenizar(texto)
        señal = frecuencia_por_bloques(palabras, palabra_objetivo, tamaño=bloque_size)
        espectro = np.abs(fft(señal))

        st.subheader(f"📊 Frecuencia de aparición de '{palabra_objetivo}' por bloque")
        st.bar_chart(señal)

        st.subheader("🎼 Espectro FFT")
        st.line_chart(espectro)
