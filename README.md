# PharmaCare Central - Sistema de Gestión de Inventario Farmacéutico

## Descripción

**PharmaCare Central** es un sistema de gestión de inventario farmacéutico desarrollado como **Trabajo Práctico Obligatorio (TPO)** para la materia **Pensamiento Computacional, Algoritmia y Programación** de la Universidad Argentina de la Empresa (UADE).

El sistema permite centralizar la administración de medicamentos, registrar nuevos productos, eliminar medicamentos discontinuados, modificar información (stock y precio), buscar productos y generar informes ordenados por vencimiento.

## Características Principales

- **Gestión de medicamentos:** Alta, baja, modificación y búsqueda.
- **Almacenamiento:** Matriz de medicamentos (lista de listas) en memoria RAM.
- **Validación de datos:** Validación robusta de entrada con funciones específicas.
- **Informe general:** Visualización de medicamentos ordenados por días de vencimiento (menor a mayor) y, en caso de igualdad, alfabéticamente por nombre.
- **Interfaz interactiva:** Menú principal con opciones numeradas (1-6); opción 8 como alternativa para salir desde menú principal.
- **Confirmaciones seguras:** Validación de respuestas "si/no" (case-insensitive) para operaciones críticas.

## Estructura del Proyecto

```
TPO-PHARMACARE/
├── main.py                          # Programa principal (coordina el flujo)
├── lucas_alegre.py                  # Módulo de matriz de medicamentos
├── gonzalo_perez_lacaze_menu.py     # Módulo de menú e interacción
├── lucas_bassi_validaciones.py      # Módulo de validaciones de entrada
├── README.md                        # Este archivo
└── .gitignore                       # Configuración de Git
```

### Descripción de Módulos

#### `lucas_alegre.py`
- `crear_matriz_inicial()` — Crea una matriz inicial con 5 medicamentos precargados.
- `mostrar_matriz(matriz)` — Muestra la matriz en formato de tabla con encabezados.

**Estructura de columnas:**
```
[codigo, nombre, laboratorio, precio, stock, cobertura, dias_vencimiento]
[0,     1,       2,           3,       4,     5,         6]
```

#### `gonzalo_perez_lacaze_menu.py`
- `mostrar_menu()` — Imprime el menú principal en pantalla (opciones 1-6 y opción 8 para salir).
- `validar_opcion(desde, hasta)` — Valida opción ingresada; acepta opción 8 como salida global.
- `validar_confirmacion(pregunta)` — Valida respuestas "si"/"no" (case-insensitive). Retorna `bool`.
- `alta_medicamentos(matriz)` — Registra nuevos medicamentos con validación y confirmación iterativa.
- `baja_medicamentos(matriz)` — Elimina medicamentos (solo si stock = 0) con confirmación.
- `buscar_medicamento(matriz)` — Busca por código o nombre (búsqueda parcial).
- `modificar_stock_precio(matriz)` — Modifica stock y/o precio con confirmación iterativa.
- `informe_general(matriz)` — Muestra medicamentos ordenados por vencimiento (Bubble Sort); sin modificar original.
- `salir()` — Mensaje de despedida; termina el programa.

#### `lucas_bassi_validaciones.py`
Proporciona funciones de validación e ingreso seguro de datos:
- `validar_codigo_medicamento(codigo)` — Valida 4-10 caracteres alfanuméricos (`.isalnum()`).
- `validar_nombre_medicamento(nombre)` — Verifica no-vacío.
- `validar_laboratorio_fabricante(laboratorio)` — Verifica no-vacío.
- `validar_entero_positivo(texto)` — Valida enteros > 0 (para stock, días).
- `validar_precio(texto)` — Valida decimales > 0.
- `validar_cobertura(cobertura)` — Valida "Con cobertura" o "Sin cobertura" (case-insensitive).
- `ingresar_codigo()`, `ingresar_medicamento()`, `ingresar_laboratorio()`, `ingresar_precio()`, `ingresar_stock()`, `ingresar_cobertura()`, `ingresar_dias_vencimiento()` — Funciones de ingreso integradas que validan y reintentan en loop hasta entrada válida.

#### `main.py`
Coordina el flujo principal:
1. Carga inventario inicial con `crear_matriz_inicial()`.
2. Menú principal en bucle: muestra opciones, valida entrada, ejecuta operación.
3. Soporta opción 6 (Salir) y opción 8 (salida alternativa).

## Cómo Ejecutar

### Requisitos
- Python 3.x

### Instrucciones

1. Clonar o descargar el repositorio:
   ```bash
   git clone https://github.com/gperezlacaze/TPO-PharmaCare
   cd TPO-PHARMACARE
   ```

2. Ejecutar el programa:
   ```bash
   python main.py
   ```
   o
   ```bash
   python3 main.py
   ```

3. Seguir las instrucciones del menú:
   - **Opción 1:** Registrar nuevo medicamento
   - **Opción 2:** Eliminar medicamento (stock = 0)
   - **Opción 3:** Buscar medicamento por código o nombre
   - **Opción 4:** Modificar stock o precio
   - **Opción 5:** Ver informe general (ordenado por vencimiento)
   - **Opción 6:** Salir del programa
   - **Opción 8:** Salir desde el menú principal (alternativa a opción 6)

4. Para operaciones con confirmación (agregar otro, eliminar otro, modificar otro), responda:
   - `si`, `SI`, `Si` — Afirmativo
   - `no`, `NO`, `No` — Negativo

**Nota:** La opción 8 para salir **solo funciona desde el menú principal**. Si ingresás 8 dentro de una operación (ej: código de medicamento), se tomará como entrada válida, no como comando de salida.

## Medicamentos Iniciales

El sistema carga 5 medicamentos de ejemplo:

| Código | Nombre | Laboratorio | Precio | Stock | Cobertura | Vencimiento |
|--------|--------|-------------|--------|-------|-----------|-------------|
| MED001 | Ibuprofeno 600mg | Roemmers | $2500.00 | 50 | Con cobertura | 180 días |
| FAR125 | Amoxicilina 500mg | Bagó | $1800.00 | 120 | Sin cobertura | 45 días |
| LAB789 | Omeprazol 20mg | Pfizer | $750.00 | 8 | Con cobertura | 365 días |
| FAR140 | Paracetamol 500mg | ISA | $1200.00 | 200 | Sin cobertura | 450 días |
| LAB456 | Metformina 850mg | Roche | $5000.00 | 30 | Con cobertura | 60 días |

## Autores

- **Gonzalo Perez Lacaze** — Módulo de menú, validaciones de confirmación, integración
- **Lucas Alegre** — Módulo de matriz y visualización
- **Lucas Bassi** — Módulo de validaciones e ingreso de datos

## Notas Técnicas

- **Almacenamiento en memoria:** Los datos se mantienen en una **lista de listas (matriz)** en memoria RAM, según requisito de la consigna. Los cambios se pierden al cerrar el programa.
- **Modularización:** Código organizado en módulos separados por responsabilidad (entrada/validación, menú, matriz, main).
- **Algoritmos propios:** Implementación manual de Bubble Sort para ordenamiento (sin uso de `sort()`); copia de matriz original en `informe_general()`.
- **Validación robusta:** Funciones de validación separan lógica de entrada de lógica de presentación (sin `print` en validadores puros).
- **Convenciones:** Adherencia a **PEP 8** y principios del **Zen de Python**.
- **Encoding:** Archivos guardados en **UTF-8** para soporte de caracteres acentuados.

## Licencia

Proyecto académico - UADE 2026.