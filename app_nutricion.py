import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Toji Nutrición", page_icon="💪")

st.title("🔥 Sistema de Nutrición Elite")
st.markdown("---")

# BARRA LATERAL PARA DATOS (Más interactivo)
st.sidebar.header("Tus Datos Biométricos")
peso = st.sidebar.number_input("Peso Actual (kg)", value=80.0)
altura = st.sidebar.number_input("Altura (cm)", value=181)
edad = st.sidebar.number_input("Edad", value=20)
genero = st.sidebar.radio("Género", ["Hombre", "Mujer"])
actividad = st.sidebar.select_slider(
    'Nivel de Actividad',
    options=['Sedentario', 'Ligero', 'Moderado', 'Atleta']
)

# Lógica de Cálculo
if genero == "Hombre":
    tmb = 66 + (13.7 * peso) + (5 * altura) - (6.8 * edad)
else:
    tmb = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad)

factores = {"Sedentario": 1.2, "Ligero": 1.375, "Moderado": 1.55, "Atleta": 1.725}
calorias_finales = tmb * factores[actividad]

# INTERACTIVIDAD: Selección de Objetivo
st.subheader("🎯 ¿Cuál es tu objetivo hoy?")
objetivo = st.selectbox("Elegí tu meta:", ["Mantener Peso", "Ganar Músculo (Volumen)", "Perder Grasa (Definición)"])

if objetivo == "Ganar Músculo (Volumen)":
    calorias_finales += 400
    st.success("Modo Volumen activado: Comé para crecer, Guerrero.")
elif objetivo == "Perder Grasa (Definición)":
    calorias_finales -= 400
    st.warning("Modo Definición: Priorizá la proteína para no perder músculo.")

# GRÁFICO INTERACTIVO DE MACROS
st.markdown("### 📊 Distribución Recomendada de Macros")

# Cálculo simple de macros
prot = peso * 2  # 2g por kilo
grasas = peso * 0.8 # 0.8g por kilo
carbs = (calorias_finales - (prot * 4) - (grasas * 9)) / 4

df_macros = pd.DataFrame({
    'Macro': ['Proteínas (g)', 'Grasas (g)', 'Carbohidratos (g)'],
    'Cantidad': [prot, grasas, carbs]
})

# Mostrar gráfico de barras
st.bar_chart(data=df_macros, x='Macro', y='Cantidad')

# Métricas finales destacadas
col1, col2, col3 = st.columns(3)
col1.metric("Calorías Totales", f"{int(calorias_finales)} kcal")
col2.metric("Proteína", f"{int(prot)}g")
col3.metric("Carbohidratos", f"{int(carbs)}g")

st.markdown("---")

# --- SECCIÓN DE RECOMENDACIÓN DE ALIMENTOS ---
st.markdown("### 🥗 Sugerencia de Alimentos para hoy")

# Creamos pestañas para que sea más interactivo
tab1, tab2, tab3 = st.tabs(["Fuentes de Proteína", "Fuentes de Carbohidratos", "Fuentes de Grasas"])

with tab1:
    st.write(f"Para llegar a tus **{int(prot)}g** de proteína, podrías elegir:")
    # Calculamos cantidades reales según el alimento
    st.write(f"- 🍗 **Pollo/Carne:** Aproximadamente {int(prot * 5)}g en crudo.")
    st.write(f"- 🥚 **Huevos:** Unos {int(prot / 6)} huevos grandes.")
    st.write(f"- 🧀 **Queso Magro:** Unos {int(prot * 4)}g.")

with tab2:
    st.write(f"Tus **{int(carbs)}g** de carbohidratos se ven así:")
    st.write(f"- 🍚 **Arroz/Fideos:** {int(carbs * 3.5)}g cocidos (unas {int((carbs * 3.5)/200)} tazas).")
    st.write(f"- 🥔 **Papa/Batata:** {int(carbs * 5)}g (unas {int((carbs * 5)/200)} unidades medianas).")
    st.write(f"- 🍎 **Frutas:** Unas {int(carbs / 20)} porciones de fruta.")

with tab3:
    st.write(f"Tus **{int(grasas)}g** de grasas saludables:")
    st.write(f"- 🥑 **Palta:** Unas {int(grasas / 15)} paltas medianas.")
    st.write(f"- 🥜 **Frutos Secos:** {int(grasas)}g (un puñado generoso).")
    st.write(f"- 🧴 **Aceite de Oliva:** {int(grasas / 9)} cucharadas soperas.")

# --- SECCIÓN DE ENTRENAMIENTO (EL TOQUE TOJI) ---
st.divider()
st.subheader("⚔️ Entrenamiento del día")
if actividad == "Atleta":
    st.write("Hoy el gasto es alto. Priorizá el descanso post-entrenamiento y no olvides el tereré para hidratar los electrolitos.")
else:
    st.write("Si querés ver cambios más rápidos, intentá subir tu nivel de actividad a 'Moderado' o 'Atleta'.")

# Botón para descargar resultados (Interacción Pro)
st.download_button(
    label="Descargar mi Plan en Texto",
    data=f"Plan Nutricional de Jonathan\nCalorías: {int(calorias_finales)}\nProteína: {int(prot)}g\nCarbos: {int(carbs)}g",
    file_name="mi_plan_nutricional.txt",
    mime="text/plain"
)

st.markdown("---")
st.caption("Desarrollado por Jonathan E. Roman Vazquez - Programación & Alto Rendimiento")
