import streamlit as st
import time
import random

# 1. ESTÉTICA "TOJI ZENIN" (DARK & NEON)
st.set_page_config(page_title="Toji Performance System", page_icon="🥷", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}
        .stApp { background-color: #0e1117; }
        [data-testid="stMetricValue"] { font-size: 30px !important; color: #00ffcc !important; text-shadow: 0 0 10px #00ffcc; }
        div.stButton > button { width: 100%; border-radius: 12px; background-color: #1f2937; color: white; border: 1px solid #374151; font-weight: bold; height: 3.5em; text-transform: uppercase; letter-spacing: 2px; }
        div.stButton > button:hover { border-color: #00ffcc; color: #00ffcc; box-shadow: 0 0 20px #00ffcc; }
        .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
        h1, h2, h3 { color: white !important; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# MÁXIMAS DEL SISTEMA
frases = [
    "«No soy un prodigio, soy un error del sistema que entrena más que vos.»",
    "«El dolor es solo información. Ignorala y seguí.»",
    "«Tu potencial genético es el techo, tu disciplina es el ascensor.»",
    "«MEMENTO MORI: ¿Vas a morir siendo un promedio o una leyenda?»"
]

st.markdown("<h1 style='text-align: center;'>🥷 TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #00ffcc; font-style: italic;'>{random.choice(frases)}</p>", unsafe_allow_html=True)

st.divider()

# 2. SECCIÓN BIOMÉTRICA (MUÑECA Y TOBILLO CLAVES)
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        genero = st.radio("BIOLOGÍA", ["Hombre", "Mujer"], horizontal=True)
        altura = st.number_input("ALTURA (cm)", 120, 230, 180)
        edad = st.number_input("EDAD", 12, 90, 20)
    with c2:
        muneca = st.number_input("MUÑECA (cm)", 10.0, 25.0, 17.0)
        tobillo = st.number_input("TOBILLO (cm)", 10.0, 35.0, 22.0)
    with c3:
        objetivo = st.selectbox("ESTRATEGIA", ["Volumen", "Definición", "Mantenimiento"])
        actividad = st.selectbox("ACTIVIDAD", ["Sedentario", "Ligero", "Moderado", "Atleta"])

# 3. EL ESTIMADOR DE PESO TÁCTICO (RECALIBRADO)
st.subheader("⚖️ MASA CORPORAL")
metodo_p = st.radio("¿ESTÁS EN BALANZA?", ["SÍ", "NO, ESTIMAR"], horizontal=True)

if metodo_p == "NO, ESTIMAR":
    referencia = st.select_slider("ESTADO VISUAL:", options=["Delgado", "Atlético", "Promedio", "Fuerte/Pesado"])
    dict_imc = {"Delgado": 18.8, "Atlético": 21.4, "Promedio": 24.0, "Fuerte/Pesado": 27.5}
    peso_base = dict_imc[referencia] * ((altura/100)**2)
    ajuste = st.slider("AJUSTE FINO (kg)", -10.0, 10.0, 0.0)
    peso = peso_base + ajuste
    st.success(f"PESO CALCULADO: **{round(peso, 1)} KG**")
else:
    peso = st.number_input("PESO REAL (kg)", 30.0, 200.0, 68.7)

# CÁLCULOS METABÓLICOS
tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 450
elif objetivo == "Definición": calorias -= 450

# 4. PESTAÑAS: RENDIMIENTO, ADN Y MENTE
tab1, tab2, tab3 = st.tabs(["🚀 RENDIMIENTO", "🧬 POTENCIAL ADN", "🧠 CENTRO MENTAL"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("CALORÍAS", f"{int(calorias)} kcal")
    col2.metric("AGUA / L", f"{round((peso*35)/1000, 1)} L")
    col3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    
    st.write("### 📊 MACROS DE COMBATE")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 Proteína: {int(p)}g"); st.progress(0.35)
    st.write(f"🍞 Carbos: {int(c)}g"); st.progress(0.65)
    st.write(f"🥑 Grasas: {int(g)}g"); st.progress(0.15)

with tab2:
    st.subheader("🧬 ANÁLISIS DE LÍMITES GENÉTICOS")
    score = (muneca + tobillo) / 2
    
    # CÁLCULOS DE POTENCIAL (LA ESENCIA)
    potencial_muscular = (altura - 100) + (muneca * 0.5) 
    st.info(f"📍 Tu límite de masa muscular magra estimado es: **{round(potencial_muscular, 1)} kg**")
    
    st.write("---")
    st.subheader("🏋️ POTENCIAL DE EMPUJE (1RM ESTIMADO)")
    # El potencial de fuerza se basa en la estructura ósea (muñeca/tobillo)
    bench_press = (peso * 1.2) * (score / 17.5)
    deadlift = (peso * 2.0) * (score / 17.5)
    
    c_f1, c_f2 = st.columns(2)
    c_f1.metric("POTENCIAL PRESS BANCA", f"{int(bench_press)} kg")
    c_f2.metric("POTENCIAL PESO MUERTO", f"{int(deadlift)} kg")
    
    st.write("⚠️ *Estos son los números que tu chasis puede soportar si entrenás como una bestia.*")

with tab3:
    st.subheader("✍️ EL MURO DEL SILENCIO (DESAHOGO)")
    st.write("Soltá acá todo lo que te dolió hoy. El mensaje que no llegó, la traición, la bronca. Escribilo y destruilo.")
    desahogo = st.text_area("Desahogate...", height=150, placeholder="Escribí aquí tu mensaje privado...")
    
    if st.button("QUEMAR Y LIBERAR"):
        st.balloons()
        st.success("MENSAJE DESTRUIDO. EL PASADO NO TIENE PODER SOBRE VOS.")
    
    st.divider()
    st.subheader("🌬️ RESPIRACIÓN TÁCTICA")
    if st.button("INICIAR REINICIO MENTAL"):
        ph = st.empty(); pb = st.progress(0)
        for i in range(2):
            for t, c in [("🟦 INHALA", "info"), ("⬜ MANTÉN", "warning"), ("🟩 EXHALA", "success"), ("🟨 VACÍO", "error")]:
                getattr(ph, c)(t)
                for p in range(101):
                    time.sleep(0.038); pb.progress(p)
        ph.success("✅ FOCO RECUPERADO. VOLVÉ AL RUEDO.")