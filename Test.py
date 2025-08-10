import json

def cargar_datos(ruta):
    with open(ruta, "r") as f:
        return json.load(f)

def test():
    print("Inicio test...")
    unidades = cargar_datos("datos/unidades.json")
    terreno = cargar_datos("datos/terreno.json")
    print("Unidades cargadas:", unidades)
    print("Terreno cargado:", terreno)
    print("Test finalizado con éxito.")

if __name__ == "__main__":
    test()
