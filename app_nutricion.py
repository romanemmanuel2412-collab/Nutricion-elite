import streamlit as st
import time

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Toji Performance System", 
    page_icon="🛡️", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. INYECCIÓN DE CSS (TU ESTILO DARK)
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
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.title("🛡️ TOJI PERFORMANCE SYSTEM")
st.write("_«El destino no se espera, se construye con código y sudor.»_")

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

# 5. MOTOR DE CÁLCULO (HARRIS-BENEDICT ACTUALIZADO)
if genero == "Hombre":
    tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.75 * edad)
else:
    tmb = 655.1 + (9.563 * peso) + (1.85 * altura) - (4.676 * edad)

factores = {"Sedentario": 1.2, "Ligero (1-2 días)": 1.375, "Moderado (3-5 días)": 1.55, "Atleta (6-7 días)": 1.725}
calorias_base = tmb * factores[actividad]

# AJUSTE SEGÚN OBJETIVO
if "Definición" in objetivo: 
    calorias_finales = calorias_base - 500
elif "Volumen" in objetivo: 
    calorias_finales = calorias_base + 500
else: 
    calorias_finales = calorias_base
 
# 6. INTERFAZ DE PESTAÑAS
tab1, tab2, tab3, tab4 = st.tabs(["📊 Resultados", "🍲 Plan de Acción", "🧬 ADN Genético", "🧠 Salud Mental"])

with tab1:
    m1, m2, m3 = st.columns(3)
    m1.metric("Calorías Diarias", f"{int(calorias_finales)} kcal")
    m2.metric("IMC", f"{round(peso / ((altura/100)**2), 1)}")
    m3.metric("Hidratación", f"{round((peso * 35) / 1000, 1)} L")
    
    st.divider()
    # Macros según protocolo ISSN
    prot = peso * 2.2
    grasas = peso * 0.9
    carbs = (calorias_finales - (prot * 4) - (grasas * 9)) / 4
    
    st.subheader("Distribución de Macronutrientes")
    c1, c2, c3 = st.columns(3)
    c1.success(f"🥩 Proteína: {int(prot)}g")
    c2.warning(f"🍞 Carbos: {max(0, int(carbs))}g") # Evita números negativos
    c3.info(f"🥑 Grasas: {int(grasas)}g")
    
    with st.expander("🔬 Fundamento Científico"):
        st.write("""
        * **Harris-Benedict Equation:** Protocolo clínico utilizado para calcular la Tasa Metabólica Basal.
        * **ISSN Protocol:** Distribución de 2.2g/kg de proteína para la preservación de masa muscular.
        """)

with tab2:
    st.subheader("🍳 Guía de Nutrición de Bajo Presupuesto")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Proteínas:** Huevos, Hígado, Lentejas + Arroz.")
    with col_b:
        st.markdown("**Carbohidratos:** Avena, Mandioca, Polenta.")
    st.info(f"**Tip Pro:** Para {objetivo}, intentá realizar 4 comidas iguales al día.")

with tab3:
    st.subheader("🧬 Análisis de Estructura Genética")
    st.write(f"Tu medida de muñeca es: **{muneca} cm**.")
    
    if muneca >= 19:
        st.error("### Biotipo: Endo-Mesomorfo")
        st.write("Potencial de fuerza superior. Sos un tanque natural.")
    elif muneca > 16.5:
        st.success("### Biotipo: Mesomorfo")
        st.write("Genética atlética. Ganás músculo con facilidad.")
    else:
        st.info("### Biotipo: Ectomorfo")
        st.write("Estructura fina. Necesitás superávit calórico agresivo.")

with tab4:
    st.subheader("🧠 Centro de Enfoque y Resiliencia")
    mood = st.select_slider("Estado mental:", options=["Agotado", "Ansioso", "Neutral", "Motivado", "Imparable"])
    
    if mood == "Ansioso":
        st.warning("⚠️ **Respiración Táctica: 4-4-4-4**")
        if st.button("🚀 Iniciar Ciclo de Calma"):
            status = st.empty()
            bar = st.progress(0)
            # 3 ciclos para efectividad real
            for ciclo in range(3):
                pasos = [("🟦 Inhalá...", 25), ("⬜ Mantené...", 50), ("🟩 Exhalá...", 75), ("🟨 Mantené...", 100)]
                for texto, p in pasos:
                    status.subheader(texto)
                    bar.progress(p)
                    time.sleep(4)
            status.success("✅ Sistema Nervioso Reseteado. Volvé al objetivo.")
            bar.empty()
    
    elif mood == "Agotado":
        st.error("Dormir es entrenar. Hoy se descansa.")
    elif mood == "Imparable":
        st.balloons()
        st.success("Aprovechá el flujo. Ejecutá ahora.")