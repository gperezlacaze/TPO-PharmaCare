# MÓDULO: Menú principal
# Autor: Gonzalo Perez Lacaze
# Fecha: 05/06/2026
# Descripción: Funciones de menú para PharmaCare
from lucas_bassi_validaciones import (
    ingresar_codigo, ingresar_medicamento,
    ingresar_laboratorio, ingresar_precio,
    ingresar_stock, ingresar_cobertura, ingresar_dias_vencimiento
)


def mostrar_menu():
    '''Muestra el menú principal con las opciones disponibles'''
    print("==================================================")
    print("SISTEMA DE GESTIÓN: PHARMACARE CENTRAL")
    print("==================================================")
    print("1. Registrar nuevo producto")
    print("2. Eliminar medicamento")
    print("3. Buscar medicamento")
    print("4. Modificar stock o precio")
    print("5. Informe general")
    print("6. Salir")
    print("==================================================")
    opcion = validar_opcion(1, 6)
    print("Seleccione una opción (1-6) o presione 8 para salir:")


def alta_medicamentos(matriz):
    '''Permite el ingreso de nuevos medicamentos al sistema'''
    print("\n(Presione 8 en el menú principal para salir)\n")
    while True:
        codigo = ingresar_codigo()
        nombre = ingresar_medicamento()
        laboratorio = ingresar_laboratorio()
        precio = ingresar_precio()
        stock = ingresar_stock()
        cobertura = ingresar_cobertura()
        vencimiento = ingresar_dias_vencimiento()
        
        nueva_fila = [codigo, nombre, laboratorio, precio, stock, cobertura, vencimiento]
        matriz.append(nueva_fila)
        if not validar_confirmacion("¿Agregar otro? (si/no): "):
            break


def baja_medicamentos(matriz):
    '''Permite eliminar medicamentos con stock = 0'''
    print("\n(Presione 8 en el menú principal para salir)\n")   
    while True:
        busqueda = input("Ingrese código o nombre del producto: ")
        encontrado = False
        for fila in range(len(matriz)):
            if matriz[fila][0] == busqueda or matriz[fila][1] == busqueda:
                encontrado = True
                print(f"Medicamento encontrado: {matriz[fila][1]}")
                print(f"Stock: {matriz[fila][4]}")
            if matriz[fila][4] == 0:
                print("¿Desea Eliminarlo? (si/no)")
                if input("¿Desea eliminar? (si/no): ") == "si":
                    matriz.pop(fila)
                    print("Medicamento eliminado correctamente")
                else:
                    print("Operación cancelada")
            else:
                print("Error: No se puede eliminar, stock > 0")
                break
        if not encontrado:
            print("Medicamento no encontrado")
        if not validar_confirmacion("¿Eliminar otro? (si/no): "):
            break
   

def buscar_medicamento(matriz):
    ''''''
    print("\n¿Cómo desea buscar?")
    print("1. Por código (búsqueda exacta)")
    print("2. Por nombre (búsqueda parcial)")
    tipo = input("Seleccione (1 o 2): ")

    while tipo not in ["1", "2"]:
        print("Opción inválida. Intente nuevamente.")
        tipo = input("Seleccione (1 o 2): ")
    
    if tipo == "1":  # CÓDIGO
        busqueda_codigo = input("Ingrese el código: ").strip().upper()
        for fila in range(len(matriz)):
            if matriz[fila][0] == busqueda_codigo:
                # Mostrar completo
                print(f"\nMedicamento encontrado:")
                print(f"{matriz[fila][0]:<12} | {matriz[fila][1]:<30} | {matriz[fila][2]:<20} | {matriz[fila][3]:<12.2f} | {matriz[fila][4]:<10} | {matriz[fila][5]:<15} | {matriz[fila][6]:<12}\n")
                return fila  # ← Retorna INDEX
        else:
            print("\nMedicamento no encontrado. Intente de nuevo o deje vacío para volver al menú.")
            respuesta = input("Ingrese el código (o Enter para volver): ").strip().upper()
            if respuesta == "":
                return None

    elif tipo == "2":
        busqueda_nombre = input("Ingrese el nombre del producto (o parte de él): ").strip().lower()
        resultados = []

        for fila in range(len(matriz)):
            if busqueda_nombre in matriz[fila][1].lower():
                resultados.append(fila)
        
        if resultados:
            print(f"\nSe encontraron {len(resultados)} medicamento(s):\n")
            
            i = 0
            while i < len(resultados):
                fila = resultados[i]
                posicion = i + 1
                print(f"[{posicion}] {matriz[fila][0]:<12} | {matriz[fila][1]:<30} | {matriz[fila][2]:<20} | {matriz[fila][3]:<12.2f} | {matriz[fila][4]:<10} | {matriz[fila][5]:<15} | {matriz[fila][6]:<12}")
                i = i + 1
            
            return resultados  # Retorna lista de índices
        else:
            print("\nMedicamento no encontrado")
            respuesta = input("Ingrese el código (o Enter para volver): ").strip().upper()
            if respuesta == "":
                return None
 

def modificar_stock_precio(matriz):
    '''Modifica el stock, precio o ambos a la vez de un medicamento ya existente'''
    while True:
        busqueda = input("Ingrese código o nombre del producto: ")
        fila = 0
        while fila < len(matriz):
            if matriz[fila][0] == busqueda or matriz[fila][1] == busqueda:
                # Mostrar medicamento encontrado
                print(f"[Fila {fila}] {matriz[fila][1]}")
                print(f"Stock actual: {matriz[fila][4]} | Precio actual: {matriz[fila][3]}")
                # MINI MENU AL ENCONTRAR EL MEDICAMENTO BUSCADO
                print("¿Qué desea modificar?")
                print("1. Stock")
                print("2. Precio")
                print("3. Ambos")
                opcion_mod = int(input("Seleccione (1-3): "))
                while opcion_mod < 1 or opcion_mod > 3:
                    print("ERROR. Ingrese una opción válida")
                    opcion_mod = int(input("Seleccione (1-3): "))
                if opcion_mod == 1:
                    nuevo_stock = ingresar_stock()
                    matriz[fila][4] = nuevo_stock
                    print("Stock modificado")
                    print(f"[Fila {fila}] {matriz[fila][1]} | Stock: {matriz[fila][4]} ")
                elif opcion_mod == 2:
                    nuevo_precio = ingresar_precio()
                    matriz[fila][3] = nuevo_precio
                    print("Precio modificado")
                    print(f"[Fila {fila}] {matriz[fila][1]} | Precio actual: {matriz[fila][3]}")
                elif opcion_mod == 3:
                    nuevo_stock = ingresar_stock()
                    matriz[fila][4] = nuevo_stock
                    nuevo_precio = ingresar_precio()
                    matriz[fila][3] = nuevo_precio
                    print("Los cambios han sido efectuados")
                    print(f"[Fila {fila}] {matriz[fila][1]} | Precio actual: {matriz[fila][3]} | Stock: {matriz[fila][4]} ")                        
                fila = len(matriz)
            else:
                fila += 1
                if fila == len(matriz):
                    print("Medicamento no encontrado")
        
        if not validar_confirmacion("¿Modificar otro? (si/no): "):
            break    


def informe_general(matriz):
    '''Muestra la matriz ordenada por vencimiento'''
    print("\n(Presione 8 en el menú principal para salir)\n")
    # COPIO LA MATRIZ PARA NO MODIFICAR LA ORIGINAL
    matriz_ordenada = [fila[:] for fila in matriz]
    # ORDENO POR VENCIMIENTO
    for i in range(len(matriz_ordenada) - 1):
        for j in range(len(matriz_ordenada) - 1 - i):
            if matriz_ordenada[j][6] > matriz_ordenada[j + 1][6]:
                aux = matriz_ordenada[j]  # ← Fila completa (7 datos)
                matriz_ordenada[j] = matriz_ordenada[j+1]
                matriz_ordenada[j+1] = aux
            elif matriz_ordenada[j][6] == matriz_ordenada[j + 1][6]:
                if matriz_ordenada[j][1] > matriz_ordenada[j + 1][1]:
                    aux = matriz_ordenada[j]
                    matriz_ordenada[j] = matriz_ordenada[j+1]
                    matriz_ordenada[j+1] = aux
    # MOSTRAR MATRIZ ORDENADA
    print("\n" + "="*120)
    print("INFORME GENERAL - MEDICAMENTOS ORDENADOS POR VENCIMIENTO (MENOR A MAYOR)")
    print("="*120)
    print(f"{'Código':<12} {'Nombre':<30} {'Laboratorio':<20} {'Precio':<12} {'Stock':<10} {'Cobertura':<15} {'Vencimiento':<12}")                
    print("-"*120)
    for fila in range(len(matriz_ordenada)):
        print(f"{matriz_ordenada[fila][0]:<12} {matriz_ordenada[fila][1]:<30} {matriz_ordenada[fila][2]:<20} {matriz_ordenada[fila][3]:<12} {matriz_ordenada[fila][4]:<10} {matriz_ordenada[fila][5]:<15} {matriz_ordenada[fila][6]:<12}")
    print("="*120)


def salir():
    '''Termina el programa'''
    print("\n" + "="*60)
    print("¡Gracias por usar PharmaCare Central!")
    print("Hasta luego.")
    print("="*60)   

