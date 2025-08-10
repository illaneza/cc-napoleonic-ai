def mostrar_tablero():
    filas = 15
    columnas = 15

    # Ejemplo: lista de celdas impasables (terreno)
    impasables = ["0-0", "0-1", "1-0", "7-7", "14-14"]

    print("Tablero 15x15:")
    for fila in range(filas):
        linea = ""
        for col in range(columnas):
            celda_id = f"{fila}-{col}"
            if celda_id in impasables:
                linea += "#  "
            else:
                linea += ".  "
        print(linea)

if __name__ == "__main__":
    mostrar_tablero()
    input("\nPulsa Enter para salir...")
