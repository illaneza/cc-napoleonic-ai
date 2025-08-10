# Colores ANSI básicos para consola (Pythonista soporta estos)
RESET = "\033[0m"
VERDE = "\033[32m"
BLANCO = "\033[37m"
AMARILLO = "\033[33m"
ROJO = "\033[31m"

FILAS = 15
COLUMNAS = 15

LIM_IZQ = 4
LIM_CENTRO = 9

impasables = ["0-0", "0-1", "7-7", "14-14"]

unidades = {
    "U1": {"tipo": "I", "pos": (2, 3), "estado": "completo"},
    "U2": {"tipo": "C", "pos": (4, 7), "estado": "completo"},
    "U3": {"tipo": "A", "pos": (10, 10), "estado": "debilitado"},
    "U4": {"tipo": "I", "pos": (6, 12), "estado": "completo"},
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
        return VERDE
    elif col <= LIM_CENTRO:
        return BLANCO
    else:
        return AMARILLO

def mostrar_tablero():
    print("TABLERO COLOREADO CON SECTORES:\n")
    for fila in range(FILAS):
        linea = ""
        for col in range(COLUMNAS):
            celda_id = f"{fila}-{col}"
            if celda_id in impasables:
                linea += ROJO + "#  " + RESET
            else:
                unidad_en_celda = None
                for uid, data in unidades.items():
                    if data["pos"] == (fila, col):
                        unidad_en_celda = data["tipo"] + uid[1]
                        break
                if unidad_en_celda:
                    # Unidades en rojo si debilitadas
                    color = ROJO if unidades[uid]["estado"] == "debilitado" else RESET
                    linea += f"{color}{unidad_en_celda} {RESET}"
                else:
                    # Fondo sector coloreado (simulado)
                    linea += f"{color_sector(col)}.  {RESET}"
        print(linea)
    print(f"\nLeyenda: {VERDE}Izquierdo{RESET}, {BLANCO}Centro{RESET}, {AMARILLO}Derecho{RESET}, {ROJO}Terreno impasable/Unidades debilitadas{RESET}")

def listar_unidades():
    print("\nUNIDADES Y SECTORES:")
    for uid, data in unidades.items():
        fila, col = data["pos"]
        sector = obtener_sector(col)
        estado = data["estado"]
        color_estado = ROJO if estado == "debilitado" else RESET
        print(f"{color_estado}{uid} ({data['tipo']}, {estado}) en {data['pos']} → Sector {sector}{RESET}")

def mover_unidad(uid, nueva_pos):
    fila, col = nueva_pos
    celda_id = f"{fila}-{col}"

    if celda_id in impasables:
        print(f"No se puede mover {uid}: terreno impasable.")
        return
    for _, data in unidades.items():
        if data["pos"] == (fila, col):
            print(f"No se puede mover {uid}: celda ocupada.")
            return

    unidades[uid]["pos"] = nueva_pos
    print(f"{uid} movida a {nueva_pos} (Sector {obtener_sector(col)}).")

if __name__ == "__main__":
    mostrar_tablero()
    listar_unidades()

    mover_unidad("U1", (3, 3))
    mover_unidad("U2", (4, 11))

    mostrar_tablero()
    listar_unidades()
    input("\nPulsa Enter para salir...")
