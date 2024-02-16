import json
with open('prueba.json', 'r') as i:
            prueba = json.load(i)

nuevo_dato = {

            "Id":str(input("Ingrese iD: ")),
            "Nombre": str(input("Nombre completo: "))
            
        }
## Agregar nuevo dato al archivo json
prueba["datos"]["gente"].append(nuevo_dato)

#guardar datos
with open('prueba.json', 'w') as i:
                json.dump(prueba, i, indent=2)

# Ordenar datos
gente=prueba["datos"]["gente"]
gente_ordenada = sorted(gente, key=lambda x: str(x["Nombre"]))

#imprimir datos
for i in gente_ordenada:
      print("   Nombre: ",i["Nombre"], "Numero de identificacion:", i["Id"], "   Nombre: ",i["Nombre"])

# Eliminar la persona con el ID proporcionado por el usuario
id_eliminar = input("Ingrese el ID que desea eliminar: ")
for i in gente:
    if i['Id'] == id_eliminar:
        gente.remove(i)
        break  # Detener el bucle una vez que se haya eliminado la persona

# Guardar los cambios en el archivo JSON
with open('prueba.json', 'w') as f:
    json.dump(prueba, f, indent=2)
    