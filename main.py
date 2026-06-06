# ============================================================
# PROGRAMA PRINCIPAL: main.py
# Proyecto: PharmaCare Central
# Equipo: Gonzalo Perez Lacaze, Lucas Alegre, Lucas Bassi
# Descripción: Coordina el flujo del sistema de gestión de inventario
# ============================================================

from lucas_alegre import crear_matriz_inicial
from gonzalo_perez_lacaze_menu import (
    mostrar_menu, validar_opcion, alta_medicamentos,
    baja_medicamentos, buscar_medicamento,
    modificar_stock_precio, informe_general, salir
)


def main():
    """Función principal que coordina el flujo del programa. Crea el inventario inicial y maneja el menú principal."""
    # Cargar el inventario inicial con 5 medicamentos
    inventario = crear_matriz_inicial()

    # Bucle principal del programa
    opcion = 0
    opcion = 0
    while opcion != 6 and opcion != 8:
        mostrar_menu()
        opcion = validar_opcion(1, 6)

        if opcion == 1:
            alta_medicamentos(inventario)
        elif opcion == 2:
            baja_medicamentos(inventario)
        elif opcion == 3:
            buscar_medicamento(inventario)
        elif opcion == 4:
            modificar_stock_precio(inventario)
        elif opcion == 5:
            informe_general(inventario)
        elif opcion == 6 or opcion == 8:
            salir()


if __name__ == "__main__":
    main()