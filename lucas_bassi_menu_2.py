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
    validar_laboratorio_fabricante,
    ingresar_stock,
    validar_laboratorio_duplicado,
    validar_stock_suficiente,
    validar_monto_efectivo
)
from lucas_alegre import (crear_matriz_inicial, mostrar_matriz_con_colores)

# CÓDIGOS DE COLOR ANSI
VERDE = '\033[92m'
AZUL = '\033[94m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
CELESTE = '\033[96m'
VIOLETA = '\033[35m'
NARANJA = '\033[33m'
RESET = '\033[0m'

laboratorios = ["Roemmers", "Bagó", "Pfizer", "Roche", "ISA"]
ventas = []

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


def agregar_laboratorio(laboratorios):
    """Agregar laboratorio a la lista"""
    
    print(f"(Presione {NARANJA}-1{RESET} para volver al menú anterior)")
    laboratorio = input("Ingresá el nombre del laboratorio (mayúscula para siglas): ").strip()
    
    # Chequea si presionó -1 para salir
    if laboratorio == "-1":
        return None
    
    # Si todo está en mayúscula, preguntar si es sigla/acrónimo
    if laboratorio.isupper() and laboratorio.isalpha():
            es_sigla = input(f"¿Es una sigla o acrónimo? ({VERDE}si{RESET}/{ROJO}no{RESET}): ").strip().lower()
            while es_sigla != "si" and es_sigla != "no":
                print(f"Opción {ROJO}inválida{RESET}. Ingrese {VERDE}si{RESET} o {ROJO}no{RESET}")
                es_sigla = input(f"¿Es una sigla o acrónimo? ({VERDE}si{RESET}/{ROJO}no{RESET}): ").strip().lower()
            if es_sigla != "si":
                laboratorio = laboratorio.capitalize()
    else:
        laboratorio = laboratorio.capitalize()

    while not validar_laboratorio_fabricante(laboratorio) or validar_laboratorio_duplicado(laboratorio, laboratorios):
        if not validar_laboratorio_fabricante(laboratorio):
            print(f"El nombre {ROJO}NO{RESET} puede estar vacío, {ROJO}NI{RESET} contener solo números o solo símbolos.")
        else:
            print(f"{AMARILLO}El laboratorio ya existe en la lista.{RESET}")
        laboratorio = input("Ingresá el nombre del laboratorio (mayúscula para siglas): ").strip()
        
        # Chequear si presionó -1 para salir
        if laboratorio == "-1":
            return None
        
        # Aplicar lógica de mayúsculas nuevamente
        if laboratorio.isupper() and laboratorio.isalpha():
            es_sigla = input(f"¿Es una sigla o acrónimo? ({VERDE}si{RESET}/{ROJO}no{RESET}): ").strip().lower()
            if es_sigla != "si":
                laboratorio = laboratorio.capitalize()
        else:
            laboratorio = laboratorio.capitalize()

    laboratorios.append(laboratorio)
    print()
    print(f"{VERDE}✓ Laboratorio {laboratorio} agregado exitosamente.{RESET}")
    print()


def modificar_laboratorio(laboratorios):
    """Modificar el laboratorio"""
    ver_laboratorios(laboratorios)
    
    print(f"(Presione {AMARILLO}-1{RESET} para volver al menú anterior)")
    numero = input("Ingrese el numero del laboratorio que desea modificar: ")
    
    # Chequea si presionó -1 para salir
    if numero == "-1":
        return None

    while not validar_entero_positivo(numero) or len(laboratorios) < int(numero):
        if not validar_entero_positivo(numero):
            print("El numero debe ser entero y positivo")
        else:
            print("El numero ingresado no tiene asignado un laboratorio")
        numero = input("Ingrese el numero del laboratorio que desea modificar: ")
        
        # Chequea si presionó -1 para salir
        if numero == "-1":
            return None
         
    nuevo_nombre = input("Ingresa nuevo nombre del laboratorio (mayúscula para siglas): ").strip()
    
    # Chequea si presionó -1 para salir
    if nuevo_nombre == "-1":
        return None
    
    # Si todo está en mayúscula, preguntar si es sigla/acrónimo
    if nuevo_nombre.isupper() and nuevo_nombre.isalpha():
        es_sigla = input(f"¿Es una sigla o acrónimo? ({VERDE}si{RESET}/{ROJO}no{RESET}): ").strip().lower()
        while es_sigla != "si" and es_sigla != "no":
            print(f"Opción {ROJO}inválida{RESET}. Ingrese {VERDE}si{RESET} o {ROJO}no{RESET}")
            es_sigla = input(f"¿Es una sigla o acrónimo? ({VERDE}si{RESET}/{ROJO}no{RESET}): ").strip().lower()
        if es_sigla != "si":
            nuevo_nombre = nuevo_nombre.capitalize()
    else:
        # Si no está todo en mayúscula, capitalizar
        nuevo_nombre = nuevo_nombre.capitalize()

    while not validar_laboratorio_fabricante(nuevo_nombre) or validar_laboratorio_duplicado(nuevo_nombre, laboratorios):
        if not validar_laboratorio_fabricante(nuevo_nombre):
            print(f"El nombre {ROJO}NO{RESET} puede estar vacío,{ROJO}NI{RESET} solo contener números o solo símbolos.")
        else:
            print(f"{AMARILLO}El laboratorio ya existe en la lista.{RESET}")
        nuevo_nombre = input("Ingresa nuevo nombre del laboratorio (mayúscula para siglas): ").strip()
        
        # Chequear si presionó -1 para salir
        if nuevo_nombre == "-1":
            return None
        
        # Aplicar lógica de mayúsculas nuevamente
        if nuevo_nombre.isupper() and nuevo_nombre.isalpha():
            es_sigla = input(f"¿Es una sigla o acrónimo? ({VERDE}si{RESET}/{ROJO}no{RESET}): ").strip().lower()
            if es_sigla != "si":
                nuevo_nombre = nuevo_nombre.capitalize()
        else:
            nuevo_nombre = nuevo_nombre.capitalize()

    laboratorios[int(numero) - 1] = nuevo_nombre    # Cambiamos al nombre nuevo
    print()
    print(f"{VERDE}✓ Laboratorio modificado exitosamente a {nuevo_nombre}.{RESET}")
    print()


# Opcion 3
def dar_de_baja_laboratorio(laboratorios):
    """Eliminar laboratorio de la lista"""
    if len(laboratorios) == 0:
        print(f"{ROJO}No hay laboratorios registrados{RESET}")
    else:
        ver_laboratorios(laboratorios)
        
        print(f"(Presione {AMARILLO}-1{RESET} para volver al menú anterior)")
        numero = input("Ingresa numero de laboratorio que desea eliminar: ")
        
        # Chequear si presionó -1 para salir
        if numero == "-1":
            return None

        while not validar_entero_positivo(numero) or len(laboratorios) < int(numero):
            if not validar_entero_positivo(numero):
                print("El numero debe ser entero y positivo")
            else:
                print(f"{ROJO}El numero ingresado no tiene asignado un laboratorio{RESET}")
            numero = input("Ingresa numero de laboratorio que desea eliminar: ")
            
            # Chequear si presionó -1 para salir
            if numero == "-1":
                return None
        
        nombre = laboratorios[int(numero) - 1]
        laboratorios.pop(int(numero) - 1)
        print()
        print(f"{VERDE}✓ Laboratorio {nombre} eliminado con exito{RESET}")
        print()


# Opcion 4:
def ver_laboratorios(laboratorios):
    """Ver lista de laboratorios registrados"""
    print(f"{CELESTE}========================================{RESET}")
    print(f"{AZUL}LABORATORIOS REGISTRADOS{RESET}")
    print(f"{CELESTE}========================================{RESET}")

    contador = 1
    # Recorrer la lista para verificar que existan laboratorios
    if len(laboratorios) == 0:
        print(f"{ROJO}No hay laboratorios registrados{RESET}")
    else:
        for lab in laboratorios:
            print(f"{contador}. {lab}")
            contador += 1
    print(f"{CELESTE}========================================{RESET}")
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


def submenu_stock(matriz, stock_minimo):  
    """Menú de gestiones de stock"""
    opcion = 0

    while opcion != 3:
        mostrar_menu_stock()
        print("(Presione una opción válida para continuar)")
        opcion = validar_opcion(1, 3)
        if opcion == 1:
            nuevo_stock = configuracion_stock_minimo() 
            if nuevo_stock is not None:
                stock_minimo = nuevo_stock  
        elif opcion == 2:
            reporte_stock_bajo(matriz, stock_minimo)  
    
    return stock_minimo  


# Opcion 1:
def configuracion_stock_minimo():
    """Configurar el stock minimo"""
    print(f"(Presione {AMARILLO}-1{RESET} para volver al menú anterior)")
    asignar_stock_minimo = ingresar_stock()
    if asignar_stock_minimo is not None:
        print()
        print(f"{VERDE}✓ Stock minimo configurado con exito{RESET}")
        print()
        return asignar_stock_minimo 
    
    return None 


# Opcion 2:
def reporte_stock_bajo(matriz, stock_minimo):
    """Informe que muestra medicamentos cuyo stock esta por debajo del minimo"""
    
    if stock_minimo == None:
        print(f"{ROJO} No hay un stock minimo asignado{RESET}")
        return False
    
    # Almacenar medicamentos(filas) con stock por debajo del minimo
    mtz_debajo_stockMin = []
    
    for f in range(len(matriz)):
        if not validar_stock_suficiente(matriz[f], stock_minimo):
            mtz_debajo_stockMin.append(matriz[f])
    
    # Verificar si dentro de la matriz existen medicamentos
    if len(mtz_debajo_stockMin) > 0:
        print(f"\n{ROJO} MEDICAMENTOS CON STOCK POR DEBAJO DEL MÍNIMO ({stock_minimo}){RESET}")
        # Mostrar informe con colores (obtiene stock_minimo internamente)
        mostrar_matriz_con_colores(mtz_debajo_stockMin, stock_minimo)
        print()
    else:
        print()
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

    print(f"{CELESTE}========================================{RESET}")
    print(f"{AZUL}MEDICAMENTOS DISPONIBLES{RESET}")
    print(f"{CELESTE}========================================{RESET}")
    print("(Presione una opción válida para continuar)")
    print()
    contador = 1
    for f in range(len(matriz)):
        # Mostrar medicamentos con stock mayor a 0
        if matriz[f][4] > 0:
            # Guardar indice(fila) en disponibles
            disponibles.append(f)
            print(f"{AMARILLO}{contador}.{RESET} {matriz[f][1]} - Stock: {matriz[f][4]} - Precio: {matriz[f][3]}")
            contador += 1

    return disponibles


def procesar_pago(total, medicamentos_comprados):
    """Procesar el pago de la venta (efectivo o tarjeta). 
    Si cancela (-1), reversa el stock de TODOS los medicamentos."""
    print(f"{CELESTE}========================================{RESET}")
    print(f"{AZUL}PROCESAR PAGO{RESET}")
    print(f"{CELESTE}========================================{RESET}")
    print(f"{AMARILLO}1.{RESET} Efectivo")
    print(f"{AMARILLO}2.{RESET} Tarjeta(10% de recargo)")
    print(f"{CELESTE}========================================{RESET}")
    print()

    print(f"(Presione {AMARILLO}-1{RESET} para volver al menú anterior)")
    opcion_str = input("Seleccione una opción: ").strip()
    
    # Chequea si presion -1 para salir
    if opcion_str == "-1":
        # Devuelve stock de todos los medicamentos
        i = 0
        while i < len(medicamentos_comprados):
            medicamento, cantidad = medicamentos_comprados[i]
            medicamento[4] += cantidad
            i = i + 1
        
        print()
        print(f"{ROJO}Operación cancelada.{RESET} Stock de todos revertido.")
        print()
        return None
    
    # Valida que sea 1 o 2
    while not opcion_str.isdigit() or int(opcion_str) < 1 or int(opcion_str) > 2:
        print(f"Opción {ROJO}inválida{RESET}. Ingrese una opción entre {AMARILLO}1{RESET} y {AMARILLO}2{RESET}")
        opcion_str = input("Seleccione una opción: ").strip()
        
        # Chequea si presion -1 para salir
        if opcion_str == "-1":
            # Devuelve stock de todos los medicamentos
            i = 0
            while i < len(medicamentos_comprados):
                medicamento, cantidad = medicamentos_comprados[i]
                medicamento[4] += cantidad
                i = i + 1
            
            print()
            print(f"{ROJO}Operación cancelada.{RESET} Stock de todos revertido.")
            print()
            return None
    
    opcion = int(opcion_str)

    if opcion == 1:
        monto = input(f"Ingresa el monto en efectivo (o {AMARILLO}-1{RESET} para volver): ").strip()
        
        # Chequear si presionó -1 para salir
        if monto == "-1":
            # Devuelve todos los medicamentos 
            i = 0
            while i < len(medicamentos_comprados):
                medicamento, cantidad = medicamentos_comprados[i]
                medicamento[4] += cantidad
                i = i + 1
            
            print()
            print(f"{ROJO}Operación cancelada.{RESET} Stock de todos revertido.")
            print()
            return None

        while not validar_precio(monto) or not validar_monto_efectivo(float(monto), total):
            if not validar_precio(monto):
                print(f"{ROJO}ERROR. El monto debe ser un valor positivo.{RESET}")
            else:
                print(f"{ROJO}Monto insuficiente{RESET}")

            monto = input(f"Ingresa el monto en efectivo (o {AMARILLO}-1{RESET} para volver): ").strip()    
            
            # Chequear si presionó -1 para salir
            if monto == "-1":
                # Devuelve todos los medicamentos 
                i = 0
                while i < len(medicamentos_comprados):
                    medicamento, cantidad = medicamentos_comprados[i]
                    medicamento[4] += cantidad
                    i = i + 1
                
                print()
                print(f"{ROJO}Operación cancelada.{RESET}2 Stock de todos revertido.")
                print()
                return None

        monto = float(monto)

        vuelto = monto - total
        print()
        print(f"{VERDE}✓ Venta registrada exitosamente{RESET}")
        print(f"{AMARILLO} El vuelto es de:{RESET} ${vuelto}")
        print()
        return True  
    
    elif opcion == 2:
        # Sumar recargo al total
        recargo = total * 0.10
        total_con_recargo = total + recargo

        print()
        print(f"{VERDE}✓ Venta registrada exitosamente{RESET}")
        print(f"{AMARILLO} El total a pagar es de:{RESET} ${total_con_recargo}")
        print()
        return True  


def registrar_venta(matriz):
    """Registrar una venta"""
    items = []
    # Lista para guardar medicamentos y cantidades
    medicamentos_comprados = []  

    # PRIMERA PREGUNTA: "¿Desea registrar una venta?"
    primera_venta = validar_confirmacion(f"¿Desea registrar una venta? ({VERDE}si{RESET}/{ROJO}no{RESET}): ")
    
    while primera_venta == "si":
        disponibles = mostrar_medicamentos_disponibles(matriz)
        
        # Si no hay medicamentos disponibles, muestra mensaje pero continúa
        if len(disponibles) == 0:
            print(f"{ROJO}No hay medicamentos disponibles para vender.{RESET}")
            print()
            # Vuelve a preguntar si desea registrar otra venta
            primera_venta = validar_confirmacion(f"¿Desea registrar otra venta? ({VERDE}si{RESET}/{ROJO}no{RESET}): ")
        else:
            # PEDIR OPCIÓN CON -1 PARA VOLVER
            print(f"(Presione {AMARILLO}-1{RESET} para volver al menú anterior)")
            numero = input("Seleccione una opción: ")
            
            # CHEQUEAR SI PRESIONÓ -1 PARA SALIR
            if numero == "-1":
                print()
                return None
            
            # Validar que sea una opción válida
            while not numero.isdigit() or int(numero) < 1 or int(numero) > len(disponibles):
                print(f"Opción {ROJO}inválida{RESET}. Ingrese una opción entre {AMARILLO}1 y {len(disponibles)}{RESET}")
                numero = input("Seleccione una opción: ")
                
                # CHEQUEAR SI PRESIONÓ -1 PARA SALIR
                if numero == "-1":
                    print()
                    return None
            
            numero = int(numero)
            
            # Obtener índice real del medicamento en la matriz
            indice_real = disponibles[numero - 1]
            # Obtener fila completa del medicamento elegido
            medicamento = matriz[indice_real]

            # Cantidad a comprar
            cantidad = input(f"Ingrese la cantidad a comprar (o {AMARILLO}-1{RESET} para volver): ")
            
            # CHEQUEAR SI PRESIONÓ -1 PARA SALIR
            if cantidad == "-1":
                print()
                print(f"{ROJO}Operación cancelada.{RESET}")
                print()
                return None
            
            # VALIDAR: entero positivo Y que haya stock suficiente
            while not validar_entero_positivo(cantidad) or not validar_stock_suficiente(medicamento, int(cantidad)):
                if not validar_entero_positivo(cantidad):
                    print("Debe ser un número positivo.")
                else:
                    print(f"{ROJO}No hay stock suficiente.{RESET}")
                cantidad = input(f"Ingrese la cantidad a comprar (o {AMARILLO}-1{RESET} para volver): ")
                
                # CHEQUEA SI SE INGRESO -1 PARA SALIR
                if cantidad == "-1":
                    print()
                    print(f"{ROJO}Operación cancelada.{RESET}")
                    print()
                    return None
            
            cantidad = int(cantidad)

            subtotal = medicamento[3] * cantidad

            # Guardamos en items: codigo, nombre, cantidad, precio unitario y subtotal
            items.append([medicamento[0], medicamento[1], cantidad, medicamento[3], subtotal])
            
            # Guardamos referencia al medicamento Y cantidad
            medicamentos_comprados.append([medicamento, cantidad])
            
            # ACTUALIZACION DE STOCK EN LA MATRIZ INMEDIATAMENTE
            medicamento[4] -= cantidad
            
            primera_venta = validar_confirmacion(f"¿Desea registrar otra venta? ({VERDE}si{RESET}/{ROJO}no{RESET}): ")

    # Verificar que se haya adquirido un producto
    if len(items) == 0:
        return None

    # Mostrar resumen de la venta
    total = 0       # Total de la compra
    print(f"{CELESTE}========================================{RESET}")
    print(f"{AZUL}RESUMEN DE VENTA{RESET}")
    print(f"{CELESTE}========================================{RESET}")
    for f in range(len(items)):
        total += items[f][4]
        print(f"{AMARILLO}{f + 1}.{RESET} {items[f][1]} - Cantidad: {items[f][2]} - Subtotal: ${items[f][4]}")
    print(f"{NARANJA}Total:{RESET} ${total}")
    print(f"{CELESTE}========================================{RESET}")
    print()

    # Forma de pago
    resultado_pago = procesar_pago(total, medicamentos_comprados)

    if resultado_pago is True:  # Solo si pagó exitoso
        for f in range(len(items)):
            ventas.append(items[f]) 


def ver_ventas(ventas):
    """Mostrar el historial de ventas registradas"""
    print(f"{CELESTE}========================================{RESET}")
    print(f"{AZUL}HISTORIAL DE VENTAS{RESET}")
    print(f"{CELESTE}========================================{RESET}")
    if len(ventas) == 0:
        print(f"{ROJO}No hay ventas registradas{RESET}")
    else:
        for f in range(len(ventas)):
            print(f"{f + 1}. {ventas[f][1]} - Cantidad: {ventas[f][2]} - Subtotal: ${ventas[f][4]}")
    print(f"{CELESTE}========================================{RESET}")
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


def mostrar_menu_gestiones(matriz, laboratorios, stock_minimo):  
    """Menú principal de gestiones"""
    opcion = 0

    while opcion != 4:
        menu_gestion()
        opcion = validar_opcion(1, 4)
        if opcion == 1:
            submenu_laboratorios(laboratorios)
        elif opcion == 2:
            stock_minimo = submenu_stock(matriz, stock_minimo)  
        elif opcion == 3:
            submenu_ventas(matriz)
        elif opcion == 4:
            print()
            print(f"{VERDE}✓ Volviendo al menú principal...{RESET}")
    
    return stock_minimo  


if __name__ == "__main__":
    matriz = crear_matriz_inicial()
    mostrar_menu_gestiones(matriz)