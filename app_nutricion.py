import streamlit as st
import time
import random

# 1. ESTÉTICA "TOJI ZENIN" (MODO GUERREO)
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
        .stExpander { background-color: #161b22 !important; border: 1px solid #30363d !important; }
    </style>
    """, unsafe_allow_html=True)

# MÁXIMAS
frases = [
    "«No soy un prodigio, soy un error del sistema que entrena más que vos.»",
    "«El dolor es solo información. Ignorala y seguí.»",
    "«Tu genética es el mapa, pero tu disciplina es el camino.»",
    "«MEMENTO MORI: ¿Vas a morir siendo un promedio o una leyenda?»",
    "«Entrená como si fueras el hombre más buscado del mundo.»"
]

st.markdown("<h1 style='text-align: center;'>🥷 TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #00ffcc; font-style: italic;'>{random.choice(frases)}</p>", unsafe_allow_html=True)

st.divider()

# PRESENTACIÓN CORDIAL
col_u, col_m = st.columns([1, 1])
with col_u:
    nombre = st.text_input("IDENTIFICATE, GUERRERO:", placeholder="Ingresá tu nombre o alias...")
    nombre = nombre if nombre else "Guerrero"
    st.write(f"### 👋 Saludos, {nombre}.")

with col_m:
    estado = st.select_slider("¿Cómo está tu mente hoy?", options=["Agotado", "Frustrado", "Neutral", "Enfocado", "Modo Bestia"])

st.write("---")

# 2. BIOMETRÍA
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

# 3. PESO TÁCTICO RECALIBRADO
st.subheader("⚖️ MASA CORPORAL")
metodo_p = st.radio("¿TENÉS BALANZA?", ["SÍ", "NO, ESTIMAR"], horizontal=True)
if metodo_p == "NO, ESTIMAR":
    ref = st.select_slider("ESTADO VISUAL:", options=["Delgado", "Atlético", "Promedio", "Fuerte/Pesado"])
    dict_imc = {"Delgado": 18.8, "Atlético": 21.2, "Promedio": 23.8, "Fuerte/Pesado": 27.5}
    peso_base = dict_imc[ref] * ((altura/100)**2)
    peso = peso_base + st.slider("AJUSTE DE PRECISIÓN (kg)", -10.0, 10.0, 0.0)
    st.success(f"PESO CALCULADO: **{round(peso, 1)} KG**")
else:
    peso = st.number_input("PESO REAL (kg)", 30.0, 200.0, 68.7)

# CÁLCULOS NUTRICIONALES
tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
fact_act = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias = tmb * fact_act[actividad]
if objetivo == "Volumen": calorias += 450
elif objetivo == "Definición": calorias -= 450

# 4. PESTAÑAS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN", "🍲 SUMINISTROS", "🧠 MENTE", "🏳️ ÚLTIMA INSTANCIA"])

with tab1:
    m1, m2, m3 = st.columns(3)
    m1.metric("CALORÍAS", f"{int(calorias)} kcal")
    m2.metric("AGUA / L", f"{round((peso*35)/1000, 1)} L")
    m3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 Proteína: {int(p)}g | 🍞 Carbos: {int(c)}g | 🥑 Grasas: {int(g)}g")

with tab2:
    st.subheader("🧬 LÍMITES BIOLÓGICOS")
    pot_m = (altura - 100) + (muneca * 0.5)
    st.info(f"📍 Masa muscular magra límite: **{round(pot_m, 1)} kg**")
    score = (muneca + tobillo) / 2
    
    # AJUSTE DE FUERZA (NIVEL GUERRERO AVANZADO)
    bench_p = (peso * 1.5) * (score / 17.5)  # Aumentado de 1.2 a 1.5
    dead_p = (peso * 2.5) * (score / 17.5)   # Aumentado de 2.0 a 2.5
    
    f1, f2 = st.columns(2)
    f1.metric("POTENCIAL PRESS BANCA", f"{int(bench_p)} kg")
    f2.metric("POTENCIAL PESO MUERTO", f"{int(dead_p)} kg")
    st.write("⚠️ *Valores ajustados para potencial de fuerza máxima según estructura ósea densa.*")

with tab3:
    st.subheader("🍲 SUMINISTROS DE COMBATE")
    with st.expander("💸 NIVEL 1: BAJOS RECURSOS (SUPERVIVENCIA)"):
        st.write("• **HUEVOS:** Fuente de proteína perfecta. • **HÍGADO DE VACA:** Multivitamínico natural. • **AVENA/ARROZ/PAPA:** Energía base. • **LENTEJAS:** Fibra y proteína económica.")
    with st.expander("⚖️ NIVEL 2: EQUILIBRADO"):
        st.write("• Pollo, carne picada magra, yogur natural y frutas de estación.")
    with st.expander("🔱 NIVEL 3: ÓPTIMO"):
        st.write("• Pescados azules, Palta, Frutos secos y Aceite de Oliva.")

with tab4:
    st.subheader("✍️ EL MURO DEL SILENCIO")
    desahogo = st.text_area("Vaciá tu mente aquí...", height=150)
    if st.button("QUEMAR MENSAJE"):
        st.balloons()
        st.success("MENSAJE DESTRUIDO.")

with tab5:
    st.subheader("⚠️ PROTOCOLO DE ÚLTIMA INSTANCIA")
    st.error(f"¿PENSANDO EN RENDIRTE, {nombre.upper()}?")
    col_x, col_y = st.columns(2)
    with col_x:
        if st.button("ME QUIERO RENDIR"):
            st.warning("❌ OPCIÓN DENEGADA. Descansá, no abandones.")
    with col_y:
        if st.button("REINICIAR ESPÍRITU"):
            st.success("⚡ ESPÍRITU RECALIBRADO.")