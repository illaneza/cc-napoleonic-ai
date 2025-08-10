import streamlit as st

FILAS = 15
COLUMNAS = 15
LIM_IZQ = 4
LIM_CENTRO = 9

impasables = [(0,0), (0,1), (7,7), (14,14)]

# Unidades con: tipo (I,C,A), posición, estado, equipo
unidades = {
    "U1": {"tipo": "I", "pos": (2, 3), "estado": "completo", "equipo": "IA"},
    "U2": {"tipo": "C", "pos": (4, 7), "estado": "completo", "equipo": "IA"},
    "U3": {"tipo": "A", "pos": (10, 10), "estado": "debilitado", "equipo": "Jugador"},
    "U4": {"tipo": "I", "pos": (6, 12), "estado": "completo", "equipo": "Jugador"},
}

def obtener_sector(col):
    if col <= LIM_IZQ:
        return "Izquierdo"
    elif col <= LIM_CENTRO:
        return "Centro"
    else:
        return "Derecho"

def color_sector(col):
    if col <= LIM_IZQ:
        return "#a0d995"  # Verde claro
    elif col <= LIM_CENTRO:
        return "#ffffff"  # Blanco
    else:
        return "#fff38f"  # Amarillo claro

def posicion_ocupada(pos):
    for uid, data in unidades.items():
        if data["pos"] == pos:
            return uid
    return None

def es_adyacente(pos1, pos2):
    # Chequea si dos posiciones son vecinas (incluye diagonales)
    fila1, col1 = pos1
    fila2, col2 = pos2
    return abs(fila1 - fila2) <= 1 and abs(col1 - col2) <= 1 and pos1 != pos2

def puede_mover(uid, nueva_pos):
    # No puede moverse fuera del tablero
    fila, col = nueva_pos
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLUMNAS:
        return False, "Fuera del tablero"
    if nueva_pos in impasables:
        return False, "Terreno impasable"
    if posicion_ocupada(nueva_pos):
        return False, "Celda ocupada"
    return True, ""

def mover_unidad(uid, nueva_pos):
    puede, motivo = puede_mover(uid, nueva_pos)
    if puede:
        unidades[uid]["pos"] = nueva_pos
        return True, f"{uid} movida a {nueva_pos} (Sector {obtener_sector(nueva_pos[1])})"
    else:
        return False, f"{uid} no se pudo mover: {motivo}"

def atacar(atacante_id, defensor_id):
    atacante = unidades[atacante_id]
    defensor = unidades[defensor_id]
    
    # Ataque simple: si están adyacentes, el defensor se debilita o elimina
    if not es_adyacente(atacante["pos"], defensor["pos"]):
        return False, "Objetivo fuera de alcance"
    
    if defensor["estado"] == "completo":
        defensor["estado"] = "debilitado"
        return True, f"{atacante_id} atacó a {defensor_id}: {defensor_id} ahora debilitado"
    else:
        # Eliminamos unidad
        del unidades[defensor_id]
        return True, f"{atacante_id} atacó y eliminó a {defensor_id}"

def mostrar_tablero():
    tablero_html = "<table style='border-collapse: collapse;'>"
    for fila in range(FILAS):
        tablero_html += "<tr>"
        for col in range(COLUMNAS):
            estilo_celda = f"width:30px; height:30px; text-align:center; border:1px solid black; "
            color_fondo = ""
            if (fila,col) in impasables:
                color_fondo = "#ff4c4c"  # Rojo para impasables
            else:
                color_fondo = color_sector(col)
            estilo_celda += f"background-color: {color_fondo};"

            contenido = ""
            for uid, data in unidades.items():
                if data["pos"] == (fila, col):
                    tipo = data["tipo"]
                    estado = data["estado"]
                    color_texto = "red" if estado == "debilitado" else "black"
                    equipo = "I" if data["equipo"] == "IA" else "J"
                    contenido = f"<span style='color:{color_texto}; font-weight:bold;'>{tipo}{equipo}</span>"
                    break

            tablero_html += f"<td style='{estilo_celda}'>{contenido}</td>"
        tablero_html += "</tr>"
    tablero_html += "</table>"
    st.markdown(tablero_html, unsafe_allow_html=True)

def listar_unidades():
    st.write("### Unidades:")
    for uid, data in unidades.items():
        pos = data["pos"]
        sector = obtener_sector(pos[1])
        estado = data["estado"]
        equipo = data["equipo"]
        color = "red" if estado == "debilitado" else "black"
        st.markdown(f"- <span style='color:{color}'>{uid} ({data['tipo']}, {estado}, Equipo: {equipo}) en {pos} - Sector {sector}</span>", unsafe_allow_html=True)

def main():
    st.title("Command & Colors Napoleonic - IA Movimiento y Combate")
    
    mostrar_tablero()
    listar_unidades()

    st.write("---")
    st.write("### Mover unidad")
    uid_mover = st.selectbox("Selecciona unidad a mover", options=list(unidades.keys()))
    fila_nueva = st.number_input("Nueva fila (0-14)", min_value=0, max_value=FILAS-1, value=unidades[uid_mover]["pos"][0])
    col_nueva = st.number_input("Nueva columna (0-14)", min_value=0, max_value=COLUMNAS-1, value=unidades[uid_mover]["pos"][1])

    if st.button("Mover"):
        exito, msg = mover_unidad(uid_mover, (fila_nueva, col_nueva))
        st.success(msg) if exito else st.error(msg)
        st.experimental_rerun()  # recarga para ver cambio

    st.write("---")
    st.write("### Atacar unidad enemiga")
    atacante = st.selectbox("Unidad atacante", options=list(unidades.keys()))
    posibles_objetivos = [uid for uid in unidades if uid != atacante and es_adyacente(unidades[atacante]["pos"], unidades[uid]["pos"])]
    if posibles_objetivos:
        defensor = st.selectbox("Unidad objetivo", options=posibles_objetivos)
        if st.button("Atacar"):
            exito, msg = atacar(atacante, defensor)
            st.success(msg) if exito else st.error(msg)
            st.experimental_rerun()
    else:
        st.info("No hay objetivos adyacentes para atacar")

if __name__ == "__main__":
    main()
