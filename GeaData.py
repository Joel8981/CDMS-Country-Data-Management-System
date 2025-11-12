#Comenzamos con el trabajo

#Importamos la biblioteca csv para crear csv
import csv

#Importamos la biblioteca os para validar si el archivo csv existe o no
import os

from operator import itemgetter # Una herramienta útil para ordenar por clave de diccionario

#Importamos la biblioteca pandas
import pandas as pd

# -------------------- CORRECCIÓN 1: Datos de Superficie --------------------
def crear_Csv(CSV):
    #Creamos una lista con los encabezados
    encabezados = ["nombre", "poblacion", "superficie", "continente"]

    # Superficie de Argentina corregida a 2,780,400 km² (aprox)
    # y datos de Canadá agregados para mayor variedad.
    filas_informacion = [["Argentina", 45376763, 2780400, "America"], 
                         ["Japon", 125800000, 377975, "Asia"], 
                         ["Brasil", 213993437, 8515767, "America"], 
                         ["Alemania", 83149300, 357022, "Europa"],
                         ["Canada", 38246108, 9984670, "America"]]

    #Validamos si el archivo existe, sino que cree uno nuevo
    if os.path.exists(CSV):
        # print("El archivo ya existe ") # Comentado para no saturar la salida
        return
    else:
        try:
            with open(CSV, "w", newline="") as archivo_csv:
                escribir = csv.writer(archivo_csv)  
                escribir.writerow(encabezados)
                escribir.writerows(filas_informacion)
                print(f"✅ Archivo '{CSV}' creado con éxito.")
                
        except Exception as e:
            print(f"❌ Hubo un error al crear el archivo: {e}")

#Funcion para mostrar opciones con un print
def mostrar_opciones():
    print("\n" + "="*25)
    print(" --- MENU PRINCIPAL ---")
    print("="*25)
    print("""
 -> 1. Buscar pais 🌍
 -> 2. Mostrar todos los Paises 🔎🏙️
 -> 3. Ordenar por (nombre, poblacion o superficie) ⌨️
 -> 4. Salir 🏃‍♂️‍➡️""")

#Creamos esta opcion para el modo lectura de la opcion 1 y 2
# Nota: Renombré 'filtrar_paises' a 'mostrar_paises' para reflejar su uso en opc 2.
def modo_lectura_csv(CSV, opcion, buscar=None):
    found = False
    
    with open(CSV, "r") as archivo_Csv:
        lector_diccionario = csv.DictReader(archivo_Csv)
        
        if opcion == 2:
             print("\n--- LISTA COMPLETA DE PAÍSES ---")
             print("-" * 60)
        
        for filas in lector_diccionario:
            nombre_pais = filas["nombre"]
            poblacion = filas["poblacion"]
            superficie = filas["superficie"]
            continente = filas["continente"]
            
            if opcion == 1:
                if nombre_pais.lower() == buscar.lower():
                    print("-------------------------------------------------------")
                    print(f" ->> País: {nombre_pais} || Población: {poblacion} || Superficie: {superficie} km² || Continente: {continente} ")
                    print("-----------------------------------------------------------")
                    found = True
                    break
            
            elif opcion == 2:
                print(f" - País: {nombre_pais:<9} || Población: {poblacion:>10} || Superficie: {superficie:>10} km² || Continente: {continente} ")
        
        if opcion == 1 and not found:
             print(f"\n🚫 País '{buscar}' no encontrado.")
            
#Funcion para buscar paises
def buscar_pais(CSV, opcion):
    print("\n - Buscar País 🔎🚩")
    buscar = input("Ingresa el nombre del país a buscar: ").capitalize()
    modo_lectura_csv(CSV, opcion, buscar)
    
#Funcion para filtrar paises
def filtrar_paises(CSV, opc):
    print("\n - Mostrar Paises - ")
    modo_lectura_csv(CSV, opc)

# -------------------- OPTIMIZACIÓN EN ordenarpaises --------------------
def ordenar_paises(CSV):
    
    # Manejo de error si el archivo no se lee correctamente
    try:
        df = pd.read_csv(CSV)
    except Exception as e:
        print(f"❌ Error al leer el archivo con Pandas: {e}")
        return
    
    print()
    print("--- OPCION DE ORDENAMIENTO ---")
    
    columna_ordenar = input("Ordenar por **(nombre, poblacion, superficie)**: ").lower()
    
    if columna_ordenar not in df.columns:
        print("❌ Columna no válida. Saliendo de la opción de ordenar.")
        return
    
    # Definir la dirrecion del ordenamiento
    ascendente = True
    direccion = "ASCENDENTE"
    
    # Preguntar la direccion solo si la columna es 'superficie'
    if columna_ordenar == "superficie":
        opcion_dir = input("Dirección **(ascendente / descendente)** para superficie: ").lower()
        
        if opcion_dir == "descendente":
            ascendente = False
            direccion = "DESCENDENTE"
        
    print(f"-> Se ordenará por **{columna_ordenar.upper()}** en modo **{direccion}**.")
    
    # Ordenar el dataFrame
    df_ordenado = df.sort_values(
        by=columna_ordenar,
        ascending=ascendente,
        ignore_index=True)
    
    # Imprimir los resultados ordenados
    print(f"\n--- PAÍSES ORDENADOS por '{columna_ordenar.upper()}' ({direccion}) ---")
    
    # to_string(index=False) elimina los números de fila
    print(df_ordenado.to_string(index=False)) 
    print("-" * 60)
    
# --------------------  Bucle del Menú --------------------
def main(CSV):
    
    while True: # Bucle infinito para repetir el menú
        
        mostrar_opciones()
        
        try:
            opc = int(input("Ingresa el número de opción: "))
            
            if opc == 1:
                buscar_pais(CSV, opc)
            elif opc == 2:
                filtrar_paises(CSV, opc)
            elif opc == 3:
                ordenar_paises(CSV)
            elif opc == 4:
                print("\n👋 Fin del Programa")
                break # Salir del bucle SOLO si se elige la opción 4
            else:
                print("⚠️ Opción no válida. Por favor, ingresa un número del 1 al 4.")
                
        except ValueError:
            print("❌ Error, el dato ingresado no es un número entero válido.")
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado: {e}")
            break # Salir en caso de error grave

# -------- INICIO DEL PROGRAMA PRINCIPAL ------------------
CSV = "paises.csv"
crear_Csv(CSV)
main(CSV)