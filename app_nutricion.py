import streamlit as st
import time
import random

# 1. ESTÉTICA "TOJI ZENIN"
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
    "«Tu genética es el mapa, pero tu disciplina es el camino.»",
    "«MEMENTO MORI: ¿Vas a morir siendo un promedio o una leyenda?»"
]

st.markdown("<h1 style='text-align: center;'>🥷 TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #00ffcc; font-style: italic;'>{random.choice(frases)}</p>", unsafe_allow_html=True)

st.divider()

# PRESENTACIÓN Y SALUDO AL USUARIO
col_user, col_mood = st.columns([1, 1])
with col_user:
    nombre_usuario = st.text_input("IDENTIFICATE, GUERRERO:", placeholder="Ingresá tu nombre o alias...")
    if not nombre_usuario:
        nombre_usuario = "Guerrero"

st.write(f"### 👋 Saludos, {nombre_usuario}.")
st.write("Bienvenido al centro de mando. Antes de procesar tu biometría, sincerate con el sistema:")

with col_mood:
    estado_animo = st.select_slider(
        "¿Cómo te sentís hoy mentalmente?",
        options=["Agotado", "Frustrado", "Neutral", "Enfocado", "Modo Bestia"]
    )

if estado_animo in ["Agotado", "Frustrado"]:
    st.warning("⚠️ El cansancio mental precede al fallo físico. Hoy priorizá la técnica sobre el peso.")
elif estado_animo == "Modo Bestia":
    st.success("🔥 Disciplina absoluta. Aprovechá este estado para aplastar tus marcas.")

st.write("---")

# 2. SECCIÓN BIOMÉTRICA
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        genero = st.radio("BIOLOGÍA", ["Hombre", "Mujer"], horizontal=True)
        altura = st.number_input("ALTURA (cm)", 120, 230, 180)
        edad = st.number_input("EDAD", 12, 90, 20)
    with c2:
        muneca = st.number_input("MUÑECA (cm)", 10.0, 25.0, 17.5)
        tobillo = st.number_input("TOBILLO (cm)", 10.0, 35.0, 22.5)
    with c3:
        objetivo = st.selectbox("ESTRATEGIA", ["Volumen", "Definición", "Mantenimiento"])
        actividad = st.selectbox("ACTIVIDAD", ["Sedentario", "Ligero", "Moderado", "Atleta"])

# 3. EL ESTIMADOR DE PESO TÁCTICO RECALIBRADO
st.subheader("⚖️ MASA CORPORAL")
metodo_p = st.radio("¿TENÉS TU PESO EXACTO HOY?", ["SÍ, TENGO BALANZA", "NO, ESTIMAR POR REFERENCIA"], horizontal=True)

if metodo_p == "NO, ESTIMAR POR REFERENCIA":
    referencia = st.select_slider("ESTADO VISUAL:", options=["Delgado", "Atlético", "Promedio", "Fuerte/Pesado"])
    dict_imc = {"Delgado": 18.8, "Atlético": 21.4, "Promedio": 24.0, "Fuerte/Pesado": 27.5}
    peso_base = dict_imc[referencia] * ((altura/100)**2)
    ajuste = st.slider("AJUSTE FINO (kg)", -10.0, 10.0, 0.0)
    peso = peso_base + ajuste
    st.success(f"PESO CALCULADO: **{round(peso, 1)} KG**")
else:
    # Usamos tus 68.7 como sugerencia inicial, pero el usuario pone lo suyo
    peso = st.number_input("PESO REAL (kg)", 30.0, 200.0, 68.7)

# CÁLCULOS METABÓLICOS
tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 450
elif objetivo == "Definición": calorias -= 450

# 4. PESTAÑAS
tab1, tab2, tab3 = st.tabs(["🚀 RENDIMIENTO", "🧬 POTENCIAL GENÉTICO", "🧠 DESAHOGO PRIVADO"])

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
    st.subheader("🧬 ANÁLISIS DE LÍMITES BIOLÓGICOS")
    score = (muneca + tobillo) / 2
    potencial_muscular = (altura - 100) + (muneca * 0.5) 
    st.info(f"📍 Tu límite de masa muscular magra estimado es: **{round(potencial_muscular, 1)} kg**")
    
    st.write("---")
    st.subheader("🏋️ POTENCIAL DE EMPUJE (1RM)")
    bench_press = (peso * 1.2) * (score / 17.5)
    deadlift = (peso * 2.0) * (score / 17.5)
    
    c_f1, c_f2 = st.columns(2)
    c_f1.metric("POTENCIAL PRESS BANCA", f"{int(bench_press)} kg")
    c_f2.metric("POTENCIAL PESO MUERTO", f"{int(deadlift)} kg")

with tab3:
    st.subheader("✍️ EL MURO DEL SILENCIO")
    st.write(f"{nombre_usuario}, este espacio es 100% privado. Soltá lo que te pese.")
    desahogo = st.text_area("Desahogate aquí...", height=150, placeholder="Escribí lo que sentís hoy...")
    
    if st.button("QUEMAR Y SOLTAR"):
        st.balloons()
        st.success("MENSAJE DESTRUIDO. SEGUÍ ADELANTE.")
    
    st.divider()
    st.subheader("🌬️ REINICIO MENTAL")
    if st.button("RESPIRACIÓN TÁCTICA"):
        ph = st.empty(); pb = st.progress(0)
        for i in range(2):
            for t, c in [("🟦 INHALA", "info"), ("⬜ MANTÉN", "warning"), ("🟩 EXHALA", "success"), ("🟨 VACÍO", "error")]:
                getattr(ph, c)(t)
                for p in range(101):
                    time.sleep(0.038); pb.progress(p)
        ph.success("✅ FOCO RECUPERADO.")