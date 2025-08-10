# Command & Color Napoleonic - IA Asistente

Este proyecto es una IA simple para asistir en las decisiones tácticas del juego de mesa Command & Color Napoleonic.

## Características

- Tablero de 15x15 celdas con unidades y terreno.
- Unidades clasificadas en Infantería, Caballería y Artillería.
- IA que recibe órdenes por sectores (Izquierdo, Centro, Derecho).
- Movimiento y ataque según tipo, estado (completo o debilitado) y distancia.
- Evita terrenos impasables y posiciones ocupadas.
- Prioriza atacar tipos de unidades según configuración.

## Archivos

- `main.py`: Entrada del programa, ejecuta el turno de la IA.
- `ia.py`: Lógica de IA (movimiento, ataque, priorización).
- `tablero.py`: Funciones para visualizar el tablero y calcular sectores.
- `datos/`: Contiene configuraciones y datos de unidades y terreno.

## Uso

1. Configurar posiciones y terreno en `datos/unidades.json` y `datos/terreno.json`.
2. Ejecutar `main.py` para simular el turno IA.
3. Modificar la IA o añadir funcionalidades según se necesite.

## Requisitos

- Python 3.x

## Licencia

Este proyecto está bajo licencia MIT.
