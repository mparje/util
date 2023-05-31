import streamlit as st
import random

def main():
    st.title("Juego de Valor y Utilidad Marginal")
    st.write("¡Bienvenido al juego interactivo que combina la teoría del valor y la utilidad marginal según la escuela austriaca de economía!")

    # Definir la lista de bienes
    goods = {
        "Manzana": 5,
        "Plátano": 7,
        "Naranja": 4,
        "Pera": 6,
        "Uva": 8
    }

    # Seleccionar un bien aleatorio
    selected_good = st.selectbox("Elige un bien:", list(goods.keys()))

    # Mostrar información del bien seleccionado
    st.subheader("Bien Seleccionado")
    st.write(f"El bien seleccionado es: {selected_good}")
    st.write(f"Valor de Intercambio: {goods[selected_good]} puntos")

    # Explicar la teoría del valor
    st.subheader("Teoría del Valor")
    st.write("La escuela austriaca de economía sostiene que el valor de un bien no se determina por su costo de producción, sino por la utilidad subjetiva que tiene para los individuos. El valor de un bien es subjetivo y varía de una persona a otra.")

    st.subheader("Valor de Uso y Valor de Intercambio")
    st.write("La teoría austriaca distingue entre el valor de uso y el valor de intercambio de un bien. El valor de uso se refiere a la utilidad directa que un individuo obtiene al consumir o utilizar el bien. El valor de intercambio se refiere a la capacidad del bien para intercambiarse por otros bienes en el mercado.")

    # Decidir si comprar o no
    options = ["Comprar", "No comprar"]
    selected_option = st.selectbox("¿Qué acción quieres tomar?", options)

    if selected_option == "Comprar":
        st.subheader("Has decidido comprar el bien.")
        st.write(f"¡Felicidades! Has adquirido {selected_good}.")

        utility_gain = random.randint(1, 10)
        st.write(f"Has obtenido {utility_gain} puntos de utilidad.")

        # Explicar la utilidad marginal
        st.subheader("Utilidad Marginal")
        st.write("La utilidad marginal se refiere al cambio en la utilidad que obtienes al consumir una unidad adicional de un bien.")

        st.subheader("Ley de la Utilidad Marginal Decreciente")
        st.write("Según la ley de la utilidad marginal decreciente, a medida que consumes más de un bien, la utilidad marginal disminuye. Cada unidad adicional proporciona menos utilidad que la unidad anterior.")

        additional_units = st.number_input("¿Cuántas unidades adicionales del bien te gustaría consumir?", min_value=0, step=1)

        total_utility = utility_gain + additional_units
        st.write(f"Tu utilidad total sería de {total_utility} puntos.")

    elif selected_option == "No comprar":
        st.subheader("Has decidido no comprar el bien.")
        st.write("No has adquirido el bien, por lo que no obtendrás utilidad directa de él.")

    # Explicar resumen de la teoría
    st.subheader("Resumen de la Teoría")
    st.write("Según la teoría del valor y la utilidad marginal de la escuela austriaca, el valor de un bien se basa en la utilidad subjetiva que tiene para los individuos. Los individuos toman decisiones de consumo basadas en la utilidad marginal, tratando de maximizar su bienestar.")

if __name__ == '__main__':
    main()
