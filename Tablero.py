# tablero.py
import math
from unidades import unidades

FILAS = 15
COLUMNAS = 15
LIM_IZQ = 4
LIM_CENTRO = 9

impasables = [(0,0), (0,1), (7,7), (14,14)]

def obtener_sector(col):
    if col <= LIM_IZQ:
        return "Izquierdo"
    elif col <= LIM_CENTRO:
        return "Centro"
    else:
        return "Derecho"

def color_sector(col):
    if col <= LIM_IZQ:
        return "#a0d995"
    elif col <= LIM_CENTRO:
        return "#ffffff"
    else:
        return "#fff38f"

def posicion_ocupada(pos):
    for uid, data in unidades.items():
        if data["pos"] == pos:
            return uid
    return None

def es_adyacente(pos1, pos2):
    fila1, col1 = pos1
    fila2, col2 = pos2
    return abs(fila1 - fila2) <= 1 and abs(col1 - col2) <= 1 and pos1 != pos2

def distancia(pos1, pos2):
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

def puede_mover(uid, nueva_pos):
    fila, col = nueva_pos
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLUMNAS:
        return False
    if nueva_pos in impasables:
        return False
    if posicion_ocupada(nueva_pos):
        return False
    return True

def mostrar_tablero(st):
    letras = "ABCDEFGHIJKLMNO"
    tablero_html = "<table style='border-collapse: collapse; text-align:center;'>"

    # Fila superior con letras
    tablero_html += "<tr><td></td>"
    for col in range(COLUMNAS):
        tablero_html += f"<td style='width:30px; height:30px; font-weight:bold;'>{letras[col]}</td>"
    tablero_html += "<td></td></tr>"

    for fila in range(FILAS):
        tablero_html += f"<tr><td style='font-weight:bold; padding-right:5px;'>{fila+1}</td>"

        for col in range(COLUMNAS):
            estilo_celda = f"width:30px; height:30px; border:1px solid black; vertical-align:middle; "
            if (fila,col) in impasables:
                color_fondo = "#ff4c4c"
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

        tablero_html += f"<td style='font-weight:bold; padding-left:5px;'>{fila+1}</td></tr>"

    tablero_html += "<tr><td></td>"
    for col in range(COLUMNAS):
        tablero_html += f"<td style='width:30px; height:30px; font-weight:bold;'>{letras[col]}</td>"
    tablero_html += "<td></td></tr>"

    tablero_html += "</table>"
    st.markdown(tablero_html, unsafe_allow_html=True)
