# ============================================================
# MODULO: matriz_medicamentos.py
# Autores: Lucas Alegre
# Descripcion: Modulo para crear y mostrar la matriz de medicamentos
# ============================================================


def crear_matriz_inicial():
    """
    Crea una matriz con 5 medicamentos
    Entrada: ninguna
    Salida: matriz (lista de listas) con los medicamentos iniciales
    """

    # Cada fila sigue el orden:
    # [codigo, nombre, laboratorio, precio, stock, cobertura, dias_vencimiento]
    matriz_medicamentos = [
        # Medicamento 1
        ["MED001", "Ibuprofeno 600mg",   "Roemmers", 2500.00,  50,  "Con cobertura", 180],
        # Medicamento 2
        ["FAR125", "Amoxicilina 500mg",  "Bagó",     1800.00, 120,  "Sin cobertura",  45],
        # Medicamento 3
        ["LAB789", "Omeprazol 20mg",     "Pfizer",    750.00,   8,  "Con cobertura", 365],
        # Medicamento 4
        ["FAR140", "Paracetamol 500mg",  "ISA",      1200.00, 200,  "Sin cobertura", 450],
        # Medicamento 5
        ["LAB456", "Metformina 850mg",   "Roche",    5000.00,  30,  "Con cobertura",  60],
    ]

    return matriz_medicamentos


def mostrar_matriz(matriz):
    """
    Muestra la matriz de medicamentos en formato de tabla.
    Entrada: matriz (lista de listas)
    Salida: imprime la tabla en pantalla
    """

    # Encabezados
    print("\n" + "=" * 100)
    print(f"{'Codigo':<12} {'Nombre':<25} {'Laboratorio':<15} {'Precio':<12} {'Stock':<8} {'Cobertura':<15} {'Vencimiento':<10}")
    print("=" * 100)

    # Filas
    i = 0
    while i < len(matriz):
        fila = matriz[i]
        print(f"{fila[0]:<12} {fila[1]:<25} {fila[2]:<15} {fila[3]:<12.2f} {fila[4]:<8} {fila[5]:<15} {fila[6]:<10}")
        i = i + 1

    print("=" * 100 + "\n")


# Prueba - eliminar después
if __name__ == "__main__":
    matriz = crear_matriz_inicial()
    mostrar_matriz(matriz)