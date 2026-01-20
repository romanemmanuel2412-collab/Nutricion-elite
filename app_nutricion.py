import streamlit as st
import time

# 1. CONFIGURACIÓN Y ESTÉTICA
st.set_page_config(page_title="Toji System", page_icon="🥷", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}
        .stApp { background-color: #0e1117; }
        [data-testid="stMetricValue"] { font-size: 28px !important; color: #00ffcc !important; }
        [data-testid="stMetricLabel"] { font-size: 16px !important; color: #808495 !important; }
        div.stButton > button { width: 100%; border-radius: 10px; background-color: #1f2937; color: white; border: 1px solid #374151; }
        div.stButton > button:hover { border-color: #00ffcc; color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🛡️ TOJI PERFORMANCE</h1>", unsafe_allow_html=True)
st.write("---")

# 2. ENTRADA DE DATOS
c1, c2, c3 = st.columns(3)
with c1:
    peso = st.number_input("Peso (kg)", 40.0, 150.0, 81.0)
    altura = st.number_input("Altura (cm)", 120, 220, 181)
with c2:
    edad = st.number_input("Edad", 12, 90, 20)
    muneca = st.number_input("Muñeca (cm)", 10.0, 25.0, 17.0)
with c3:
    objetivo = st.selectbox("Objetivo", ["Volumen", "Definición", "Mantenimiento"])
    genero = st.radio("Género", ["Hombre", "Mujer"], horizontal=True)

actividad = st.select_slider("Actividad", options=["Sedentario", "Ligero", "Moderado", "Atleta"])

# MOTOR DE CÁLCULO
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
tmb = (66 + (13.7 * peso) + (5 * altura) - (6.8 * edad)) if genero == "Hombre" else (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad))
calorias = (tmb * factores[actividad]) + (400 if objetivo == "Volumen" else -400 if objetivo == "Definición" else 0)

# 3. PESTAÑAS
tab1, tab2, tab3 = st.tabs(["🚀 RENDIMIENTO", "🧬 GENÉTICA", "🧠 MENTALIDAD"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("CALORÍAS", f"{int(calorias)} kcal")
    col2.metric("AGUA", f"{round((peso*35)/1000, 1)} L")
    col3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    
    st.write("### 📊 DISTRIBUCIÓN")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.progress(0.4); st.write(f"🥩 Proteínas: {int(p)}g")
    st.progress(0.7); st.write(f"🍞 Carbos: {int(c)}g")

with tab2:
    st.subheader("🧬 Diagnóstico de Estructura")
    biotipo = "Endo-Mesomorfo" if muneca >= 19 else "Mesomorfo" if muneca > 16.5 else "Ectomorfo"
    st.info(f"Tu biotipo es: **{biotipo}**")
    st.write("---")
    st.write("🍲 **Opciones Económicas:** Huevos, Lentejas, Hígado, Arroz.")

with tab3:
    st.subheader("🌬️ RESPIRACIÓN TÁCTICA")
    if st.button("INICIAR TEMPORIZADOR"):
        ph_txt = st.empty(); ph_bar = st.progress(0)
        pasos = [("🟦 INHALA", "info"), ("⬜ MANTÉN", "warning"), ("🟩 EXHALA", "success"), ("🟨 VACÍO", "error")]
        for ciclo in range(2):
            for txt, tipo in pasos:
                getattr(ph_txt, tipo)(txt)
                for i in range(101):
                    time.sleep(0.035); ph_bar.progress(i)
        ph_txt.success("✅ CALMA RECUPERADA")
    
    st.divider()
    st.text_area("📓 DESCARGA TÁCTICA", placeholder="Escribí para soltar...")