# MÓDULO: Menú principal
# Autor: Gonzalo Perez Lacaze
# Fecha: 05/06/2026
# Descripción: Funciones de menú para PharmaCare
from lucas_bassi_validaciones import (
    ingresar_codigo, ingresar_medicamento,
    ingresar_laboratorio, ingresar_precio,
    ingresar_stock, ingresar_cobertura, ingresar_fecha_vencimiento,
    validar_confirmacion
)
from lucas_alegre import mostrar_matriz, crear_matriz_inicial


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
    print("6. Gestiones")
    print("==================================================")
    print("Seleccione una opción (1-6) o presione 8 para salir:")


def alta_medicamentos(matriz, laboratorios):
    '''Permite el ingreso de nuevos medicamentos al sistema'''
    if len(laboratorios) == 0:
        print("No se puede agregar sin laboratorios registrados.")
        return None
    
    print("\n(Presione 8 en el menú principal para salir)\n")
    while True:
        codigo = ingresar_codigo(matriz)
        nombre = ingresar_medicamento()
        laboratorio = ingresar_laboratorio(laboratorios)
        precio = ingresar_precio()
        stock = ingresar_stock()
        cobertura = ingresar_cobertura()
        vencimiento = ingresar_fecha_vencimiento()
        
        nueva_fila = [codigo, nombre, laboratorio, precio, stock, cobertura, vencimiento]
        matriz.append(nueva_fila)
        if not validar_confirmacion("¿Agregar otro? (si/no): "):
            break


def baja_medicamentos(matriz):
    '''Permite eliminar medicamentos con stock = 0'''
    print("\n(Presione 8 en el menú principal para salir)\n")
    
    print("¿Cómo desea buscar el medicamento?")
    print("1. Por código (búsqueda exacta)")
    print("2. Por nombre (búsqueda parcial)")
    tipo = input("Seleccione (1 o 2): ")

    while tipo not in ["1", "2"]:
        print("Opción inválida. Intente nuevamente.")
        tipo = input("Seleccione (1 o 2): ")
    
    if tipo == "1":
        busqueda_codigo = input("Ingrese el código: ").strip().upper()
        while busqueda_codigo != "":
            resultado = buscar_por_codigo(matriz, busqueda_codigo)
            if procesar_eliminacion(matriz, resultado):
                resultado = buscar_por_codigo(matriz, input("Ingrese el código: ").strip().upper())
            else:
                busqueda_codigo = ""
    
    elif tipo == "2":
        busqueda_nombre = input("Ingrese el nombre del producto (o parte de él): ").strip().lower()
        while busqueda_nombre != "":
            resultado = buscar_por_nombre(matriz, busqueda_nombre)
            if procesar_eliminacion(matriz, resultado):
                busqueda_nombre = input("Ingrese el nombre del producto (o parte de él): ").strip().lower()
            else:
                busqueda_nombre = ""


def procesar_eliminacion(matriz, resultado):
    '''Procesa el filtrado, selección y eliminación de medicamentos con stock = 0'''
    if resultado == -1:
        return False
    
    medicamentos_a_eliminar = []
    i = 0
    while i < len(resultado):                         
        fila = resultado[i]        
        if matriz[fila][4] == 0: 
            medicamentos_a_eliminar.append(fila)
        i = i + 1
    
    if len(medicamentos_a_eliminar) == 0:
        print("Ningún medicamento encontrado tiene stock = 0")
    elif len(medicamentos_a_eliminar) == 1:
        fila = medicamentos_a_eliminar[0]
        print(f"\nMedicamento a eliminar: {matriz[fila][1]}")
    else:
        print(f"\nSe encontraron {len(medicamentos_a_eliminar)} medicamento(s) con stock = 0:\n")
        mostrar_posiciones_resultados(matriz, medicamentos_a_eliminar)
        eleccion = input(f"¿Cuál desea eliminar? (1-{len(medicamentos_a_eliminar)}): ")
        while not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(medicamentos_a_eliminar):
            print("Selección inválida")
            eleccion = input(f"Ingrese el número (1-{len(medicamentos_a_eliminar)}): ")
        fila = medicamentos_a_eliminar[int(eleccion) - 1]

    if validar_confirmacion(f"¿Eliminar {matriz[fila][1]}? (si/no): "):
        print(f"Eliminando: {matriz[fila][0]:<12} | {matriz[fila][1]:<30} | {matriz[fila][2]:<20} | {matriz[fila][3]:<12.2f} | {matriz[fila][4]:<10} | {matriz[fila][5]:<15} | {matriz[fila][6]:<12}")
        matriz.pop(fila)
        print("Medicamento eliminado correctamente")
        return validar_confirmacion("¿Eliminar otro?")
    else:
        print("Operación cancelada")
        return validar_confirmacion("¿Eliminar otro?")


def mostrar_medicamento(matriz):
    '''La funcion busca por codigo (resultado unico) o por nombre (resultados multiples posibles) y muestra los resultados con posiciones'''
    print("\n¿Cómo desea buscar?")
    print("1. Por código (búsqueda exacta)")
    print("2. Por nombre (búsqueda parcial)")
    tipo = input("Seleccione (1 o 2): ")

    while tipo not in ["1", "2"]:
        print("Opción inválida. Intente nuevamente.")
        tipo = input("Seleccione (1 o 2): ")
        
    if tipo == "1":  # CÓDIGO
        busqueda_codigo = input("Ingrese el código: ").strip().upper()
        while busqueda_codigo != "":
            resultado = buscar_por_codigo(matriz, busqueda_codigo)
            
            if resultado != -1:
                print(f"\nMedicamento encontrado:")
                fila = resultado[0]
                print(f"{matriz[fila][0]:<12} | {matriz[fila][1]:<30} | {matriz[fila][2]:<20} | {matriz[fila][3]:<12.2f} | {matriz[fila][4]:<10} | {matriz[fila][5]:<15} | {matriz[fila][6]:<12}\n")
                return resultado
            else:
                print("\nMedicamento no encontrado. Intente de nuevo o deje vacío para volver al menú.")
                busqueda_codigo = input("Ingrese el código: ").strip().upper()
        return None

    elif tipo == "2":
        busqueda_nombre = input("Ingrese el nombre del producto (o parte de él): ").strip().lower()
        while busqueda_nombre != "":
            resultados = buscar_por_nombre(matriz, busqueda_nombre)
            
            if resultados != -1:  # ← Interpreta el -1
                print(f"\nSe encontraron {len(resultados)} medicamento(s):\n")
                mostrar_posiciones_resultados(matriz, resultados)
                return resultados
            else:
                print("\nMedicamento no encontrado")
                busqueda_nombre = input("Ingrese el nombre del producto (o parte de él): ").strip().lower()

        return None


def buscar_por_codigo(matriz, codigo):
    '''Busca medicamento por código exacto.
    Retorna lista con índice si encuentra o -1 si no encuentra.'''
    i = 0
    while i < len(matriz):
        if matriz[i][0] == codigo:
            return [i]
        else:
            i = i + 1
    return -1


def buscar_por_nombre(matriz, nombre):
    '''Busca medicamentos por nombre (búsqueda parcial).
    Retorna lista de índices si encuentra o -1 si no encuentra.'''
    resultados = []
    i = 0
    while i < len(matriz):
        if nombre.lower() in matriz[i][1].lower():
            resultados.append(i)
        i = i + 1
    
    if resultados:
        return resultados
    else:
        return -1


def mostrar_posiciones_resultados(matriz, resultados):
    '''Le otorga posiciones a los resultados de busqueda para su visualizacion y seleccion'''
    i = 0
    while i < len(resultados):
        fila = resultados[i]
        posicion = i + 1
        print(f"[{posicion}] {matriz[fila][0]:<12} | {matriz[fila][1]:<30} | {matriz[fila][2]:<20} | {matriz[fila][3]:<12.2f} | {matriz[fila][4]:<10} | {matriz[fila][5]:<15} | {matriz[fila][6]:<12}")
        i = i + 1


def modificar_stock_precio(matriz):
    '''Modifica el stock, precio o ambos de un medicamento ya existente utilizando las funciones genéricas de búsqueda'''
    print("\n¿Cómo desea buscar?")
    print("1. Por código (búsqueda exacta)")
    print("2. Por nombre (búsqueda parcial)")
    tipo = input("Seleccione (1 o 2): ")

    while tipo not in ["1", "2"]:
        print("Opción inválida. Intente nuevamente.")
        tipo = input("Seleccione (1 o 2): ")
    
    if tipo == "1":
        busqueda_codigo = input("Ingrese el código: ").strip().upper()
        while busqueda_codigo != "":
            resultado = buscar_por_codigo(matriz, busqueda_codigo)
            if resultado != -1:
                fila = resultado[0]
                procesar_modificacion_medicamento(matriz, fila)
                
                if validar_confirmacion("¿Modificar otro medicamento? (si/no): "):
                    busqueda_codigo = input("Ingrese el código: ").strip().upper()
                else:
                    busqueda_codigo = ""
            else:
                print("Medicamento no encontrado. Intente de nuevo o deje vacío para volver al menú.")
                busqueda_codigo = input("Ingrese el código: ").strip().upper()
    
    elif tipo == "2":
        busqueda_nombre = input("Ingrese el nombre del producto (o parte de él): ").strip().lower()
        while busqueda_nombre != "":
            resultados = buscar_por_nombre(matriz, busqueda_nombre)
            if resultados != -1:
                print(f"\nSe encontraron {len(resultados)} medicamento(s):\n")
                mostrar_posiciones_resultados(matriz, resultados)
                eleccion = input(f"¿Cuál desea modificar? (1-{len(resultados)}) o deje vacío para volver: ")
                
                while eleccion != "" and (not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(resultados)):
                    print("Selección inválida")
                    eleccion = input(f"Ingrese el número (1-{len(resultados)}) o deje vacío para volver: ")
                
                if eleccion != "":
                    fila = resultados[int(eleccion) - 1]
                    procesar_modificacion_medicamento(matriz, fila)
                    
                    if validar_confirmacion("¿Modificar otro medicamento? (si/no): "):
                        busqueda_nombre = input("Ingrese el nombre del producto (o parte de él): ").strip().lower()
                    else:
                        busqueda_nombre = ""
                else:
                    busqueda_nombre = ""
            else:
                print("Medicamento no encontrado. Intente de nuevo o deje vacío para volver al menú.")
                busqueda_nombre = input("Ingrese el nombre del producto (o parte de él): ").strip().lower()


def procesar_modificacion_medicamento(matriz, fila):
    '''Muestra el submenú de qué modificar y aplica los cambios utilizando las validaciones de Lucas Bassi'''
    print(f"\nMedicamento encontrado: {matriz[fila][1]}")
    print(f"Stock actual: {matriz[fila][4]} | Precio actual: ${matriz[fila][3]:.2f}")
    
    print("\n¿Qué desea modificar?")
    print("1. Stock")
    print("2. Precio")
    print("3. Ambos")
    opcion_mod = input("Seleccione (1-3): ")
    
    while not opcion_mod.isdigit() or int(opcion_mod) < 1 or int(opcion_mod) > 3:
        print("Opción inválida. Intente nuevamente.")
        opcion_mod = input("Seleccione (1-3): ")
    
    opcion_mod = int(opcion_mod)
    
    if opcion_mod == 1:
        nuevo_stock = ingresar_stock()
        matriz[fila][4] = nuevo_stock
        print(f"Stock modificado: {matriz[fila][1]} | Stock: {matriz[fila][4]}")
    elif opcion_mod == 2:
        nuevo_precio = ingresar_precio()
        matriz[fila][3] = nuevo_precio
        print(f"Precio modificado: {matriz[fila][1]} | Precio: ${matriz[fila][3]:.2f}")
    elif opcion_mod == 3:
        nuevo_stock = ingresar_stock()
        matriz[fila][4] = nuevo_stock
        nuevo_precio = ingresar_precio()
        matriz[fila][3] = nuevo_precio
        print(f"Cambios realizados: {matriz[fila][1]} | Precio: ${matriz[fila][3]:.2f} | Stock: {matriz[fila][4]}")   


def ordenar_por_vencimiento(matriz):
    '''Ordena la matriz por vencimiento (ascendente) y por nombre (tiebreak)'''
    for i in range(len(matriz) - 1):
        for j in range(len(matriz) - 1 - i):
            # Extraer fechas y convertir a formato comparable (aaaa+mm+dd)
            d1, m1, a1 = matriz[j][6].split("/")
            d2, m2, a2 = matriz[j + 1][6].split("/")
            
            fecha1 = a1 + m1 + d1
            fecha2 = a2 + m2 + d2
            
            # Si fecha1 > fecha2, intercambia (ordena ascendente)
            if fecha1 > fecha2:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
            # Si fechas iguales, ordena por nombre alfabético (tiebreak)
            elif fecha1 == fecha2:
                if matriz[j][1] > matriz[j + 1][1]:
                    matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]


def informe_general(matriz):
    '''Ordena y muestra el informe de medicamentos por vencimiento, con opción de ver días restantes'''
    ordenar_por_vencimiento(matriz)
    mostrar_matriz(matriz)
    
    if validar_confirmacion("¿Desea visualizar días restantes para el vencimiento? (si/no): "):
        mostrar_dias_restantes(matriz)


def mostrar_dias_restantes(matriz):
    '''Calcula y muestra el código, nombre y días restantes para el vencimiento de cada medicamento'''
    import time
    
    print("\n" + "=" * 70)
    print(f"{'Código':<12} {'Nombre':<30} {'Días Restantes':<15}")
    print("=" * 70)
    
    i = 0
    while i < len(matriz):
        fila = matriz[i]
        codigo = fila[0]
        nombre = fila[1]
        fecha_vencimiento_str = fila[6]
        
        # Convertir string "dd/mm/aaaa" a struct_time
        fecha_vencimiento = time.strptime(fecha_vencimiento_str, "%d/%m/%Y")
        
        # Convertir struct_time a timestamp (segundos desde 1970)
        timestamp_vencimiento = time.mktime(fecha_vencimiento)
        
        # Obtener timestamp actual
        timestamp_hoy = time.time()
        
        # Calcular diferencia en segundos y convertir a días
        segundos_restantes = timestamp_vencimiento - timestamp_hoy
        dias_restantes = int(segundos_restantes // 86400)  # 86400 segundos = 1 día
        
        print(f"{codigo:<12} {nombre:<30} {dias_restantes:<15}")
        i = i + 1
    
    print("=" * 70 + "\n")


def salir():
    '''Termina el programa'''
    print("\n" + "="*60)
    print("¡Gracias por usar PharmaCare Central!")
    print("Hasta luego.")
    print("="*60)


if __name__ == '__main__':
    print("=== PRUEBAS UNITARIAS - MÓDULO MENÚ PRINCIPAL ===\n")
    
    # Usar la matriz inicial del sistema
    matriz_prueba = crear_matriz_inicial()
    
    # PRUEBA 1: buscar_por_codigo()
    print("1. PRUEBA: buscar_por_codigo()")
    print(f"   Buscar 'MED001': {buscar_por_codigo(matriz_prueba, 'MED001')} (Esperado: [0]) ✓")
    print(f"   Buscar 'FAR125': {buscar_por_codigo(matriz_prueba, 'FAR125')} (Esperado: [1]) ✓")
    print(f"   Buscar 'XYZ999': {buscar_por_codigo(matriz_prueba, 'XYZ999')} (Esperado: -1) ✓")
    
    # PRUEBA 2: buscar_por_nombre()
    print("\n2. PRUEBA: buscar_por_nombre()")
    print(f"   Buscar 'ibuprofeno': {buscar_por_nombre(matriz_prueba, 'ibuprofeno')} (Esperado: [0]) ✓")
    print(f"   Buscar '500': {buscar_por_nombre(matriz_prueba, '500')} (Esperado: [1, 3]) ✓")
    print(f"   Buscar 'mg': {buscar_por_nombre(matriz_prueba, 'mg')} (Esperado: [0, 1, 2, 3, 4]) ✓")
    print(f"   Buscar 'aspirina': {buscar_por_nombre(matriz_prueba, 'aspirina')} (Esperado: -1) ✓")
    
    # PRUEBA 3: mostrar_posiciones_resultados()
    print("\n3. PRUEBA: mostrar_posiciones_resultados()")
    print("   Mostrar posiciones de [0, 3]:")
    mostrar_posiciones_resultados(matriz_prueba, [0, 3])
    
    # PRUEBA 4: ordenar_por_vencimiento()
    print("\n4. PRUEBA: ordenar_por_vencimiento()")
    matriz_copia = [fila[:] for fila in matriz_prueba]
    ordenar_por_vencimiento(matriz_copia)
    fechas = [matriz_copia[i][6] for i in range(len(matriz_copia))]
    print(f"   Orden de fechas: {fechas}")
    print(f"   Esperado: ['20/07/2026', '04/08/2026', '02/12/2026', '05/06/2027', '29/08/2027'] ✓")
    
    # PRUEBA 5: mostrar_dias_restantes()
    print("\n5. PRUEBA: mostrar_dias_restantes()")
    mostrar_dias_restantes(matriz_prueba)
    
    print("=== FIN DE PRUEBAS ===")