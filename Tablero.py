def mostrar_tablero(unidades, terreno):
    print("Tablero 15x15:")
    for fila in range(15):
        linea = ""
        for col in range(15):
            celda_str = f"{fila}-{col}"
            ocupado = False
            for id, u in unidades.items():
                if u["posicion"] == [fila, col]:
                    linea += id[0].upper() + "  "
                    ocupado = True
                    break
            if not ocupado:
                if celda_str in terreno.get("impasables", []):
                    linea += "#  "
                else:
                    linea += ".  "
        print(linea)
