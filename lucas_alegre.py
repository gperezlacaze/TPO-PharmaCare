# ============================================================
# MODULO: lucas_alegre.py (matriz_medicamentos.py)
# Autor: Lucas Alegre
# Descripcion: Modulo para crear, mostrar y mostrar con colores la matriz de medicamentos
# ============================================================

# CÓDIGOS DE COLOR ANSI
ROJO = '\033[91m'
VIOLETA = '\033[35m'
CELESTE = '\033[96m'
RESET = '\033[0m'


def crear_matriz_inicial():
    """
    Crea una matriz con 5 medicamentos
    Entrada: ninguna
    Salida: matriz (lista de listas) con los medicamentos iniciales
    """

    # Cada fila sigue el orden:
    # [codigo, nombre, laboratorio, precio, stock, cobertura, fecha_vencimiento]
    matriz_medicamentos = [
        # Medicamento 1
        ["MED001", "Ibuprofeno 600mg",   "Roemmers", 2500.00,  50,  "Con cobertura", "02/12/2026"],
        # Medicamento 2
        ["FAR125", "Amoxicilina 500mg",  "Bagó",     1800.00, 120,  "Sin cobertura",  "20/07/2026"],
        # Medicamento 3
        ["LAB789", "Omeprazol 20mg",     "Pfizer",    750.00,   8,  "Con cobertura", "05/06/2027"],
        # Medicamento 4
        ["FAR140", "Paracetamol 500mg",  "ISA",      1200.00, 200,  "Sin cobertura", "29/08/2027"],
        # Medicamento 5
        ["LAB456", "Metformina 850mg",   "Roche",    5000.00,  30,  "Con cobertura",  "04/08/2026"],
    ]

    return matriz_medicamentos


def mostrar_matriz(matriz):
    """
    Muestra la matriz de medicamentos en formato de tabla.
    Entrada: matriz (lista de listas)
    Salida: imprime la tabla en pantalla
    """

    # Encabezados con colores
    print("\n" + f"{CELESTE}" + "=" * 115 + f"{RESET}")
    print(f"{VIOLETA}{'Codigo':<12}{'Nombre':<30}{'Laboratorio':<20}{'Precio':<12}{'Stock':<10}{'Cobertura':<15}{'Fecha de Vencimiento':<20}{RESET}")
    print(f"{CELESTE}" + "=" * 115 + f"{RESET}")

    # Filas
    i = 0
    while i < len(matriz):
        fila = matriz[i]
        print(f"{fila[0]:<12}{fila[1]:<30}{fila[2]:<20}{fila[3]:<12.2f}{fila[4]:<10}{fila[5]:<15}{fila[6]:<20}")
        i = i + 1

    print(f"{CELESTE}" + "=" * 115 + f"{RESET}\n")


def mostrar_matriz_con_colores(matriz):
    """
    Muestra la matriz de medicamentos en formato de tabla.
    Obtiene stock_minimo dinámicamente y muestra el stock en ROJO si está por debajo.
    Entrada: matriz (lista de listas)
    Salida: imprime la tabla en pantalla con colores (RF03)
    """
    # Importar dinámicamente para evitar ciclos
    from lucas_bassi_menu_2 import obtener_stock_minimo
    
    stock_minimo = obtener_stock_minimo()

    # Encabezados con colores
    print("\n" + f"{CELESTE}" + "=" * 115 + f"{RESET}")
    print(f"{VIOLETA}{'Codigo':<12}{'Nombre':<30}{'Laboratorio':<20}{'Precio':<12}{'Stock':<10}{'Cobertura':<15}{'Fecha de Vencimiento':<20}{RESET}")
    print(f"{CELESTE}" + "=" * 115 + f"{RESET}")

    # Filas
    i = 0
    while i < len(matriz):
        fila = matriz[i]
        stock = fila[4]
        
        # Colorear stock en ROJO si está por debajo del mínimo
        if stock_minimo is not None and stock < stock_minimo:
            stock_mostrar = f"{ROJO}{stock}{RESET}"
        else:
            stock_mostrar = str(stock)
        
        print(f"{fila[0]:<12}{fila[1]:<30}{fila[2]:<20}{fila[3]:<12.2f}{stock_mostrar:<10}{fila[5]:<15}{fila[6]:<20}")
        i = i + 1

    print(f"{CELESTE}" + "=" * 115 + f"{RESET}\n")


if __name__ == "__main__":
    # Prueba funcional del modulo
    matriz = crear_matriz_inicial()
    mostrar_matriz(matriz)
    
    # Prueba con colores (stock_minimo = 50)
    print("MATRIZ CON COLORES (stock_minimo = 50):")
    mostrar_matriz_con_colores(matriz, 50)