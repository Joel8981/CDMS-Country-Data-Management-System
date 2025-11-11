#Comenzamos con el trabajo

#Importamos la biblioteca csv para crear csv

import csv

#Importamos la biblioteca os para validar si el archivo csv existe o no

import os

#Creamos el csv si no existe
def crear_Csv(CSV):
    #Creamos una lista con los encabezados
    encabezados = ["nombre", "poblacion", "superficie", "continente"]

    #Creamos otra lista formato matriz para cada una de las filas y columnas de los encabezados
    filas_informacion = [["Argentina", 45376763, 45376763, "America"], ["Japon", 125800000,377975, "Asia"], ["Brasil", 213993437, 8515767, "America"], ["Alemania", 83149300, 357022, "Europa"]]


    #Validamos si el archivo existe, sino que cree uno nuevo
    if os.path.exists(CSV):
        print("El archivo ya existe ")
        return
    else:
        
        #Usamos excepciones si al crear el archivo hay un error
        try:
            #Aqui creamos el archivo especificando la dirrecion, metodo de escritura
            with open(CSV, "w", newline="") as archivo_csv:
            
                escribir = csv.writer(archivo_csv)  
                escribir.writerow(encabezados)
                escribir.writerows(filas_informacion)
                
        except:
            print("Hubo un error al crear el archivo.")

#Funcion para mostrar opciones con un print
def mostrar_opciones():
    
    print(" --- MENU PRINCIPAL ---")
    print("""
   -> 1. Buscar pais 🌍
   -> 2. Filtrar Paises 🔎🏙️
   -> 3. Ordenar por (nombre, poblacion o superficie) ⌨️
   -> 4. Mostrar estadisticas 🧮
   -> 5. Salir 🏃‍♂️‍➡️""")
    
def buscar_pais(CSV):
    
    print(" - Buscar Pais 🔎🚩")
    
    #Le pedimos el pais a buscar
    buscar = input("Ingresa el nombre del pais a buscar: ").capitalize()
    
    try:
        #Abrimos el archivo en modo lectura para buscar
        with open(CSV, "r") as archivo_Csv:
        
            # Creamos el objeto DictReader.
            #Transformamos cada columna del archivo csv en claves
            lector_diccionario = csv.DictReader(archivo_Csv)
            
            #
            #Con un bucle recorremos para buscar el pais del usuario
            for filas in lector_diccionario:
                
                #Defini en variables cada
                nombre_pais = filas["nombre"]
                poblacion = filas["poblacion"]
                superficie = filas["superficie"]
                continente = filas["continente"]
                if nombre_pais == buscar:
                    print("-------------------------------------------------------")
                    print(f" ->> Pais: {nombre_pais} || Poblacion: {poblacion} || Superficie: {superficie}km² || Continente: {continente} ")
                    print("-----------------------------------------------------------")
                    break
    except:
        print("Error, El dato ingresado no corresponde a un pais")
                
#Creamos el menu
def main(CSV):
    
    #Creamos un bucle para darle al usuario que interactue tantas veces como quiera
    while True:
        
        #Llamamos a una funcion que nos mostrara el menu principal
        mostrar_opciones()
        
        
        
        try:
            #Le pedimos el numero de opcion al usuario
            opc = int(input("Ingresa el numero de opcion: "))
            
            #Condicional para llamar a las funciones segun lo que quiera el usuario
            if opc == 1:
                buscar_pais(CSV)
            
            break
        except:
            print("❌ Error, el dato ingresado no corresponde a una opcion")

#  -------- INICIO DEL PROGRAMA PRINCIPAL ------------------
#Creamos el nombre del archivo csv con su extension
CSV = "paises.csv"

#Funcion para crear csv si no existe
crear_Csv(CSV)

#Llamamos a la funcion del menu
main(CSV)