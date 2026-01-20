import streamlit as st
import time
import random

# 1. CONFIGURACIÓN Y ESTÉTICA
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

# FRASES DE INICIO (ESTOICAS)
estoicas = [
    "«No nos afecta lo que nos sucede, sino lo que nos decimos sobre lo que nos sucede.» — Epicteto",
    "«La mejor venganza es ser diferente a quien causó el daño.» — Marco Aurelio",
    "«Si no es correcto, no lo hagas; si no es verdad, no lo digas.» — Marco Aurelio",
    "«Nadie puede herirte sin tu consentimiento.» — Séneca",
    "«El hombre conquista el mundo conquistándose a sí mismo.» — Zenón de Citio"
]

st.markdown("<h1 style='text-align: center; color: white;'>🛡️ TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #808495; font-style: italic;'>{random.choice(estoicas)}</p>", unsafe_allow_html=True)

# 2. PRESENTACIÓN
st.write("### 👋 ¡Hola, Guerrero!")
st.write("Bienvenido a tu centro de mando. Aquí optimizamos el cuerpo y blindamos la mente.")

st.divider()

# 3. ENTRADA DE DATOS
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

with st.expander("⚖️ ESTIMAR PESO SIN BALANZA"):
    c_cuello = st.number_input("Cuello (cm)", 20.0, 60.0, 38.0)
    c_cintura = st.number_input("Cintura ombligo (cm)", 40.0, 150.0, 85.0)
    peso_est = (c_cintura * 0.7) + (c_cuello * 0.5) + (altura * 0.1) - 105
    if genero == "Mujer": peso_est -= 5
    st.info(f"Peso estimado: **{round(peso_est, 1)} kg**")

peso = st.number_input("Peso para cálculos (kg)", 40.0, 200.0, 80.0)

# LÓGICA DE CÁLCULO
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
tmb = (66 + (13.7 * peso) + (5 * altura) - (6.8 * edad)) if genero == "Hombre" else (655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad))
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 450
elif objetivo == "Definición": calorias -= 450

# 4. PESTAÑAS
tab1, tab2, tab3 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN GENÉTICO", "🧠 FILOSOFÍA & MENTE"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("CALORÍAS", f"{int(calorias)} kcal")
    col2.metric("AGUA / DÍA", f"{round((peso*35)/1000, 1)} L")
    col3.metric("PROTEÍNA", f"{int(peso*2.2)}g")
    p, g = peso * 2.2, peso * 0.9
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 Proteína: {int(p)}g"); st.progress(0.35)
    st.write(f"🍞 Carbos: {int(c)}g"); st.progress(0.65)
    st.write(f"🥑 Grasas: {int(g)}g"); st.progress(0.15)

with tab2:
    st.subheader("🧬 DIAGNÓSTICO ESTRUCTURAL")
    biotipo = "ENDOMORFO" if muneca >= 19 else "MESOMORFO" if muneca > 16.5 else "ECTOMORFO"
    st.success(f"**Biotipo Detectado:** {biotipo}")
    

with tab3:
    st.subheader("🏛️ FORTALEZA ESTOICA")
    st.write("«Amor Fati: No solo aceptes lo que sucede, ámalo como necesario.»")
    
    # Herramienta de Dicotomía del Control
    with st.expander("⚖️ LA DICOTOMÍA DEL CONTROL"):
        st.write("Dividí tus preocupaciones de hoy:")
        c_si, c_no = st.columns(2)
        with c_si:
            st.info("**Bajo tu control:** Tus pensamientos, tus acciones, tu dieta, tu entrenamiento.")
        with c_no:
            st.error("**Fuera de tu control:** Lo que otros piensan de vos, el clima, las respuestas de los demás.")
            
    st.divider()
    
    # Respiración Táctica
    st.subheader("🌬️ RESPIRACIÓN TÁCTICA")
    if st.button("INICIAR TEMPORIZADOR"):
        ph_t = st.empty(); ph_b = st.progress(0)
        for ciclo in range(2):
            for t, tip in [("🟦 INHALA", "info"), ("⬜ MANTÉN", "warning"), ("🟩 EXHALA", "success"), ("🟨 VACÍO", "error")]:
                getattr(ph_t, tip)(t)
                for i in range(101):
                    time.sleep(0.038); ph_b.progress(i)
        ph_t.success("✅ MENTE EN CALMA")

    st.divider()
    st.subheader("📓 DIARIO DE REFLEXIÓN")
    st.text_area("«Memento Mori»: Recordá que el tiempo es finito. ¿Qué hiciste hoy para ser la versión que querés ser?")