# ============================================================
# Módulo: Menú de Gestiones - Fase II
# Autor: Lucas Bassi
# Proyecto: PharmaCare Central
# ============================================================

# CÓDIGOS DE COLOR ANSI
VERDE = '\033[92m'
AZUL = '\033[94m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
CELESTE = '\033[96m'
VIOLETA = '\033[35m'
NARANJA = '\033[33m'
RESET = '\033[0m'

from lucas_bassi_validaciones import (
    validar_opcion,
    validar_opcion_menu_anterior,
    validar_entero_positivo,
    validar_confirmacion,
    validar_precio,
    validar_laboratorio_fabricante,
    ingresar_stock,
    validar_laboratorio_duplicado,
    validar_stock_suficiente,
    validar_monto_efectivo
)
from lucas_alegre import (crear_matriz_inicial, mostrar_matriz, mostrar_matriz_con_colores)

laboratorios = ["Roemmers", "Bagó", "Pfizer", "Roche", "ISA"]
ventas = []
stock_minimo_configurado = None  # Variable que almacena el stock mínimo configurado


def obtener_stock_minimo():
    """Retorna el stock mínimo configurado"""
    return stock_minimo_configurado


def establecer_stock_minimo(nuevo_stock_minimo):
    """Establece el stock mínimo configurado"""
    global stock_minimo_configurado
    stock_minimo_configurado = nuevo_stock_minimo

# ------------------------------------------------------------
# FUNCIONES - GESTIÓN DE LABORATORIOS
# ------------------------------------------------------------


def mostrar_menu_laboratorios():
    """Mostrar el menu de laboratorios y sus opciones"""

    print(f"{CELESTE}========================================#{RESET}")
    print(f"{AZUL}GESTIÓN DE LABORATORIOS{RESET}")
    print(f"{CELESTE}========================================#{RESET}")
    print(f"{AMARILLO}1.{RESET} Agregar laboratorio")
    print(f"{AMARILLO}2.{RESET} Modificar laboratorio")
    print(f"{AMARILLO}3.{RESET} Dar de baja laboratorio")
    print(f"{AMARILLO}4.{RESET} Ver laboratorios")
    print(f"{AMARILLO}5.{RESET} Volver al menú anterior")
    print(f"{CELESTE}========================================#{RESET}")
    print()


def submenu_laboratorios(laboratorios):
    """Submenú de gestión de laboratorios"""
    opcion = 0
    while opcion != 5:
        mostrar_menu_laboratorios()
        print("(Presione una opción válida para continuar)")
        opcion = validar_opcion(1, 5)
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
    
    print(f"(Presione {NARANJA}-1{RESET} para volver al menú anterior)")
    laboratorio = input("Ingresá el nombre del laboratorio (mayúscula para siglas): ").strip()
    
    # Chequear si presionó -1 para salir
    if laboratorio == "-1":
        return None
    
    # Si TODO está en mayúscula, preguntar si es sigla/acrónimo
    if laboratorio.isupper() and laboratorio.isalpha():
        es_sigla = input("¿Es una sigla o acrónimo? (si/no): ").strip().lower()
        if es_sigla != "si":
            laboratorio = laboratorio.capitalize()
    else:
        # Si no está TODO en mayúscula, capitalizar (primera letra mayúscula, resto minúscula)
        laboratorio = laboratorio.capitalize()

    while not validar_laboratorio_fabricante(laboratorio) or validar_laboratorio_duplicado(laboratorio, laboratorios):
        if not validar_laboratorio_fabricante(laboratorio):
            print("El nombre no puede estar vacío, solo contener números o solo símbolos.")
        else:
            print("El laboratorio ya existe en la lista.")
        laboratorio = input("Ingresá el nombre del laboratorio (mayúscula para siglas): ").strip()
        
        # Chequear si presionó -1 para salir
        if laboratorio == "-1":
            return None
        
        # Aplicar lógica de mayúsculas nuevamente
        if laboratorio.isupper() and laboratorio.isalpha():
            es_sigla = input("¿Es una sigla o acrónimo? (si/no): ").strip().lower()
            if es_sigla != "si":
                laboratorio = laboratorio.capitalize()
        else:
            laboratorio = laboratorio.capitalize()

    laboratorios.append(laboratorio)
    print(f"{VERDE}✓ Laboratorio {laboratorio} agregado exitosamente.{RESET}")
    print()


# Opcion 2
def modificar_laboratorio(laboratorios):
    """Modificar el laboratorio"""
    ver_laboratorios(laboratorios)
    
    print(f"(Presione {NARANJA}-1{RESET} para volver al menú anterior)")
    numero = input("Ingrese el numero del laboratorio que desea modificar: ")
    
    # Chequear si presionó -1 para salir
    if numero == "-1":
        return None

    while not validar_entero_positivo(numero) or len(laboratorios) < int(numero):
        if not validar_entero_positivo(numero):
            print("El numero debe ser entero y positivo")
        else:
            print("El numero ingresado no tiene asignado un laboratorio")
        numero = input("Ingrese el numero del laboratorio que desea modificar: ")
        
        # Chequear si presionó -1 para salir
        if numero == "-1":
            return None
         
    nuevo_nombre = input("Ingresa nuevo nombre del laboratorio (mayúscula para siglas): ").strip()
    
    # Chequear si presionó -1 para salir
    if nuevo_nombre == "-1":
        return None
    
    # Si TODO está en mayúscula, preguntar si es sigla/acrónimo
    if nuevo_nombre.isupper() and nuevo_nombre.isalpha():
        es_sigla = input("¿Es una sigla o acrónimo? (si/no): ").strip().lower()
        if es_sigla != "si":
            nuevo_nombre = nuevo_nombre.capitalize()
    else:
        # Si no está TODO en mayúscula, capitalizar
        nuevo_nombre = nuevo_nombre.capitalize()

    while not validar_laboratorio_fabricante(nuevo_nombre) or validar_laboratorio_duplicado(nuevo_nombre, laboratorios):
        if not validar_laboratorio_fabricante(nuevo_nombre):
            print("El nombre no puede estar vacío, solo contener números o solo símbolos.")
        else:
            print("El laboratorio ya existe en la lista.")
        nuevo_nombre = input("Ingresa nuevo nombre del laboratorio (mayúscula para siglas): ").strip()
        
        # Chequear si presionó -1 para salir
        if nuevo_nombre == "-1":
            return None
        
        # Aplicar lógica de mayúsculas nuevamente
        if nuevo_nombre.isupper() and nuevo_nombre.isalpha():
            es_sigla = input("¿Es una sigla o acrónimo? (si/no): ").strip().lower()
            if es_sigla != "si":
                nuevo_nombre = nuevo_nombre.capitalize()
        else:
            nuevo_nombre = nuevo_nombre.capitalize()

    laboratorios[int(numero) - 1] = nuevo_nombre    # Cambiamos al nombre nuevo
    print(f"{VERDE}✓ Laboratorio modificado exitosamente a {nuevo_nombre}.{RESET}")
    print()


# Opcion 3
def dar_de_baja_laboratorio(laboratorios):
    """Eliminar laboratorio de la lista"""
    if len(laboratorios) == 0:
        print(f"{ROJO}No hay laboratorios registrados{RESET}")
    else:
        ver_laboratorios(laboratorios)
        
        print(f"(Presione {NARANJA}-1{RESET} para volver al menú anterior)")
        numero = input("Ingresa numero de laboratorio que desea eliminar: ")
        
        # Chequear si presionó -1 para salir
        if numero == "-1":
            return None

        while not validar_entero_positivo(numero) or len(laboratorios) < int(numero):
            if not validar_entero_positivo(numero):
                print("El numero debe ser entero y positivo")
            else:
                print("El numero ingresado no tiene asignado un laboratorio")
            numero = input("Ingresa numero de laboratorio que desea eliminar: ")
            
            # Chequear si presionó -1 para salir
            if numero == "-1":
                return None
        
        nombre = laboratorios[int(numero) - 1]
        laboratorios.pop(int(numero) - 1)
        print(f"{ROJO}✓ Laboratorio {nombre} eliminado con exito{RESET}")
        print()


# Opcion 4:
def ver_laboratorios(laboratorios):
    """Ver lista de laboratorios registrados"""
    print("========================================")
    print("LABORATORIOS REGISTRADOS")
    print("========================================")

    contador = 1
    # Recorrer la lista para verificar que existan laboratorios
    if len(laboratorios) == 0:
        print(f"{ROJO}No hay laboratorios registrados{RESET}")
    else:
        for lab in laboratorios:
            print(f"{contador}. {lab}")
            contador += 1
    print("========================================")
    print()

# ------------------------------------------------------------
# FUNCIONES - GESTIÓN DE STOCK
# ------------------------------------------------------------


def mostrar_menu_stock():
    """Mostrar el menu de stock y sus opciones"""

    print(f"{CELESTE}========================================#{RESET}")
    print(f"{AZUL}GESTIÓN DE STOCK{RESET}")
    print(f"{CELESTE}========================================#{RESET}")
    print(f"{AMARILLO}1.{RESET} Configurar stock mínimo")
    print(f"{AMARILLO}2.{RESET} Reporte stock bajo mínimo")
    print(f"{AMARILLO}3.{RESET} Volver al menú anterior")
    print(f"{CELESTE}========================================#{RESET}")
    print()


def submenu_stock(matriz):
    """Menú de gestiones de stock"""
    opcion = 0

    while opcion != 3:
        mostrar_menu_stock()
        print("(Presione una opción válida para continuar)")
        opcion = validar_opcion(1, 3)
        if opcion == 1:
            configuracion_stock_minimo()
        elif opcion == 2:
            reporte_stock_bajo(matriz, obtener_stock_minimo())


# Opcion 1:
def configuracion_stock_minimo():
    """Configurar el stock minimo"""
    print(f"(Presione {NARANJA}-1{RESET} para volver al menú anterior)")
    asignar_stock_minimo = ingresar_stock()
    if asignar_stock_minimo is not None:
        establecer_stock_minimo(asignar_stock_minimo)
        print(f"{VERDE}✓ Stock minimo configurado con exito{RESET}")
        print()
    
    return None  # No retorna el valor, lo establece globalmente


# Opcion 2:
def reporte_stock_bajo(matriz, stock_minimo):
    """Informe que muestra medicamentos cuyo stock esta por debajo del minimo"""
    
    if stock_minimo == None:
        print(f"{ROJO}✗ No hay un stock minimo asignado{RESET}")
        return False
    
    # Almacenar medicamentos(filas) con stock por debajo del minimo
    mtz_debajo_stockMin = []
    
    for f in range(len(matriz)):
        if not validar_stock_suficiente(matriz[f], stock_minimo):
            mtz_debajo_stockMin.append(matriz[f])
    
    # Verificar si dentro de la matriz existen medicamentos
    if len(mtz_debajo_stockMin) > 0:
        print(f"\n{ROJO}⚠ MEDICAMENTOS CON STOCK POR DEBAJO DEL MÍNIMO ({stock_minimo}){RESET}")
        # Mostrar informe con colores (obtiene stock_minimo internamente)
        mostrar_matriz_con_colores(mtz_debajo_stockMin)
        print()
    else:
        print(f"{VERDE}✓ Todos los medicamentos tienen stock suficiente{RESET}")
        print()


# ------------------------------------------------------------
# FUNCIONES - GESTIÓN DE VENTAS
# ------------------------------------------------------------

def mostrar_menu_ventas():
    """Mostrar el menu de ventas y sus opciones"""

    print(f"{CELESTE}========================================#{RESET}")
    print(f"{AZUL}GESTIÓN DE VENTAS{RESET}")
    print(f"{CELESTE}========================================#{RESET}")
    print(f"{AMARILLO}1.{RESET} Registrar venta")
    print(f"{AMARILLO}2.{RESET} Ver ventas")
    print(f"{AMARILLO}3.{RESET} Volver al menú anterior")
    print(f"{CELESTE}========================================#{RESET}")
    print()


def submenu_ventas(matriz):
    """Submenú de gestión de ventas"""
    opcion = 0
    while opcion != 3:
        mostrar_menu_ventas()
        print("(Presione una opción válida para continuar)")
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
    print("(Presione una opción válida para continuar)")
    print()
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
    print("(Presione una opción válida para continuar)")
    print()

    opcion = validar_opcion(1, 2)

    if opcion == 1:
        monto = input("Ingresa el monto en efectivo (o -1 para volver): ")
        
        # Chequear si presionó -1 para salir
        if monto == "-1":
            return None

        while not validar_precio(monto) or not validar_monto_efectivo(float(monto), total):
            if not validar_precio(monto):
                print("El monto es decimal y debe ser positivo")
            else:
                print("Monto insuficiente")

            monto = input("Ingresa el monto en efectivo (o -1 para volver): ")
            
            # Chequear si presionó -1 para salir
            if monto == "-1":
                return None

        monto = float(monto)

        vuelto = monto - total
        print(f"{VERDE}✓ El vuelto es de ${vuelto}{RESET}")
        print()
    elif opcion == 2:
        # Sumar recargo al total
        recargo = total * 0.10
        total = total + recargo

        print(f"{AMARILLO}✓ El total a pagar es de ${total}{RESET}")
        print()


def registrar_venta(matriz):
    """Registrar una venta"""
    items = []

    # ✅ PRIMERA PREGUNTA: "¿Desea registrar una venta?"
    primera_venta = validar_confirmacion("¿Desea registrar una venta? (si/no): ")
    
    while primera_venta == "si":
        disponibles = mostrar_medicamentos_disponibles(matriz)
        
        # Si no hay medicamentos disponibles, muestra mensaje pero continúa
        if len(disponibles) == 0:
            print(f"{ROJO}No hay medicamentos disponibles para vender.{RESET}")
            print()
            # Vuelve a preguntar si desea registrar otra venta
            primera_venta = validar_confirmacion("¿Desea registrar otra venta? (si/no): ")
        else:
            # ✅ PEDIR OPCIÓN CON -1 PARA VOLVER
            print(f"(Presione {NARANJA}-1{RESET} para volver al menú anterior)")
            numero = input("Seleccione una opción: ")
            
            # ✅ CHEQUEAR SI PRESIONÓ -1 PARA SALIR
            if numero == "-1":
                print()
                return None
            
            # Validar que sea una opción válida
            while not numero.isdigit() or int(numero) < 1 or int(numero) > len(disponibles):
                print(f"Opción {ROJO}inválida{RESET}. Ingrese una opción entre 1 y {len(disponibles)}")
                numero = input("Seleccione una opción: ")
                
                # ✅ CHEQUEAR SI PRESIONÓ -1 PARA SALIR
                if numero == "-1":
                    print()
                    return None
            
            numero = int(numero)
            
            # Obtener índice real del medicamento en la matriz
            indice_real = disponibles[numero - 1]
            # Obtener fila completa del medicamento elegido
            medicamento = matriz[indice_real]

            # Cantidad a comprar
            cantidad = input("Ingrese la cantidad a comprar (o -1 para volver): ")
            
            # ✅ CHEQUEAR SI PRESIONÓ -1 PARA SALIR
            if cantidad == "-1":
                print()
                print("Operación cancelada.")
                print()
                return None
            
            # ✅ VALIDAR: entero positivo Y que haya stock suficiente
            while not validar_entero_positivo(cantidad) or not validar_stock_suficiente(medicamento, int(cantidad)):
                if not validar_entero_positivo(cantidad):
                    print("Debe ser un número positivo.")
                else:
                    print(f"{ROJO}No hay stock suficiente.{RESET}")
                cantidad = input("Ingrese la cantidad a comprar (o -1 para volver): ")
                
                # ✅ CHEQUEAR SI PRESIONÓ -1 PARA SALIR
                if cantidad == "-1":
                    print()
                    print("Operación cancelada.")
                    print()
                    return None
            
            cantidad = int(cantidad)

            subtotal = medicamento[3] * cantidad

            # Guardamos en items: codigo, nombre, cantidad, precio unitario y subtotal
            items.append([medicamento[0], medicamento[1], cantidad, medicamento[3], subtotal])
            
            # ✅ ACTUALIZAR STOCK EN LA MATRIZ INMEDIATAMENTE
            # Así la próxima vuelta del while mostrará el stock correcto
            medicamento[4] -= cantidad
            
            # ✅ PREGUNTA MEJORADA: "¿Desea registrar OTRA venta?"
            primera_venta = validar_confirmacion("¿Desea registrar otra venta? (si/no): ")

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
    print()

    # Forma de pago
    procesar_pago(total)

    # ✅ EL STOCK YA FUE DESCONTADO EN EL WHILE ANTERIOR
    # Entonces NO necesitamos descontar de nuevo
    # Simplemente guardamos las ventas

    # Guardar la venta en ventas
    for f in range(len(items)):
        ventas.append(items[f])


def ver_ventas(ventas):
    """Mostrar el historial de ventas registradas"""
    print("========================================")
    print("HISTORIAL DE VENTAS")
    print("========================================")
    if len(ventas) == 0:
        print(f"{ROJO}No hay ventas registradas{RESET}")
    else:
        for f in range(len(ventas)):
            print(f"{f + 1}. {ventas[f][1]} - Cantidad: {ventas[f][2]} - Subtotal: ${ventas[f][4]}")
    print("========================================")
    print()


# ------------------------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------------------------


def menu_gestion():
    """Mostrar menu de gestiones con todas sus opciones"""
    print(f"{CELESTE}========================================#{RESET}")
    print(f"{AZUL}GESTIONES - PHARMACARE CENTRAL{RESET}")
    print(f"{CELESTE}========================================#{RESET}")
    print(f"{AMARILLO}1.{RESET} Gestión de Laboratorios")
    print(f"{AMARILLO}2.{RESET} Gestión de Stock")
    print(f"{AMARILLO}3.{RESET} Gestión de Ventas")
    print(f"{AMARILLO}4.{RESET} Volver al menú principal")
    print(f"{CELESTE}========================================#{RESET}")
    print()


def mostrar_menu(matriz, laboratorios):
    """Menú principal de gestiones"""
    opcion = 0

    while opcion != 4:
        menu_gestion()
        opcion = validar_opcion(1, 4)
        if opcion == 1:
            submenu_laboratorios(laboratorios)
        elif opcion == 2:
            submenu_stock(matriz)
        elif opcion == 3:
            submenu_ventas(matriz)
        elif opcion == 4:
            print(f"{VERDE}✓ Volviendo al menú principal...{RESET}")


if __name__ == "__main__":
    matriz = crear_matriz_inicial()
    mostrar_menu(matriz)