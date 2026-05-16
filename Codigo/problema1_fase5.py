
'''
Problema 1: Una matriz almacena datos de sesiones de clientes con el formato:
[ID Cliente, Duración (segundos), Eventos Clics].
Se necesita una herramienta para evaluar el nivel de compromiso de cada sesión.

Requisitos de Desarrollo:
- Datos Iniciales: Una matriz con al menos 5 filas de datos.
- Módulos: Se requiere un módulo (función) para calcular la clasificación de
compromiso de una sesión basándose en su duración y clics.
- Lógica de Negocio:
  ✓ Clasificar como "Alto" (si Duración > 180s y Clics > 8).
  ✓ Clasificar como "Bajo" (si Duración < 60s o Clics < 3).
  ✓ Clasificar como "Medio" en todos los demás casos.
- Salida: Generar un informe listando el ID del cliente y su clasificación final.
'''

# Declaro CONSTANTES para los límites a evaluar
DURACION_ALTA = 180
CLICS_ALTOS = 8

DURACION_BAJA = 60
CLICS_BAJOS = 3

# Declaro una Lista de listas para crear la MATRIZ con 5 filas
# Formato de cada fila: [ID Cliente, Duración (segundos), Eventos Clics]
MATRIZ_SESIONES = [
    [101, 220, 12],  # Duración > 180 Y Clics > 8 -> Alto
    [102, 45, 1],    # Duración < 60 O Clics < 3 -> Bajo
    [103, 120, 5],   # No cumple ninguna de las anteriores -> Medio
    [104, 190, 2],   # Duración es alta, pero clics < 3 -> Bajo
    [105, 80, 6]     # No cumple ninguna de las anteriores -> Medio
]

def evaluar_compromiso(duracion, clics):
    """
    Determina el nivel de compromiso de una sesión.

    Recibe la duración y los clics, y aplica las reglas de negocio
    para retornar "Alto", "Bajo" o "Medio".
    """
    if duracion > DURACION_ALTA and clics > CLICS_ALTOS:
        resultado = "Alto"

    elif duracion < DURACION_BAJA or clics < CLICS_BAJOS:
        resultado = "Bajo"

    else:
        resultado = "Medio"

    return resultado

def generar_informe(matriz_datos):
    """
    Recorre la matriz de sesiones y genera el informe final en consola.
    """
    print("========================================")
    print("     INFORME DE COMPROMISO DE CLIENTES   ")
    print("========================================")
    print(f"{'ID CLIENTE':<15} | {'CLASIFICACIÓN':<15}")
    print("----------------------------------------")

    # Recorro la matriz fila por fila usando un ciclo for
    for fila in matriz_datos:

        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]

        clasificacion = evaluar_compromiso(duracion, clics)

        print(f"{id_cliente:<15} | {clasificacion:<15}")

    print("========================================")

# LLAMO A LA FUNCIÓN PRINCIPAL
generar_informe(MATRIZ_SESIONES)