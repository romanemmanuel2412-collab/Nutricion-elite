import streamlit as st
import time

# 1. CONFIGURACIÓN E IDENTIDAD DEL SISTEMA
st.set_page_config(
    page_title="Toji Performance System", 
    page_icon="🛡️", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. ESTILO VISUAL (DARK MODE & CUSTOM CSS)
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
        div[data-testid="stExpander"] {
            background-color: #1a1c23;
            border: 1px solid #444;
        }
        .muro-text {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #ff4b4b;
            padding-top: 50px;
        }
        .emergency-box {
            background-color: #1a1c23; 
            padding: 25px; 
            border-radius: 15px; 
            border-left: 5px solid #ff4b4b;
        }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE ESTADO (MEMORIA DEL SISTEMA)
if 'muro_activo' not in st.session_state:
    st.session_state.muro_activo = False

def toggle_muro():
    st.session_state.muro_activo = not st.session_state.muro_activo

# ==========================================
# INTERFAZ A: MURO DE SILENCIO (PRIVACIDAD & DESAHOGO)
# ==========================================
if st.session_state.muro_activo:
    st.markdown("<div class='muro-text'>🛡️ MURO DE SILENCIO</div>", unsafe_allow_html=True)
    st.write("---")
    
    st.subheader("🗑️ Cámara de Descarga Emocional")
    st.write("_Escribí todo lo que genera ruido. Al quemar o salir, esto desaparece para siempre._")
    
    desahogo = st.text_area("Vaciá tu mente acá...", height=250, placeholder="Soltá la carga...")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        if st.button("🔥 Quemar Pensamientos", use_container_width=True):
            st.success("✅ Pensamientos eliminados. Sistema Nervioso Limpio.")
            time.sleep(1.5)
            st.rerun()
    with col_m2:
        if st.button("🔓 Salir del Muro", use_container_width=True):
            toggle_muro()
            st.rerun()
    
    st.divider()
    st.markdown("> *«El silencio es donde el acero se vuelve más fuerte.»*")

# ==========================================
# INTERFAZ B: SISTEMA PRINCIPAL (PERFORMANCE)
# ==========================================
else:
    # CABECERA
    c_head1, c_head2 = st.columns([0.8, 0.2])
    with c_head1:
        st.title("🛡️ TOJI PERFORMANCE SYSTEM")
        st.write("_«El destino no se espera, se construye con código y sudor.»_")
    with c_head2:
        if st.button("🤫 Activar Muro", use_container_width=True):
            toggle_muro()
            st.rerun()

    # 4. ENTRADA DE DATOS
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso Actual (kg)", 40.0, 200.0, 81.0)
        altura = st.number_input("Altura (cm)", 120, 230, 181)
        genero = st.radio("Género", ["Hombre", "Mujer"], horizontal=True)
    with col2:
        edad = st.number_input("Edad", 10, 100, 20)
        muneca = st.number_input("Medida de muñeca (cm)", 10.0, 25.0, 17.0)
        objetivo = st.selectbox("Objetivo Estratégico", 
                                ["Definición (Quemar Grasa)", "Mantenimiento", "Volumen (Ganar Músculo)"])

    actividad = st.select_slider("Nivel de Actividad Física", 
        options=["Sedentario", "Ligero (1-2 días)", "Moderado (3-5 días)", "Atleta (6-7 días)"])

    # 5. MOTOR DE CÁLCULO CIENTÍFICO (HARRIS-BENEDICT)
    if genero == "Hombre":
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.75 * edad)
    else:
        tmb = 655.1 + (9.563 * peso) + (1.85 * altura) - (4.676 * edad)

    factores = {"Sedentario": 1.2, "Ligero (1-2 días)": 1.375, "Moderado (3-5 días)": 1.55, "Atleta (6-7 días)": 1.725}
    calorias_base = tmb * factores[actividad]

    if "Definición" in objetivo: calorias_finales = calorias_base - 500
    elif "Volumen" in objetivo: calorias_finales = calorias_base + 500
    else: calorias_finales = calorias_base

    # 6. PESTAÑAS DE NAVEGACIÓN
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Resultados", "🍲 Plan", "🧬 ADN", "🧠 Salud Mental"])

    with tab1:
        m1, m2, m3 = st.columns(3)
        m1.metric("Calorías Diarias", f"{int(calorias_finales)} kcal")
        m2.metric("IMC", f"{round(peso / ((altura/100)**2), 1)}")
        m3.metric("Hidratación", f"{round((peso * 35) / 1000, 1)} L")
        
        st.divider()
        prot = peso * 2.2
        grasas = peso * 0.9
        carbs = (calorias_finales - (prot * 4) - (grasas * 9)) / 4
        
        st.subheader("Distribución de Macronutrientes")
        c1, c2, c3 = st.columns(3)
        c1.success(f"🥩 Proteína: {int(prot)}g")
        c2.warning(f"🍞 Carbos: {max(0, int(carbs))}g")
        c3.info(f"🥑 Grasas: {int(grasas)}g")

    with tab2:
        st.subheader("🍳 Estrategia de Nutrición")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**Proteína Real:** Huevos, Menudencias, Lentejas + Arroz.")
        with col_b:
            st.markdown("**Energía:** Avena, Mandioca, Polenta.")
        st.info(f"Prioridad {objetivo}: Realizá 4 comidas iguales para mantener el metabolismo activo.")

    with tab3:
        st.subheader("🧬 Estructura Ósea & Biotipo")
        if muneca >= 19: st.error("### Biotipo: Endo-Mesomorfo (Tanque)")
        elif muneca > 16.5: st.success("### Biotipo: Mesomorfo (Atlético)")
        else: st.info("### Biotipo: Ectomorfo (Fino)")
        st.write(f"Cálculo basado en circunferencia de muñeca: {muneca} cm.")

    with tab4:
        st.subheader("🧠 Centro de Resiliencia")
        mood = st.select_slider("¿Cómo está tu mente hoy?", 
                                options=["Rendirse", "Agotado", "Ansioso", "Neutral", "Motivado", "Imparable"])
        
        # --- LÓGICA DE ÚLTIMA INSTANCIA ---
        if mood == "Rendirse":
            st.markdown(f"""
                <div class='emergency-box'>
                    <h2 style='color: #ff4b4b; margin-bottom: 0;'>🛡️ PROTOCOLO DE RECONSTRUCCIÓN</h2>
                    <p style='color: #888;'><i>«El hombre que se levanta es más fuerte que el que nunca cayó.»</i></p>
                </div>
            """, unsafe_allow_html=True)
            
            st.error("### RETIRO TÁCTICO ACTIVADO")
            st.write("""
            1. **DESCONEXIÓN TOTAL:** Cerrá la app. Apagá el monitor.
            2. **COMBUSTIBLE:** Agua y comida sólida. Tu cerebro necesita energía para salir del pozo.
            3. **SILENCIO:** Salí a caminar 10 min sin celular. Recuperá tu voz.
            4. **EL PACTO:** Mañana volvés. No por obligación, sino por tu destino.
            """)
            
            if st.button("🔥 SELLAR EL PACTO Y VOLVER MÁS FUERTE"):
                st.balloons()
                st.success("Pacto sellado. El descanso de hoy es la victoria de mañana.")

        elif mood == "Ansioso":
            st.warning("⚠️ **Respiración Táctica Activada**")
            if st.button("🚀 Iniciar Ciclo de Calma"):
                status = st.empty()
                bar = st.progress(0)
                for ciclo in range(3):
                    pasos = [("🟦 Inhalá...", 25), ("⬜ Mantené...", 50), ("🟩 Exhalá...", 75), ("🟨 Mantené...", 100)]
                    for texto, p in pasos:
                        status.subheader(texto); bar.progress(p); time.sleep(4)
                status.success("Sistema Nervioso Reseteado.")
                bar.empty()