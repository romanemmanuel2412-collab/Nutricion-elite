import streamlit as st
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Toji Performance System", 
    page_icon="🛡️", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. INYECCIÓN DE CSS (TU ESTILO DARK + MURO DE SILENCIO)
st.markdown("""
    <style>
        [data-testid="collapsedControl"] { display: none; }
        section[data-testid="stSidebar"] { display: none; }
        .main { background-color: #0e1117; color: #ffffff; }
        .stMetric { 
            background-color: #1a1c23; 
            padding: 15px; 
            border-radius: 10px; 
            border: 1px solid #333; 
        }
        .muro-text {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #ff4b4b;
            margin-top: 100px;
        }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DEL MURO DE SILENCIO ---
if 'muro_activo' not in st.session_state:
    st.session_state.muro_activo = False

def toggle_muro():
    st.session_state.muro_activo = not st.session_state.muro_activo

# 3. INTERFAZ CONDICIONAL (MURO DE SILENCIO)
if st.session_state.muro_activo:
    st.markdown("<div class='muro-text'>MURO DE SILENCIO ACTIVADO</div>", unsafe_allow_html=True)
    st.write("---")
    st.subheader("«El mundo hace ruido, vos hacés historia.»")
    st.info("Todo el sistema ha sido ocultado para proteger tu enfoque. Nada te distrae ahora.")
    if st.button("🔓 Desactivar Muro"):
        toggle_muro()
        st.rerun()

else:
    # 4. CABECERA (Solo se ve si el muro está apagado)
    st.title("🛡️ TOJI PERFORMANCE SYSTEM")
    
    # BOTÓN RÁPIDO PARA ACTIVAR EL MURO
    if st.button("🤫 Activar Muro de Silencio"):
        toggle_muro()
        st.rerun()

    # 5. ENTRADA DE DATOS
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso Actual (kg)", 40.0, 200.0, 81.0)
        altura = st.number_input("Altura (cm)", 120, 230, 181)
        genero = st.radio("Género", ["Hombre", "Mujer"], horizontal=True)
    with col2:
        edad = st.number_input("Edad", 10, 100, 20)
        muneca = st.number_input("Medida de muñeca (cm)", 10.0, 25.0, 17.0)
        objetivo = st.selectbox("Objetivo Estratégico", ["Definición", "Mantenimiento", "Volumen"])

    actividad = st.select_slider("Nivel de Actividad Física", options=["Sedentario", "Ligero", "Moderado", "Atleta"])

    # 6. CÁLCULOS
    if genero == "Hombre":
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.75 * edad)
    else:
        tmb = 655.1 + (9.563 * peso) + (1.85 * altura) - (4.676 * edad)
    
    factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
    calorias_base = tmb * factores[actividad]
    
    # 7. TABS
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Resultados", "🍲 Plan", "🧬 ADN", "🧠 Salud Mental"])

    with tab1:
        m1, m2, m3 = st.columns(3)
        m1.metric("Calorías Diarias", f"{int(calorias_base)} kcal")
        m2.metric("IMC", f"{round(peso / ((altura/100)**2), 1)}")
        m3.metric("Hidratación", f"{round((peso * 35) / 1000, 1)} L")

    with tab4:
        st.subheader("🧠 Centro de Enfoque")
        mood = st.select_slider("Estado mental:", options=["Agotado", "Ansioso", "Neutral", "Motivado", "Imparable"])
        
        if mood == "Ansioso":
            if st.button("🚀 Iniciar Ciclo de Calma"):
                status = st.empty()
                bar = st.progress(0)
                for ciclo in range(2):
                    pasos = [("🟦 Inhalá...", 25), ("⬜ Mantené...", 50), ("🟩 Exhalá...", 75), ("🟨 Mantené...", 100)]
                    for texto, p in pasos:
                        status.subheader(texto); bar.progress(p); time.sleep(4)
                status.success("✅ Reseteado.")