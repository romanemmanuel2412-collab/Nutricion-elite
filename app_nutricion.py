import streamlit as st
import time
import random

# 1. CONFIGURACIÓN DE ÉLITE
st.set_page_config(page_title="Toji System", page_icon="🥷", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}
        .stApp { background-color: #0e1117; }
        [data-testid="stMetricValue"] { font-size: 32px !important; color: #00ffcc !important; }
        div.stButton > button { width: 100%; border-radius: 12px; background-color: #1f2937; color: white; border: 1px solid #374151; font-weight: bold; height: 3em; }
        div.stButton > button:hover { border-color: #00ffcc; color: #00ffcc; }
        .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# FRASES ESTOICAS
estoicas = [
    "«No nos afecta lo que nos sucede, sino lo que nos decimos sobre lo que nos sucede.» — Epicteto",
    "«La mejor venganza es ser diferente a quien causó el daño.» — Marco Aurelio",
    "«Nadie puede herirte sin tu consentimiento.» — Séneca"
]

st.markdown("<h1 style='text-align: center; color: white;'>🛡️ TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #808495; font-style: italic;'>{random.choice(estoicas)}</p>", unsafe_allow_html=True)

st.write("### 👋 ¡Hola, Guerrero!")
st.write("Bienvenido. Ingresá tus mediciones para que el sistema calcule tu potencial real.")

st.divider()

# 2. SECCIÓN DE MEDICIONES ÓSEAS Y PERSONALES
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        genero = st.radio("Género Biológico", ["Hombre", "Mujer"], horizontal=True)
        altura = st.number_input("Altura (cm)", 120, 230, 180)
        edad = st.number_input("Edad", 12, 90, 20)
    with c2:
        muneca = st.number_input("Medida de Muñeca (cm)", 10.0, 25.0, 17.0)
        tobillo = st.number_input("Medida de Tobillo (cm)", 15.0, 35.0, 22.0)
    with c3:
        objetivo = st.selectbox("Objetivo Estratégico", ["Volumen", "Definición", "Mantenimiento"])
        actividad = st.selectbox("Nivel de Actividad", ["Sedentario", "Ligero", "Moderado", "Atleta"])

# 3. LÓGICA DE PESO (BALANZA O ESTIMACIÓN)
st.subheader("⚖️ Control de Masa Corporal")
metodo_peso = st.radio("¿Tenés balanza a mano?", ["Sí, ingresar peso", "No, estimar por medidas"], horizontal=True)

if metodo_peso == "No, estimar por medidas":
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        c_cuello = st.number_input("Cuello (cm)", 20.0, 60.0, 38.0)
    with col_e2:
        c_cintura = st.number_input("Cintura a la altura del ombligo (cm)", 40.0, 150.0, 85.0)
    
    # Fórmula robusta: evita negativos asegurando que la altura sea en CM
    peso = (c_cintura * 0.7) + (c_cuello * 0.5) + (altura * 0.1) - 105
    if genero == "Mujer": peso -= 5
    if peso < 30: peso = 30 # Piso mínimo de seguridad
    st.info(f"Peso Estimado: **{round(peso, 1)} kg**")
else:
    peso = st.number_input("Ingresá tu peso de balanza (kg)", 30.0, 200.0, 80.0)

# CÁLCULOS METABÓLICOS
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
tmb = (66 + (13.7 * peso) + (5 * altura) - (6.8 * edad)) if genero == "Hombre" else (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad))
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 450
elif objetivo == "Definición": calorias -= 450

# 4. PESTAÑAS
tab1, tab2, tab3 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN GENÉTICO", "🧠 FILOSOFÍA & MENTE"])

with tab1:
    m1, m2, m3 = st.columns(3)
    m1.metric("CALORÍAS", f"{int(calorias)} kcal")
    m2.metric("AGUA / DÍA", f"{round((peso*35)/1000, 1)} L")
    m3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    
    st.write("### 📊 MACROS")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 Proteína: {int(p)}g"); st.progress(0.35)
    st.write(f"🍞 Carbos: {int(c)}g"); st.progress(0.65)
    st.write(f"🥑 Grasas: {int(g)}g"); st.progress(0.15)
    st.write("---")
    st.write("🍲 **Combustible Económico:** Huevos, Lentejas, Hígado, Arroz, Papa.")

with tab2:
    st.subheader("🧬 ANÁLISIS ESTRUCTURAL")
    # El tobillo ayuda a definir biotipos mixtos
    if muneca >= 19 and tobillo >= 23:
        biotipo, desc = "ENDOMORFO MASIVO", "Huesos pesados. Máximo potencial de fuerza bruta."
    elif muneca > 16.5 and tobillo > 20:
        biotipo, desc = "MESOMORFO", "Estructura atlética perfecta. Ganancia muscular eficiente."
    else:
        biotipo, desc = "ECTOMORFO", "Estructura ligera. Gran definición, requiere superávit calórico."
    
    st.success(f"**Biotipo:** {biotipo}")
    st.write(desc)
    

with tab3:
    st.subheader("🏛️ FORTALEZA MENTAL")
    with st.expander("⚖️ DICOTOMÍA DEL CONTROL"):
        st.info("**Controlás:** Tu dieta, tu entrenamiento, tu reacción ante los mensajes de otros.")
        st.error("**No controlás:** Las decisiones de los demás, el pasado, el resultado inmediato.")
    
    if st.button("INICIAR RESPIRACIÓN TÁCTICA"):
        ph_t = st.empty(); ph_b = st.progress(0)
        for ciclo in range(2):
            for t, tip in [("🟦 INHALA", "info"), ("⬜ MANTÉN", "warning"), ("🟩 EXHALA", "success"), ("🟨 VACÍO", "error")]:
                getattr(ph_t, tip)(t)
                for i in range(101):
                    time.sleep(0.038); ph_b.progress(i)
        ph_t.success("✅ MENTE RESETEADA")
    
    st.text_area("📓 DIARIO MEMENTO MORI", placeholder="¿Qué harías hoy si fuera tu último día?")