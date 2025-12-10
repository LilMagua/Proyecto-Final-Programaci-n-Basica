# Funciones
# Menu de notas
# Obtener el ID de la nota que se va a crear
# Guardar nota
# Verificar que el nombre de la nota ingresado por el usuario sea correcto
# Verificar que la informacion de la nota sea correcta
# Mostrar notas
# Editar nota
# Eliminar nota

### Funciones para CRUD de notas
def menu_notas():
    print("¿Que deseas hacer?");
    print("Opcion #1 Crear nota");
    print("Opcion #2 Ver notas");
    print("Opcion #3 Editar nota");
    print("Opcion #4 Eliminar nota");
    print("Opcion #5 Editar usuario");
    print("Opcion #6 Salir");

# Obtener el ID de la nueva nota
def obtener_nuevo_id(archivo):
    try:
        f = open(archivo, "r")
        lineas = f.readlines()
        f.close()

        if len(lineas) == 0:
            return 1 # Devuelve uno si es la primera nota que se crea

        # El ID está en datos[0]
        ultimo_id = int(lineas[-1].strip().split("|")[0])
        return ultimo_id + 1
    except:
        return 1  # Si el archivo no existe o esta vacio


def guardar_nota(usuario, nombreNota, informacion, archivo):
    # generar nuevo ID
    id_nuevo = obtener_nuevo_id(archivo)

    f = open(archivo, "a");
    # ID queda en la posicion 0
    linea = f"{id_nuevo}|{usuario}|{nombreNota}|{informacion}\n"
    f.write(linea);
    f.close() 
    print("##########################");
    print("Nota registrada con éxito.")
    print("##########################");


def registrar_nombreNota():
    while (True):
        nombreNota = input("Ingresa el nombre de tu nota. \n");
        if (len(nombreNota) >= 3 and len(nombreNota) <= 15):
            return nombreNota
        else: 
            print("El nombre de la nota debe tener entre 3 y 15 caracteres. \n")

def registrar_informacion():
    while (True):
        informacionNota = input("Ingresa la informacion de tu nota. \n");
        if (len(informacionNota) >= 3 and len(informacionNota) <= 50):
            return informacionNota
        else:
            print("La nota debe tener entre 3 y 50 caracteres. \n")

def mostrar_notas(usuario, archivo):
    f = open(archivo, "r")
    lineas = f.readlines()
    f.close()

    notas_encontradas = False

    for linea in lineas:
        datos = linea.strip().split("|")  
        # datos[0] = id  
        # datos[1] = usuario
        # datos[2] = nombre de la nota
        # datos[3] = información

        if (datos[1] == usuario):
            notas_encontradas = True
            print("---------------------------")
            print(f"ID: {datos[0]}") 
            print(f"Nombre de la nota: {datos[2]}")
            print(f"Información: {datos[3]}")
            print("---------------------------")

    if (notas_encontradas == False):
        print("No tienes notas registradas.") 

def editar_nota(usuario, archivo):
    id_editar = input("Ingresa el ID de la nota que deseas editar:\n")

    f = open(archivo, "r")
    lineas = f.readlines()
    f.close()

    nota_editada = False
    nuevas_lineas = []

    for linea in lineas:
        datos = linea.strip().split("|")
        # datos[0] = id
        # datos[1] = usuario
        # datos[2] = nombreNota
        # datos[3] = informacion

        # Verificar si es la nota del usuario y el ID solicitado
        if datos[0] == id_editar and datos[1] == usuario:
            print("Nota encontrada. Ingresa los nuevos datos.")

            nuevo_nombre = registrar_nombreNota()
            nueva_info = registrar_informacion()

            nueva_linea = f"{datos[0]}|{usuario}|{nuevo_nombre}|{nueva_info}\n"
            nuevas_lineas.append(nueva_linea)

            nota_editada = True
        else:
            nuevas_lineas.append(linea)

    # Si la nota no existía
    if nota_editada == False:
        print("Ninguna nota con ese ID te pertenece")
        return

    # Reescribir archivo con cambios
    f = open(archivo, "w")
    f.writelines(nuevas_lineas)
    f.close()

    print("################################")
    print("Nota editada correctamente.")
    print("################################")        

# Para eliminar una nota, reescribimos nuevamente todo el archivo, exceptuando la que queremos eliminar 
def eliminar_nota(usuario, archivo):
    id_borrar = input("Ingresa el ID de la nota que deseas eliminar: ")

    f = open(archivo, "r")
    lineas = f.readlines()
    f.close()

    f = open(archivo, "w")

    nota_eliminada = False

    for linea in lineas:
        datos = linea.strip().split("|")
        # datos[0] = id
        # datos[1] = usuario
        # datos[2] = nombre de la nota
        # datos[3] = información

        # si coincide el ID y además pertenece al usuario, NO la escribimos de nuevo
        if datos[0] == id_borrar and datos[1] == usuario:
            nota_eliminada = True
            continue  # saltar esta linea para borrarla dicha nota

        # si no coincide, se conserva
        f.write(linea)

    f.close()

    if nota_eliminada == True:
        print("###########################")
        print("Nota eliminada correctamente.")
        print("###########################")
    else:
        print("No existe una nota con ese ID o no te pertenece.")

