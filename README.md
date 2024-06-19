# Humorify
</div>

<div style="text-align:center">
    <img src="C:\\Users\\mingo\\Downloads\\HUMORIFY\\Humorify.png.png" alt="Logo" width="250"/>
</div>

Proyecto de Aplicación Web para Generación Automática de Posts
Este proyecto se enmarca dentro del módulo de productivización del bootcamp de data science y tiene como objetivo 
la creación de una aplicación web en Python que genere posts automáticos con humor basados en un modelo preentrenado, en este caso ChatGPT. 

# Objetivos
Desarrollar una aplicación web en Python con Flask:
La aplicación debe conectarse a la API de GPT-3 para generar respuestas a preguntas específicas.
Debe contar con un front end sencillo pero usable por el usuario.
Almacenar las preguntas, respuestas y fechas correspondientes:
Utilizar una base de datos desplegada en la nube (AWS) para almacenar esta información.
Desplegar la aplicación en Docker:
Asegurarse de que la aplicación se pueda ejecutar en contenedores utilizando Docker.

# El repositorio en GitHub contiene:

Aplicación web en Python con Flask:
Código fuente de la aplicación.
Estructura del proyecto organizada.

Archivo Dockerfile:
Archivo necesario para desplegar la aplicación en contenedores Docker.

Archivo README:
Instrucciones detalladas para el despliegue de la aplicación en Docker.

# Requisitos Previos
Antes de comenzar con el despliegue, asegúrate de tener instalados los siguientes requisitos:
Flask==2.0.2
openai==0.27.0
mysql-connector-python==8.0.26
Werkzeug==2.0.2
Cuenta de AWS para la base de datos

# Instrucciones para el Despliegue
1. Clonar el Repositorio
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
2. Configurar el Entorno Virtual
Crea y activa un entorno virtual para gestionar las dependencias del proyecto.
python3 -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
3. Instalar Dependencias
Instala las dependencias necesarias usando pip.
pip install -r requirements.txt
4. Configurar Variables de Entorno
Crea un archivo .env en el directorio raíz del proyecto con las siguientes variables de entorno:
FLASK_APP=app.py
FLASK_ENV=development
API_KEY=tu_clave_de_api_de_openai
DATABASE_URL=tu_url_de_base_de_datos_en_aws
5. Ejecutar la Aplicación Localmente
Inicia la aplicación Flask.
6. Construir y Ejecutar el Contenedor Docker
Construye la imagen Docker.
docker build -t nombre_de_tu_imagen .
Ejecuta el contenedor Docker.
docker run -d -p 5000:5000 nombre_de_tu_imagen
7. Despliegue en AWS
Sigue las instrucciones en la documentación para desplegar la base de datos en AWS y configurar la conexión desde la aplicación Flask.

# Estructura del Proyecto
plaintext
Copiar código
```
├── app.py,
├── Dockerfile
├── requirements.txt
├── README.md
├── .env
└── templates
   └── index.html
```

Documentación del Proceso de Desarrollo y Despliegue
Se adjunta la documentación detallada del proceso de desarrollo y despliegue de la aplicación en el repositorio, donde se explican los siguientes aspectos:

Configuración de Flask y conexión con la API de GPT-3.
Diseño y desarrollo del front end.
Configuración y despliegue de la base de datos en AWS.
Creación y despliegue de contenedores Docker.
