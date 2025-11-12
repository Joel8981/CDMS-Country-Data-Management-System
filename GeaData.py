# ==============================================================================
# GESTIÓN DE DATOS DE PAÍSES (CSV Y PANDAS)
# Este programa gestiona datos geográficos y demográficos de países
# utilizando la biblioteca estándar 'csv' y la potente biblioteca 'pandas'.
# ==============================================================================

# Importamos la biblioteca csv para crear y manejar archivos de valores separados por comas.
import csv
# Importamos la biblioteca os para validar si el archivo csv existe o no en el sistema de archivos.
import os

# Importamos la biblioteca pandas (alias 'pd'), crucial para el manejo eficiente de datos tabulares,
# incluyendo ordenamiento y estadísticas.
import pandas as pd
# Importamos numpy para el manejo eficiente de operaciones numéricas, a menudo usado junto a Pandas.
import numpy as np 

# -------------------- CREACIÓN DE DATOS Y ARCHIVO CSV --------------------
def crear_Csv(CSV):
    """
    Crea el archivo CSV inicial si no existe, con los datos de ejemplo.
    :param CSV: Nombre del archivo CSV a crear.
    """
    # Lista de encabezados que serán los nombres de las columnas.
    encabezados = ["nombre", "poblacion", "superficie", "continente"]

    # Definición de los datos de los países. Las columnas 'poblacion' y 'superficie'
    # deben contener valores numéricos para el análisis posterior.
    filas_informacion = [["Argentina", 45376763, 2780400, "America"], 
                         ["Japon", 125800000, 377975, "Asia"], 
                         ["Brasil", 213993437, 8515767, "America"], 
                         ["Alemania", 83149300, 357022, "Europa"],
                         ["Canada", 38246108, 9984670, "America"]]

    # Validación: Si el archivo existe, la función termina para no sobrescribir los datos.
    if os.path.exists(CSV):
        return
    else:
        try:
            # Abre el archivo en modo escritura ('w').
            # 'newline=""' es una práctica recomendada para evitar líneas en blanco adicionales,
            # especialmente en sistemas Windows.
            with open(CSV, "w", newline="") as archivo_csv:
                escribir = csv.writer(archivo_csv)  
                # Escribe la primera fila con los nombres de los encabezados.
                escribir.writerow(encabezados)
                # Escribe todas las filas de datos.
                escribir.writerows(filas_informacion)
                print(f"✅ Archivo '{CSV}' creado con éxito.")
                
        except Exception as e:
            print(f"❌ Hubo un error al crear el archivo: {e}")

# -------------------- FUNCIONES DE INTERFAZ DE USUARIO --------------------

def mostrar_opciones():
    """Imprime el menú principal en la consola."""
    print("\n" + "="*25)
    print(" --- MENU PRINCIPAL ---")
    print("="*25)
    print("""
 -> 1. Buscar país 🌍
 -> 2. Mostrar todos los Países 🔎🏙️
 -> 3. Ordenar por (nombre, poblacion o superficie) ⌨️
 -> 4. Mostrar estadísticas 🧮
 -> 5. Salir 🏃‍♂️‍➡️""")

# -------------------- MODO LECTURA Y FILTRADO (Opciones 1 y 2) --------------------
def modo_lectura_csv(CSV, opcion, buscar=None):
    """
    Carga el CSV usando Pandas y realiza la búsqueda o muestra todos los datos.
    :param CSV: Nombre del archivo.
    :param opcion: 1 para buscar, 2 para mostrar todo.
    :param buscar: Nombre del país a buscar (solo usado si opcion == 1).
    """
    try:
        # Cargamos el CSV en un DataFrame de Pandas para operaciones sencillas de filtrado.
        df = pd.read_csv(CSV)
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return

    if opcion == 1:
        # Filtramos el DataFrame donde el nombre del país (en minúsculas) coincida con la búsqueda.
        pais_buscado = df[df['nombre'].str.lower() == buscar.lower()]
        
        if not pais_buscado.empty:
            print("-------------------------------------------------------")
            # Obtenemos la primera fila (iloc[0]) del resultado.
            fila = pais_buscado.iloc[0]
            # Imprimimos los detalles, usando formato de miles (:,) para números grandes.
            print(f" ->> País: {fila['nombre']} || Población: {fila['poblacion']:,} || Superficie: {fila['superficie']:,} km² || Continente: {fila['continente']} ")
            print("-------------------------------------------------------")
        else:
            print(f"\n🚫 País '{buscar}' no encontrado.")
            
    elif opcion == 2:
        print("\n--- LISTA COMPLETA DE PAÍSES ---")
        print("-" * 60)
        # to_string(index=False) imprime el DataFrame sin los índices de fila de Pandas, mejorando la presentación.
        print(df.to_string(index=False))
        print("-" * 60)
            
def buscar_pais(CSV):
    """Pide el nombre del país y llama a la función de lectura/filtrado."""
    print("\n - Buscar País 🔎🚩")
    # .strip() elimina espacios en blanco al inicio/final de la entrada.
    buscar = input("Ingresa el nombre del país a buscar: ").strip() 
    if buscar:
        modo_lectura_csv(CSV, 1, buscar)
    else:
        print("El nombre del país no puede estar vacío.")
    
def filtrar_paises(CSV):
    """Muestra la lista completa de países."""
    modo_lectura_csv(CSV, 2)

# -------------------- ORDENAMIENTO (Opción 3 - Pandas) --------------------
def ordenar_paises(CSV):
    """
    Permite al usuario ordenar los datos por la columna seleccionada (nombre, poblacion, superficie).
    """
    try:
        df = pd.read_csv(CSV)
    except Exception as e:
        print(f"❌ Error al leer el archivo con Pandas: {e}")
        return
    
    print()
    print("--- OPCION DE ORDENAMIENTO ---")
    
    columna_ordenar = input("Ordenar por **(nombre, poblacion, superficie)**: ").lower()
    
    # Validación de que la columna existe en el DataFrame.
    if columna_ordenar not in df.columns:
        print("❌ Columna no válida. Saliendo de la opción de ordenar.")
        return
    
    # Manejo de la dirección de ordenamiento.
    ascendente = True
    direccion = "ASCENDENTE"
    
    # Preguntamos la dirección solo si la columna es numérica (poblacion o superficie).
    if columna_ordenar in ["poblacion", "superficie"]:
        opcion_dir = input(f"Dirección **(ascendente / descendente)** para {columna_ordenar}: ").lower()
        
        if opcion_dir == "descendente":
            ascendente = False
            direccion = "DESCENDENTE"
        
    print(f"-> Se ordenará por **{columna_ordenar.upper()}** en modo **{direccion}**.")
    
    # df.sort_values es el método de Pandas para ordenar.
    df_ordenado = df.sort_values(
        by=columna_ordenar, # Columna por la que ordenar.
        ascending=ascendente, # True para ascendente, False para descendente.
        ignore_index=True) # Resetea el índice después de ordenar.
    
    # ... (código para imprimir resultados) ...
    print(df_ordenado.to_string(index=False)) 
    print("-" * 60)

# -------------------- ESTADÍSTICAS (Opción 4 - CORREGIDA Y Optimizada con Pandas) --------------------
def mostrar_estadisticas(CSV):
    """
    Calcula y muestra estadísticas clave (máximos, mínimos, totales) usando Pandas.
    Esta función es la que más se beneficia de la eficiencia de Pandas.
    """
    try:
        df = pd.read_csv(CSV)
        # Conversión explícita a numérico para asegurar cálculos correctos. 
        # Esto es vital, ya que Python leería estos campos como cadenas por defecto del CSV.
        df['poblacion'] = pd.to_numeric(df['poblacion'], errors='coerce')
        df['superficie'] = pd.to_numeric(df['superficie'], errors='coerce')
    except Exception as e:
        print(f"❌ Error al cargar datos para estadísticas: {e}")
        return

    print("\n--- RESUMEN ESTADÍSTICO DE PAÍSES ---")
    print("-" * 40)
    
    # 1. Población Total (usando df['columna'].sum())
    poblacion_total = df['poblacion'].sum()
    print(f"🌎 Población Total (Muestra): {poblacion_total:,.0f} habitantes") # Formato con separadores de miles

    # 2. Máximos y Mínimos (usando idxmax/idxmin)
    # idxmax() devuelve el índice de la fila que contiene el valor máximo.
    idx_max_pob = df['poblacion'].idxmax()
    pais_max_pob = df.loc[idx_max_pob] # df.loc[] recupera la fila completa por índice.
    
    idx_min_pob = df['poblacion'].idxmin()
    pais_min_pob = df.loc[idx_min_pob]
    
    print(f"⬆️ Mayor Población: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']:,.0f})")
    print(f"⬇️ Menor Población: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']:,.0f})")

    # 3. Agrupación por Continente (usando groupby)
    print("\n--- Estadísticas por Continente ---")
    # Agrupamos por la columna 'continente' y aplicamos funciones de agregación (sumar, contar).
    resumen_continente = df.groupby('continente').agg(
        Poblacion_Total=('poblacion', 'sum'),
        Superficie_Total=('superficie', 'sum'),
        Países=('nombre', 'size') # size cuenta cuántos elementos hay en cada grupo.
    ).reset_index()

    # Formateamos los resultados para una mejor lectura en la salida.
    resumen_continente['Poblacion_Total'] = resumen_continente['Poblacion_Total'].apply(lambda x: f"{x:,.0f}")
    resumen_continente['Superficie_Total'] = resumen_continente['Superficie_Total'].apply(lambda x: f"{x:,.0f} km²")
    
    print(resumen_continente.to_string(index=False))
    print("-" * 40)


# -------------------- BUCLE PRINCIPAL DEL PROGRAMA --------------------
def main(CSV):
    """Función principal que ejecuta el bucle del menú."""
    while True: # Bucle infinito hasta que se selecciona la opción de salida (5).
        mostrar_opciones()
        
        try:
            # Capturamos la entrada del usuario y la convertimos a entero.
            opc = int(input("Ingresa el número de opción: "))
        except ValueError:
            # Manejamos el error si el usuario ingresa texto en lugar de un número.
            print("⚠️ Entrada no válida. Por favor, ingresa un número.")
            continue # Vuelve al inicio del bucle.
        
        # Lógica de enrutamiento del menú.
        if opc == 1:
            buscar_pais(CSV)
        elif opc == 2:
            filtrar_paises(CSV)
        elif opc == 3:
            ordenar_paises(CSV)
        elif opc == 4:
            mostrar_estadisticas(CSV)
        elif opc == 5:
            print("\n👋 Fin del Programa")
            break # Sale del bucle 'while True' y termina el programa.
        else:
            print("⚠️ Opción no válida. Por favor, ingresa un número del 1 al 5.")

# -------- INICIO DEL PROGRAMA PRINCIPAL ------------------
CSV = "paises.csv"
# Paso 1: Asegurar que el archivo de datos existe.
crear_Csv(CSV)
# Paso 2: Iniciar la interacción con el usuario.
main(CSV)