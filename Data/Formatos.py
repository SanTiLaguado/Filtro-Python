import json
try:
    with open("formatos.json", "r") as form:
        formatos = json.load(form)
except FileNotFoundError:
    formatos = {}
    
def agregar_formato(formatos):
    count = 1

    nombre = input("Ingrese el nombre del formato: ")

    if count <= 9:
        id = "F0"+str(count)
    else:
        id = "F"+str(count)

    if not formatos.get(id, {}):
        formatos.setdefault(id, {})

    if formatos[id].get("nombre", ""):
        print(f"{nombre} ya se encuentra registrado y su id es {id}")
    else:
        formatos[id]["id"] = id
        formatos[id]["nombre"] = nombre
        count += 1
        
        with open("formatos.json", "w+") as form:
            json.dump(formatos, form, indent=2)

def listar_formatos(formatos):
    print("Lista de Formatos:")
    for formato, detalle_formato in formatos.items():
        print("Formato",formato)
        for clave, valor in detalle_formato.items():
            print(f"{clave}:{valor}")

def buscarFormatoId(formatos, id):
    for formato in formatos:
        if formato['id'] == id:
            return formato
    return None