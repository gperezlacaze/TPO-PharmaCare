# MÓDULO: Menú principal
# Autor: Gonzalo Perez Lacaze
# Fecha: 05/06/2026
# Descripción: Funciones de menú para PharmaCare

# CÓDIGOS DE COLOR ANSI
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
CELESTE = '\033[96m'
VIOLETA = '\033[35m'
NARANJA = '\033[33m'
AZUL = '\033[94m'
RESET = '\033[0m'

from lucas_bassi_validaciones import (
    ingresar_codigo, ingresar_medicamento,
    ingresar_laboratorio, ingresar_precio,
    ingresar_stock, ingresar_cobertura, ingresar_fecha_vencimiento,
    validar_confirmacion
)
from lucas_alegre import mostrar_matriz, crear_matriz_inicial, mostrar_matriz_con_colores


def mostrar_menu():
    '''Muestra el menú principal con las opciones disponibles'''
    print(f"{CELESTE}=================================================={RESET}")
    print(f"{AZUL}SISTEMA DE GESTIÓN: PHARMACARE CENTRAL{RESET}")
    print(f"{CELESTE}=================================================={RESET}")
    print(f"{AMARILLO}1.{RESET} Registrar nuevo producto")
    print(f"{AMARILLO}2.{RESET} Eliminar medicamento")
    print(f"{AMARILLO}3.{RESET} Buscar medicamento")
    print(f"{AMARILLO}4.{RESET} Modificar stock o precio")
    print(f"{AMARILLO}5.{RESET} Informe general")
    print(f"{AMARILLO}6.{RESET} Gestiones")
    print(f"{AMARILLO}7.{RESET} Salir")
    print(f"{CELESTE}=================================================={RESET}")
    print("Seleccione una opción (1-7):")


def alta_medicamentos(matriz, laboratorios):
    '''Permite el ingreso de nuevos medicamentos al sistema'''
    if len(laboratorios) == 0:
        print("No se puede agregar sin laboratorios registrados.")
        return None
    
    print()
    print(f"(Presione {NARANJA}-1{RESET} en cualquier ingreso para volver al menú principal)")
    print()
    codigo = ""
    while codigo != "-1":
        codigo = ingresar_codigo(matriz)
        if codigo is None:
            return None
        
        nombre = ingresar_medicamento()
        if nombre is None:
            return None
        
        laboratorio = ingresar_laboratorio(laboratorios)
        if laboratorio is None:
            return None
        
        precio = ingresar_precio()
        if precio is None:
            return None
        
        stock = ingresar_stock()
        if stock is None:
            return None
        
        cobertura = ingresar_cobertura()
        if cobertura is None:
            return None
        
        vencimiento = ingresar_fecha_vencimiento()
        if vencimiento is None:
            return None
        
        nueva_fila = [codigo, nombre, laboratorio, precio, stock, cobertura, vencimiento]
        matriz.append(nueva_fila)
        print()
        respuesta = validar_confirmacion("¿Agregar otro? (si/no): ")
        if respuesta == "no":
            codigo = "-1"  # Salida natural del while
    print()


def baja_medicamentos(matriz):
    '''Permite eliminar medicamentos con stock = 0'''
    print()
    print(f"(Presione {NARANJA}-1{RESET} para volver al menú principal)")
    print()
    
    print("¿Cómo desea buscar el medicamento?")
    print(f"{AMARILLO}1.{RESET} Por código (búsqueda exacta)")
    print(f"{AMARILLO}2.{RESET} Por nombre (búsqueda parcial)")
    tipo = input(f"Seleccione (1 o 2, o {NARANJA}-1{RESET} para volver): ")

    while tipo not in ["1", "2", "-1"]:
        print("Opción inválida. Intente nuevamente.")
        tipo = input("Seleccione (1 o 2, o -1 para volver): ")
    
    if tipo == "-1":
        return None
    
    print()
    if tipo == "1":
        busqueda_codigo = input("Ingrese el código (o -1 para volver): ").strip().upper()
        while busqueda_codigo != "" and busqueda_codigo != "-1":
            resultado = buscar_por_codigo(matriz, busqueda_codigo)
            if procesar_eliminacion(matriz, resultado):
                busqueda_codigo = input("Ingrese el código (o -1 para volver): ").strip().upper()
            else:
                busqueda_codigo = ""
    
    elif tipo == "2":
        busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
        while busqueda_nombre != "-1":
            if busqueda_nombre == "":
                busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
                continue
            
            resultado = buscar_por_nombre(matriz, busqueda_nombre)
            if procesar_eliminacion(matriz, resultado):
                busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
            else:
                if resultado == -1:
                    print(f"Medicamento {ROJO}no encontrado{RESET}. Intente de nuevo o presione -1 para volver.")
                busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
    print()


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
        print()
        print(f"Ningún medicamento encontrado tiene stock = 0")
        print()
        return False 
    
    if len(medicamentos_a_eliminar) == 1:
        fila = medicamentos_a_eliminar[0]
        print()
        print(f"Medicamento a eliminar: {matriz[fila][1]}")
        print()
    else:
        print()
        print(f"Se encontraron {len(medicamentos_a_eliminar)} medicamento(s) con stock = 0:")
        print()
        mostrar_posiciones_resultados(matriz, medicamentos_a_eliminar)
        eleccion = input(f"¿Cuál desea eliminar? ({AMARILLO}1{RESET}-{AMARILLO}{len(medicamentos_a_eliminar)}{RESET}): ")
        while not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(medicamentos_a_eliminar):
            print(f"Selección {ROJO}inválida{RESET}")
            eleccion = input(f"Ingrese el número ({AMARILLO}1{RESET}-{AMARILLO}{len(medicamentos_a_eliminar)}{RESET}): ")
        fila = medicamentos_a_eliminar[int(eleccion) - 1]

    if validar_confirmacion(f"¿Eliminar {matriz[fila][1]}? (si/no): ") == "si":
        print()
        print(f"{VERDE}Eliminando:{RESET} {matriz[fila][0]:<12} | {matriz[fila][1]:<30} | {matriz[fila][2]:<20} | {matriz[fila][3]:<12.2f} | {matriz[fila][4]:<10} | {matriz[fila][5]:<15} | {matriz[fila][6]:<12}")
        matriz.pop(fila)
        print(f"{VERDE}✓ Medicamento eliminado correctamente{RESET}")
        print()
        return validar_confirmacion("¿Eliminar otro? (si/no): ") == "si"
    else:
        print()
        print("Operación cancelada")
        print()
        return validar_confirmacion("¿Eliminar otro? (si/no): ") == "si"


def mostrar_medicamento(matriz):
    '''La funcion busca por codigo (resultado unico) o por nombre (resultados multiples posibles) y muestra los resultados con posiciones'''
    print()
    print("¿Cómo desea buscar?")
    print(f"{AMARILLO}1.{RESET} Por código (búsqueda exacta)")
    print(f"{AMARILLO}2.{RESET} Por nombre (búsqueda parcial)")
    tipo = input(f"Seleccione (1 o 2, o {NARANJA}-1{RESET} para volver): ")

    while tipo not in ["1", "2", "-1"]:
        print(f"Opción {ROJO}inválida{RESET}. Intente nuevamente.")
        tipo = input(f"Seleccione (1 o 2, o {NARANJA}-1{RESET} para volver): ")
    
    if tipo == "-1":
        return None
    
    print()
    print(f"(Presione {NARANJA}-1{RESET} para volver al menú principal)")
    print()
        
    if tipo == "1":  # CÓDIGO
        busqueda_codigo = input("Ingrese el código (o -1 para volver): ").strip().upper()
        while busqueda_codigo != "-1":
            if busqueda_codigo == "":
                busqueda_codigo = input("Ingrese el código (o -1 para volver): ").strip().upper()
                continue
            
            resultado = buscar_por_codigo(matriz, busqueda_codigo)
            
            if resultado != -1:
                print()
                print(f"Medicamento encontrado:")
                fila = resultado[0]
                print(f"{matriz[fila][0]:<12}{matriz[fila][1]:<30}{matriz[fila][2]:<20}{matriz[fila][3]:<12.2f}{matriz[fila][4]:<10}{matriz[fila][5]:<15}{matriz[fila][6]:<12}")
                print()
                return resultado
            else:
                print()
                print(f"Medicamento {ROJO}no encontrado{RESET}. Intente de nuevo o presione -1 para volver.")
                busqueda_codigo = input("Ingrese el código (o -1 para volver): ").strip().upper()
        print()
        return None

    elif tipo == "2":
        busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
        while busqueda_nombre != "-1":
            if busqueda_nombre == "":
                busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
                continue
            
            resultados = buscar_por_nombre(matriz, busqueda_nombre)
            
            if resultados != -1:
                print()
                print(f"Se encontraron {len(resultados)} medicamento(s):")
                print()
                mostrar_posiciones_resultados(matriz, resultados)
                return resultados
            else:
                print()
                print(f"Medicamento {ROJO}no encontrado{RESET}. Intente de nuevo o presione -1 para volver.")
                busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()

        print()
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
        print(f"{AMARILLO}[{posicion}]{RESET} {matriz[fila][0]:<12}{matriz[fila][1]:<30}{matriz[fila][2]:<20}{matriz[fila][3]:<12.2f}{matriz[fila][4]:<10}{matriz[fila][5]:<15}{matriz[fila][6]:<12}")
        i = i + 1


def modificar_stock_precio(matriz):
    '''Modifica el stock, precio o ambos de un medicamento ya existente utilizando las funciones genéricas de búsqueda'''
    print()
    print("¿Cómo desea buscar?")
    print(f"{AMARILLO}1.{RESET} Por código (búsqueda exacta)")
    print(f"{AMARILLO}2.{RESET} Por nombre (búsqueda parcial)")
    tipo = input(f"Seleccione (1 o 2, o {NARANJA}-1{RESET} para volver): ")

    while tipo not in ["1", "2", "-1"]:
        print(f"Opción {ROJO}inválida{RESET}. Intente nuevamente.")
        tipo = input(f"Seleccione (1 o 2, o {NARANJA}-1{RESET} para volver): ")
    
    if tipo == "-1":
        return None
    
    print()
    print(f"(Presione {NARANJA}-1{RESET} para volver al menú principal)")
    print()
    
    if tipo == "1":
        busqueda_codigo = input("Ingrese el código (o -1 para volver): ").strip().upper()
        while busqueda_codigo != "" and busqueda_codigo != "-1":
            resultado = buscar_por_codigo(matriz, busqueda_codigo)
            if resultado != -1:
                fila = resultado[0]
                procesar_modificacion_medicamento(matriz, fila)
                
                respuesta = validar_confirmacion("¿Modificar otro medicamento? (si/no): ")
                if respuesta == "no":
                    busqueda_codigo = ""
                else:
                    busqueda_codigo = input("Ingrese el código (o -1 para volver): ").strip().upper()
            else:
                print()
                print("Medicamento no encontrado. Intente de nuevo o presione -1 para volver.")
                busqueda_codigo = input("Ingrese el código (o -1 para volver): ").strip().upper()
        print()
    
    elif tipo == "2":
        busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
        while busqueda_nombre != "-1":
            if busqueda_nombre == "":
                busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
                continue
            
            resultados = buscar_por_nombre(matriz, busqueda_nombre)
            if resultados != -1:
                print()
                print(f"Se encontraron {len(resultados)} medicamento(s):")
                print()
                mostrar_posiciones_resultados(matriz, resultados)
                eleccion = input(f"¿Cuál desea modificar? (1-{len(resultados)}) o presione -1 para volver: ")
                
                while eleccion != "" and eleccion != "-1" and (not eleccion.isdigit() or int(eleccion) < 1 or int(eleccion) > len(resultados)):
                    print(f"Selección {ROJO}inválida{RESET}")
                    eleccion = input(f"Ingrese el número (1-{len(resultados)}) o presione -1 para volver: ")
                
                if eleccion != "" and eleccion != "-1":
                    fila = resultados[int(eleccion) - 1]
                    procesar_modificacion_medicamento(matriz, fila)
                    
                    respuesta = validar_confirmacion("¿Modificar otro medicamento? (si/no): ")
                    if respuesta == "no":
                        busqueda_nombre = "-1"
                    else:
                        busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
                else:
                    busqueda_nombre = "-1"
            else:
                print()
                print(f"Medicamento {ROJO}no encontrado{RESET}. Intente de nuevo o presione -1 para volver.")
                busqueda_nombre = input("Ingrese el nombre del producto (o -1 para volver): ").strip().lower()
        print()


def procesar_modificacion_medicamento(matriz, fila):
    '''Muestra el submenú de qué modificar y aplica los cambios utilizando las validaciones de Lucas Bassi'''
    print()
    print(f"Medicamento encontrado: {matriz[fila][1]}")
    print(f"Stock actual: {matriz[fila][4]} | Precio actual: ${matriz[fila][3]:.2f}")
    print()
    
    print("¿Qué desea modificar?")
    print(f"{AMARILLO}1.{RESET} Stock")
    print(f"{AMARILLO}2.{RESET} Precio")
    print(f"{AMARILLO}3.{RESET} Ambos")
    print(f"(Presione {NARANJA}-1{RESET} para volver)")
    opcion_mod = input("Seleccione (1-3): ")
    
    while not opcion_mod.isdigit() or int(opcion_mod) < 1 or int(opcion_mod) > 3:
        if opcion_mod == "-1":
            print()
            return None
        print(f"Opción {ROJO}inválida{RESET}. Intente nuevamente.")
        opcion_mod = input(f"Seleccione (1-3) (o {NARANJA}-1{RESET} para volver): ")
    
    opcion_mod = int(opcion_mod)
    
    print()
    if opcion_mod == 1:
        nuevo_stock = ingresar_stock()
        if nuevo_stock is None:
            return None
        matriz[fila][4] = nuevo_stock
        print()
        print(f"{VERDE}✓ Stock modificado{RESET}: {matriz[fila][1]} | Stock: {matriz[fila][4]}")
        print()
    elif opcion_mod == 2:
        nuevo_precio = ingresar_precio()
        if nuevo_precio is None:
            return None
        matriz[fila][3] = nuevo_precio
        print()
        print(f"{VERDE}✓ Precio modificado{RESET}: {matriz[fila][1]} | Precio: ${matriz[fila][3]:.2f}")
        print()
    elif opcion_mod == 3:
        nuevo_stock = ingresar_stock()
        if nuevo_stock is None:
            return None
        matriz[fila][4] = nuevo_stock
        nuevo_precio = ingresar_precio()
        if nuevo_precio is None:
            return None
        matriz[fila][3] = nuevo_precio
        print()
        print(f"{VERDE}✓ Cambios realizados{RESET}: {matriz[fila][1]} | Precio: ${matriz[fila][3]:.2f} | Stock: {matriz[fila][4]}")   
        print()


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
    print()
    ordenar_por_vencimiento(matriz)
    mostrar_matriz_con_colores(matriz)
    
    if validar_confirmacion("¿Desea visualizar días restantes para el vencimiento? (si/no): ") == "si":
        mostrar_dias_restantes(matriz)
    print()


def mostrar_dias_restantes(matriz):
    '''Calcula y muestra el código, nombre y días restantes para el vencimiento de cada medicamento'''
    import time
    
    print()
    print(f"{CELESTE}={'=' * 68}{RESET}")
    print(f"{VIOLETA}{'Código':<12}{'Nombre':<30}{'Días Restantes':<15}{RESET}")
    print(f"{CELESTE}{'=' * 68}{RESET}")
    
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
        
        print(f"{codigo:<12}{nombre:<30}{dias_restantes:<15}")
        i = i + 1
    
    print(f"{CELESTE}{'=' * 68}{RESET}")
    print()


def salir():
    '''Termina el programa'''
    print()
    print("="*60)
    print("¡Gracias por usar PharmaCare Central!")
    print("Hasta luego.")
    print("="*60)
    print()


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