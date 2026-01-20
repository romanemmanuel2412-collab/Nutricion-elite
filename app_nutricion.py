import streamlit as st
import time
import random

# 1. ESTÉTICA DE ÉLITE (TOJI STYLE)
st.set_page_config(page_title="Toji System", page_icon="🥷", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}
        .stApp { background-color: #0e1117; }
        [data-testid="stMetricValue"] { font-size: 32px !important; color: #00ffcc !important; }
        div.stButton > button { width: 100%; border-radius: 12px; background-color: #1f2937; color: white; border: 1px solid #374151; font-weight: bold; height: 3.5em; }
        div.stButton > button:hover { border-color: #00ffcc; color: #00ffcc; }
        .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# FRASES ESTOICAS DE BIENVENIDA
estoicas = [
    "«La mejor venganza es ser diferente a quien causó el daño.» — Marco Aurelio",
    "«No controlás lo que te sucede, pero sí cómo reaccionás.» — Epicteto",
    "«Si no es correcto, no lo hagas. Si no es verdad, no lo digas.»",
    "«Nadie es libre si no es dueño de sí mismo.»"
]

st.markdown("<h1 style='text-align: center; color: white;'>🛡️ TOJI PERFORMANCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #00ffcc; font-style: italic;'>{random.choice(estoicas)}</p>", unsafe_allow_html=True)

st.write("### 👋 ¡Hola, Guerrero!")
st.write("Bienvenido a tu centro de mando. Optimizamos tu cuerpo y blindamos tu mente.")

st.divider()

# 2. MEDICIONES Y ENTRADA DE DATOS
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        genero = st.radio("Género Biológico", ["Hombre", "Mujer"], horizontal=True)
        altura = st.number_input("Altura (cm)", 120, 230, 180)
        edad = st.number_input("Edad", 12, 90, 20)
    with c2:
        muneca = st.number_input("Muñeca (cm)", 10.0, 25.0, 17.0)
        tobillo = st.number_input("Tobillo (cm)", 10.0, 35.0, 22.0)
    with c3:
        objetivo = st.selectbox("Objetivo Estratégico", ["Volumen", "Definición", "Mantenimiento"])
        actividad = st.selectbox("Nivel de Actividad", ["Sedentario", "Ligero", "Moderado", "Atleta"])

# 3. LÓGICA DE PESO (BALANZA O ESTIMACIÓN)
st.subheader("⚖️ Registro de Peso")
metodo_p = st.radio("¿Cómo vas a registrar tu peso hoy?", ["Usar Balanza", "Estimar por Medidas"], horizontal=True)

if metodo_p == "Estimar por Medidas":
    st.write("📏 *Usá una cinta métrica:*")
    ce1, ce2 = st.columns(2)
    with ce1:
        c_cuello = st.number_input("Cuello (cm)", 20.0, 60.0, 38.0)
    with ce2:
        c_cintura = st.number_input("Cintura (cm)", 40.0, 150.0, 85.0)
    
    # Cálculo manual para evitar errores
    peso_est = (c_cintura * 0.7) + (c_cuello * 0.5) + (altura * 0.1) - 105
    if genero == "Mujer": peso_est -= 5
    st.info(f"Cálculo automático: {round(peso_est, 1)} kg")
    # Te permite corregir si el cálculo falla
    peso = st.number_input("Confirmá tu peso para los cálculos:", 30.0, 200.0, float(max(peso_est, 45.0)))
else:
    peso = st.number_input("Ingresá tu peso real (kg)", 30.0, 200.0, 68.7)

# CÁLCULOS METABÓLICOS (Mifflin-St Jeor)
tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 if genero == "Hombre" else -161)
factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias = tmb * factores[actividad]
if objetivo == "Volumen": calorias += 400
elif objetivo == "Definición": calorias -= 400

# 4. PESTAÑAS DE CONTENIDO
tab1, tab2, tab3 = st.tabs(["🚀 RENDIMIENTO", "🧬 ADN GENÉTICO", "🧠 SALUD MENTAL"])

with tab1:
    m1, m2, m3 = st.columns(3)
    m1.metric("ENERGÍA DIARIA", f"{int(calorias)} kcal")
    m2.metric("HIDRATACIÓN", f"{round((peso*35)/1000, 1)} L")
    m3.metric("PROTEÍNA", f"{int(peso*2)}g")
    
    st.write("### 📊 MACRONUTRIENTES")
    p, g = peso * 2, peso * 0.8
    c = (calorias - (p*4) - (g*9)) / 4
    st.write(f"🥩 Proteína: {int(p)}g"); st.progress(0.3)
    st.write(f"🍞 Carbohidratos: {int(c)}g"); st.progress(0.6)
    st.write(f"🥑 Grasas: {int(g)}g"); st.progress(0.15)

with tab2:
    st.subheader("🧬 DIAGNÓSTICO DE BIOTIPO")
    # Score óseo usando muñeca y tobillo
    score = (muneca + tobillo) / 2
    if score >= 19.5:
        biotipo, desc = "ENDOMORFO MASIVO", "Gran chasis óseo. Potencial de fuerza bruta de élite."
    elif score >= 17:
        biotipo, desc = "MESOMORFO", "Estructura atlética. Respuesta rápida al entrenamiento y estética."
    else:
        biotipo, desc = "ECTOMORFO", "Estructura ligera. Gran definición, requiere comer mucho para ganar volumen."
    
    st.success(f"Biotipo Detectado: **{biotipo}**")
    st.write(desc)

with tab3:
    st.subheader("✍️ EL MURO DEL SILENCIO")
    st.write("Escribí acá todo lo que te pese: broncas, mensajes no respondidos o frustraciones. Este espacio es tuyo y nada de lo que escribas se guarda en la base de datos.")
    
    desahogo = st.text_area("Vaciá tu mente aquí...", height=200, placeholder="Ejemplo: No me respondió el mensaje, me siento rechazado pero voy a usar esa bronca para entrenar...")
    
    if st.button("BORRAR Y SOLTAR"):
        st.balloons() # Pequeño efecto visual de liberación
        st.success("Mensaje liberado. Lo que escribiste ya no existe. Seguí adelante.")
    
    st.divider()
    
    st.subheader("🌬️ RESPIRACIÓN TÁCTICA")
    if st.button("INICIAR TEMPORIZADOR VISUAL"):
        ph = st.empty(); pb = st.progress(0)
        for ciclo in range(2):
            for txt, col in [("🟦 INHALA (4s)", "info"), ("⬜ MANTÉN (4s)", "warning"), ("🟩 EXHALA (4s)", "success"), ("🟨 VACÍO (4s)", "error")]:
                getattr(ph, col)(txt)
                for i in range(101):
                    time.sleep(0.038); pb.progress(i)
        ph.success("✅ FOCO RECUPERADO. SOS EL DUEÑO DE TUS ACCIONES.")