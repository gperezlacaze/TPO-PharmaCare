# ============================================================
# MÓDULO: lucas_bassi_validaciones.py
# Autor: Lucas Bassi
# Descripción: Funciones de validación para PharmaCare
# ============================================================

# CÓDIGOS DE COLOR ANSI
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
CELESTE = '\033[96m'
VIOLETA = '\033[35m'
NARANJA = '\033[33m'
AZUL = '\033[94m'
RESET = '\033[0m'


# ============================================================
# SECCIÓN: FUNCIONES DE VALIDACIÓN
# (para validar datos ingresados por el usuario)
# ============================================================


def validar_nombre_medicamento(nombre):
    '''Valida que el nombre tenga letras, no sea solo números o símbolos. Retorna True/False.'''
    nombre = nombre.strip()
    
    # No puede estar vacío
    if len(nombre) == 0:
        return False
    
    # Debe tener al menos una letra
    tiene_letra = any(c.isalpha() for c in nombre)
    
    if not tiene_letra:
        return False
    
    return True


def validar_codigo_medicamento(codigo):
    '''Valida el código: 4-8 caracteres alfanuméricos, sin espacios internos. Retorna True/False.'''
    codigo = codigo.strip().upper()
    
    if len(codigo) < 4 or len(codigo) > 8:
        return False
    
    if not codigo.isalnum():
        return False
    
    return True


def validar_codigo_unico(codigo, matriz):
    '''Valida que el código no exista ya en la matriz. Retorna True si es único, False si está duplicado.'''
    codigo = codigo.strip().upper()
    i = 0
    while i < len(matriz):
        if matriz[i][0] == codigo:
            return False  # Código duplicado
        i = i + 1
    return True  # Código único


def validar_laboratorio_fabricante(nombre):
    '''Valida que el laboratorio no esté vacío y tenga al menos una letra. Rechaza solo números y solo símbolos. Retorna True/False.'''
    nombre = nombre.strip()
    
    if len(nombre) == 0:
        return False
    
    # Rechazar si solo contiene números
    if nombre.isdigit():
        return False
    
    # Rechazar si solo contiene símbolos (sin letras ni números)
    if not any(c.isalnum() for c in nombre):
        return False
    
    return True


def validar_entero_positivo(valor):
    '''Valida que sea un entero positivo (sin decimales, sin negativos). Retorna True/False.'''
    valor = valor.strip()
    
    if not valor.isdigit():
        return False
    
    return int(valor) > 0


def validar_fecha_vencimiento(fecha):
    '''Valida fecha en formato dd/mm/aaaa. Retorna True/False.
    El año debe tener exactamente 4 dígitos (ej: 2026, no 26)'''
    fecha = fecha.strip()
    
    if fecha.count('/') != 2:
        return False
    
    partes = fecha.split('/')
    
    if len(partes) != 3:
        return False
    
    dia_str, mes_str, anio_str = partes
    
    # Validar que todos sean números
    if not (dia_str.isdigit() and mes_str.isdigit() and anio_str.isdigit()):
        return False
    
    # Validar que el año tenga exactamente 4 dígitos
    if len(anio_str) != 4:
        return False
    
    dia = int(dia_str)
    mes = int(mes_str)
    anio = int(anio_str)
    
    if mes < 1 or mes > 12:
        return False
    
    # Días máximos por mes (sin considerar bisiestos)
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False
    
    return True


def validar_precio(precio):
    '''Valida que sea un número positivo (entero o decimal). Retorna True/False.'''
    precio = precio.strip()
    
    if len(precio) == 0:
        return False
    
    # Contar puntos
    if precio.count('.') > 1:
        return False
    
    # Si solo hay un punto
    if '.' in precio:
        partes = precio.split('.')
        if len(partes) != 2:
            return False
        if not (partes[0].isdigit() and partes[1].isdigit()):
            return False
        if len(partes[0]) == 0 or len(partes[1]) == 0:
            return False
    else:
        # Sin punto, solo dígitos
        if not precio.isdigit():
            return False
    
    return float(precio) > 0


def validar_cobertura(cobertura):
    '''Valida que sea "Con cobertura" o "Sin cobertura" (case-insensitive). Retorna True/False.'''
    cobertura = cobertura.strip().lower()
    return cobertura in ["con cobertura", "sin cobertura"]


# ============================================================
# SECCIÓN: FUNCIONES DE INGRESO
# (piden datos al usuario y retornan valores o None si -1)
# ============================================================


def ingresar_codigo(matriz):
    '''Pedir y validar el código del medicamento. Presione -1 para salir.'''
    codigo = input(f"Ingrese el código {AMARILLO}(4-8 caracteres){RESET} (o {AMARILLO}-1{RESET} para volver): ").strip().upper()
    
    if codigo == "-1":
        return None
    
    while not validar_codigo_medicamento(codigo):
        print(f"Código {ROJO}inválido{RESET}: debe tener 4-8 caracteres alfanuméricos sin espacios.")
        codigo = input(f"Ingrese el código {AMARILLO}(4-8 caracteres){RESET} (o {AMARILLO}-1{RESET} para volver): ").strip().upper()
        if codigo == "-1":
            return None
    
    while not validar_codigo_unico(codigo, matriz):
        print(f"Código {ROJO}duplicado{RESET}: ya existe en el sistema.")
        codigo = input(f"Ingrese el código {AMARILLO}(4-8 caracteres){RESET} (o {AMARILLO}-1{RESET} para volver): ").strip().upper()
        if codigo == "-1":
            return None
    
    return codigo


def ingresar_medicamento():
    '''Pedir y validar el nombre del medicamento. Presione -1 para salir.'''
    nombre = input("Ingrese el nombre del medicamento (o -1 para volver): ")
    
    if nombre == "-1":
        return None
    
    while not validar_nombre_medicamento(nombre):
        print(f"Nombre {ROJO}inválido{RESET}: debe contener al menos una letra (no solo números o símbolos).")
        nombre = input("Ingrese el nombre del medicamento (o -1 para volver): ")
        if nombre == "-1":
            return None
    
    return nombre


def ingresar_laboratorio(laboratorios):
    laboratorio = input("Ingrese el laboratorio (o -1 para volver): ").strip()
    
    if laboratorio == "-1":
        return None
    
    while not validar_laboratorio_fabricante(laboratorio):
        print(f"El nombre no puede estar vacío, solo contener números o solo símbolos.")
        laboratorio = input("Ingrese el laboratorio (o -1 para volver): ").strip()
        if laboratorio == "-1":
            return None
    
    # Detección automática de siglas
    if laboratorio.isupper() and laboratorio.isalpha():
        print()
        respuesta = input("¿Es una sigla o acrónimo? (si/no): ").strip().lower()
        print()
        
        while respuesta not in ["si", "no"]:
            print(f"Respuesta {ROJO}inválida{RESET}. Ingrese 'si' o 'no'")
            respuesta = input("¿Es una sigla o acrónimo? (si/no): ").strip().lower()
            print()
        
        if respuesta == "no":
            laboratorio = laboratorio.capitalize()
    else:
        # Mezcla de mayúsculas/minúsculas → capitalizar automáticamente
        laboratorio = laboratorio.capitalize()
    
    # Validar duplicados
    while True:
        es_duplicado = validar_laboratorio_duplicado(laboratorio, laboratorios)
        if es_duplicado:
            print(f"Laboratorio {ROJO}duplicado{RESET}: ya existe en el sistema.")
            laboratorio = input("Ingrese el laboratorio (o -1 para volver): ").strip()
            if laboratorio == "-1":
                return None
        else:
            break
    
    return laboratorio


def ingresar_precio():
    '''Pedir y validar el precio del medicamento. Presione -1 para salir.'''
    precio = input("Ingrese el precio (o -1 para volver): ")
    
    if precio == "-1":
        return None
    
    while not validar_precio(precio):
        print(f"Precio {ROJO}inválido{RESET}: debe ser un número positivo.")
        precio = input("Ingrese el precio (o -1 para volver): ")
        if precio == "-1":
            return None
    
    return float(precio)


def ingresar_stock():
    '''Pedir y validar el stock del medicamento. Presione -1 para salir.'''
    stock = input("Ingrese el stock (o -1 para volver): ")
    
    if stock == "-1":
        return None
    
    while not validar_entero_positivo(stock):
        print(f"Stock {ROJO}inválido{RESET}: debe ser un número entero positivo.")
        stock = input("Ingrese el stock (o -1 para volver): ")
        if stock == "-1":
            return None
    
    return int(stock)


def ingresar_fecha_vencimiento():
    '''Pedir y validar la fecha de vencimiento. Presione -1 para salir.'''
    fecha = input('Ingrese la fecha de vencimiento (dd/mm/aaaa) (o -1 para volver): ')
    
    if fecha == "-1":
        return None
    
    while not validar_fecha_vencimiento(fecha):
        print(f'Fecha {ROJO}inválida{RESET}: debe estar en formato dd/mm/aaaa (año con 4 dígitos, ej: 2026 no 26)')
        fecha = input('Ingrese la fecha de vencimiento (dd/mm/aaaa) (o -1 para volver): ')
        if fecha == "-1":
            return None
    return fecha


def ingresar_cobertura():
    '''Pedir y validar la cobertura médica del medicamento. Presione -1 para salir.'''
    cobertura = input("Ingrese la cobertura (Con cobertura / Sin cobertura) (o -1 para volver): ").strip()
    
    if cobertura == "-1":
        return None
    
    cobertura = cobertura.capitalize()
    while not validar_cobertura(cobertura):
        print(f"Cobertura {ROJO}inválida{RESET}: debe ser 'Con cobertura' o 'Sin cobertura'.")
        cobertura = input("Ingrese la cobertura (Con cobertura / Sin cobertura) (o -1 para volver): ").strip()
        if cobertura == "-1":
            return None
        cobertura = cobertura.capitalize()
    return cobertura


# ============================================================
# SECCIÓN: FUNCIONES DE MENÚ
# (interactúan con el usuario para opciones y confirmaciones)
# ============================================================


def validar_opcion_menu_anterior(desde, hasta):
    '''Valida opción en funciones. Permite -1 para volver al menú anterior.'''
    opcion = input("Seleccione una opción: ")
    # Permitir números negativos para -1 (salida)
    while not (opcion.lstrip('-').isdigit() or opcion == '-1'):
        print("La opción debe ser un número.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)
    while (opcion < desde or opcion > hasta) and opcion != -1:
        print(f"La opción seleccionada no es {ROJO}válida{RESET}") 
        opcion = input("Seleccione una opción: ")
        while not (opcion.lstrip('-').isdigit() or opcion == '-1'):
            print("La opción debe ser un número.")
            opcion = input("Seleccione una opción: ")
        opcion = int(opcion)
    return opcion


def validar_confirmacion(pregunta):
    '''Valida que la respuesta sea "si" o "no" (case-insensitive). Solo acepta estas dos palabras.'''
    respuesta = input(pregunta).strip().lower()
    while respuesta not in ["si", "no"]:
        print(f"Respuesta {ROJO}inválida{RESET}. Ingrese '{VERDE}si{RESET}' o '{ROJO}no{RESET}':")
        respuesta = input(pregunta).strip().lower()
    return respuesta


# ============================================================
# FASE 2 - VALIDACIONES ADICIONALES
# Autor: Lucas Alegre
# ============================================================

def seleccionar_laboratorio(laboratorios):
    '''Permite seleccionar un laboratorio de la lista existente. Presione -1 para salir.
    Función nueva implementada en Fase 2 para permitir seleccionar laboratorios existentes al dar de alta medicamentos.'''
    print()
    print("Laboratorios disponibles:")
    
    i = 0
    while i < len(laboratorios):
        print(f"{AMARILLO}{i + 1}.{RESET} {laboratorios[i]}")
        i = i + 1
    
    print()
    seleccion = input(f"Seleccione un laboratorio ({AMARILLO}1{RESET}-{AMARILLO}{len(laboratorios)}{RESET}) (o {AMARILLO}-1{RESET} para volver): ").strip()
    
    if seleccion == "-1":
        return None
    
    while not seleccion.isdigit() or int(seleccion) < 1 or int(seleccion) > len(laboratorios):
        print(f"Selección {ROJO}inválida{RESET}. Intente de nuevo.")
        seleccion = input(f"Seleccione un laboratorio ({AMARILLO}1{RESET}-{AMARILLO}{len(laboratorios)}{RESET}) (o {AMARILLO}-1{RESET} para volver): ").strip()
        if seleccion == "-1":
            return None
    
    laboratorio_seleccionado = laboratorios[int(seleccion) - 1]
    return laboratorio_seleccionado


def validar_opcion(desde, hasta):
    '''Valida opción en menús (principal, gestiones, submenús). NO permite -1 (solo opciones válidas).'''
    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or int(opcion) < desde or int(opcion) > hasta:
        print(f"La opción seleccionada no es {ROJO}válida{RESET}. Ingrese una opción entre {desde} y {hasta}")
        opcion = input("Seleccione una opción: ")
    return int(opcion)


def validar_laboratorio_duplicado(nombre, lista_laboratorios):
    '''Valida si un laboratorio ya existe en la lista (case-insensitive)'''
    nombre_normalizado = nombre.strip().lower()
    i = 0
    while i < len(lista_laboratorios):
        if lista_laboratorios[i].lower() == nombre_normalizado:
            return True
        i = i + 1
    return False


def validar_stock_suficiente(medicamento, cantidad):
    '''Valida si hay stock suficiente. medicamento es una fila de la matriz, cantidad es un int'''
    stock_disponible = medicamento[4]  # Índice 4 es el stock
    return stock_disponible >= cantidad


def validar_monto_efectivo(monto, total):
    '''Valida si el monto en efectivo es suficiente para pagar el total'''
    return monto >= total


if __name__ == "__main__":

    # Funcion 1: validar_codigo_medicamento
    print("\nvalidar_codigo_medicamento:")
    print("VÁLIDO - 'MED3452': ", validar_codigo_medicamento("Med3452"))  # True
    print("VÁLIDO - '  RST2578P ': ", validar_codigo_medicamento("  RST2578P "))  # True
    print("VÁLIDO - 'ouRS56': ", validar_codigo_medicamento("ouRS56"))  # True
    print("INVÁLIDO -  'RTX 456' (Espacio central): ", validar_codigo_medicamento("RTX 456"))  # False
    print("INVÁLIDO -  ' ' (Vacio): ", validar_codigo_medicamento(" "))  # False
    print("INVÁLIDO -  'as3'(Muy corto): ", validar_codigo_medicamento("as3"))  # False
    print("INVÁLIDO -  'UEYDMWM34675'(Muy largo): ", validar_codigo_medicamento("UEYDMWM34675"))  # False
    print("INVÁLIDO -  'WES@546'(Caracteres especiales): ", validar_codigo_medicamento("WES@546"))  # False
    
    # Funcion 2: validar_nombre_medicamento
    print("\nvalidar_nombre_medicamento:")
    print("VÁLIDO - 'Ibuprofeno 600mg': ", validar_nombre_medicamento("Ibuprofeno 600mg"))  # True
    print("VÁLIDO - '  Omeprazol  ': ", validar_nombre_medicamento("  Omeprazol  "))  # True
    print("INVÁLIDO - '  '(Vacio): ", validar_nombre_medicamento("  "))  # False

    # Funcion 3: validar_laboratorio_fabricante
    print("\nvalidar_laboratorio_fabricante:")
    print("VÁLIDO - 'Roemmers': ", validar_laboratorio_fabricante("Roemmers")) # True
    print("VÁLIDO - 'ISA  ': ", validar_laboratorio_fabricante("ISA  ")) # True
    print("INVÁLIDO - '  '(Vacio): ", validar_laboratorio_fabricante("  ")) # False

    # Funcion 4: validar_entero_positivo
    print("\nvalidar_entero_positivo:")
    print("VÁLIDO - '12': ", validar_entero_positivo("12")) # True
    print("VÁLIDO - ' 6732': ", validar_entero_positivo(" 6732")) # True
    print("INVÁLIDO - '56.8'(Decimal): ", validar_entero_positivo("56.8")) # False
    print("INVÁLIDO - '43,9'(Coma): ", validar_entero_positivo("43,9")) # False
    print("INVÁLIDO - '-78'(Negativo): ", validar_entero_positivo("-78")) # False

    # Funcion 5: validar_fecha_vencimiento
    print("\nvalidar_fecha_vencimiento: ")
    print("VÁLIDO - '12/09/2034': ", validar_fecha_vencimiento("12/09/2034"))  # True
    print("VÁLIDO - '07/12/2012': ", validar_fecha_vencimiento("07/12/2012"))  # True
    print("VÁLIDO - '2/2/2012': ", validar_fecha_vencimiento("2/2/2012"))  # True
    print("INVÁLIDO - ''(Vacio): ", validar_fecha_vencimiento(""))  # False
    print("INVÁLIDO - '//'(Barras): ", validar_fecha_vencimiento("//")) # False
    print("INVÁLIDO - '32/1/2052'(dia no valido): ", validar_fecha_vencimiento("32/1/2052"))  # False
    print("INVÁLIDO - '32/1/2052'(vacio): ", validar_fecha_vencimiento("32/1/2052"))  # False
    print("INVÁLIDO - '12-1-2018'(guiones): ", validar_fecha_vencimiento("12-1-2018"))  # False
    print("INVÁLIDO - '12/01'(sin año): ", validar_fecha_vencimiento("12/01")) # False
    print("INVÁLIDO - '12/12/27'(año 2 dígitos): ", validar_fecha_vencimiento("12/12/27"))  # False - NUEVO
    print("INVÁLIDO - '12/12/2026a'(año con letra): ", validar_fecha_vencimiento("12/12/2026a"))  # False - NUEVO

    # Funcion 6: validar_precio
    print("\nvalidar_precio:")
    print("VÁLIDO - '674': ", validar_precio("674"))  # True
    print("VÁLIDO - '3980  ': ", validar_precio("3980  "))  # True
    print("VÁLIDO - '34.65': ", validar_precio("34.65"))  # True
    print("INVÁLIDO - ' '(Vacio): ", validar_precio(" "))  # False
    print("INVÁLIDO - 'noventa'(Texto): ", validar_precio("noventa"))  # False
    print("INVÁLIDO - '23.65.8':(mas puntos) ", validar_precio("23.65.8"))  # False
    print("INVÁLIDO - '.'(Solo un punto): ", validar_precio("."))  # False
    print("INVÁLIDO - '-34.8'(Negativo): ", validar_precio("-34.8"))  # False

    # Funcion 7:validar_cobertura
    print("\nvalidar_cobertura:")
    print("VÁLIDO - 'Con cobertura': ", validar_cobertura("Con cobertura")) # True
    print("VÁLIDO - 'Sin cobertura  ': ", validar_cobertura("Sin cobertura  ")) # True
    print("VÁLIDO - 'CoN cobeRtuRa': ", validar_cobertura("CoN cobeRtuRa")) # True
    print("INVÁLIDO - ' '(Vacio): ", validar_cobertura(" ")) # False
    print("INVÁLIDO - 'Con'(Vacio): ", validar_cobertura("Con")) # False

    # Funcion 8: validar_codigo_unico
    print("\nvalidar_codigo_unico:")
    matriz_prueba = [
        ["MED001", "Ibuprofeno", "Roemmers", 2500, 50, "Con cobertura", "02/12/2026"],
        ["FAR125", "Amoxicilina", "Bagó", 1800, 120, "Sin cobertura", "20/07/2026"],
    ]
    print("VÁLIDO - 'MED999' (no existe): ", validar_codigo_unico("MED999", matriz_prueba))  # True
    print("INVÁLIDO - 'MED001' (ya existe): ", validar_codigo_unico("MED001", matriz_prueba))  # False

    # PRUEBAS FASE 2
    print("\n=== PRUEBAS FASE 2 ===")
    
    # validar_laboratorio_duplicado
    print("\nvalidar_laboratorio_duplicado:")
    laboratorios = ["Roemmers", "Bagó", "Pfizer"]
    print("VÁLIDO - 'ISA' (no existe): ", validar_laboratorio_duplicado("ISA", laboratorios))  # False
    print("INVÁLIDO - 'Roemmers' (existe): ", validar_laboratorio_duplicado("Roemmers", laboratorios))  # True
    
    # validar_stock_suficiente
    print("\nvalidar_stock_suficiente:")
    medicamento = ["MED001", "Ibuprofeno", "Roemmers", 2500, 50, "Con cobertura", "02/12/2026"]
    print("VÁLIDO - Stock 50, cantidad 30: ", validar_stock_suficiente(medicamento, 30))  # True
    print("INVÁLIDO - Stock 50, cantidad 60: ", validar_stock_suficiente(medicamento, 60))  # False
    
    # validar_monto_efectivo
    print("\nvalidar_monto_efectivo:")
    print("VÁLIDO - Monto 1000, total 800: ", validar_monto_efectivo(1000, 800))  # True
    print("INVÁLIDO - Monto 500, total 800: ", validar_monto_efectivo(500, 800))  # False

    # FASE 2 - seleccionar_laboratorio (Nueva función)
    print("\n" + "="*70)
    print("FASE 2 - VALIDACIONES NUEVAS (Lucas Alegre)")
    print("="*70)
    print("\nseleccionar_laboratorio:")
    print("NOTA: Esta función requiere entrada interactiva del usuario.")
    print("Pruebas de validación lógica:")
    
    # Prueba con lista de laboratorios
    laboratorios_prueba = ["Roemmers", "Bagó", "Pfizer", "Roche", "ISA"]
    print(f"\nLaboratorios disponibles: {laboratorios_prueba}")
    print("\nCasos de prueba esperados:")
    print("  ✓ Seleccionar '1' → Retorna 'Roemmers'")
    print("  ✓ Seleccionar '3' → Retorna 'Pfizer'")
    print("  ✓ Seleccionar '5' → Retorna 'ISA'")
    print("  ✓ Seleccionar '-2' → Rechaza (negativo)")
    print("  ✓ Seleccionar '10' → Rechaza (fuera de rango)")
    print("  ✓ Seleccionar 'abc' → Rechaza (no es número)")
    print("  ✓ Seleccionar '-1' → Retorna None (salir)")
    print("  ✓ Seleccionar '' (vacío) → Rechaza")
    print("  ✓ Seleccionar '1.5' → Rechaza (decimal)")
    print("  ✓ Seleccionar '!@#$' → Rechaza (símbolos)")
    
    print("\nEjemplo de ejecución interactiva (comentado para no bloquear):")
    print("# resultado = seleccionar_laboratorio(laboratorios_prueba)")
    print("# if resultado:")
    print("#     print(f'Laboratorio seleccionado: {resultado}')")
    print("# else:")
    print("#     print('Salió sin seleccionar')")