from commons.utilities import *
from commons.menus import *
from Data.Peliculas import *
from Data.Generos import *
from Data.Formatos import *
from Data.Actores import *

def peliculas():
    limpiar_pantalla()
    op = menu_peliculas()

    if op == 1:
        buscar_peliculas()
    elif op == 2:
        agregar_peliculas(peliculas)
    elif op == 3:
        editar_peliculas()
    elif op == 4:
        listar_peliculas()
    elif op == 5:
        eliminar_peliculas()

    input("Pulse cualquier tecla para volver")

def generos():
    limpiar_pantalla()
    op=menu_generos()
    
    if op ==1:
        listar_generos()
    elif op ==2:
        registrarGenero(generos)    
        
def actores():
    limpiar_pantalla()
    op=menu_actores()
    
    if op==1:
        agregar_actor()
    elif op==2:
        listar_actores()

    input("Pulse cualquier tecla para volver")    

def formatos():
    limpiar_pantalla()
    op=menu_formatos()
    
    if op==1:
        agregar_formato()
    elif op==2:
        listar_formatos()

    input("Pulse cualquier tecla para volver")


while True:
    limpiar_pantalla()
    op = menu_principal()

    if op == 1:
        peliculas()
    elif op == 2:
        generos()
    elif op == 3:
        actores()
    elif op == 4:
        formatos()
    elif op == 5:
        print("Saliendo")
        break
