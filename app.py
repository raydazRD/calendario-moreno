import streamlit as st
import calendar
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Familia Moreno 2026", page_icon="📅", layout="wide")

# Estilos visuales
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab"] { font-size: 14px; padding: 10px 5px; }
    .memorial { background-color: #f0f2f6; padding: 10px; border-radius: 10px; border-left: 5px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #d4af37;'>📅 Familia Moreno 2026</h1>", unsafe_allow_html=True)

# 2. LISTA DE MESES Y PESTAÑAS
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

FECHAS_ESPECIALES = {
    4: {10: "Aniversario Luctuoso: Abuela 🎗️"},
    11: {27: "Aniversario Luctuoso: Abuelo (Denny) 🎗️"},
    12: {14: "Aniversario Luctuoso: Abdon 🎗️"}
}

# Creamos las pestañas (Tabs)
tabs = st.tabs(MESES)

# 3. LÓGICA PARA CADA MES
for i, tab in enumerate(tabs):
    with tab:
        mes_num = i + 1
        mes_nombre = MESES[i]
        
        # --- MOSTRAR FOTO ---
        # Buscamos archivos que empiecen con el número del mes (Ej: "2-COLLAGE")
        # Sumamos 1 porque Enero es la imagen 2 (la 1 es la portada)
        num_foto = str(mes_num + 1)
        archivos = os.listdir('.')
        foto_a_mostrar = None
        
        for f in archivos:
            if f.startswith(f"{num_foto}-COLLAGE") and f.lower().endswith(".jpg"):
                foto_a_mostrar = f
                break
        
        if foto_a_mostrar:
            st.image(foto_a_mostrar, use_container_width=True)
        else:
            st.warning(f"No se encontró la imagen para {mes_nombre}. Verifica que el nombre empiece con '{num_foto}-COLLAGE'")

        # --- CALENDARIO ---
        st.markdown(f"### Calendario {mes_nombre} 2026")
        cal = calendar.monthcalendar(2026, mes_num)
        
        # Dibujar cuadrícula
        cols = st.columns(7)
        for j, d in enumerate(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]):
            cols[j].markdown(f"**{d}**")

        for semana in cal:
            cols = st.columns(7)
            for k, dia in enumerate(semana):
                if dia == 0:
                    cols[k].text("")
                else:
                    # Resaltar fechas especiales
                    if mes_num in FECHAS_ESPECIALES and dia in FECHAS_ESPECIALES[mes_num]:
                        cols[k].markdown(f"<div class='memorial'>{dia}<br><span style='font-size:10px;'>🎗️</span></div>", unsafe_allow_html=True)
                    else:
                        cols[k].text(str(dia))

# 4. BARRA LATERAL (Sidebar)
st.sidebar.title("🎗️ En Memoria")
st.sidebar.info("""
**Abril 10:** Abuela  
**Nov. 27:** Abuelo (Denny)  
**Dic. 14:** Abdon
""")
