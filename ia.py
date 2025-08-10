# ia.py
from tablero import obtener_sector, posicion_ocupada, es_adyacente, distancia, puede_mover
from unidades import unidades

def mover_unidad(uid, nueva_pos):
    if puede_mover(uid, nueva_pos):
        unidades[uid]["pos"] = nueva_pos
        return True
    return False

def atacar(atacante_id, defensor_id):
    atacante = unidades[atacante_id]
    defensor = unidades[defensor_id]

    if not es_adyacente(atacante["pos"], defensor["pos"]):
        return False

    if defensor["estado"] == "completo":
        defensor["estado"] = "debilitado"
        return True
    else:
        del unidades[defensor_id]
        return True

def ia_accion(sector_objetivo):
    acciones = []
    for uid, data in list(unidades.items()):
        if data["equipo"] != "IA":
            continue
        if obtener_sector(data["pos"][1]) != sector_objetivo:
            continue

        pos = data["pos"]
        enemigos_ady = [eid for eid, edata in unidades.items()
                       if edata["equipo"] != "IA" and es_adyacente(pos, edata["pos"])]
        if enemigos_ady:
            atacante = uid
            defensor = enemigos_ady[0]
            atacar(atacante, defensor)
            acciones.append(f"{atacante} atacó a {defensor}")
            continue

        enemigos_sector = [edata for edata in unidades.values() if edata["equipo"] != "IA" and obtener_sector(edata["pos"][1]) == sector_objetivo]
        if enemigos_sector:
            enemigo_cercano = min(enemigos_sector, key=lambda e: distancia(pos, e["pos"]))
            efila, ecol = enemigo_cercano["pos"]
            fila, col = pos

            nuevas_posibles = [
                (fila + df, col + dc)
                for df in (-1,0,1)
                for dc in (-1,0,1)
                if (df != 0 or dc != 0)
            ]
            nuevas_posibles = sorted(nuevas_posibles, key=lambda p: distancia(p, (efila, ecol)))
            moved = False
            for np in nuevas_posibles:
                if puede_mover(uid, np):
                    mover_unidad(uid, np)
                    acciones.append(f"{uid} se movió a {np}")
                    moved = True
                    break
            if not moved:
                acciones.append(f"{uid} no pudo moverse")
        else:
            acciones.append(f"{uid} sin enemigos en sector para atacar o mover")
    return acciones
