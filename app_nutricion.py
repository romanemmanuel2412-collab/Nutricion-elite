import streamlit as st
import time
import random

# 1. CONFIGURACIÓN Y ESTÉTICA "TOJI MODE"
st.set_page_config(page_title="Toji Performance System", page_icon="🥷", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}
        .stApp { background-color: #0e1117; }
        [data-testid="stMetricValue"] { font-size: 32px !important; color: #00ffcc !important; text-shadow: 0 0 10px #00ffcc; }
        div.stButton > button { width: 100%; border-radius: 12px; background-color: #1f2937; color: white; border: 1px solid #374151; font-weight: bold; height: 3.5em; text-transform: uppercase; letter-spacing: 1px; }
        div.stButton > button:hover { border-color: #00ffcc; color: #00ffcc; box-shadow: 0 0 15px #00ffcc; }
        .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
        h1, h2, h3 { color: white !important; }
        .stProgress > div > div > div > div { background-color: #00ffcc !important; }
    </style>
    """, unsafe_allow_html=True)

# FRASES DE PODER (LA ESENCIA)
frases = [
    "«El dolor es el combustible de tu nueva versión.»",
    "«No nos afecta lo que sucede, sino lo que nos decimos sobre ello.» — Marco Aurelio",
    "«Tu genética es el mapa, pero tu disciplina es el camino.»",
    "«La mejor venganza es un éxito masivo y una mente en calma.»",
    "«MEMENTO MORI: Recordá que vas a morir, hacé que hoy valga la pena.»",
    "«Entrená como si fueras el hombre más buscado del mundo.»"
]

st.markdown("<h1 style='text-align: center;'>🛡️ TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #00ffcc; font-style: italic; font-size: 1.2rem;'>{random.choice(frases)}</p>", unsafe_allow_html=True)

st.write("---")
st.write("### 👋 ¡HOLA, GUERRERO!")
st.write("Bienvenido a tu centro de mando. Aquí optimizamos el cuerpo y blindamos la mente. Sin excusas.")

# 2. SECCIÓN DE BIOMETRÍA Y DATOS
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        genero = st.radio("GÉNERO BIOLÓGICO", ["Hombre", "Mujer"], horizontal=True)
        altura = st.number_input("ALTURA (cm)", 120, 230, 180)
        edad = st.number_input("EDAD", 12, 90, 20)
    with c2:
        muneca = st.number_input("MUÑECA (cm)", 10.0, 25.0, 17.0)
        tobillo = st.number_input("TOBILLO (cm)", 10.0, 35.0, 22.0)
    with c3:
        objetivo = st.selectbox("OBJETIVO ESTRATÉGICO", ["Volumen", "Definición", "Mantenimiento"])
        actividad = st.selectbox("NIVEL DE ACTIVIDAD", ["Sedentario", "Ligero", "Moderado", "Atleta"])

# 3. ESTIMADOR DE PESO TÁCTICO RECALIBRADO
st.subheader("⚖️ CONTROL DE MASA CORPORAL")
metodo_p = st.radio("¿TENÉS TU PESO EXACTO?", ["SÍ, TENGO BALANZA", "NO, ESTIMAR POR REFERENCIA"], horizontal=True)

if metodo_p == "NO, ESTIMAR POR REFERENCIA":
    st.info("💡 Calcularemos tu peso basándonos en tu altura y estado visual.")
    referencia = st.select_slider(
        "¿CÓMO TE VES HOY?",
        options=["Muy Delgado", "Atlético", "Promedio", "Sobrepeso", "Musculoso"]
    )
    # IMC recalibrado para mayor coherencia
    dict_imc = {"Muy Delgado": 18.5, "Atlético": 21.2, "Promedio": 23.8, "Sobrepeso": 27.5, "Musculoso": 26.5}
    peso_base = dict_imc[referencia] * ((altura/100)**2)
    
    # Ajuste manual de precisión para el usuario
    ajuste_fino = st.slider("Ajuste de precisión (kg)", -10.0, 10.0, 0.0, help="Mové esto para terminar de calzar tu peso real.")
    peso = peso_base + ajuste_fino
    st.success(f"PESO CALCULADO: **{round(peso, 1)} KG**")
else:
    peso = st.number_input("INGRESA TU PESO REAL (kg)", 30.0, 200.0, 68.7)

# MOTOR DE CÁLCULO
tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 450
elif objetivo == "Definición": calorias -= 450

# 4. PESTAÑAS DE CONTENIDO
tab1, tab2, tab3 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN & GENÉTICA", "🧠 MURO DE DESAHOGO"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("CALORÍAS", f"{int(calorias)} kcal")
    col2.metric("AGUA / DÍA", f"{round((peso*35)/1000, 1)} L")
    col3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    
    st.write("---")
    st.subheader("📊 DISTRIBUCIÓN DE COMBATE (MACROS)")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 **PROTEÍNA:** {int(p)}g"); st.progress(0.35)
    st.write(f"🍞 **CARBOS:** {int(c)}g"); st.progress(0.65)
    st.write(f"🥑 **GRASAS:** {int(g)}g"); st.progress(0.15)
    
    with st.expander("🍲 COMBUSTIBLE ECONÓMICO"):
        st.write("• **HUEVOS:** El oro nutricional.")
        st.write("• **HÍGADO:** Fuerza pura a bajo costo.")
        st.write("• **AVENA/ARROZ:** Tu motor de energía.")

with tab2:
    st.subheader("🧬 DIAGNÓSTICO BIO-ESTRUCTURAL")
    score = (muneca + tobillo) / 2
    if score >= 19.5: biotipo, desc = "ENDOMORFO", "Chasis de tanque. Potencial de fuerza bruta de élite."
    elif score >= 17: biotipo, desc = "MESOMORFO", "Estructura atlética perfecta. Respuesta rápida al estímulo."
    else: biotipo, desc = "ECTOMORFO", "Estructura ligera. Definición estética natural, pero necesita comer por dos."
    
    st.success(f"BIOTIPO: **{biotipo}**")
    st.write(f"**ANÁLISIS:** {desc}")

with tab3:
    st.subheader("✍️ EL MURO DEL SILENCIO (DESAHOGO)")
    st.write("Escribí acá lo que te quema por dentro: el rechazo, la bronca o la frustración. Nadie lo verá.")
    desahogo = st.text_area("Desahogate, Guerrero...", height=180, placeholder="Soltá la rabia de hoy... escribí lo que no podés decir.")
    
    if st.button("QUEMAR MENSAJE Y SOLTAR"):
        st.balloons()
        st.success("MENSAJE DESTRUIDO. TU MENTE ESTÁ LIMPIA. SEGUÍ ADELANTE.")
    
    st.divider()
    st.subheader("🌬️ RESPIRACIÓN TÁCTICA (BOX BREATHING)")
    if st.button("INICIAR CICLO DE CALMA (4-4-4-4)"):
        ph = st.empty(); pb = st.progress(0)
        for i in range(2):
            for t, col in [("🟦 INHALA", "info"), ("⬜ MANTÉN", "warning"), ("🟩 EXHALA", "success"), ("🟨 VACÍO", "error")]:
                getattr(ph, col)(t)
                for p in range(101):
                    time.sleep(0.038); pb.progress(p)
        ph.success("✅ FOCO RECUPERADO.")