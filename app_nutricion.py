import streamlit as st
import time
import random

# 1. ESTÉTICA "TOJI MODE"
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
    "«MEMENTO MORI: ¿Vas a morir siendo un promedio o una leyenda?»"
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

# 3. MASA CORPORAL
st.subheader("⚖️ MASA CORPORAL")
metodo_p = st.radio("¿TENÉS BALANZA?", ["SÍ", "NO, ESTIMAR"], horizontal=True)
if metodo_p == "NO, ESTIMAR":
    ref = st.select_slider("ESTADO VISUAL:", options=["Delgado", "Atlético", "Promedio", "Fuerte/Pesado"])
    dict_imc = {"Delgado": 18.8, "Atlético": 21.2, "Promedio": 23.8, "Fuerte/Pesado": 27.5}
    peso = (dict_imc[ref] * ((altura/100)**2)) + st.slider("AJUSTE FINO (kg)", -10.0, 10.0, 0.0)
    st.success(f"PESO CALCULADO: **{round(peso, 1)} KG**")
else:
    peso = st.number_input("PESO REAL (kg)", 30.0, 200.0, 68.7)

# CÁLCULOS
tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias = (tmb * factores[actividad]) + (450 if objetivo == "Volumen" else -450 if objetivo == "Definición" else 0)

# 4. PESTAÑAS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN", "🍲 SUMINISTROS", "🧠 MENTE", "🏳️ ÚLTIMA INSTANCIA"])

with tab1:
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("CALORÍAS", f"{int(calorias)} kcal")
    col_m2.metric("AGUA / L", f"{round((peso*35)/1000, 1)} L")
    col_m3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 Proteína: {int(p)}g | 🍞 Carbos: {int(c)}g | 🥑 Grasas: {int(g)}g")

with tab2:
    st.subheader("🧬 LÍMITES BIOLÓGICOS")
    pot_m = (altura - 100) + (muneca * 0.5)
    st.info(f"📍 Límite de masa muscular magra: **{round(pot_m, 1)} kg**")
    score = (muneca + tobillo) / 2
    f1, f2 = st.columns(2)
    f1.metric("POTENCIAL PRESS BANCA", f"{int((peso * 1.2) * (score / 17.5))} kg")
    f2.metric("POTENCIAL PESO MUERTO", f"{int((peso * 2.0) * (score / 17.5))} kg")

with tab3:
    st.subheader("🍲 SUMINISTROS DE COMBATE")
    with st.expander("💸 BAJOS RECURSOS (SUPERVIVENCIA)"):
        st.write("• HUEVOS (30 unidades) • HÍGADO DE VACA (Nutrientes base) • AVENA Y ARROZ (Energía) • LENTEJAS (Proteína vegetal)")

with tab4:
    st.subheader("✍️ EL MURO DEL SILENCIO")
    desahogo = st.text_area("Vaciá tu mente aquí...", height=150)
    if st.button("QUEMAR MENSAJE"):
        st.success("MENSAJE DESTRUIDO.")

with tab5:
    st.subheader("⚠️ PROTOCOLO DE ÚLTIMA INSTANCIA")
    st.error("¿ESTÁS PENSANDO EN RENDIRTE?")
    st.write(f"""
    {nombre}, escuchame bien:
    Rendirse es la opción más fácil, es lo que hace el 99% de la gente. 
    Si te rendís hoy, el dolor no se va, solo se transforma en arrepentimiento. 
    El mundo no se va a detener porque vos estés cansado. 
    
    ¿Mañana vas a estar feliz de haber abandonado hoy? La respuesta es NO.
    """)
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("ME QUIERO RENDIR"):
            st.write("---")
            st.write("❌ **OPCIÓN DENEGADA.**")
            st.write("Tu sistema no acepta la rendición como una variable válida. Tomate 10 minutos, lavate la cara con agua fría y volvé a la pestaña de 'RENDIMIENTO'.")
    
    with col_b:
        if st.button("REINICIAR ESPÍRITU"):
            st.success("⚡ PROTOCOLO DE REINICIO ACTIVADO.")
            st.write("Recuperá tu foco. No sos tus emociones, sos tus acciones. Levantá la cabeza.")