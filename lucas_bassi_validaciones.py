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
    if nombre.strip() == "":
        return False
    return True


def validar_codigo_medicamento(codigo):
    """Validar que el código tenga entre 4 y 10 caracteres alfanuméricos."""
    cantidad = len(codigo)
    if not (4 <= cantidad <= 10):
        return False
    if not codigo.isalnum():
        return False
    return True


def validar_laboratorio_fabricante(laboratorio):
    """Validar que el nombre del laboratorio no esté vacío."""
    if laboratorio.strip() == "":
        return False
    return True


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
    if cobertura == "Con cobertura" or cobertura == "Sin cobertura":
        return True
    return False


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


def ingresar_codigo():
    """Pedir y validar el código del medicamento."""
    codigo = input("Ingrese el código del medicamento: ").strip().upper()
    while not validar_codigo_medicamento(codigo):
        print("Código inválido: debe tener entre 4 y 10 caracteres "
              "alfanuméricos (sin espacios ni símbolos).")
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


    

