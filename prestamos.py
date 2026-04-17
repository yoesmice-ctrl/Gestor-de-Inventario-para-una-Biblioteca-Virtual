from data import cargar_libros, guardar_libros

def prestar_libro():
    libros = cargar_libros()
    titulo = input("Ingrese el título a prestar: ")

    for l in libros:
        if l["titulo"].lower() == titulo.lower():
            if l["estado"] == "Prestado":
                print("El libro ya está prestado.")
                return

            usuario = input("Nombre del usuario: ")
            l["estado"] = "Prestado"
            l["prestado_a"] = usuario

            guardar_libros(libros)
            print(f' Libro prestado a {usuario}')
            return

    print(" Libro no encontrado.")

def devolver_libro():
    libros = cargar_libros()
    titulo = input("Ingrese el título a devolver: ")

    for l in libros:
        if l["titulo"].lower() == titulo.lower():
            if l["estado"] == "Disponible":
                print(" El libro ya está disponible.")
                return

            l["estado"] = "Disponible"
            l["prestado_a"] = None

            guardar_libros(libros)
            print(f' Libro "{titulo}" devuelto.')
            return

    print(" Libro no encontrado.")