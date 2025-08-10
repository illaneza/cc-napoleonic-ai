class IA:
    def __init__(self, unidades, terreno):
        self.unidades = unidades
        self.terreno = terreno

    def ejecutar_turno(self, orden_sector):
        print(f"Ejecutando turno IA en sector {orden_sector}")
        any_action = False
        for id, unidad in self.unidades.items():
            if unidad["sector"] == orden_sector:
                estado = unidad["estado"]
                tipo = unidad["tipo"]
                pos = unidad["posicion"]
                print(f"Unidad {id} ({tipo}, {estado}) en posición {pos} actúa.")
                any_action = True
        if not any_action:
            print("No hay unidades para actuar en ese sector.")
