import streamlit as st
import calendar

st.set_page_config(page_title="Familia Moreno 2026", page_icon="📅")
st.markdown("<h1 style='text-align: center; color: #d4af37;'>📅 Familia Moreno 2026</h1>", unsafe_allow_html=True)

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# FECHAS CORREGIDAS
FECHAS_ESPECIALES = {
    4: {10: "Aniversario Luctuoso: Abuela 🎗️"},
    11: {27: "Aniversario Luctuoso: Abuelo (Denny) 🎗️"}, # <-- CORREGIDO
    12: {14: "Aniversario Luctuoso: Abdon 🎗️"}
}

mes_nombre = st.select_slider("Desliza para cambiar de mes:", options=MESES)
mes_num = MESES.index(mes_nombre) + 1

st.info(f"Visualizando mes de {mes_nombre}")

st.markdown(f"### Calendario {mes_nombre}")
cal = calendar.monthcalendar(2026, mes_num)
cols = st.columns(7)
for i, d in enumerate(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]):
    cols[i].markdown(f"**{d}**")

for semana in cal:
    cols = st.columns(7)
    for i, dia in enumerate(semana):
        if dia == 0:
            cols[i].text("")
        else:
            if mes_num in FECHAS_ESPECIALES and dia in FECHAS_ESPECIALES[mes_num]:
                cols[i].markdown(f"<div style='background-color:#f0f0f0; border-radius:5px; padding:5px; border-left:3px solid #555;'>{dia}<br><span style='font-size:10px;'>🎗️</span></div>", unsafe_allow_html=True)
            else:
                cols[i].text(str(dia))

st.sidebar.markdown("### 🎗️ En Memoria")
st.sidebar.write("Abril 10: Abuela")
st.sidebar.write("Nov. 27: Abuelo (Denny)")
st.sidebar.write("Dic. 14: Abdon")
