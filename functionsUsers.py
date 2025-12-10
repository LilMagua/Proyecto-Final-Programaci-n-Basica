# Funciones para CRUD de usuarios
# Menu de ingreso
# Verficar que el dato ingresado por el usuario este en un rango especifico
# Guardar usuario
# Verificar que el nombre ingresado por el usuario sea correcto
# Verificar que la edad ingresada por el usuario sea correcto
# Verificar que la contraseña ingresada por el usuario sea correcto
# Ingresar usuario
# Salir de la aplicacion

import sys

def menu_ingreso():
    # Bienvenida a la plataforma
    print("### Bienvenido a la plataforma ###")
    print("¿Qué deseas hacer?")
    # Dar opciones
    print("Opción #1 Registrarse")
    print("Opción #2 Ingresar")
    print("Opción #3 Salir")

# Revisar que el numero ingresado por el usuario este en el rango de las opciones
def revisar_rango(opcionSeleccionada, numInicio, numFinal):
    try:
        numero = int(opcionSeleccionada)

        if numInicio <= numero <= numFinal:
            return numero   # devuelve el número válido
        else:
            print("El número ingresado no está dentro del rango.")
            return False

    except ValueError:
        print("Lo ingresado no es un número entero.")
        return False
    

### Funciones para registrar usuario
def guardar_usuario(nombre, edad, contrasena, archivo):
    f = open(archivo, "a") # O tambien podemos usar with open(archivo, "a") as f:  
    # "a" = Añadir (append) al final
    linea = f"{nombre}|{contrasena}|{edad}\n"
    f.write(linea)
    f.close() 
    print("##################################");
    print("Usuario registrado correctamente.\n");
    print("##################################");

    menu_ingreso();

# FALTA VERIFICACION DE QUE NO EXISTE OTRO USUARIO CON ESE NOMBRE
def registrar_nombre():
    while (True):
        nombre = input("Digita tu nombre de usuario. \n")
        if (len(nombre) >= 3 and len(nombre) <= 10):
            return nombre;
        else:    
            print("Tu nombre de usuario debe tener entre 3 y 10 caracteres. \n")

def registrar_edad():
    while (True):
        edad = input("Digita tu edad. \n")
        try:
            numero = int(edad) 
            if (numero > 5 and numero < 100):           
                return edad;
            else:
                print("Tu edad debe estar entre 5 y 100.");                  
        except:
            print("No ingresaste un numero, intenta de nuevo.")      

def registrar_contrasena():
    while(True):
        contrasena = input("Digita tu contraseña. \n");

        if(len(contrasena) < 3 or len(contrasena) > 10):
            print("La contraseña debe tener entre 3 y 10 caracteres.");
            continue  # Vuelve al inicio del while y pide de nuevo la contraseña
        
        contrasenaConfirmar = input("Confirma tu contraseña. \n");

        if(contrasena != contrasenaConfirmar):
            print("Las contraseñas no coinciden.");    

        if(contrasena == contrasenaConfirmar and len(contrasena) >= 3 and len(contrasena) <= 10): 
            return contrasena;

### Editar usuario (solo el usuario actualmente ingresado)
def editar_usuario(usuario_actual, archivo):
    try:
        # Abrir archivo en modo lectura
        f = open(archivo, "r")
        lineas = f.readlines()
        f.close()

        nuevas_lineas = []
        usuario_encontrado = False

        # Buscar el usuario que se desea editar
        for linea in lineas:
            nombre, contrasena, edad = linea.strip().split("|")

            if nombre == usuario_actual:
                usuario_encontrado = True

                # Pedir nuevos valores
                nuevo_nombre = registrar_nombre()
                nueva_contrasena = registrar_contrasena()
                nueva_edad = registrar_edad()

                # Crear la nueva línea con los datos actualizados
                nueva_linea = f"{nuevo_nombre}|{nueva_contrasena}|{nueva_edad}\n"
                nuevas_lineas.append(nueva_linea)
            else:
                # Mantener los demás usuarios exactamente igual
                nuevas_lineas.append(linea)

        if usuario_encontrado == False:
            print("Error: No se encontró el usuario para editar.")
            return False

        # Guardar todo nuevamente en el archivo
        f = open(archivo, "w")
        f.writelines(nuevas_lineas)
        f.close()

        print("##################################")
        print("Usuario editado correctamente.")
        print("##################################")

        # Retornar el nuevo nombre por si cambió
        return nuevo_nombre

    except FileNotFoundError:
        print("Error: el archivo de usuarios no existe.")
        return False
        
  
### Funciones para ingresar
nombre = "";
def ingresar_usuario(archivo):

    usuarioIngresado = input("Digita tu nombre de usuario. \n")
    contrasenaIngresada = input("Digita tu contraseña. \n")

    try:
        # Abrir archivo en modo lectura
        f = open(archivo, "r")
        lineas = f.readlines()
        f.close()

        # Buscar usuario
        for linea in lineas:
            nombre, contrasena, edad = linea.strip().split("|") # Strip para quitar el salto de linea y split para separar por |

            if usuarioIngresado == nombre:
                # Usuario encontrado → Validar contraseña
                if contrasenaIngresada == contrasena:
                    print(f"Bienvenido {nombre}, sesión iniciada correctamente.")
                    return nombre;
                else:
                    print("Contraseña incorrecta.")
                    return False

        # Se busco en todo el listado y no se encontro el usuario
        print("El usuario no existe.")
        return False

    except FileNotFoundError:
        print("Error: el archivo de usuarios no existe.")
        return False
    
def salir():
    print("Saliendo del programa...")
    sys.exit()