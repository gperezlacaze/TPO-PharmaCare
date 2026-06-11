# ============================================================
# Módulo de Validaciones e Ingreso de Datos
# Autor: Lucas Bassi
# Proyecto: PharmaCare Central
# ============================================================

# ------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN
# (puras: reciben un dato y devuelven True/False, sin imprimir)
# ------------------------------------------------------------


def validar_nombre_medicamento(nombre):
    """Validar que el nombre del medicamento no esté vacío."""
    return nombre.strip() != ""


def validar_codigo_medicamento(codigo):
    """Validar que el código tenga entre 4 y 10 caracteres alfanuméricos"""
    codigo = codigo.strip()
    cantidad = len(codigo)
    if not (4 <= cantidad <= 10):
        return False
    if not codigo.isalnum():
        return False
    return True


def validar_codigo_unico(codigo, matriz):
    """ Validar que el codigo no exista en la matriz"""
    for f in range(len(matriz)):
        if matriz[f][0] == codigo:
            return False
    return True


def validar_laboratorio_fabricante(laboratorio):
    """Validar que el nombre del laboratorio no esté vacío."""
    return laboratorio.strip() != ""


def validar_entero_positivo(texto):
    """Validar que el texto represente un número entero positivo (> 0)."""
    texto = texto.strip()
    if not texto.isdigit():
        return False
    if int(texto) <= 0:
        return False
    return True


def validar_precio(texto):
    """Validar que el texto represente un número decimal positivo (> 0)."""
    texto = texto.strip()
    if texto == "":
        return False
    # Como máximo puede haber un punto decimal
    if texto.count(".") > 1:
        return False
    # Saco un único punto y verifico que lo demás sean dígitos
    sin_punto = texto.replace(".", "", 1)
    if sin_punto == "":
        return False
    if not sin_punto.isdigit():
        return False
    # El formato ya es numérico válido: ahora exijo que sea mayor a cero
    if float(texto) <= 0:
        return False
    return True


def validar_cobertura(cobertura):
    """Validar que la cobertura sea 'Con cobertura' o 'Sin cobertura'."""
    cobertura = cobertura.strip().capitalize()
    return cobertura in ["Con cobertura", "Sin cobertura" ]


# ------------------------------------------------------------
# FUNCIONES DE INGRESO
# (interactúan con el usuario y reutilizan las validaciones)
# ------------------------------------------------------------


def ingresar_medicamento():
    """Pedir y validar el nombre del medicamento."""
    nombre = input("Ingrese el nombre del medicamento: ").strip().capitalize()
    while not validar_nombre_medicamento(nombre):
        print("El nombre no puede estar vacío. Intente nuevamente.")
        nombre = input("Ingrese el nombre del medicamento: ").strip().capitalize()
    return nombre


def ingresar_codigo(matriz):
    """Pedir y validar el código del medicamento."""
    codigo = input("Ingrese el código del medicamento: ").upper()
    while not validar_codigo_medicamento(codigo) or not validar_codigo_unico(codigo, matriz):
        if not validar_codigo_medicamento(codigo):
            print("Código inválido: debe tener entre 4 y 10 caracteres "
            "alfanuméricos (sin espacios ni símbolos).")
        else:
            print("Codigo ya existente en la matriz")
        codigo = input("Ingrese el código del medicamento: ").strip().upper()
    return codigo


def ingresar_laboratorio():
    """Pedir y validar el nombre del laboratorio."""
    laboratorio = input("Ingrese el nombre del laboratorio: ").strip()
    while not validar_laboratorio_fabricante(laboratorio):
        print("El nombre del laboratorio no puede estar vacío. Intente nuevamente.")
        laboratorio = input("Ingrese el nombre del laboratorio: ").strip()
    return laboratorio


def ingresar_precio():
    """Pedir y validar el precio unitario del medicamento."""
    texto = input("Ingrese el precio del medicamento: ")
    while not validar_precio(texto):
        print("Precio inválido: debe ser un número positivo mayor a cero (ej: 2500.50).")
        texto = input("Ingrese el precio del medicamento: ")
    return float(texto)


def ingresar_stock():
    """Pedir y validar el stock disponible del medicamento."""
    texto = input("Ingrese el stock del medicamento: ")
    while not validar_entero_positivo(texto):
        print("Stock inválido: debe ser un número entero positivo (mayor a cero).")
        texto = input("Ingrese el stock del medicamento: ")
    return int(texto)


def ingresar_dias_vencimiento():
    """Pedir y validar los días restantes para el vencimiento."""
    texto = input("Ingrese los días para el vencimiento: ")
    while not validar_entero_positivo(texto):
        print("Valor inválido: debe ser un número entero positivo (mayor a cero).")
        texto = input("Ingrese los días para el vencimiento: ")
    return int(texto)


def ingresar_cobertura():
    """Pedir y validar la cobertura médica del medicamento."""
    cobertura = input("Ingrese la cobertura (Con cobertura / Sin cobertura): ").strip().capitalize()
    while not validar_cobertura(cobertura):
        print("Cobertura inválida: debe ser 'Con cobertura' o 'Sin cobertura'.")
        cobertura = input("Ingrese la cobertura (Con cobertura / Sin cobertura): ").strip().capitalize()
    return cobertura


# ------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN DE MENÚ
# (interactúan con el usuario para opciones y confirmaciones)
# ------------------------------------------------------------


def validar_opcion(desde, hasta):
    '''Esta funcion es auxiliar y valida que el usuario ingrese una opcion valida del menu'''
    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit():
        print("La opción debe ser un número.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)
    while (opcion < desde or opcion > hasta) and opcion != 8:
        print("La opción seleccionada no es válida") 
        opcion = input("Seleccione una opción: ")
        while not opcion.isdigit():
            print("La opción debe ser un número.")
            opcion = input("Seleccione una opción: ")
        opcion = int(opcion)
    return opcion


def validar_confirmacion(pregunta):
    """Valida que la respuesta sea 'si' o 'no' (case-insensitive)"""
    respuesta = input(pregunta).strip().lower()
    while respuesta not in ["si", "no"]:
        print("Respuesta inválida. Ingrese 'si' o 'no':")
        respuesta = input(pregunta).strip().lower()
    return respuesta == "si"


if __name__ == "__main__":

    # Funcion 1: validar_codigo_medicamento
    print("\nvalidar_codigo_medicamento:")
    print("VÁLIDO - 'MED3452': ", validar_codigo_medicamento("Med3452")) # True
    print("VÁLIDO - '  RST2578P ': ", validar_codigo_medicamento("  RST2578P ")) # True
    print("VÁLIDO - 'ouRS56': ", validar_codigo_medicamento("ouRS56")) # True
    print("INVÁLIDO -  'RTX 456' (Espacio central): ", validar_codigo_medicamento("RTX 456")) # False
    print("INVÁLIDO -  ' ' (Vacio): ", validar_codigo_medicamento(" ")) # False
    print("INVÁLIDO -  'as3'(Muy corto): ", validar_codigo_medicamento("as3")) # False
    print("INVÁLIDO -  'UEYDMWM34675'(Muy largo): ", validar_codigo_medicamento("UEYDMWM34675")) # False
    print("INVÁLIDO -  'WES@546'(Caracteres especiales): ", validar_codigo_medicamento("WES@546")) # False
    
    # Funcion 2: validar_nombre_medicamento
    print("\nvalidar_nombre_medicamento:")
    print("VÁLIDO - 'Ibuprofeno 600mg': ", validar_nombre_medicamento("Ibuprofeno 600mg")) # True
    print("VÁLIDO - '  Omeprazol  ': ", validar_nombre_medicamento("  Omeprazol  ")) # True
    print("INVÁLIDO - '  '(Vacio): ", validar_nombre_medicamento("  ")) # False

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

    # Funcion 5: validar_precio
    print("\nvalidar_precio:")
    print("VÁLIDO - '674': ", validar_precio("674")) # True
    print("VÁLIDO - '3980  ': ", validar_precio("3980  ")) # True
    print("VÁLIDO - '34.65': ", validar_precio("34.65")) # True
    print("INVÁLIDO - ' '(Vacio): ", validar_precio(" ")) # False
    print("INVÁLIDO - 'noventa'(Texto): ", validar_precio("noventa")) # False
    print("INVÁLIDO - '23.65.8':(mas puntos) ", validar_precio("23.65.8")) # False
    print("INVÁLIDO - '.'(Solo un punto): ", validar_precio(".")) # False
    print("INVÁLIDO - '-34.8'(Negativo): ", validar_precio("-34.8")) # False

    # Funcion 6:validar_cobertura
    print("\nvalidar_cobertura:")
    print("VÁLIDO - 'Con cobertura': ", validar_cobertura("Con cobertura")) # True
    print("VÁLIDO - 'Sin cobertura  ': ", validar_cobertura("Sin cobertura  ")) # True
    print("VÁLIDO - 'CoN cobeRtuRa': ", validar_cobertura("CoN cobeRtuRa")) # True
    print("INVÁLIDO - ' '(Vacio): ", validar_cobertura(" ")) # False
    print("INVÁLIDO - 'Con'(Vacio): ", validar_cobertura("Con")) # False

    # Funcion 7: validar_codigo_unico
    print("\nvalidar_codigo_unico:")
    matriz_prueba = [
        ["MED001", "Ibuprofeno 600mg"],
        ["FAR125", "Amoxicilina 500mg"],
        ["LAB789", "Omeprazol 20mg"]] 
    
    print("VÁLIDO - 'LAB999' (No existe): ", validar_codigo_unico("LAB999", matriz_prueba)) # True
    print("INVÁLIDO - 'FAR125' (Existe): ", validar_codigo_unico("FAR125", matriz_prueba)) # False
   



    


    

    
    


    
