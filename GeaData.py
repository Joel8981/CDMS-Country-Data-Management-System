#Comenzamos con el trabajo

#Importamos la biblioteca csv para crear csv

import csv

#Importamos la biblioteca os para validar si el archivo csv existe o no

import os



#Creamos el nombre del archivo csv con su extension
CSV = "paises.csv"
#Creamos una lista con los encabezados
encabezados = ["nombre", "poblacion", "superficie", "continente"]

#Creamos otra lista formato matriz para cada una de las filas y columnas de los encabezados
filas_informacion = [["Argentina", 45376763, 45376763, "America"], ["Japon", 125800000,377975, "Asia"], ["Brasil", 213993437, 8515767, "America"], ["Alemania", 83149300, 357022, "Europa"]]


#Validamos si el archivo existe, sino que cree uno nuevo
if os.path.exists(CSV):
    print("El archivo ya existe ")
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
