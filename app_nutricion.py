import streamlit as st
import time
import random

# 1. CONFIGURACIÓN DE ÉLITE Y ESTÉTICA
st.set_page_config(page_title="Toji System", page_icon="🥷", layout="wide", initial_sidebar_state="collapsed")

# CSS para matar la barra lateral y estilizar tarjetas
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}
        .stApp { background-color: #0e1117; }
        [data-testid="stMetricValue"] { font-size: 32px !important; color: #00ffcc !important; }
        [data-testid="stMetricLabel"] { font-size: 16px !important; color: #808495 !important; }
        div.stButton > button { width: 100%; border-radius: 12px; background-color: #1f2937; color: white; border: 1px solid #374151; font-weight: bold; height: 3em; }
        div.stButton > button:hover { border-color: #00ffcc; color: #00ffcc; }
        .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. PRESENTACIÓN Y FRASES
frases = [
    "«El dolor es temporal, el orgullo es para siempre.»",
    "«No te detengas cuando estés cansado, detente cuando hayas terminado.»",
    "«Tu genética es el chasis, tu disciplina es el motor.»",
    "«La claridad mental es el arma más letal de un guerrero.»"
]

st.markdown("<h1 style='text-align: center; color: white;'>🛡️ TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #00ffcc; font-style: italic;'>{random.choice(frases)}</p>", unsafe_allow_html=True)

st.write("### 👋 ¡Hola, Guerrero!")
st.write("Bienvenido a tu centro de mando. Antes de optimizar tu rendimiento, ¿podrías brindarnos tus datos básicos para ajustar el sistema a tu biotipo?")

st.divider()

# 3. ENTRADA DE DATOS E INTERACTIVIDAD
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        altura = st.number_input("Altura (cm)", 120, 230, 181)
        genero = st.radio("Género Biológico", ["Hombre", "Mujer"], horizontal=True)
    with c2:
        edad = st.number_input("Edad", 12, 90, 20)
        muneca = st.number_input("Muñeca (cm)", 10.0, 25.0, 17.0)
    with c3:
        objetivo = st.selectbox("Objetivo Estratégico", ["Volumen", "Definición", "Mantenimiento"])
        actividad = st.selectbox("Nivel de Actividad", ["Sedentario", "Ligero", "Moderado", "Atleta"])

# FUNCIÓN: ESTIMACIÓN DE PESO SIN BALANZA
st.write("---")
with st.expander("⚖️ ¿NO TENÉS BALANZA? CALCULÁ TU PESO AQUÍ"):
    st.write("Si no tenés balanza a mano, usá una cinta métrica:")
    c_cuello = st.number_input("Cuello (cm)", 20.0, 60.0, 38.0)
    c_cintura = st.number_input("Cintura ombligo (cm)", 40.0, 150.0, 85.0)
    
    peso_est = (c_cintura * 0.7) + (c_cuello * 0.5) + (altura * 0.1) - 105
    if genero == "Mujer": peso_est -= 5
    st.info(f"Peso estimado: **{round(peso_est, 1)} kg**")
    
peso = st.number_input("Ingresá tu peso final (o el estimado de arriba)", 40.0, 200.0, 80.0)

# MOTOR DE CÁLCULO
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
tmb = (66 + (13.7 * peso) + (5 * altura) - (6.8 * edad)) if genero == "Hombre" else (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad))
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 450
elif objetivo == "Definición": calorias -= 450

# 4. PESTAÑAS DE CONTENIDO
tab1, tab2, tab3 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN GENÉTICO", "🧠 SALUD MENTAL"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("CALORÍAS", f"{int(calorias)} kcal")
    col2.metric("AGUA / DÍA", f"{round((peso*35)/1000, 1)} L")
    col3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    
    st.write("### 📊 DISTRIBUCIÓN DE MACROS")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 Proteína: {int(p)}g"); st.progress(0.35)
    st.write(f"🍞 Carbos: {int(c)}g"); st.progress(0.65)
    st.write(f"🥑 Grasas: {int(g)}g"); st.progress(0.15)
    
    st.divider()
    st.subheader("🍲 COMBUSTIBLE ECONÓMICO")
    st.write("• **Proteínas:** Huevos hervidos, Hígado vacuno, Lentejas.")
    st.write("• **Carbos:** Arroz, Avena suelta, Papa hervida.")

with tab2:
    st.subheader("🧬 DIAGNÓSTICO ESTRUCTURAL")
    if muneca >= 19:
        biotipo, desc = "ENDOMORFO", "Estructura ósea masiva. Gran facilidad para ganar fuerza bruta."
    elif muneca > 16.5:
        biotipo, desc = "MESOMORFO", "Estructura atlética. Ganancia muscular rápida y estética."
    else:
        biotipo, desc = "ECTOMORFO", "Estructura fina. Definición natural, requiere comer más para ganar volumen."
    
    st.success(f"**Biotipo Detectado:** {biotipo}")
    st.write(desc)
    

with tab3:
    st.subheader("🌬️ RESPIRACIÓN TÁCTICA (BOX BREATHING)")
    if st.button("INICIAR TEMPORIZADOR VISUAL"):
        ph_t = st.empty(); ph_b = st.progress(0)
        pasos = [("🟦 INHALA...", "info"), ("⬜ MANTÉN...", "warning"), ("🟩 EXHALA...", "success"), ("🟨 VACÍO...", "error")]
        for ciclo in range(2):
            for t, tip in pasos:
                getattr(ph_t, tip)(t)
                for i in range(101):
                    time.sleep(0.038); ph_b.progress(i)
        ph_t.success("✅ SISTEMA RESETEADO")
    
    st.divider()
    st.subheader("📓 DESCARGA TÁCTICA")
    st.text_area("Vaciá tu mente aquí...", placeholder="Soltá lo que te pesa...")