import streamlit as st
import time
import random

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Toji System", page_icon="🥷", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}
        .stApp { background-color: #0e1117; }
        [data-testid="stMetricValue"] { font-size: 32px !important; color: #00ffcc !important; }
        div.stButton > button { width: 100%; border-radius: 12px; background-color: #1f2937; color: white; border: 1px solid #374151; font-weight: bold; height: 3.5em; }
        div.stButton > button:hover { border-color: #00ffcc; color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🛡️ TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)

# 2. SECCIÓN DE DATOS INICIALES
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        genero = st.radio("Género Biológico", ["Hombre", "Mujer"], horizontal=True)
        altura = st.number_input("Altura (cm)", 120, 230, 180)
    with c2:
        edad = st.number_input("Edad", 12, 90, 20)
        actividad = st.selectbox("Nivel de Actividad", ["Sedentario", "Ligero", "Moderado", "Atleta"])
    with c3:
        muneca = st.number_input("Muñeca (cm)", 10.0, 25.0, 17.0)
        tobillo = st.number_input("Tobillo (cm)", 10.0, 35.0, 22.0)

st.divider()

# 3. EL ESTIMADOR DE PESO COHERENTE
st.subheader("⚖️ Registro de Masa Corporal")
metodo_p = st.radio("Seleccioná tu situación:", ["Tengo mi peso exacto", "No tengo balanza (Estimar por referencia)"], horizontal=True)

if metodo_p == "No tengo balanza (Estimar por referencia)":
    st.write("Seleccioná el estado actual de tu físico para calcular tu peso según tu altura:")
    
    # Imagen de referencia visual (contextual)
    
    
    referencia = st.select_slider(
        "¿Cómo te ves hoy?",
        options=["Muy Delgado", "Atlético / Marcado", "Promedio", "Con sobrepeso", "Mucha masa muscular"]
    )
    
    # Lógica de IMC inverso según referencia visual
    dict_referencia = {
        "Muy Delgado": 19.5,
        "Atlético / Marcado": 22.5,
        "Promedio": 25.0,
        "Con sobrepeso": 29.0,
        "Mucha masa muscular": 27.5
    }
    
    imc_base = dict_referencia[referencia]
    # El peso se calcula: IMC * (Altura en m)^2
    peso_calculado = imc_base * ((altura/100)**2)
    
    # Ajuste por estructura ósea (muñeca y tobillo)
    # Si tiene huesos grandes, sumamos un poco de peso "extra" por densidad ósea
    if (muneca + tobillo) / 2 > 19:
        peso_calculado *= 1.05 
        
    st.success(f"Tu peso estimado según tu altura y físico es: **{round(peso_calculado, 1)} kg**")
    peso = peso_calculado
else:
    peso = st.number_input("Ingresá tu peso real (kg)", 30.0, 200.0, 68.7)

# CÁLCULOS METABÓLICOS
objetivo = st.selectbox("Objetivo Estratégico", ["Volumen", "Definición", "Mantenimiento"])
tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 400
elif objetivo == "Definición": calorias -= 400

# 4. PESTAÑAS
t1, t2, t3 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN", "🧠 DESAHOGO & CALMA"])

with t1:
    m1, m2, m3 = st.columns(3)
    m1.metric("CALORÍAS", f"{int(calorias)} kcal")
    m2.metric("AGUA", f"{round((peso*35)/1000, 1)} L")
    m3.metric("PROTEÍNA", f"{int(peso*2)}g")

with t2:
    st.subheader("🧬 ESTRUCTURA ÓSEA")
    score = (muneca + tobillo) / 2
    if score >= 19.5: biotipo = "ENDOMORFO"
    elif score >= 17: biotipo = "MESOMORFO"
    else: biotipo = "ECTOMORFO"
    st.success(f"Biotipo: {biotipo}")

with t3:
    st.subheader("✍️ MURO DEL SILENCIO (DESAHOGO PRIVADO)")
    st.write("Escribí lo que sentís. Al tocar el botón, el mensaje se destruye.")
    desahogo = st.text_area("Vaciá tu mente aquí...", height=150)
    if st.button("QUEMAR Y SOLTAR"):
        st.success("Liberado.")
    
    st.divider()
    if st.button("INICIAR RESPIRACIÓN TÁCTICA"):
        ph = st.empty(); pb = st.progress(0)
        for i in range(2):
            for t, c in [("🟦 INHALA", "info"), ("⬜ MANTÉN", "warning"), ("🟩 EXHALA", "success"), ("🟨 VACÍO", "error")]:
                getattr(ph, c)(t)
                for p in range(101):
                    time.sleep(0.038); pb.progress(p)