📘 Sistema de Usuarios y Notas (Python)

Link del Manual de usuario -> https://drive.google.com/file/d/1Z2hiJnjSVxzuLA6SFq8EaMaTTIcnXu-2/view?usp=sharing

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar usuarios y notas utilizando archivos de texto como almacenamiento simple. No requiere librerías externas ni bases de datos.

🚀 Características principales

👤 Gestión de usuarios
Registro de usuarios
Validación de nombre, edad y contraseña
Inicio de sesión
Edición del usuario actualmente autenticado
Salida del sistema

📝 Gestión de notas
Los usuarios pueden:
Crear notas
Ver solo sus notas
Editar notas
Eliminar notas
Cada nota tiene un ID autogenerado (en la posición 0 del registro)  

📁 Estructura del proyecto
Proyecto/
├── main.py # Archivo principal
├── functionsUsers.py # CRUD de usuarios
├── functionsNotes.py # CRUD de notas
├── config.py # Rutas a los archivos de almacenamiento
├── usuarios.txt # Archivo donde se guardan usuarios
└── notas.txt # Archivo donde se guardan notas

📦 Archivos utilizados
usuarios.txt

Formato por línea:
nombre|contrasena|edad

notas.txt

Formato por línea:
id|usuario|nombreNota|informacion

▶️ Cómo ejecutar el programa

Clonar el repositorio:
git clone https://github.com/LilMagua/Proyecto-Final-Programaci-n-Basica.git

Entrar al proyecto:
cd Proyecto-Final-Programaci-n-Basica

Ejecutar el programa:
python3 main.py

(No se requieren librerías externas)

🧠 Funcionamiento general
Menú principal
Registrarse
Ingresar
Salir

Menú del sistema después de iniciar sesión
Crear nota
Ver notas
Editar nota
Eliminar nota
Editar usuario
Salir

📌 Validaciones
Usuarios
Nombre: 3 a 10 caracteres
Edad: entre 5 y 100
Contraseña: 3 a 10 caracteres y confirmación

Notas
Título: 3 a 15 caracteres
Contenido: 3 a 50 caracteres
IDs autogenerados y únicos

🛠️ Tecnologías utilizadas
Python 
Archivos .txt como persistencia

👨‍💻 Autores
Javier Alexander Buitrago Torres
Airann Estiben Yepes Barrera