# app.py
import streamlit as st
from tablero import mostrar_tablero
from ia import ia_accion
from unidades import unidades

def listar_unidades(st):
    st.write("### Unidades:")
    for uid, data in unidades.items():
        pos = data["pos"]
        sector = ""
        # Lógica para obtener sector si quieres mostrar aquí (o importarla)
        sector = "Izquierdo" if pos[1] <= 4 else ("Centro" if pos[1] <= 9 else "Derecho")
        estado = data["estado"]
        equipo = data["equipo"]
        color = "red" if estado == "debilitado" else "black"
        st.markdown(f"- <span style='color:{color}'>{uid} ({data['tipo']}, {estado}, Equipo: {equipo}) en {pos} - Sector {sector}</span>", unsafe_allow_html=True)

def main():
    st.title("Command & Colors Napoleonic - IA simple")
    mostrar_tablero(st)
    listar_unidades(st)

    st.write("---")
    sector_obj = st.selectbox("Orden IA: Atacar sector", ["Izquierdo", "Centro", "Derecho"])
    if st.button("Ejecutar acción IA"):
        acciones = ia_accion(sector_obj)
        for a in acciones:
            st.write(a)
        st.experimental_rerun()

if __name__ == "__main__":
    main()
