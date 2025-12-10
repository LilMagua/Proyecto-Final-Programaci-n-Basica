### Funciones para CRUD de notas
def menu_notas():
    print("¿Que deseas hacer?");
    print("Opcion #1 Crear nota");
    print("Opcion #2 Ver notas");
    print("Opcion #3 Editar nota");
    print("Opcion #4 Eliminar nota");
    print("Opcion #5 Editar usuario");
    print("Opcion #6 Salir");


def guardar_nota(usuario, nombreNota, informacion, archivo):
    f = open(archivo, "a");
    linea = f"{usuario}|{nombreNota}|{informacion}\n"
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


