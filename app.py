import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Calculadora de Rebajas", page_icon="🏷️")

# Título y descripción
st.title("🛍️ Calculadora de Rebajas")
st.markdown("Introduce el precio original y el descuento para calcular el precio final.")
st.write("---")

# 2. Entrada de datos (Barra lateral)
st.sidebar.header("Datos del producto")
precio_original = st.sidebar.number_input(
    "Precio original (€)", min_value=0.0, max_value=10000.0, value=100.0
)

descuento = st.sidebar.slider(
    "Descuento (%)", min_value=0, max_value=99, value=20
)

# 3. Botón de cálculo y lógica
if st.button("Calcular rebaja"):
    
    # Cálculos
    ahorro = precio_original * descuento / 100
    precio_final = precio_original - ahorro

    # 4. Mostrar resultados con diseño
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Precio final (€)", value=f"{precio_final:.2f}")

    with col2:
        st.metric(label="Te ahorras (€)", value=f"{ahorro:.2f}")

        
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r'''
    Precio\ final = Precio\ original - \left(\frac{Precio\ original \times Descuento}{100}\right)
    ''')
