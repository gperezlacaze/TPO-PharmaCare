from lucas_bassi_menu_2 import(validar_opcion)


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
    opcion = 0
    while opcion <= 4:
     menu_gestion()
     opcion = validar_opcion(1,4)
     if opcion == 1:
         pass # gestión laboratorios
     elif opcion == 2:
         pass # gestión stock
     elif opcion == 3:
         pass # gestión ventas
     elif opcion == 4:
         pass #salir
     


        



