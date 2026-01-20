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
        .meal-card {
            background-color: #1a1c23;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #444;
            margin-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE ESTADO (MEMORIA DEL SISTEMA)
if 'muro_activo' not in st.session_state:
    st.session_state.muro_activo = False

def toggle_muro():
    st.session_state.muro_activo = not st.session_state.muro_activo

# ==========================================
# INTERFAZ A: MURO DE SILENCIO (DESAHOGO)
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
        objetivo = st.selectbox("Objetivo Estratégico", ["Definición", "Mantenimiento", "Volumen"])

    actividad = st.select_slider("Nivel de Actividad Física", 
        options=["Sedentario", "Ligero (1-2 días)", "Moderado (3-5 días)", "Atleta (6-7 días)"])

    # MOTOR DE CÁLCULO
    if genero == "Hombre":
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.75 * edad)
    else:
        tmb = 655.1 + (9.563 * peso) + (1.85 * altura) - (4.676 * edad)

    factores = {"Sedentario": 1.2, "Ligero (1-2 días)": 1.375, "Moderado (3-5 días)": 1.55, "Atleta (6-7 días)": 1.725}
    calorias_base = tmb * factores[actividad]
    calorias_finales = calorias_base - 500 if "Definición" in objetivo else (calorias_base + 500 if "Volumen" in objetivo else calorias_base)

    # 5. PESTAÑAS DE NAVEGACIÓN
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Resultados", "🍲 Nutrición de Guerrilla", "🧬 ADN Genético", "🧠 Salud Mental"])

    with tab1:
        m1, m2, m3 = st.columns(3)
        m1.metric("Calorías Diarias", f"{int(calorias_finales)} kcal")
        m2.metric("IMC", f"{round(peso / ((altura/100)**2), 1)}")
        m3.metric("Hidratación", f"{round((peso * 35) / 1000, 1)} L")
        
        prot = peso * 2.2
        grasas = peso * 0.9
        carbs = (calorias_finales - (prot * 4) - (grasas * 9)) / 4
        
        st.subheader("Distribución de Macronutrientes")
        c1, c2, c3 = st.columns(3)
        c1.success(f"🥩 Proteína: {int(prot)}g")
        c2.warning(f"🍞 Carbos: {max(0, int(carbs))}g")
        c3.info(f"🥑 Grasas: {int(grasas)}g")

    with tab2:
        st.subheader("🍲 Plan de Alimentación Estratégico")
        presupuesto = st.radio("Seleccioná tu nivel económico para hoy:", ["Supervivencia (Mínimo)", "Estándar (Mercado)", "Premium (Óptimo)"], horizontal=True)
        
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        dia_sel = st.selectbox("Seleccioná el día:", dias)

        menu = {
            "Supervivencia (Mínimo)": {
                "Plato": "Lentejas con Arroz y Huevo",
                "Detalle": "Proteína completa por combinación de legumbre + cereal. El huevo aporta grasa saludable.",
                "Costo": "Muy Bajo"
            },
            "Estándar (Mercado)": {
                "Plato": "Hígado encebollado con Mandioca",
                "Detalle": "El hígado es el multivitamínico de la naturaleza. Mandioca para energía duradera.",
                "Costo": "Bajo/Medio"
            },
            "Premium (Óptimo)": {
                "Plato": "Pechuga de Pollo/Vaca con Batata y Brócoli",
                "Detalle": "Digestión rápida, fibra alta y perfil de aminoácidos perfecto para el músculo.",
                "Costo": "Medio/Alto"
            }
        }
        
        res = menu[presupuesto]
        st.markdown(f"""
            <div class='meal-card'>
                <h3 style='color: #2ecc71;'>{res['Plato']}</h3>
                <p><b>Estrategia:</b> {res['Detalle']}</p>
                <p><b>Costo Estimado:</b> {res['Costo']}</p>
            </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.subheader("🧬 Análisis de Biotipo")
        if muneca >= 19: st.error("### Biotipo: Endo-Mesomorfo (Tanque)")
        elif muneca > 16.5: st.success("### Biotipo: Mesomorfo (Atlético)")
        else: st.info("### Biotipo: Ectomorfo (Fino)")
        st.write(f"Basado en estructura ósea ({muneca} cm).")

    with tab4:
        st.subheader("🧠 Centro de Resiliencia y Ego")
        mood = st.select_slider("Frecuencia actual:", options=["Rendirse", "Agotado", "Ansioso", "Neutral", "Motivado", "Modo Caza", "Ego de Acero", "Bendecido"])
        
        if mood == "Rendirse":
            st.markdown("<div class='emergency-box'><h2 style='color: #ff4b4b;'>🛡️ PROTOCOLO DE RECONSTRUCCIÓN</h2></div>", unsafe_allow_html=True)
            st.error("### RETIRO TÁCTICO: No es rendirse, es reagruparse.")
            st.write("1. Apagá todo. 2. Agua y comida. 3. 10 min de caminata. 4. Mañana volvés.")
            if st.button("🔥 SELLAR EL PACTO"): st.balloons(); st.success("Pacto sellado.")

        elif mood == "Ansioso":
            if st.button("🚀 Iniciar Respiración Táctica"):
                status = st.empty()
                bar = st.progress(0)
                for ciclo in range(3):
                    for texto, p in [("🟦 Inhalá", 25), ("⬜ Mantené", 50), ("🟩 Exhalá", 75), ("🟨 Mantené", 100)]:
                        status.subheader(texto); bar.progress(p); time.sleep(4)
                status.success("Reseteado."); bar.empty()

        elif mood == "Ego de Acero":
            st.markdown("<div style='background-color: #1a1c23; padding: 20px; border-left: 5px solid #f1c40f;'><h2 style='color: #f1c40f;'>👑 EGO DE ACERO</h2><p><i>«Soy solo un humano que puso a los dioses de rodillas.»</i></p></div>", unsafe_allow_html=True)
            if st.button("🔥 REAFIRMAR DOMINIO"): st.snow(); st.success("Presencia imponente.")

        elif mood == "Bendecido":
            st.balloons()
            st.markdown("<div style='text-align: center; padding: 30px; border: 2px solid white; border-radius: 20px;'><h1>⚡ ESTADO DE GRACIA</h1><p><i>«He recuperado mis sentidos. Soy el más fuerte.»</i></p></div>", unsafe_allow_html=True)