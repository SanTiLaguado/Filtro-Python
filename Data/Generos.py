import json
import os

def load_generos_json():
    try:
      with open(os.path.join("data", "generos.json"), 'r') as archivo_json:        
        lista_generos = json.load(archivo_json)
        print("La lista de generos ha sido guardada")
        return lista_generos
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
      
def guardar_json():
    try:
      with open(os.path.join("data", "generos.json"), 'w') as archivo_json:
        json.dump(lista_generos, archivo_json, indent=2)
        print("La lista de generos ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya generos guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
        
lista_generos = load_generos_json()

def registrarGenero(generos):
    count = 1
    nombre = input("Ingrese el nombre del género: ")

    if count <= 9:
        id = "G0"+str(count)
    else:
        id = "G"+str(count)

    if nombre in generos[id]:
        print(f"{nombre} ya se encuentra registrado y su id es {id}")
    else:
        generos[id]["id"] = id
        generos[id]["nombre"] = nombre
        count += 1
        
        with open("generos.json", "w+") as gen:
            json.dump(generos, gen, indent=2)
guardar_json

def listar_generos(generos):
    print("Lista de Generos:")
    for genero, detalle_genero in generos.items():
        print("Genero",genero)
        for clave, valor in detalle_genero.items():
            print(f"{clave}:{valor}")
    
def buscarGeneroId(generos, id):
    for genero in generos:
        if genero['id'] == id:
            return genero
    return None