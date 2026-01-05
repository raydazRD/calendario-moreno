import streamlit as st
import calendar
import os

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Familia Moreno 2026", page_icon="📅")

# ESTILO CSS CORREGIDO (Días visibles y negros)
st.markdown("""
    <style>
    .calendario-tabla { 
        width: 100%; 
        border-collapse: collapse; 
        table-layout: fixed; 
        background-color: white; 
        color: black !important; 
    }
    .calendario-tabla th, .calendario-tabla td { 
        border: 1px solid #ddd; 
        padding: 8px; 
        text-align: center; 
        font-size: 14px; 
        color: black !important; 
    }
    .calendario-tabla th { 
        background-color: #f0f2f6; 
        font-weight: bold; 
        color: #333 !important; 
    }
    .dia-especial { 
        background-color: #fff4e6; 
        border-left: 3px solid #d4af37 !important; 
        font-weight: bold; 
    }
    .stTabs [data-baseweb="tab"] { font-size: 12px; padding: 10px 2px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #d4af37;'>📅 Familia Moreno 2026</h1>", unsafe_allow_html=True)

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

FECHAS_ESPECIALES = {
    4: {10: "Abuela 🎗️"},
    11: {27: "Abuelo 🎗️"},
    12: {14: "Abdon 🎗️"}
}

tabs = st.tabs(MESES)

for i, tab in enumerate(tabs):
    with tab:
        mes_num = i + 1
        mes_nombre = MESES[i]
        
        # --- FOTO ---
        num_foto = str(mes_num + 1)
        archivos = os.listdir('.')
        foto_a_mostrar = next((f for f in archivos if f.startswith(f"{num_foto}-COLLAGE") and f.lower().endswith(".jpg")), None)
        
        if foto_a_mostrar:
            st.image(foto_a_mostrar, use_container_width=True)

        # --- CALENDARIO EN FORMATO TABLA ---
        cal = calendar.monthcalendar(2026, mes_num)
        
        # Inicia la tabla
        html_cal = '<table class="calendario-tabla"><thead><tr>'
        for d in ["Lu", "Ma", "Mi", "Ju", "Vi", "Sá", "Do"]:
            html_cal += f'<th>{d}</th>'
        html_cal += '</tr></thead><tbody>'

        for semana in cal:
            html_cal += '<tr>'
            for dia in semana:
                if dia == 0:
                    html_cal += '<td></td>'
                else:
                    clase = 'dia-especial' if (mes_num in FECHAS_ESPECIALES and dia in FECHAS_ESPECIALES[mes_num]) else ''
                    emoji = '🎗️' if clase else ''
                    html_cal += f'<td class="{clase}">{dia}<br><span style="font-size:10px;">{emoji}</span></td>'
            html_cal += '</tr>'
        html_cal += '</tbody></table>'
        
        st.markdown(html_cal, unsafe_allow_html=True)

st.sidebar.title("🎗️ En Memoria")
st.sidebar.info("Abril 10: Abuela\n\nNov. 27: Abuelo\n\nDic. 14: Abdon")
