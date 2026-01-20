import streamlit as st

st.set_page_config(page_title="Toji Performance", page_icon="🧬", layout="wide")

st.title("🛡️ TOJI PERFORMANCE SYSTEM")
st.write("*" + "El destino es lo que construyes con el código y el sudor." + "*")

# Pestañas actualizadas
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Calculadora", "🍱 Macros", "🧬 ADN & Genética", "🧠 Mentalidad", "🧘 Salud Mental"])

with tab1:
    # (Aquí va la lógica que ya tenías de peso, altura y calorías...)
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso Actual (kg)", 40.0, 200.0, 81.0)
        altura = st.number_input("Altura (cm)", 120, 230, 181)
        genero = st.radio("Género", ["Hombre", "Mujer"], horizontal=True)
    with col2:
        edad = st.number_input("Edad", 10, 100, 20)
        # ESTA ES LA LÍNEA QUE TE FALTA:
        muneca = st.number_input("Medida de muneca (cm)", 10.0, 30.0, 17.0)
        objetivo = st.selectbox("Tu Objetivo", ["Definición", "Mantenimiento", "Volumen"])

with tab2:
    st.subheader("🍱 Distribución de Energía (Macros)")
    
    # REPETIMOS EL CÁLCULO AQUÍ PARA QUE LA PESTAÑA TENGA LOS DATOS
    # (Asegurate de que estas variables usen los datos que ingresaste en la Tab 1)
    
    proteina = peso * 2.2 
    grasas = peso * 0.9
    
    # Calculamos carbohidratos restando al total de calorías
    # Usamos la variable 'calorias_finales' que calculamos en la Tab 1
    carbo_cal = 2500 - (proteina * 4) - (grasas * 9)
    carbohidratos = carbo_cal / 4

    # CREAMOS LAS COLUMNAS VISUALES
    c1, c2, c3 = st.columns(3)
    c1.metric("🥩 Proteínas", f"{int(proteina)}g")
    c2.metric("🍞 Carbos", f"{int(carbohidratos)}g")
    c3.metric("🥑 Grasas", f"{int(grasas)}g")
    
    st.divider()
    st.info("💡 **Dato de Elite:** Esta distribución está optimizada para maximizar tu rendimiento deportivo sin perder masa muscular.")

with tab3:
    st.header("Análisis de Potencial Genético")
    st.write("Calculamos tu biotipo y límite natural basado en tu estructura ósea.")
    
    c1, c2 = st.columns(2)
    with c1:
        muneca = st.number_input("Medida de muneca (cm)", 10.0, 25.0, 17.0)
    with c2:
        tobillo = st.number_input("Medida de tobillo (cm)", 15.0, 35.0, 22.0)

    # Cálculo del Índice de Estructura Ósea (Estatura / Muneca)
    r_medida = altura / muneca
    
    st.subheader("Tu Diagnóstico Genético:")
    
    if r_medida > 10.4:
        biotipo = "Ectomorfo (Estructura Fina)"
    elif 9.6 <= r_medida <= 10.4:
        biotipo = "Mesomorfo (Estructura Atlética)"
    else:
        biotipo = "Endomorfo / Estructura Pesada (Potencial de Fuerza)"
    
    if biotipo == "Ectomorfo (Estructura Fina)":
        st.success(f"Biotipo: **{biotipo}**")
        st.write("🚀 **Ventaja Genética:** Gran capacidad de definición y velocidad. Ideal para saltos explosivos en la arena.")
    elif biotipo == "Mesomorfo (Estructura Atlética)":
        st.success(f"Biotipo: **{biotipo}**")
        st.write("🚀 **Ventaja Genética:** Facilidad para ganar músculo y perder grasa. Genética de guerrero balanceado.")
    else:
        st.success(f"Biotipo: **{biotipo}**")
        st.write("🚀 **Ventaja Genética:** Fuerza bruta masiva y potencia de empuje. Capacidad de carga superior.")

    # Cálculo de Potencial de Masa Muscular Máxima (Fórmula de Casey Butt)
    potencial = (altura * 0.15) + (muneca * 0.5) + (tobillo * 0.5) # Simplificación pro
    st.metric("Tu límite de peso muscular estimado (Natural)", f"{round(potencial, 1)} kg")
    st.info("💡 Este es el peso máximo que tu estructura ósea puede soportar con un nivel bajo de grasa de forma natural.")

with tab4:
    st.subheader("🦁 Filosofía Estoica para Guerreros")
    st.write("*Sabiduría de los grandes filósofos para forjar tu mente de acero*")
    
    st.divider()
    
    # Citas estoicas
    citas = {
        "Marco Aurelio": "«No pidas que las cosas salgan como quieres, sino que quieras que salgan como salen.»",
        "Epicteto": "«No eres tú quien controla los eventos externos, sino solo tu juicio sobre ellos.»",
        "Séneca": "«El gran guerrero es quien controla sus emociones, no sus enemigos.»",
        "Zenón de Citio": "«La virtud es el único bien verdadero. Todo lo demás es indiferente.»",
        "Cleantes": "«Lo que importa no es lo que te sucede, sino cómo respondes ante ello.»",
        "Diógenes": "«La riqueza consiste no en tener bienes, sino en tener pocas necesidades.»"
    }
    
    col_citas = st.columns(2)
    contador = 0
    
    for filosofo, cita in citas.items():
        with col_citas[contador % 2]:
            st.write(f"**{filosofo}**")
            st.write(f"_{cita}_")
            st.divider()
        contador += 1
    
    st.success("💪 **Recuerda:** El cuerpo es el templo, pero la mente es el guerrero.")

with tab5:
    st.subheader("🛠️ Caja de Herramientas Mental")
    st.write("El músculo más importante es el que no se ve.")

    # 1. Selector de Estado de Ánimo (Interactividad pura)
    mood = st.select_slider(
        "¿Cómo está tu nivel de energía mental hoy?",
        options=["Agotado", "Ansioso", "Neutral", "Motivado", "Imparable"]
    )

    if mood == "Agotado":
        st.error("🚨 **Orden de Toji:** Hoy el descanso es tu entrenamiento. Dormí 8 horas y desconectá del celular.")
    elif mood == "Ansioso":
        st.warning("⚖️ **Equilibrio:** Tu mente va más rápido que la realidad. Escribí 3 cosas que podés controlar hoy y olvidate del resto.")
    elif mood == "Neutral":
        st.info("🔄 **Modo Ejecución:** Ni frío ni calor. Es el mejor momento para programar o entrenar sin distracciones.")
    elif mood == "Motivado":
        st.success("🔥 **Aprovechá el Fuego:** Subí el peso en el gym o resolvé ese bug difícil en el código.")
    elif mood == "Imparable":
        st.snow() # Un efecto visual de festejo
        st.write("🦾 **Dominio Total:** Sos el arquitecto de tu propio destino. No dejes que nadie te saque de este estado.")

    st.divider()

    # 2. Ejercicio de Respiración Táctica (Box Breathing)
    st.subheader("🌬️ Respiración Táctica (4-4-4-4)")
    st.write("Usada por fuerzas de élite para resetear el sistema nervioso en segundos.")
    
    if st.button("Iniciar Ciclo de Calma"):
        with st.empty():
            for i in range(1):
                st.write("🟦 **Inhalá...** (1, 2, 3, 4)")
                # Aquí podrías usar time.sleep(4) si querés que sea real
                st.write("⬜ **Mantené...** (1, 2, 3, 4)")
                st.write("🟩 **Exhalá...** (1, 2, 3, 4)")
                st.write("🟨 **Mantené...** (1, 2, 3, 4)")
        st.success("Sistema Nervioso Reseteado.")

    # 3. El Diario del Villano (Input interactivo)
    st.subheader("📓 Descarga de Pensamientos")
    pensamiento = st.text_area("¿Qué te está pesando hoy? Sacalo de tu cabeza y ponelo acá (no se guarda en ningún lado, es solo para vos).")
    if pensamiento:
        st.write("✅ *Pensamiento procesado. Ahora volvé a la acción.*")

# Creamos una pestaña nueva de "Ciencia" o lo ponemos debajo de los resultados
st.divider() # Una línea divisoria para separar
st.subheader("🔬 Evidencias Científicas y Metodología")

with st.expander("Ver fuentes bibliográficas y fórmulas utilizadas"):
    st.write("""
    Este sistema no utiliza estimaciones al azar. Los resultados se basan en los siguientes pilares de la nutrición deportiva y la antropometría:
    """)
    
    # 1. Harris-Benedict
    st.markdown("### 1. Tasa Metabólica Basal (TMB)")
    st.write("""
    Se utiliza la **Ecuación de Harris-Benedict revisada**. Es el estándar de oro para calcular las calorías en reposo.
    * *Fuente:* Roza AM, Shizgal HM. (1984). "The Harris Benedict equation reevaluated".
    """)

    # 2. Índice de Grant
    st.markdown("### 2. Biotipificación por Estructura Ósea")
    st.write("""
    Para determinar si eres Ectomorfo, Mesomorfo o Endomorfo, utilizamos el **Índice de Grant**, que relaciona la estatura con la circunferencia de la muñeca.
    * *Fórmula:* $R = Altura (cm) / Muneca (cm)$
    * *Fuente:* Grant JP. (1980). "Handbook of Total Parenteral Nutrition".
    """)

    # 3. Proteínas
    st.markdown("### 3. Requerimientos de Proteína")
    st.write("""
    El objetivo de 2.2g de proteína por kg de peso está basado en las recomendaciones de la **ISSN** para atletas de fuerza y deportes de equipo (como el Handball) para maximizar la síntesis proteica.
    * *Fuente:* Jäger et al. (2017). "International Society of Sports Nutrition Conference Stand: protein and exercise".
    """)
    
    st.info("💡 **Nota del desarrollador:** Estas fórmulas son herramientas de orientación. Para un plan médico, siempre consulta a un profesional.")

st.divider()
st.subheader("🛠️ Menú de Acción (Presupuesto Real)")

# Diccionario de alimentos accesibles y rendidores
alimentos_baratos = {
    "Huevos (La base de todo)": "Baratos y proteína pura. 3 huevos equivalen a una porción de carne.",
    "Legumbres (Lentejas/Porotos)": "Súper baratas. Si las mezclás con arroz, tenés proteína completa.",
    "Hígado o Menudencias": "Es la carne más barata y la que más vitaminas tiene para el gym.",
    "Arroz y Fideos": "El combustible más económico. Usalos para llegar a tus carbohidratos.",
    "Avena pesada": "Comprada suelta es barata y te mantiene lleno toda la mañana en la facu."
}

with st.expander("💡 Cómo cumplir tus macros con poco presupuesto"):
    for alimento, beneficio in alimentos_baratos.items():
        st.write(f"✅ **{alimento}:** {beneficio}")

st.subheader("🍲 Sugerencia de Plato según tus objetivos")

# Lógica de sugerencia basada en el presupuesto y los macros calculados
if objetivo == "Volumen":
    st.info(f"👉 **Tu plato ideal hoy:** Un buen plato de Arroz con Lentejas y 2 huevos hervidos. Es barato, te da los carbohidratos para crecer y la proteína necesaria.")
elif objetivo == "Definición":
    st.info(f"👉 **Tu plato ideal hoy:** Salteado de hígado o pollo con mucha verdura de estación (lo que esté barato en la feria) y poca cantidad de arroz.")
else:
    st.info(f"👉 **Tu plato ideal hoy:** Guiso de fideos con menudencias o trozos de carne económica. Un equilibrio justo.")

st.warning("⚠️ **Tip de Ahorro:** Comprá siempre en la feria o mayoristas. Evitá los procesados (galletitas, saquitos) que son caros y no alimentan.")

# --- SECCIÓN DE AUTOR (LA FIRMA DE TOJI) ---
st.divider()
col_autor, col_vacio = st.columns([2, 1])

with col_autor:
    st.subheader("👨‍💻 Sobre el Desarrollador")
    st.write("""
    **Jonathan | Atleta y Desarrollador**
    
    Este sistema nació de la necesidad de optimizar el rendimiento físico sin perder la claridad mental. 
    Como jugador de Handball y apasionado por la tecnología, creo en la disciplina como la única 
    herramienta para superar el entorno. 
    
    *«El destino no se espera, se programa.»*
    """)
    
    # Botón con efecto para que te contacten o te sigan
    if st.button("🚀 Contactar para Proyectos"):
        st.balloons()
        st.write("Mandame un mensaje si buscás optimizar tu rendimiento o necesitás software a medida.")


