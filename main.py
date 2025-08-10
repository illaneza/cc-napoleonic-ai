from ia import IA
from tablero import mostrar_tablero
import json

def cargar_datos(ruta):
    with open(ruta, "r") as f:
        return json.load(f)

def main():
    unidades = cargar_datos("datos/unidades.json")
    terreno = cargar_datos("datos/terreno.json")
    ia = IA(unidades, terreno)
    print("Estado inicial del tablero:")
    mostrar_tablero(unidades, terreno)
    ia.ejecutar_turno("Centro")  # Ejemplo de orden para IA
    print("Estado del tablero después del turno IA:")
    mostrar_tablero(unidades, terreno)

if __name__ == "__main__":
    main()
