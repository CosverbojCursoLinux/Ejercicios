# Ejemplo de Diccionario en Python
# Un diccionario almacena datos en forma de pares clave : valor.

# Diccionario con datos de un alumno
alumno = {
    "nombre": "Cosme",
    "edad": 40,
    "curso": "Python"
}

print(alumno)

# ¿Qué puedes hacer con un diccionario?

alumno["edad"] = 41            # Modificar un valor
alumno["calificacion"] = 9.5   # Agregar un nuevo par clave-valor
del alumno["curso"]             # Eliminar una clave

# Recorrer un diccionario

paises = {
    "México": "Ciudad de México",
    "España": "Madrid",
    "Argentina": "Buenos Aires"
}

for pais, capital in paises.items():
    print(pais, "→", capital)
    