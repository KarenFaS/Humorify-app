# Humorify
</div>

<div style="text-align:center">
    <img src="https://github.com/cmingoi/Taller-Humorify/blob/main/imagen.png"/>
</div>


# Proyecto de Aplicación Web para Generación Automática de Posts

Este proyecto se enmarca dentro del módulo de productivización y tiene como objetivo la creación de una aplicación web en Python que genere posts automáticos con humor basados en un modelo preentrenado, en este caso ChatGPT.

## Objetivos

1. **Desarrollar una aplicación web en Python con Flask:**
    - La aplicación debe conectarse a la API de GPT-3 para generar respuestas a preguntas específicas.
    - Debe contar con un front end sencillo pero usable por el usuario.
2. **Almacenar las preguntas, respuestas y fechas correspondientes:**
    - Utilizar una base de datos desplegada en la nube (AWS) para almacenar esta información.
3. **Desplegar la aplicación en Docker:**
    - Asegurarse de que la aplicación se pueda ejecutar en contenedores utilizando Docker.

## El Repositorio en GitHub Contiene:

1. **Aplicación web en Python con Flask:**
    - Código fuente de la aplicación.
    - Estructura del proyecto organizada.
2. **Archivo Dockerfile:**
    - Archivo necesario para desplegar la aplicación en contenedores Docker.
3. **Archivo README:**
    - Instrucciones detalladas para el despliegue de la aplicación en Docker.

## Requisitos Previos

Antes de comenzar con el despliegue, asegúrate de tener instalados los siguientes requisitos:
- `Flask==2.0.2`
- `openai==0.27.0`
- `mysql-connector-python==8.0.26`
- `Werkzeug==2.0.2`
- Cuenta de AWS para la base de datos

## Instrucciones para el Despliegue

1. **Clonar el Repositorio**
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```
2. **Configurar el Entorno Virtual**
    Crea y activa un entorno virtual para gestionar las dependencias del proyecto.
    ```bash
    python3 -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```
3. **Instalar Dependencias**
    Instala las dependencias necesarias usando pip.
    ```bash
    pip install -r requirements.txt
    ```
4. **Configurar Variables de Entorno**
    Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables de entorno:
    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    API_KEY=tu_clave_de_api_de_openai
    DATABASE_URL=tu_url_de_base_de_datos_en_aws
    ```
5. **Ejecutar la Aplicación Localmente**
    Inicia la aplicación Flask.
    ```bash
    flask run
    ```
6. **Construir y Ejecutar el Contenedor Docker**
    Construye la imagen Docker.
    ```bash
    docker build -t nombre_de_tu_imagen .
    ```
    Ejecuta el contenedor Docker.
    ```bash
    docker run -d -p 5000:5000 nombre_de_tu_imagen
    ```
7. **Despliegue en AWS**
    Sigue las instrucciones en la documentación para desplegar la base de datos en AWS y configurar la conexión desde la aplicación Flask.

## Estructura del Proyecto

```plaintext
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── .env
└── templates
    └── index.html

