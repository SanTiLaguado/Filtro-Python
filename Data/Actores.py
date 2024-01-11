import json
try:
    with open("actores.json", "r") as act:
        actores = json.load(act)
except FileNotFoundError:
    actores = {}

def agregar_actor(actores):
    count = 1

    nombre = input("Ingrese el nombre del Actor: ")

    if count <= 9:
        id = "A0"+str(count)
    else:
        id = "A"+str(count)

    if not actores.get(id, {}):
        actores.setdefault(id, {})

    if actores[id].get("nombre", ""):
        print(f"{nombre} ya se encuentra registrado y su id es {id}")
    else:
        actores[id]["id"] = id
        actores[id]["nombre"] = nombre
        count += 1

        with open("generos.json", "w+") as act:
            json.dump(actores, act, indent=2)

def listar_actores(actores):
    print("Lista de Actores:")
    for actor, detalle_actor in actores.items():
        print("Actor",actor)
        for clave, valor in detalle_actor.items():
            print(f"{clave}:{valor}")
    
def buscarActorId(actores, id):
    for actor in actores:
        if actor['id'] == id:
            return actor
    return None