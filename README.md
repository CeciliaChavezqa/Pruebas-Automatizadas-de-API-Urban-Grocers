# Proyecto Pruebas Automatizadas de API Urban Grocers
## Proyecto Sprint 8 del Bootcamp QA Engineer de TripleTen

Este proyecto consiste en la automatización de pruebas para el campo `name` en la solicitud de creación de un kit de productos de la aplicación **Urban Grocers**. El objetivo es validar que la API responda correctamente según las especificaciones técnicas proporcionadas en la documentación de la aplicación.

---
## 📝 Descripción del Proyecto

Este proyecto automatiza la validación del proceso de creación de kits personalizados en la plataforma **Urban Grocers**. La lógica de automatización se centra en el endpoint de la API encargado de recibir los nombres de los nuevos kits, asegurando que el sistema gestione correctamente tanto las entradas válidas como las excepciones de seguridad y formato.

A través de este proyecto, se implementa un flujo completo de pruebas que incluye:
1. **Generación dinámica de usuarios**: Creación de una cuenta nueva para cada ejecución para obtener tokens de autorización únicos.
2. **Pruebas de Caja Negra**: Verificación de límites de caracteres, tipos de datos y manejo de errores mediante el envío de solicitudes HTTP.
3. **Validación de Respuestas**: Comprobación de códigos de estado (201 Created, 400 Bad Request) y la integridad de los datos devueltos en el cuerpo de la respuesta.

Es una herramienta esencial para garantizar la estabilidad de la API antes de cada despliegue, reduciendo el margen de error manual en las pruebas de regresión.
## 🛠 Precondiciones

Antes de comenzar, asegúrate de tener instalado y configurado lo siguiente:

1.  **Git Bash**: Para la gestión del repositorio.
2.  **Python**: Versión 3.x instalada.
3.  **Clonación del Repositorio**:
    ```bash
    git clone git@github.com:tu_usuario/qa-project-Urban-Grocers-app-es.git
    ```
4.  **Librerías de Python**: Instala las dependencias necesarias utilizando pip:
    ```bash
    pip install pytest requests
    ```

---

## 📋 Contenido del Proyecto

El proyecto se enfoca en verificar las reglas de negocio para el kit de productos (endpoint `POST /api/v1/kits`). La lista de comprobación incluye:

* Validación de número de caracteres (límites permitidos de 1 a 511).
* Validación de caracteres especiales y espacios.
* Validación de tipos de datos (números permitidos como string).
* Pruebas de error (campos vacíos, parámetros ausentes o tipos de datos incorrectos como números enteros).

---

## 🏗 Estructura del Proyecto

El archivo principal y los archivos de soporte deben seguir esta lógica:

* `data.py`: Contiene los diccionarios de datos necesarios para las solicitudes (cuerpos de solicitud, encabezados).
* `configuration.py`: Almacena la URL base del servidor y las rutas de los endpoints (URL_SERVICE, KITS_PATH, etc.).
* `sender_stand_request.py`: Contiene las funciones para enviar solicitudes `POST` a la API. Incluye la lógica para crear un nuevo usuario y obtener el `authToken`.
* `create_kit_test.py`: Contiene las pruebas automatizadas (funciones que empiezan con `test_`) que ejecutan cada caso de la lista de comprobación.

---

## 🚀 Guía de Ejecución y Flujo de Trabajo

Sigue estas instrucciones detalladas para configurar el entorno, comprender la arquitectura del código y ejecutar la suite de pruebas automatizadas.

### 📌 Especificaciones del Entorno (Versiones Utilizadas)
Para asegurar la compatibilidad y evitar errores de ejecución, este proyecto utiliza de manera estricta las siguientes tecnologías:
* **Python:** v3.14 (Entorno virtual `.venv` configurado)
* **pytest:** v7.4.x
* **requests:** v2.31.x
* **IDE Recomendado:** PyCharm

---

### 🛠️ Flujo de Trabajo del Equipo: ¿Cómo añadir y definir una nueva prueba?

Para mantener la consistencia y el orden del framework, cualquier miembro del equipo que necesite automatizar un nuevo caso de la lista de comprobación debe seguir obligatoriamente este flujo de 2 pasos:

#### Paso 1: Declarar el valor de la prueba en `data.py`
No se deben usar valores estáticos (*hardcoded*) dentro de las pruebas. Primero, abre el archivo `data.py` y declara la variable con la cadena o el tipo de dato exacto que vas a evaluar en el cuerpo de la solicitud (`kit_body`).
* *Ejemplo en `data.py`:*
    ```python
    Numero_caracteres_min_permitido = "a"
    Caracteres_especiales = "№%@"
    ```

#### Paso 2: Definir y programar la prueba en `create_kit_name_test.py`
Una vez declarada la variable de datos, dirígete a `create_kit_name_test.py` para construir la lógica de tu caso de prueba:
1.  Genera el cuerpo del kit dinámicamente llamando a la función auxiliar `get_kit_body()` y pasándole como argumento la variable que creaste en el paso anterior (`data.Numero_caracteres_min_permitido`).
2.  Utiliza las funciones de aserción predefinidas (`possitive_assert` para esperar un código de estado `201` o `negative_assert` para un código `400`) para evaluar el resultado de forma limpia.
* *Ejemplo de estructura en `create_kit_name_test.py`:*
    ```python
    def test_1_nombre_del_kit_con_1_caracter():
        current_kit_body = get_kit_body(data.Numero_caracteres_min_permitido)
        possitive_assert(current_kit_body)
    ```

---

### 🏃‍♂️ Pasos para Ejecutar el Proyecto desde Cero

#### Paso 1: Clonar el Repositorio
Abre tu terminal (Git Bash o la terminal integrada de PyCharm) y clona el proyecto en tu máquina local:
bash
git clone git@github.com: tu_usuario/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es

## 🚀 Ejecución

Para correr las pruebas, sigue estos pasos:

1.  **Inicia el servidor** en la plataforma de TripleTen para obtener la URL activa.
2.  **Actualiza la URL** en el archivo `configuration.py` si es necesario.
3.  **Ejecuta las pruebas** desde la terminal de PyCharm o Git Bash usando el comando:
    ```bash
  

## 🧪 Casos de Prueba Cubiertos

Se automatizaron 9 casos de prueba basados en la lista de comprobación:
1. Valor mínimo de caracteres (1).
2. Valor máximo de caracteres (511).
3. Menos del mínimo (0 caracteres).
4. Más del máximo (512 caracteres).
5. Uso de caracteres especiales.
6. Uso de espacios en el nombre.
7. Uso de números como cadena de texto.
8. Parámetro `name` ausente en la solicitud.
9. Tipo de parámetro incorrecto (número en lugar de string).
 
👤 Autor
Cecilia Mena Chavez | Ingeniera en Tecnología Automotriz | QA Engineer "Transformando la precisión técnica en software confiable."
