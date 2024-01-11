from commons.utilities import validar_opcion

def menu_principal():
    print("-------------------------------------------------")
    print("      CATALOGO CINEMATOGRAFICO BLOCKBUSTER       ")
    print("                   BIENVENIDO                   ")
    print("             SELECCIONE UNA OPCION              ")
    print("-------------------------------------------------")

    print("1. Menu Peliculas")
    print("2. Menu Generos ")
    print("3. Menu Actores ")
    print("4. Menu Formatos")
    print("5. Salir")      
    op=validar_opcion("Opcion: ",1,5)
    return op

def menu_peliculas():
    print("-------------------------------------------------")
    print("                MENU PELICULAS                   ")
    print("             SELECCIONE UNA OPCION               ")
    print("-------------------------------------------------")
    print("1. Buscar peliculas")
    print("2. Agregar Peliculas ")
    print("3. Editar Peliculas")
    print("4. Listar Peliculas")
    print("5. Eliminar Peliculas")
    print("6. Regresar") 
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_generos():
    print("-------------------------------------------------")
    print("              GESTOR DE GENEROS                  ")
    print("            SELECCIONE UNA OPCION               ")
    print("-------------------------------------------------")
    print("1. Listar Generos")
    print("2. Agregar Generos ")
    print("3. Regresar") 
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_actores():
    print("-------------------------------------------------")
    print("               GESTOR DE ACTORES                 ")
    print("             SELECCIONE UNA OPCION               ")
    print("-------------------------------------------------")
    print("1. Crear Actor")
    print("2. Listar Actores ")
    print("3. Regresar") 
    op=validar_opcion("Opcion: ",1,3)
    
def menu_formatos():
    print("-------------------------------------------------")
    print("                 MENU FORMATOS                   ")
    print("             SELECCIONE UNA OPCION               ")
    print("-------------------------------------------------")
    print("1. Crear Formato")
    print("2. Listar Formatos ")
    print("3. Regresar") 
    op=validar_opcion("Opcion: ",1,3)

    

