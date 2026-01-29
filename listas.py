alumnos = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "María", "edad": 21}
]

for alumno in alumnos:
    print(alumno["nombre"], alumno["edad"])
    

# Lista de frutas
frutas = ["manzana", "naranja", "plátano", "uva"]

print(frutas)

# ¿Qué puedes hacer con una lista?

frutas.append("mango")    # Agregar un elemento
frutas[1] = "pera"        # Modificar un elemento
del frutas[0]             # Eliminar por índice
