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

# MÁXIMAS DEL SISTEMA
frases = [
    "«No soy un prodigio, soy un error del sistema que entrena más que vos.»",
    "«El dolor es solo información. Ignorala y seguí.»",
    "«Tu genética es el mapa, pero tu disciplina es el camino.»",
    "«La mejor venganza es un éxito masivo y una mente en calma.»",
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

# 3. MASA CORPORAL (ESTIMADOR TÁCTICO)
st.subheader("⚖️ MASA CORPORAL")
metodo_p = st.radio("¿TENÉS BALANZA?", ["SÍ", "NO, ESTIMAR"], horizontal=True)

if metodo_p == "NO, ESTIMAR":
    ref = st.select_slider("ESTADO VISUAL:", options=["Delgado", "Atlético", "Promedio", "Fuerte/Pesado"])
    dict_imc = {"Delgado": 18.8, "Atlético": 21.2, "Promedio": 23.8, "Fuerte/Pesado": 27.5}
    peso_est = dict_imc[ref] * ((altura/100)**2)
    ajuste = st.slider("AJUSTE FINO (kg)", -10.0, 10.0, 0.0)
    peso = peso_est + ajuste
    st.success(f"PESO CALCULADO: **{round(peso, 1)} KG**")
else:
    peso = st.number_input("PESO REAL (kg)", 30.0, 200.0, 68.7)

# CÁLCULOS
tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 450
elif objetivo == "Definición": calorias -= 450

# 4. PESTAÑAS (TODA LA ESENCIA)
tab1, tab2, tab3, tab4 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN", "🍲 SUMINISTROS", "🧠 MENTE"])

with tab1:
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("CALORÍAS", f"{int(calorias)} kcal")
    col_m2.metric("AGUA / L", f"{round((peso*35)/1000, 1)} L")
    col_m3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    
    st.write("---")
    st.subheader("📊 MACROS DE COMBATE")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 **PROTEÍNA:** {int(p)}g"); st.progress(0.35)
    st.write(f"🍞 **CARBOS:** {int(c)}g"); st.progress(0.65)
    st.write(f"🥑 **GRASAS:** {int(g)}g"); st.progress(0.15)

with tab2:
    st.subheader("🧬 LÍMITES BIOLÓGICOS")
    score = (muneca + tobillo) / 2
    potencial_m = (altura - 100) + (muneca * 0.5)
    st.info(f"📍 Límite de masa muscular magra: **{round(potencial_m, 1)} kg**")
    
    st.write("---")
    st.subheader("🏋️ POTENCIAL DE EMPUJE (1RM)")
    bench = (peso * 1.2) * (score / 17.5)
    dead = (peso * 2.0) * (score / 17.5)
    f1, f2 = st.columns(2)
    f1.metric("PRESS BANCA", f"{int(bench)} kg")
    f2.metric("PESO MUERTO", f"{int(dead)} kg")

with tab3:
    st.subheader("🍲 SUMINISTROS DE COMBATE")
    st.write("No necesitás lujos. Necesitás nutrientes. Optimizá tu presupuesto.")
    
    with st.expander("💸 NIVEL 1: PRESUPUESTO DE SUPERVIVENCIA (Bajos Recursos)"):
        st.write("""
        * **HUEVOS:** La fuente de proteína más barata. Comprá el cartón de 30.
        * **HÍGADO DE VACA:** El multivitamínico más potente y económico del mundo.
        * **AVENA:** Carbohidrato de absorción lenta, ideal para fuerza.
        * **LENTEJAS/POROTOS:** Proteína vegetal y fibra para saciedad.
        * **ARROZ/PAPA:** Tu combustible principal de bajo costo.
        """)

    with st.expander("⚖️ NIVEL 2: PRESUPUESTO EQUILIBRADO"):
        st.write("""
        * **POLLO (Pechuga o Pata Muslo):** Proteína magra versátil.
        * **CARNE PICADA (Magra):** Hierro y creatina natural.
        * **YOGUR NATURAL:** Probióticos para absorber mejor lo que comés.
        * **BANANAS/FRUTA DE ESTACIÓN:** Energía rápida y potasio.
        """)

    with st.expander("🔱 NIVEL 3: SUMINISTRO ÓPTIMO"):
        st.write("""
        * **PESCADO (Atún/Caballa):** Omega 3 para desinflamar.
        * **FRUTOS SECOS:** Grasas saludables y energía compacta.
        * **PALTA:** La mejor fuente de grasa para tus hormonas.
        """)

with tab4:
    st.subheader("✍️ EL MURO DEL SILENCIO")
    st.write(f"{nombre}, soltá lo que te pese hoy. Escribilo y destruilo.")
    desahogo = st.text_area("Desahogate...", height=150)
    if st.button("QUEMAR Y SOLTAR"):
        st.balloons()
        st.success("MENSAJE DESTRUIDO. TU MENTE ESTÁ LIMPIA.")
    
    st.divider()
    if st.button("REINICIO MENTAL (4-4-4-4)"):
        ph = st.empty(); pb = st.progress(0)
        for i in range(2):
            for t, c in [("🟦 INHALA", "info"), ("⬜ MANTÉN", "warning"), ("🟩 EXHALA", "success"), ("🟨 VACÍO", "error")]:
                getattr(ph, c)(t)
                for p in range(101):
                    time.sleep(0.038); pb.progress(p)