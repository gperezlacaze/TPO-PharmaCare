# Módulo: Menú de Gestiones - Fase II
# Autor: Lucas Bassi
# Proyecto: PharmaCare Central

from lucas_bassi_validaciones import(validar_opcion)

# "Roemmers", "Bagó", "Pfizer", "Roche", "ISA"
laboratorios = ["Roemmers", "Bagó", "Pfizer", "Roche", "ISA"]


# ------------------------------------------------------------
# FUNCIONES RF04 - GESTIÓN DE LABORATORIOS
# ------------------------------------------------------------


def mostrar_menu_laboratorios():
    """Mostrar el menu de laboratorios y sus opciones"""

    print("========================================")
    print("GESTIÓN DE LABORATORIOS")
    print("========================================")
    print("1. Agregar laboratorio")
    print("2. Modificar laboratorio")
    print("3. Dar de baja laboratorio")
    print("4. Ver laboratorios")
    print("5. Salir")
    print("========================================")


def submenu_laboratorios(laboratorios):
    """Submenú de gestión de laboratorios"""
    opcion = 0
    while opcion != 5:
     mostrar_menu_laboratorios()
     opcion = validar_opcion(1,5)
     if opcion == 1:
         pass # Agregar laboratorios
     elif opcion == 2:
         pass # modificar laboratorios
     elif opcion == 3:
         pass # dar de baja laboratorios
     elif opcion == 4:
         ver_laboratorios(laboratorios)
     elif opcion == 5:
         pass # salir
    
# Opcion 4:
def ver_laboratorios(laboratorios):
    print("========================================")
    print("LABORATORIOS REGISTRADOS")
    print("========================================")

    contador = 1
    # Recorrer la lista para verificar que existan laboratorios
    if len(laboratorios) == 0:
        print("No hay laboratorios registrados")
    else:
        for lab in laboratorios:
         print(f"{contador}. {lab}")
         contador += 1
    print("========================================")


# ------------------------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------------------------


def menu_gestion():
    "Mostrar menu de gestiones con todas sus opciones"
    print("========================================")
    print("GESTIONES - PHARMACARE CENTRAL")
    print("========================================")
    print("1. Gestión de Laboratorios")
    print("2. Gestión de Stock")
    print("3. Gestión de Ventas")
    print("4. Salir")
    print("========================================")


def mostrar_menu():
    """Menú principal de gestiones"""
    opcion = 0
    while opcion != 4:
     menu_gestion()
     opcion = validar_opcion(1,4)
     if opcion == 1:
         submenu_laboratorios(laboratorios)
     elif opcion == 2:
         pass # gestión stock
     elif opcion == 3:
         pass # gestión ventas
     elif opcion == 4:
         pass # salir
     


if __name__ == "__main__":
    mostrar_menu(laboratorios)