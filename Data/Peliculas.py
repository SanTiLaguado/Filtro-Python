import json
from Data.Generos import *
from Data.Actores import *
from Data.Formatos import *

try:
    with open("peliculas.json", "r") as pel:
        peliculas = json.load(pel)
except FileNotFoundError:
    peliculas = {}
    
def buscar_peliculas():
    print("            BUSQUEDA DE PELICULAS                ")
    
def agregar_peliculas(peliculas):
    count = 1
    nombre = input("Ingrese el nombre de la pelicula: ")
    duracion = input("Ingrese la duracion de la pelicula: ")
    sinopsis = input("Ingrese la sinopsis de la pelicula: ")
    generos = {buscarGeneroId(generos,input("Ingrese el id del genero de la pelicula: "))}
    actores = {buscarGeneroId(actores,input("Ingrese el id del actor de la pelicula: "))}
    
    if count <= 9:
        id = "G0"+str(count)
    else:
        id = "G"+str(count)

    if not peliculas.get(id, {}):
        peliculas.setdefault(id, {})

    if peliculas[id].get("nombre", ""):
        print(f"{nombre} ya se encuentra registrado y su id es {id}")
    else:
        peliculas[id]["id"] = id
        peliculas[id]["nombre"] = nombre
        peliculas[id]["duracion"] = duracion
        peliculas[id]["sinopsis"] = sinopsis
        peliculas[id]["genero"] = generos
        peliculas[id]["actor"] = actores
        count += 1
        
        with open("peliculas.json", "w+") as pel:
            json.dump(peliculas, pel, indent=2)


def listar_peliculas():
    print("Listado de Peliculas: ")
    
def editar_peliculas():
    peli=input("Ingrese el ID de la pelicula que desea editar")

def eliminar_peliculas():
    peli=input("Ingrese el ID de la pelicula que desea ELIMINAR")
    
    