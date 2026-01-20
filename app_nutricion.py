import streamlit as st

st.set_page_config(page_title="Toji Performance", page_icon="🧬", layout="wide")

st.title("🛡️ TOJI PERFORMANCE SYSTEM")
st.write("*" + "El destino es lo que construyes con el código y el sudor." + "*")

# Pestañas actualizadas
tab1, tab2, tab3, tab4 = st.tabs(["📊 Calculadora", "🍱 Macros", "🧬 ADN & Genética", "🧠 Mentalidad"])

with tab1:
    # (Aquí va la lógica que ya tenías de peso, altura y calorías...)
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso Actual (kg)", 40.0, 200.0, 81.0)
        altura = st.number_input("Altura (cm)", 120, 230, 181)
        genero = st.radio("Género", ["Hombre", "Mujer"], horizontal=True)
    with col2:
        edad = st.number_input("Edad", 10, 100, 20)
        objetivo = st.selectbox("Tu Objetivo", ["Definición", "Mantenimiento", "Volumen"])

with tab3:
    st.header("Análisis de Potencial Genético")
    st.write("Calculamos tu biotipo y límite natural basado en tu estructura ósea.")
    
    c1, c2 = st.columns(2)
    with c1:
        muneca = st.number_input("Medida de muñeca (cm)", 10.0, 25.0, 17.0)
    with c2:
        tobillo = st.number_input("Medida de tobillo (cm)", 15.0, 35.0, 22.0)

    # Lógica de Biotipo por estructura ósea
    # Relación muñeca/altura es un estándar científico para biotipos
    ratio = altura / muneca
    
    st.subheader("Tu Diagnóstico Genético:")
    
    if ratio > 10.4:
        st.success("Biotipo: **ECTOMORFO** (Estructura fina)")
        st.write("🚀 **Ventaja Genética:** Gran capacidad de definición y velocidad. Ideal para saltos explosivos en la arena.")
    elif 9.6 <= ratio <= 10.4:
        st.success("Biotipo: **MESOMORFO** (Estructura atlética)")
        st.write("🚀 **Ventaja Genética:** Facilidad para ganar músculo y perder grasa. Genética de guerrero balanceado.")
    else:
        st.success("Biotipo: **ENDOMORFO** (Estructura robusta)")
        st.write("🚀 **Ventaja Genética:** Fuerza bruta masiva y potencia de empuje. Capacidad de carga superior.")

    # Cálculo de Potencial de Masa Muscular Máxima (Fórmula de Casey Butt)
    potencial = (altura * 0.15) + (muneca * 0.5) + (tobillo * 0.5) # Simplificación pro
    st.metric("Tu límite de peso muscular estimado (Natural)", f"{round(potencial, 1)} kg")
    st.info("💡 Este es el peso máximo que tu estructura ósea puede soportar con un nivel bajo de grasa de forma natural.")

with tab4:
    st.subheader("Citas de Poder")
    st.write("«No importa si no apuestan por mí, yo ya aposté todo lo que tengo.»")

