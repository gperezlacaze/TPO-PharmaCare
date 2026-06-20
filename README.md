# PharmaCare Central - Sistema de Gestión de Inventario Farmacéutico

## Descripción

**PharmaCare Central** es un sistema de gestión de inventario farmacéutico desarrollado como **Trabajo Práctico Obligatorio (TPO)** para la materia **Pensamiento Computacional, Algoritmia y Programación** de la Universidad Argentina de la Empresa (UADE).

El sistema permite centralizar la administración de medicamentos, registrar nuevos productos, eliminar medicamentos discontinuados, modificar información (stock y precio), buscar productos y generar informes ordenados por vencimiento. **Además, gestiona laboratorios fabricantes, configura stock mínimo con reportes de disponibilidad, y registra ventas con procesamiento de pagos [Agregado en Fase 2].**


## Características Principales

- **Gestión de medicamentos:** Alta, baja, modificación y búsqueda.
- **Almacenamiento:** Matriz de medicamentos (lista de listas) en memoria RAM.
- **Validación de datos:** Validación robusta de entrada con funciones específicas.
- **Informe general:** Visualización de medicamentos ordenados por días de vencimiento (menor a mayor) y, en caso de igualdad, alfabéticamente por nombre.
- **Interfaz interactiva:** Menú principal con opciones numeradas.
- **Confirmaciones seguras:** Validación de respuestas "si/no" (case-insensitive) para operaciones críticas.
- **Gestión de laboratorios:** Alta, modificación y baja de laboratorios fabricantes con validación de duplicados y detección de siglas. **[Agregado en Fase 2]**
- **Gestión de stock mínimo:** Configuración de stock mínimo y reporte de medicamentos con stock bajo la línea configurada, con visualización en color rojo en todos los informes de productos del programa. **[Agregado en Fase 2]**
- **Gestión de ventas:** Registro de ventas múltiples, selección de medios de pago (efectivo con vuelto o tarjeta con 10% de recargo), e informe de ventas realizadas. **[Agregado en Fase 2]**
- **Colores ANSI mejorados:** Interfaz visual con códigos de color para errores, éxitos, opciones y datos resaltados. **[Agregado en Fase 2]**

**Nota:** Todo lo marcado como [Agregado en Fase 2] corresponde a funcionalidades nuevas implementadas en la segunda fase del proyecto.


## Estructura del Proyecto

```
TPO-PHARMACARE/
├── programa_principal.py                # Programa principal (coordina el flujo)
├── matriz_lucas_alegre.py               # Módulo de matriz de medicamentos (Fase 1)
├── gonzalo_pl_menu_principal.py         # Módulo de menú principal e interacción (Fase 1)
├── alegre_bassi_validaciones.py         # Módulo de validaciones de entrada (Fase 1 y 2)
├── lucas_bassi_submenus.py              # Módulo de gestiones (laboratorios, stock, ventas) (Fase 2)
├── Informe programa PharmaCare.md       # Este archivo
├── cambios_al_alcance_fase2.txt         # Documento de cambios y mejoras (Fase 2)
└── .gitignore                           # Configuración de Git
```


## Descripción de Módulos

#### `matriz_lucas_alegre.py`
- `crear_matriz_inicial()` — Crea una matriz inicial con 5 medicamentos precargados.
- `mostrar_matriz_con_colores(matriz, stock_minimo)` — Muestra la matriz en formato de tabla con encabezados y colores ANSI. Si `stock_minimo` tiene valor, colorea el stock en ROJO si está por debajo. **[Actualizado en Fase 2]**

**Estructura de columnas:**
```
[codigo, nombre, laboratorio, precio, stock, cobertura, fecha_de_vencimiento]
[0,     1,       2,           3,       4,     5,         6]
```

**Cambio en el formato de vencimiento:** La columna 6 de la matriz fue actualizada, el vencimiento se ve en formato de fecha "dd/mm/aa", y los calculos de los dias restantes para el vencimiento se pueden calcular en el informe general. **[Actualizado en Fase 2]**

#### `gonzalo_pl_menu_principal.py`
- `mostrar_menu()` — Imprime el menú principal en pantalla (opciones 1-7).
- `alta_medicamentos(matriz, laboratorios)` — Registra nuevos medicamentos con validación y confirmación iterativa. Requiere para el ingreso seleccionar laboratorios registrados. [Actualizado en Fase 2]
- `baja_medicamentos(matriz)` — Elimina medicamentos (solo si stock = 0) con confirmación. Búsqueda por código o nombre con manejo de múltiples resultados. [Actualizado en Fase 2]
- `procesar_eliminacion(matriz, resultado)` — Procesa el filtrado, selección y eliminación de medicamentos con stock = 0. [Agregado en Fase 2]
- `mostrar_medicamento(matriz)` — Busca medicamentos por código (búsqueda exacta) o nombre (búsqueda parcial) y muestra los resultados (funcion renombrada, version anterior = buscar_medicamento()). [Actualizado en Fase 2]
- `buscar_por_codigo(matriz, codigo)` — Busca medicamento por código exacto. Retorna lista con índice o -1 si no encuentra. [Agregado en Fase 2]
- `buscar_por_nombre(matriz, nombre)` — Busca medicamentos por nombre (búsqueda parcial). Retorna lista de índices o -1 si no encuentra. [Agregado en Fase 2]
- `mostrar_posiciones_resultados(matriz, resultados)` — Muestra los resultados de búsqueda con posiciones numeradas para selección. [Agregado en Fase 2]
- `modificar_stock_precio(matriz)` — Modifica stock y/o precio de un medicamento existente con búsqueda por código o nombre. [Actualizado en Fase 2]
- `procesar_modificacion_medicamento(matriz, fila)` — Submenú para seleccionar qué modificar (stock, precio o ambos). [Agregado en Fase 2]
- `ordenar_por_vencimiento(matriz)` — Ordena la matriz por vencimiento (ascendente) y por nombre (tiebreak alfabético). [Agregado en Fase 2]
- `informe_general(matriz, stock_minimo)` — Muestra medicamentos ordenados por vencimiento (Bubble Sort); sin modificar original. Permite visualizar días restantes para vencimiento. [Actualizado en Fase 2]
- `mostrar_dias_restantes(matriz)` — Calcula y muestra el código, nombre y días restantes para el vencimiento de cada medicamento. [Agregado en Fase 2]
- `salir()` — Mensaje de despedida; termina el programa.

#### `alegre_bassi_validaciones.py`
Proporciona funciones de validación e ingreso seguro de datos (fusión de validaciones de Lucas Alegre y Lucas Bassi):
 
**Funciones de Validación (Retornan True/False):**
- `validar_codigo_medicamento(codigo)` — Valida 4-8 caracteres alfanuméricos con combinación de letras Y números.
- `validar_codigo_unico(codigo, matriz)` — Verifica que el código no esté duplicado en la matriz.
- `validar_nombre_medicamento(nombre)` — Verifica que tenga al menos una letra.
- `validar_laboratorio_fabricante(laboratorio)` — Verifica no-vacío, rechaza solo números o solo símbolos.
- `validar_entero_positivo(texto)` — Valida enteros > 0.
- `validar_precio(texto)` — Valida decimales > 0.
- `validar_cobertura(cobertura)` — Valida "Con cobertura" o "Sin cobertura" (case-insensitive).
- `validar_fecha_vencimiento(fecha)` — Valida formato dd/mm/aaaa con año de 4 dígitos. Considera años bisiestos. [Actualizado en Fase 2]
- `validar_laboratorio_duplicado(nombre, lista_laboratorios)` — Valida si un laboratorio ya existe en la lista (case-insensitive). [Agregado en Fase 2]
- `validar_stock_suficiente(medicamento, cantidad)` — Valida si hay stock suficiente para una venta. [Agregado en Fase 2]
- `validar_monto_efectivo(monto, total)` — Valida si el monto en efectivo es suficiente para pagar el total. [Agregado en Fase 2]
**Funciones de Ingreso (Piden datos al usuario y validan iterativamente):**
- `ingresar_codigo(matriz)` — Pide y valida el código del medicamento. Retorna código o None si presiona -1.
- `ingresar_medicamento()` — Pide y valida el nombre del medicamento. Retorna nombre capitalizado o None si presiona -1.
- `ingresar_laboratorio(laboratorios)` — Pide y valida el laboratorio con detección automática de siglas y validación de duplicados. Retorna laboratorio o None si presiona -1. [Actualizado en Fase 2]
- `ingresar_precio()` — Pide y valida el precio del medicamento. Retorna precio como float o None si presiona -1.
- `ingresar_stock()` — Pide y valida el stock del medicamento. Retorna stock como int o None si presiona -1.
- `ingresar_cobertura()` — Pide y valida la cobertura médica. Retorna cobertura capitalizada o None si presiona -1.
- `ingresar_fecha_vencimiento()` — Pide y valida la fecha de vencimiento (dd/mm/aaaa). Retorna fecha como string o None si presiona -1.
**Funciones de Menú y Confirmación:**
- `validar_opcion(desde, hasta)` — Valida opción en menús (principal, gestiones, submenús). NO permite -1, solo opciones válidas dentro del rango. Retorna int. [Agregado en Fase 2]
- `validar_opcion_menu_anterior(desde, hasta)` — Valida opción en funciones secundarias. Permite -1 para volver al menú anterior. Retorna int.
- `validar_confirmacion(pregunta)` — Valida respuestas "si"/"no" (case-insensitive). Retorna string "si" o "no".
**Funciones de Selección (Fase 2):**
- `seleccionar_laboratorio(laboratorios)` — Permite seleccionar un laboratorio de la lista existente con validación de selección. Retorna laboratorio o None si presiona -1. [Agregado en Fase 2]

#### `lucas_bassi_submenus.py` [Fase 2]
Módulo completo de gestiones adicionales (laboratorios, stock mínimo, ventas):
 
**Gestión de Laboratorios:**
- `mostrar_menu_laboratorios()` — Menú de laboratorios con opciones 1-5.
- `submenu_laboratorios(laboratorios)` — Bucle principal del submenú.
- `agregar_laboratorio(laboratorios)` — Agrega laboratorio con detección de siglas.
- `modificar_laboratorio(laboratorios)` — Modifica nombre de laboratorio existente con validaciones.
- `dar_de_baja_laboratorio(laboratorios)` — Elimina laboratorio de la lista.
- `ver_laboratorios(laboratorios)` — Muestra lista numerada de laboratorios.
**Gestión de Stock Mínimo:**
- `mostrar_menu_stock()` — Menú de stock con opciones 1-3.
- `submenu_stock(matriz, stock_minimo)` — Bucle principal del submenú. Retorna el nuevo stock mínimo configurado.
- `configuracion_stock_minimo()` — Permite configurar valor de stock mínimo. Retorna valor configurado o None si cancela.
- `reporte_stock_bajo(matriz, stock_minimo)` — Muestra tabla de medicamentos con stock por debajo del mínimo configurado.
**Gestión de Ventas:**
- `mostrar_menu_ventas()` — Menú de ventas con opciones 1-3.
- `submenu_ventas(matriz)` — Bucle principal del submenú.
- `mostrar_medicamentos_disponibles(matriz)` — Muestra medicamentos con stock > 0 numerados. Retorna lista de índices disponibles.
- `registrar_venta(matriz)` — Permite registrar múltiples medicamentos en una venta con descuento inmediato de stock. Retorna None si cancela.
- `procesar_pago(total, medicamentos_comprados)` — Gestiona selección de medio de pago (efectivo con vuelto o tarjeta con 10% de recargo). Reversa stock de todos los medicamentos si se cancela. Retorna True si pago exitoso, None si cancela.
- `ver_ventas(ventas)` — Muestra historial de ventas registradas.
**Menú Principal de Gestiones:**
- `menu_gestion()` — Menú de gestiones con opciones 1-4.
- `mostrar_menu_gestiones(matriz, laboratorios, stock_minimo)` — Bucle principal que coordina laboratorios, stock y ventas. Retorna el stock mínimo actualizado.

#### `programa_principal.py`
Coordina el flujo principal del sistema:
 
- `main()` — Función principal que ejecuta el programa.
**Flujo de operación:**
1. Carga inventario inicial con `crear_matriz_inicial()`.
2. Inicializa `stock_minimo` en `None`.
3. Carga lista inicial de laboratorios desde `lucas_bassi_submenus`.
4. Menú principal en bucle: muestra opciones (1-7), valida entrada con `validar_opcion(1, 7)`, ejecuta operación correspondiente.
5. **Opción 1:** Registrar nuevo medicamento con `alta_medicamentos()`.
6. **Opción 2:** Eliminar medicamento con `baja_medicamentos()`.
7. **Opción 3:** Buscar medicamento con `mostrar_medicamento()`.
8. **Opción 4:** Modificar stock o precio con `modificar_stock_precio()`.
9. **Opción 5:** Ver informe general ordenado por vencimiento con `informe_general()`.
10. **Opción 6:** Acceder a gestiones (laboratorios, stock, ventas) con `mostrar_menu_gestiones()`. Retorna y actualiza `stock_minimo`. [Fase 2]
11. **Opción 7:** Salir del programa con `salir()`.


## Cómo Ejecutar
 
### Requisitos
- Python 3.x
### Instrucciones de ejecución
 
1. Clonar o descargar el repositorio:
```bash
   git clone https://github.com/gperezlacaze/TPO-PharmaCare
   cd TPO-PHARMACARE
```
 
2. Ejecutar el programa:
```bash
   python programa_principal.py
```
   o
```bash
   python3 programa_principal.py
```
 
### Guía de Menús
 
#### Menú Principal
Al iniciar el programa, aparece el menú principal con las siguientes opciones:
 
- **Opción 1:** Registrar nuevo producto — Permite agregar medicamentos a la matriz. Sistema de confirmación iterativa (si/no).
- **Opción 2:** Eliminar medicamento — Elimina medicamentos solo si su stock es 0. Búsqueda por código o nombre con manejo de múltiples resultados.
- **Opción 3:** Buscar medicamento — Búsqueda por código (exacta) o nombre (parcial). Muestra resultados con posiciones numeradas.
- **Opción 4:** Modificar stock o precio — Buscar medicamento y modificar stock, precio o ambos.
- **Opción 5:** Informe general — Muestra medicamentos ordenados por vencimiento con opción de visualizar días restantes.
- **Opción 6:** Gestiones — Accede a submenu de laboratorios, stock mínimo y ventas. [Fase 2]
- **Opción 7:** Salir — Termina el programa.

#### Menú Gestiones (Opción 6) [Fase 2]
Acceso a tres submenues principales:
 
**1. Gestión de Laboratorios**
- Opción 1: Agregar laboratorio — Ingresa nuevo laboratorio con detección automática de siglas.
- Opción 2: Modificar laboratorio — Modifica nombre de laboratorio existente.
- Opción 3: Dar de baja laboratorio — Elimina laboratorio de la lista.
- Opción 4: Ver laboratorios — Muestra lista numerada de laboratorios registrados.
- Opción 5: Volver al menú anterior.
**2. Gestión de Stock**
- Opción 1: Configurar stock mínimo — Define el valor mínimo de stock a monitorear.
- Opción 2: Reporte stock bajo mínimo — Muestra medicamentos con stock por debajo del mínimo configurado (resaltados en ROJO).
- Opción 3: Volver al menú anterior.
**3. Gestión de Ventas**
- Opción 1: Registrar venta — Permite registrar una o más ventas. Sistema de confirmación iterativa. Procesa pago (efectivo o tarjeta con 10% recargo). Si cancela, reversa stock automáticamente.
- Opción 2: Ver ventas — Muestra historial de ventas registradas.
- Opción 3: Volver al menú anterior.

### Confirmaciones y Navegación
 
**Para operaciones que requieren confirmación:**
- Responda `si`, `SI`, `Si` — Afirmativo
- Responda `no`, `NO`, `No` — Negativo
**Para cancelar o volver a través de inputs de datos:**
- Presione `-1` en campos de entrada de datos (códigos, precios, stock, fechas, etc.) para volver al menú anterior.
**Para volver desde submenús:**
- Seleccione la opción de "Volver al menú anterior" en cada submenu (ej: opción 5 en Laboratorios, opción 3 en Stock, opción 3 en Ventas).
- Desde el menú de Gestiones (opción 4), vuelve al menú principal.
- Desde el menú principal (opción 7), sale del programa.
 

 ## Medicamentos Iniciales
 
El sistema carga 5 medicamentos de ejemplo al iniciar:
 
| Código | Nombre | Laboratorio | Precio | Stock | Cobertura | Fecha Vencimiento |
|--------|--------|-------------|--------|-------|-----------|------------------|
| MED001 | Ibuprofeno 600mg | Roemmers | $2500.00 | 50 | Con cobertura | 02/12/2026 |
| FAR125 | Amoxicilina 500mg | Bagó | $1800.00 | 120 | Sin cobertura | 20/07/2026 |
| LAB789 | Omeprazol 20mg | Pfizer | $750.00 | 8 | Con cobertura | 02/12/2026 |
| FAR140 | Paracetamol 500mg | ISA | $1200.00 | 200 | Sin cobertura | 05/06/2027 |
| LAB456 | Metformina 850mg | Roche | $5000.00 | 30 | Con cobertura | 04/08/2026 |
 
**Nota:** Las fechas de vencimiento se utilizan para ordenar el informe general (menor a mayor vencimiento). El cálculo de días restantes se realiza dinámicamente en la opción de informe general.


## Autores
 
- **Gonzalo Perez Lacaze** — Módulo de menú, modificaciones para Fase 2, cálculo de vencimiento en días, integración, aplicación de colores al programa, archivos README y cambios al alcance.
- **Lucas Alegre** — Módulo de matriz y visualización, funciones de validación para Fase 2.
- **Lucas Bassi** — Módulo de validaciones e ingreso de datos, módulos de submenús.

**Nota:** Todos participamos de las correcciones de errores en todos los códigos y en las pruebas.


## Notas Técnicas
 
- **Almacenamiento en memoria:** Los datos se mantienen en una **lista de listas (matriz)** en memoria RAM, según requisito de la consigna. Los cambios se pierden al cerrar el programa.
- **Modularización:** Código organizado en módulos separados por responsabilidad:
  - `matriz_lucas_alegre.py` — Creación y visualización de la matriz.
  - `gonzalo_pl_menu_principal.py` — Menú principal, búsqueda, modificación, eliminación e informe general.
  - `alegre_bassi_validaciones.py` — Validaciones de entrada, funciones de ingreso de datos, y confirmaciones.
  - `lucas_bassi_submenus.py` — Gestiones de laboratorios, stock mínimo y ventas [Fase 2].
  - `programa_principal.py` — Coordinación del flujo principal.
- **Algoritmos propios:** 
  - Implementación manual de **Bubble Sort** para ordenamiento por fecha de vencimiento (formato dd/mm/aaaa) con tiebreak alfabético por nombre. **Lógica desarrollada con asesoramiento del profesor Santiago Ricardo Jose Mendoza.**
  - Búsqueda secuencial por código (exacta) y por nombre (parcial) sin uso de métodos built-in de búsqueda.
  - Cálculo dinámico de días restantes para vencimiento mediante conversión de fechas a timestamps (módulo `time`).
- **Validación robusta:** Funciones de validación separan lógica de entrada de lógica de presentación (sin `print` en validadores puros). Las funciones `ingresar_*()` manejan la presentación y reintentos.
- **Convenciones:** Adherencia a **PEP 8** y principios del **Zen de Python**.
- **Encoding:** Archivos guardados en **UTF-8** para soporte de caracteres acentuados.
- **Colores ANSI:** Implementación de códigos de color para mejorar la interfaz visual (VERDE, ROJO, AMARILLO, AZUL, CELESTE, VIOLETA, NARANJA). **Implementación realizada con asesoramiento del profesor Santiago Ricardo Jose Mendoza y la herramienta Claude Pro.**
- **Bloque `if __name__ == "__main__":`** 
  Cada módulo incluye un bloque `if __name__ == "__main__":` para pruebas unitarias:
  
  - `matriz_lucas_alegre.py` — Pruebas de `crear_matriz_inicial()` y `mostrar_matriz_con_colores()`.
  - `gonzalo_pl_menu_principal.py` — Pruebas de funciones de búsqueda (`buscar_por_codigo()`, `buscar_por_nombre()`), ordenamiento (`ordenar_por_vencimiento()`) y cálculo de días (`mostrar_dias_restantes()`).
  - `alegre_bassi_validaciones.py` — Pruebas de todas las funciones de validación con casos válidos e inválidos. Pruebas Fase 2 incluidas.
  - `lucas_bassi_submenus.py` — Pruebas interactivas de menús y gestiones.
  
  **Propósito:** Permitir validación rápida de cada módulo de forma independiente sin ejecutar el programa principal.
- **Herramientas y Asistencia:** Las pruebas efectuadas en cada módulo fueron realizadas con la ayuda de **Claude Pro**. La implementación de colores ANSI fue desarrollada con asesoramiento del profesor **Santiago Ricardo Jose Mendoza** y **Claude Pro**.
- **Uso de IA:** Se utilizó **Claude Pro** para consultas, corrección de errores, implementación de colores ANSI y pruebas necesarias en cada archivo.
- **Fundamentos teóricos:** Los conceptos básicos para la realización del código se obtuvieron de las presentaciones de todas las clases y ejemplos de códigos presentes en la carpeta de la clase en Microsoft Teams.


## Licencia
 
Proyecto académico - UADE 2026.
 
URL repository: https://github.com/gperezlacaze/TPO-PharmaCare