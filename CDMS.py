# ==============================================================================
# GESTIÓN DE DATOS DE PAÍSES (CSV Y PANDAS)
# Este programa gestiona datos geográficos y demográficos de países
# utilizando la biblioteca estándar 'csv' y la potente biblioteca 'pandas'.
# ==============================================================================

# Importamos la biblioteca csv para crear y manejar archivos de valores separados por comas.
import csv
# Importamos la biblioteca os para validar si el archivo csv existe o no en el sistema de archivos.
import os



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
    found = False

    #Abrimos el archivo en modo lectura para buscar
    with open(CSV, "r") as archivo_Csv:
    
        # Creamos el objeto DictReader.
        #Transformamos cada columna del archivo csv en claves
        lector_diccionario = csv.DictReader(archivo_Csv)

        #
        #Con un bucle recorremos para buscar el pais del usuario
        if opcion == 2:
             print("\n--- LISTA COMPLETA DE PAÍSES ---")
             print("-" * 60)
        
        for filas in lector_diccionario:
            
            #Defini en variables cada clave del diccionario
            nombre_pais = filas["nombre"]
            poblacion = filas["poblacion"]
            superficie = filas["superficie"]
            continente = filas["continente"]

            #Condicional para la opcion 1 (buscar y mostrar el pais buscante)
            if opcion == 1:
                if nombre_pais.lower() == buscar.lower():
                    print("-------------------------------------------------------")
                    print(f" ->> Pais: {nombre_pais} || Poblacion: {poblacion} || Superficie: {superficie} km² || Continente: {continente} ")
                    print("-----------------------------------------------------------")
                    found = True
                    break

            #Este para la opcion 2 (mostrar todos lo paises con su informacion )
            elif opcion == 2:
                print(f" - Pais: {nombre_pais} || Poblacion: {poblacion} || Superficie: {superficie} km² || Continente: {continente} ")
                continue

        if opcion == 1 and not found:
             print(f"\n🚫 País '{buscar}' no encontrado.")
            
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
    Permite al usuario ordenar los datos por la columna seleccionada (nombre, poblacion, superficie)
    utilizando solo el módulo CSV y lógica pura de Python.
    """
    datos_paises = []
    
    # Mapeo de columnas a tipos de dato
    mapeo_tipo = {
        "nombre": str,
        "poblacion": int,
        "superficie": float,
        "continente": str
    }

    try:
        # 1. CARGA DE DATOS (Módulo CSV)
        with open(CSV, mode='r', newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Convertimos explícitamente los campos numéricos a su tipo
                try:
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = float(fila['superficie'])
                    datos_paises.append(fila)
                except ValueError:
                    print(f"⚠️ Advertencia: Fila con datos numéricos inválidos omitida: {fila['nombre']}")
                    continue
                    
    except FileNotFoundError:
        print(f"❌ Error al leer el archivo: {CSV} no fue encontrado.")
        return
    
    # 2. INTERACCIÓN CON EL USUARIO
    print()
    print("--- OPCION DE ORDENAMIENTO ---")
    
    columna_ordenar = input("Ordenar por **(nombre, poblacion, superficie)**: ").lower()
    
    # Validación de la columna
    if columna_ordenar not in ["nombre", "poblacion", "superficie"]:
        print("❌ Columna no válida. Saliendo de la opción de ordenar.")
        return
    
    # 3. MANEJO DE LA DIRECCIÓN
    ascendente = True
    direccion = "ASCENDENTE"
    
    if columna_ordenar in ["poblacion", "superficie"]:
        opcion_dir = input(f"Dirección **(ascendente / descendente)** para {columna_ordenar}: ").lower()
        
        if opcion_dir == "descendente":
            ascendente = False
            direccion = "DESCENDENTE"
        
    print(f"-> Se ordenará por **{columna_ordenar.upper()}** en modo **{direccion}**.")
    
    # 4. ORDENAMIENTO (Usando la función sorted() de Python)
    
    # La clave de ordenamiento es una función lambda que extrae el valor de la columna elegida.
    datos_ordenados = sorted(
        datos_paises, 
        key=lambda pais: pais[columna_ordenar], 
        reverse=not ascendente # reverse=True si queremos descendente
    )
    
    # 5. IMPRESIÓN DE RESULTADOS
    print("\n" + "=" * 80)
    
    # Imprimir encabezados manualmente
    print(f"{'País':<15} | {'Población':>20} | {'Superficie (km²)' :>20} | {'Continente':<10}")
    print("-" * 80)
    
    for pais in datos_ordenados:
        # Formato de salida con separadores de miles (:,)
        pob_f = f"{pais['poblacion']:,.0f}"
        sup_f = f"{pais['superficie']:,.0f}"
        
        print(f"{pais['nombre']:<15} | {pob_f:>20} | {sup_f:>20} | {pais['continente']:<10}")

    print("-" * 80)

# -------------------- ESTADÍSTICAS (Opción 4 - CORREGIDA Y Optimizada con Pandas) --------------------
def mostrar_estadisticas(CSV):
    
    """
    Calcula y muestra estadísticas clave (totales, promedios, extremos y conteo por continente)
    usando solo el módulo CSV y lógica de Python.
    """
    poblacion_total = 0
    superficie_total = 0.0
    conteo_paises = 0  
    
    max_pob = -1
    min_pob = float('inf')
    pais_max = ""
    pais_min = ""
    
    # Diccionario para contar países por continente
    paises_por_continente = {} 
    
    try:
        with open(CSV, mode='r', newline="") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                try:
                    poblacion = int(fila['poblacion'])
                    superficie = float(fila['superficie'])
                    continente = fila['continente']
                    
                    # 1. CÁLCULO DE TOTALES Y CONTEO GLOBAL
                    poblacion_total += poblacion
                    superficie_total += superficie
                    conteo_paises += 1 
                    
                    # 2. AGRUPACIÓN POR CONTINENTE
                    # Si el continente no está en el diccionario, lo inicializa; si ya está, suma 1.
                    if continente in paises_por_continente:
                        paises_por_continente[continente] += 1
                    else:
                        paises_por_continente[continente] = 1
                    
                    # 3. BÚSQUEDA DE MÁXIMOS Y MÍNIMOS
                    if poblacion > max_pob:
                        max_pob = poblacion
                        pais_max = fila['nombre']
                        
                    if poblacion < min_pob:
                        min_pob = poblacion
                        pais_min = fila['nombre']

                except ValueError:
                    # Ignorar filas donde los datos numéricos no son válidos
                    continue
                    
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{CSV}' no fue encontrado.")
        return
    
    # --- CÁLCULO DE PROMEDIOS ---
    poblacion_promedio = 0
    superficie_promedio = 0.0
    
    if conteo_paises > 0:
        poblacion_promedio = poblacion_total / conteo_paises
        superficie_promedio = superficie_total / conteo_paises

    # ------------------ IMPRESIÓN DE RESULTADOS ------------------
    
    ## Totales y Promedios
    print("\n--- RESUMEN ESTADÍSTICO DE PAÍSES ---")
    print("-" * 35)
    
    print(f" Población Total:    {poblacion_total:,.0f} habitantes")
    print(f" Superficie Total:   {superficie_total:,.0f} km²")
    print(f" Población Promedio: {poblacion_promedio:,.2f} habitantes")
    print(f" Sup. Promedio:      {superficie_promedio:,.2f} km²")
    print("-" * 35)
    
    ## Extremos
    print(f" Mayor Población:    {pais_max} ({max_pob:,.0f})")
    print(f" Menor Población:    {pais_min} ({min_pob:,.0f})")
    print("-" * 35)
    
    ## Conteo por Continente
    print("📋 Países Contados por Continente:")
    for continente, conteo in paises_por_continente.items():
        print(f"   -> {continente}: {conteo} países")
    print("-" * 35)

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