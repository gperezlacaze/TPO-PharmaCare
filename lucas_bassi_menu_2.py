# ============================================================
# Módulo: Menú de Gestiones - Fase II
# Autor: Lucas Bassi
# Proyecto: PharmaCare Central
# ============================================================

from lucas_bassi_validaciones import (
    validar_opcion,
    validar_entero_positivo,
    validar_confirmacion,
    validar_precio,
)
from lucas_alegre_validaciones_fase_2 import (
    validar_laboratorio_duplicado,
    validar_nombre_laboratorio,
    validar_stock_suficiente,
    validar_monto_efectivo,
)
from lucas_alegre import (crear_matriz_inicial, mostrar_matriz)

laboratorios = ["Roemmers", "Bagó", "Pfizer", "Roche", "ISA"]
ventas = []

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

    laboratorios[int(numero) - 1] = nuevo_nombre    # Cambiamos al nombre nuevo
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
# FUNCIONES - GESTIÓN DE STOCK
# ------------------------------------------------------------


def mostrar_menu_stock():
    """Mostrar el menu de stock y sus opciones"""

    print("========================================")
    print("GESTIÓN DE STOCK")
    print("========================================")
    print("1. Configurar stock mínimo")
    print("2. Reporte stock bajo mínimo")
    print("3. Salir")
    print("========================================")


def submenu_stock(matriz):
    """Menú principal de gestiones"""
    opcion = 0
    stock_minimo = None

    while opcion != 3:
        mostrar_menu_stock()
        opcion = validar_opcion(1,3)
        if opcion == 1:
            stock_minimo = configuracion_stock_minimo()
        elif opcion == 2:
            reporte_stock_bajo(matriz, stock_minimo)


# Opcion 1:
def configuracion_stock_minimo():
    """Configurar el stock minimo"""
    asignar_stock_minimo = input("Ingrese stock minimo: ")

    while not validar_entero_positivo(asignar_stock_minimo):
        print("Debe ser un número positivo.")
        asignar_stock_minimo = input("Ingrese stock minimo: ")
    
    print("Stock minimo configurado con exito")
    return int(asignar_stock_minimo)


# Opcion 2:
def reporte_stock_bajo(matriz, stock_minimo):
    """Informe que muestra medicamentos cuyo stock esta por debajo del minimo"""
    
    if stock_minimo == None:
        print("No hay un stock minimo asignado")
        return False
    
    # Almacenar medicamentos(filas) con stock por debajo del minimo
    mtz_debajo_stockMin = []
    
    for f in range(len(matriz)):
        if not validar_stock_suficiente(matriz[f], stock_minimo):
            mtz_debajo_stockMin.append(matriz[f])
    
    # Verificar si dentro de la matriz existen medicamentos
    if len(mtz_debajo_stockMin) > 0:
        # Mostrar informe
        mostrar_matriz(mtz_debajo_stockMin)
    else:
        print("Todos los medicamentos tienen stock suficiente")


# ------------------------------------------------------------
# FUNCIONES - GESTIÓN DE VENTAS
# ------------------------------------------------------------

def mostrar_menu_ventas():
    """Mostrar el menu de ventas y sus opciones"""

    print("========================================")
    print("GESTIÓN DE VENTAS")
    print("========================================")
    print("1. Registrar venta")
    print("2. Ver ventas")
    print("3. Salir")
    print("========================================")


def submenu_ventas(matriz):
    """Submenú de gestión de ventas"""
    opcion = 0
    while opcion != 3:
        mostrar_menu_ventas()
        opcion = validar_opcion(1, 3)
        if opcion == 1:
            registrar_venta(matriz)
        elif opcion == 2:
            ver_ventas(ventas)


# Opcion 1/2:
def mostrar_medicamentos_disponibles(matriz):
    """Mostrar medicamentos disponibles para la venta"""
    disponibles = []

    print("========================================")
    print("MEDICAMENTOS DISPONIBLES")
    print("========================================")
    contador = 1
    for f in range(len(matriz)):
        # Mostrar medicamentos con stock mayor a 0
        if matriz[f][4] > 0:
            # Guardar indice(fila) en disponibles
            disponibles.append(f)
            print(f"{contador}. {matriz[f][1]} - Stock: {matriz[f][4]} - Precio: {matriz[f][3]}")
            contador += 1

    return disponibles


def procesar_pago(total):
    """Procesar el pago de la venta(fectivo o tarjeta)"""
    print("========================================")
    print("PROCESAR PAGO")
    print("========================================")
    print("1. Efectivo")
    print("2. Tarjeta(10% de recargo)")
    print("========================================")

    opcion = validar_opcion(1, 2)

    if opcion == 1:
        monto = input("Ingresa el monto en efectivo: ")

        while not validar_precio(monto) or not validar_monto_efectivo(float(monto), total):
            if not validar_precio(monto):
                print("El monto es decimal y debe ser positivo")
            else:
                print("Monto insuficiente")

            monto = input("Ingresa el monto en efectivo: ")

        monto = float(monto)

        vuelto = monto - total
        print(f"El vuelto es de ${vuelto}")
    elif opcion == 2:
        # Sumar recargo al total
        recargo = total * 0.10
        total = total + recargo

        print(f"El total a pagar es de ${total}")


def registrar_venta(matriz):
    """Registrar una venta"""
    items = []

    while validar_confirmacion("¿Desea registrar una venta? (si/no): "):
        disponibles = mostrar_medicamentos_disponibles(matriz)
        # Pedir medicamento a comprar1
        numero = validar_opcion(1, len(disponibles))
        # Obtener índice real del medicamento en la matriz
        indice_real = disponibles[numero - 1]
        # Obtener fila completa del medicamento elegido
        medicamento = matriz[indice_real]

        # Cantidad a comprar
        cantidad = input("Ingrese la cantidad a comprar: ")
        while not validar_entero_positivo(cantidad) or not validar_stock_suficiente(medicamento, int(cantidad)):
            if not validar_entero_positivo(cantidad):
                print("Debe ser un número positivo.")
            else:
                print("No hay stock suficiente.")
            cantidad = input("Ingrese la cantidad a comprar: ")
        cantidad = int(cantidad)

        subtotal = medicamento[3] * cantidad

        # Guardamos en items: codigo, nombre, cantidad, precio unitario y subtotal
        items.append([medicamento[0], medicamento[1], cantidad, medicamento[3], subtotal])

    # Verificar que se haya adquirido un producto
    if len(items) == 0:
        return None

    # Mostrar resumen de la venta
    total = 0       # Total de la compra
    print("========================================")
    print("RESUMEN DE VENTA")
    print("========================================")
    for f in range(len(items)):
        total += items[f][4]
        print(f"{f + 1}. {items[f][1]} - Cantidad: {items[f][2]} - Subtotal: ${items[f][4]}")
    print(f"Total: ${total}")
    print("========================================")

    # Forma de pago
    procesar_pago(total)

    # Descontar stock
    for f in range(len(items)):
        for m in range(len(matriz)):
            if matriz[m][0] == items[f][0]:  # buscar por codigo
                matriz[m][4] -= items[f][2]  # restamos stock

    # Guardar la venta en ventas
    for f in range(len(items)):
        ventas.append(items[f])


def ver_ventas(ventas):
    """Mostrar el historial de ventas registradas"""
    print("========================================")
    print("HISTORIAL DE VENTAS")
    print("========================================")
    if len(ventas) == 0:
        print("No hay ventas registradas")
    else:
        for f in range(len(ventas)):
            print(f"{f + 1}. {ventas[f][1]} - Cantidad: {ventas[f][2]} - Subtotal: ${ventas[f][4]}")


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


def mostrar_menu(matriz, laboratorios):
    """Menú principal de gestiones"""
    opcion = 0

    while opcion != 4:
        menu_gestion()
        opcion = validar_opcion(1,4)
        if opcion == 1:
            submenu_laboratorios(laboratorios)
        elif opcion == 2:
            submenu_stock(matriz)
        elif opcion == 3:
            submenu_ventas(matriz)
        elif opcion == 4:
            print("Volviendo al menu principal...")


if __name__ == "__main__":
    matriz = crear_matriz_inicial()
    mostrar_menu(matriz)
    