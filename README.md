# 🌍 Sistema de Gestión de Datos de Países (Python & Pandas)

## 📝 Descripción del Programa

Este proyecto implementa un Sistema de Gestión de Datos (SGD) enfocado en información geográfica y demográfica de países. El sistema simula la gestión de un conjunto de datos estático, permitiendo realizar operaciones fundamentales de análisis de datos como **filtrado**, **ordenamiento** y **cálculo de estadísticas agregadas**.

El desarrollo se realizó en **Python** utilizando un enfoque modular basado en **funciones**. La persistencia de los datos se maneja a través de un archivo **CSV**, y el procesamiento avanzado de los datos en memoria se realiza mediante las librerías **Pandas** y **NumPy**, asegurando la eficiencia en las operaciones de análisis y la correcta gestión de los **tipos numéricos** de `Población` y `Superficie`.

***

## 🚀 Instrucciones de Uso

Para poder ejecutar y utilizar el Sistema de Gestión de Datos de Países, sigue los siguientes pasos:

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

El programa opera a través de un **Menú Principal** de consola. Debes ingresar el **número** de la opción deseada (del 1 al 5) y presionar `Enter`. El sistema incluye manejo de errores para entradas no válidas.

***

## 💻 Ejemplos de Entradas y Salidas

### Menú Principal y Búsqueda

| Opción | Funcionalidad |
| :---: | :--- |
| **1** | Buscar un país específico por su nombre (ej. `argentina`). |
| **3** | Ordenar los países por `nombre`, `poblacion` o `superficie`. |
| **4** | Mostrar un resumen estadístico. |

**Salida de Ejemplo (Opción 1: Buscar)**
***

## 👥 Participación de los Integrantes

Este proyecto fue desarrollado como Trabajo Integrador de Programación para la Universidad Tecnológica Nacional (UTN) por:

* **Joel Alvarez**
* **Marcos Bermejo**

***

## 🔮 Trabajo Futuro

Se proponen las siguientes mejoras para expandir el alcance del proyecto:

* **Migración a Base de Datos:** Migrar a una base de datos relacional (ej. SQLite o MySQL) para gestionar un mayor volumen de datos.
* **Interfaz Gráfica (GUI):** Desarrollar una interfaz gráfica (utilizando Tkinter o PyQt) para reemplazar la interfaz de consola.
* **Funcionalidad de Edición:** Agregar la capacidad de modificar, crear o eliminar registros de países (operaciones CRUD).
