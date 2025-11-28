# Confirmar que el numero ingresado sea 1 o 2 
ingreso = False;

# Este while se realiza, por posible error humano, siempre seguir preguntando (Mostrando opciones)
while(ingreso == False):
    # Bienvenida a la plataforma
    print("Bienvenido a la plataforma");
    print("¿Que deseas hacer?");
    # Dar opciones
    print("Opcion #1 Ingresar");
    print("Opcion #2 Registrarse");
    opcionSeleccionada = input("");

    # Intentar convertir la entrada del usuario en un int
    try:
        opcionSeleccionadaNumero = int(opcionSeleccionada)
        if(opcionSeleccionadaNumero == 1 or opcionSeleccionadaNumero == 2):
            print("Es valido");
            ingreso = True;
        else:
            print("El numero ingresado no es un numero valido");
    except ValueError:
        print("Lo ingresado no fue un numero entero")


# Ingresar usuario
if(opcionSeleccionadaNumero == 1):
    print("Formulario para iniciar sesión");
    usuarioIngresado = input("");
    contrasenaIngresado = input("");

    with open("archivo.txt", "a") as file:
        file.write("\nNueva línea agregada")


# Registrar usuario
if(opcionSeleccionadaNumero == 2):
# Usuarigo digita su nombre

    print("Formulario para registrarse");
    nombre=""
    while (nombre == ""):
        nombre = input("Digita tu nombre de usuario ")
    if (nombre == ""):
        print("Espacio vacio vuelve a intentar")
    print("Hola!!",nombre)

# solicitar edad de usuario
    #intentar converit la edad a un numero para que sea valido
    edad = False
    while (edad == False):
        dato = input("Digita tu edad ")
        try:
            numero = int(dato) 
            if (numero > 100):
                print(" numero no valido")
            else :
                edad = True        
        except:
            print("Eso no es un número, intenta de nuevo.\n")

