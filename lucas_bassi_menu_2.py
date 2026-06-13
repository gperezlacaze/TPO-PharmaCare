# Módulo: Menú de Gestiones - Fase II
# Autor: Lucas Bassi
# Proyecto: PharmaCare Central

from lucas_bassi_validaciones import(validar_opcion, validar_entero_positivo)
from lucas_alegre_validaciones_fase_2 import(validar_laboratorio_duplicado, 
    validar_nombre_laboratorio)

# "Roemmers", "Bagó", "Pfizer", "Roche", "ISA"
laboratorios = ["Roemmers", "Bagó", "Pfizer", "Roche", "ISA"]


# ------------------------------------------------------------
# FUNCIONES - GESTIÓN DE LABORATORIOS
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
         agregar_laboratorio(laboratorios)
     elif opcion == 2:
         modificar_laboratorio(laboratorios)
     elif opcion == 3:
         dar_de_baja_laboratorio(laboratorios)
     elif opcion == 4:
         ver_laboratorios(laboratorios)


# Opcion 1:
def agregar_laboratorio(laboratorios):
    """Agregar laboratorio a la lista"""

    laboratorio = input("Ingresá el nombre del laboratorio: ").strip()

    while not validar_nombre_laboratorio(laboratorio) or validar_laboratorio_duplicado(laboratorio, laboratorios):
        if not validar_nombre_laboratorio(laboratorio):
            print("El nombre no puede estar vacío.")
        else:
            print("El laboratorio ya existe en la lista.")
        laboratorio = input("Ingresá el nombre del laboratorio: ").strip()

    laboratorios.append(laboratorio)
    print(f"Laboratorio {laboratorio} agregado exitosamente.")

# Opcion 2
def modificar_laboratorio(laboratorios):
    """Modificar el laboratorio"""
    ver_laboratorios(laboratorios)
    
    numero = input("Ingrese el numero del laboratorio que desea modificar: ")

    while not validar_entero_positivo(numero) or len(laboratorios) < int(numero):
        if not validar_entero_positivo(numero):
            print("El numero debe ser entero y positivo")
        else:
            print("El numero ingresado no tiene asignado un laboratorio")
        numero = input("Ingrese el numero del laboratorio que desea modificar: ")
         
    nuevo_nombre = input("Ingresa nuevo nombre del laboratorio: ").strip()

    while not validar_nombre_laboratorio(nuevo_nombre) or validar_laboratorio_duplicado(nuevo_nombre, laboratorios):
        if not validar_nombre_laboratorio(nuevo_nombre):
            print("El nombre no puede estar vacío.")
        else:
            print("El laboratorio ya existe en la lista.")
        nuevo_nombre = input("Ingresa nuevo nombre del laboratorio: ").strip()

    laboratorios[int(numero) - 1] = nuevo_nombre
    print(f"Laboratorio modificado exitosamente a {nuevo_nombre}.")

# Opcion 3
def dar_de_baja_laboratorio(laboratorios):
    """Eliminar laboratorio de la lista"""
    if len(laboratorios) == 0:
        print("No hay laboratorios registrados")
    else:
        ver_laboratorios(laboratorios)

        numero = input("Ingresa numero de laboratorio que desea eliminar: ")

        while not validar_entero_positivo(numero) or len(laboratorios) < int(numero):
          if not validar_entero_positivo(numero):
             print("El numero debe ser entero y positivo")
          else:
             print("El numero ingresado no tiene asignado un laboratorio")
          numero = input("Ingresa numero de laboratorio que desea eliminar: ")
        
        nombre = laboratorios[int(numero) - 1]
        laboratorios.pop(int(numero) - 1)
        print(f"Laboratorio {nombre} eliminado con exito")


# Opcion 4:
def ver_laboratorios(laboratorios):
    """Ver lista de laboratorios registrados"""
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
    """Mostrar menu de gestiones con todas sus opciones"""
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
    mostrar_menu()