# Importaciones
from functionsUsers import menu_ingreso, revisar_rango, guardar_usuario, registrar_nombre, registrar_edad, registrar_contrasena, ingresar_usuario, editar_usuario,salir # O podemos usar *
from functionsNotes import menu_notas, guardar_nota, registrar_informacion, registrar_nombreNota, mostrar_notas, editar_nota, eliminar_nota # O podemos usar *
from config import lista_usuarios, lista_notas

while True:  
    menu_ingreso()
    
    opcionSeleccionada = input("")
    opcion = revisar_rango(opcionSeleccionada, 1, 3)

    if opcion == False:
        continue  # Continue = No tener en cuenta lo siguiente, volver al inicio del while

    # Registrar 
    if opcion == 1:
        print("### Formulario para registrarse ###")
        nombre = registrar_nombre()
        edad = registrar_edad()
        contrasena = registrar_contrasena()
        guardar_usuario(nombre, edad, contrasena, lista_usuarios)

    # Ingresar 
    elif opcion == 2:
        print("### Formulario para iniciar sesión ###")

        nombre_usuario_ingresado = ingresar_usuario(lista_usuarios);
        if nombre_usuario_ingresado != False:
            # ✔ Entró correctamente -> mostrar menú de notas
            while True:
                menu_notas()

                opcionNotasTexto = input("")  # Esto guarda la opcion como texto

                opcionNotas = revisar_rango(opcionNotasTexto, 1, 6)  
                # Esto valida y devuelve el número o False

                if opcionNotas == False:
                    continue  # seguir pidiendo una opción vAlida

                # ----- AQUI VAN LAS ACCIONES DE LAS NOTAS -----
                if opcionNotas == 1:
                    print("### Formulario para crear nota ###")
                    nombreNota = registrar_nombreNota();
                    informacion = registrar_informacion();
                
                    guardar_nota(nombre_usuario_ingresado,nombreNota,informacion, lista_notas);
                    
                elif opcionNotas == 2:
                    print("### Tus notas ###")
                    mostrar_notas(nombre_usuario_ingresado, lista_notas)

                elif opcionNotas == 3:
                    print("### Editar nota ###")
                    editar_nota(nombre_usuario_ingresado,lista_notas);
                
                elif opcionNotas == 4:
                    print("### Eliminar nota ###")
                    eliminar_nota(nombre_usuario_ingresado,lista_notas);
                
                elif opcionNotas == 5:
                        print("### Editar usuario ###")
                        nuevo_nombre = editar_usuario(nombre_usuario_ingresado, lista_usuarios)

                        if nuevo_nombre != False:
                            # Si cambió su nombre, actualizar la variable en sesión
                            nombre_usuario_ingresado = nuevo_nombre
                
                elif opcionNotas == 6:
                    salir();

    # Salir 
    elif opcion == 3:
        salir();
