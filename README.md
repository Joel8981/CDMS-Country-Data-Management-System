# 🌐 CDMS: Country Data Management System (Python & Pandas)

## 📝 Descripción del Programa

El **CDMS** implementa un Sistema de Gestión de Datos (SGD) enfocado en el análisis de información geográfica y demográfica de países. El objetivo principal es simular la gestión de un conjunto de datos estático, permitiendo al usuario realizar las operaciones fundamentales de procesamiento de datos: **filtrado**, **ordenamiento** y **cálculo de estadísticas agregadas**.

El desarrollo se realizó en **Python**, utilizando un enfoque modular basado en funciones. Los datos se gestionan a través de un archivo **CSV**, y el procesamiento avanzado en memoria se realiza mediante las librerías **Pandas** y **NumPy**, cruciales para la eficiencia en el análisis numérico de campos como Población y Superficie.

***

## 🚀 Instrucciones de Uso

Para poder ejecutar y utilizar el CDMS, debes seguir dos pasos principales: preparar tu entorno y luego ejecutar el script de Python.

### 1. Preparación del Entorno (Requisitos Previos)

El proyecto requiere **Python 3.x** y las librerías especializadas en análisis de datos.

1.  **Instalar Librerías:** Las funcionalidades de ordenamiento y estadísticas requieren las librerías **Pandas** y **NumPy**. Abre tu terminal o línea de comandos y ejecuta el siguiente comando para instalarlas:

    ```bash
    pip install pandas numpy
    ```

### 2. Ejecución del Programa

1.  **Descargar el Código:**
    * Clona este repositorio en tu máquina local:
      ```bash
      git clone [TU-LINK-AL-REPOSITORIO]
      cd nombre-del-repositorio
      ```
2.  **Iniciar el Script:** Ejecuta el archivo de Python desde la terminal:

    ```bash
    python gestion_paises.py
    ```

3.  **Creación de Archivo CSV:** Al iniciar, el programa crea automáticamente el archivo de datos (`paises.csv`) si no existe, utilizando una muestra inicial de países.

### 3. Interacción con el Menú Principal

El programa opera a través de un **Menú Principal** de consola. Debes ingresar el **número** de la opción deseada (del 1 al 5) y presionar Enter. El sistema incluye manejo de errores básico para entradas no válidas.

***

## 💻 Ejemplos de Entradas y Salidas

### Menú Principal y Funcionalidades

| Opción | Descripción de la Funcionalidad |
| :---: | :--- |
| **1** | Buscar un país específico por su nombre (ej. `argentina`). |
| **2** | Mostrar todos los países de la muestra. |
| **3** | Ordenar los países por `nombre`, `poblacion` o `superficie`. |
| **4** | Mostrar un resumen estadístico global y por continente. |
| **5** | Salir del programa. |

**Salida de Ejemplo (Opción 4: Estadísticas por Continente)**

--- Estadísticas por Continente --- continente Poblacion_Total Superficie_Total Países America 297,616,308 21,280,837 km² 3 Asia 125,800,000 377,975 km² 1 Europa 83,149,300 357,022 km² 1

***

## 👥 Participación de los Integrantes

Este proyecto fue desarrollado como **Trabajo Integrador de Programación** para la Universidad Tecnológica Nacional (UTN) por:

* **Joel Alvarez**
* **Marcos Bermejo**

***

## 🔮 Trabajo Futuro

Se proponen las siguientes mejoras para expandir el alcance del proyecto:

* **Persistencia Avanzada:** Migrar a una base de datos relacional (ej. SQLite o MySQL) para gestionar un mayor volumen de datos y garantizar la integridad.
* **Interfaz Gráfica (GUI):** Desarrollar una interfaz gráfica (utilizando Tkinter o PyQt) para reemplazar la interfaz de consola.
* **Funcionalidad de Edición:** Agregar la capacidad de modificar, crear o eliminar registros de países (operaciones CRUD).
