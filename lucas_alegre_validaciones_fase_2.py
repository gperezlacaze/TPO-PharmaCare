# ============================================================
# MODULO: lucas_alegre_validaciones_fase_2.py
# Autor: Lucas Alegre
# Descripcion: Validaciones de Fase 2 (RF04, RF05, RF07, RF08)
# ============================================================

#Paso 1: Validar nombre de laboratorio

def validar_nombre_laboratorio(nombre):
    """
    Valida que el nombre del laboratorio no sea None ni este vacio
    Entrada: nombre (string)
    Salida: True si es valido, False si no
    """

    return nombre != None and nombre.strip() !=""

#Paso 2: Validar laboratorio duplicado

def validar_laboratorio_duplicado(nombre, lista_laboratorios):
    """
    Valida si el laboratorio ya existe en la lista (duplicado)
    Entrada: nombre (string), lista_laboratorios (lista de strings)
    Salida: True si ya existe (duplicado), False si no existe (no duplicado)
    """

    for lab in lista_laboratorios:
        if nombre.lower() == lab.lower():
            return True
    return False
    
#Paso 3: Validar si existe laboratorio

def validar_laboratorio_existe(nombre, lista_laboratorios):
    """
    Valida si el laboratorio existe en la lista
    Entrada: nombre (string), lista_laboratorios (lista de strings)
    Salida: True si existe, False si no existe 
    """

    for lab in lista_laboratorios: 
        if nombre.lower() == lab.lower():
            return True
    return False

#Paso 4: Validar stock minimo

def validar_stock_minimo(stock):
    """
    Valida que el stock sea mayor a 0
    Entrada: stock (int)
    Salida: True si es valido, False si no
    """
    return stock > 0

#Paso 5: Validar cantidad positiva de medicamentos

def validar_cantidad_positiva(cantidad):
    """
    Valida que la cantidad sea mayor a 0
    Entrada: cantidad (int)
    Salida: True si es valido, False si no
    """
    return cantidad > 0

#Paso 6: Validar stock suficiente

def validar_stock_suficiente(medicamento, cantidad):
    """
    Valida que el stock sea suficiente para la cantidad solicitada
    Entrada: medicamento (lista, fila de la matriz), cantidad (int)
    Salida: True si el stock es suficiente, False si no es suficiente
    """
    return medicamento[4] >= cantidad

#Paso 7: Validar monto efectivo

def validar_monto_efectivo(monto, total):
    """
    Valida que el monto efectivo sea mayor o igual al total a pagar
    Entrada: monto (float), total (float)
    Salida: True si el monto es suficiente, False si no es suficiente
    """
    return monto >= total

if __name__ == "__main__":
    print("=== Prueba de validaciones ===")
    print(validar_nombre_laboratorio("Roemmers"))
    print(validar_nombre_laboratorio(""))