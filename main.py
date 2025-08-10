from ia import IA
from tablero import mostrar_tablero

unidades = {
    "U1": {"tipo": "infanteria", "posicion": [7,7], "estado": "completo", "sector": "Centro"},
    "U2": {"tipo": "caballeria", "posicion": [6,7], "estado": "debilitado", "sector": "Centro"}
}

terreno = {
    "impasables": ["0-0", "0-1"]
}

def main():
    ia = IA(unidades, terreno)
    print("Estado inicial del tablero:")
    mostrar_tablero(unidades, terreno)
    ia.ejecutar_turno("Centro")
    print("Estado del tablero después del turno IA:")
    mostrar_tablero(unidades, terreno)

if __name__ == "__main__":
    main()
