import json
import os
import config

RUTA = config.ruta_absoluta/"data/libros.json"

def cargar_libros():
    if not os.path.exists(RUTA):
        return []
    with open(RUTA, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_libros(libros):
    with open(RUTA, "w", encoding="utf-8") as f:
        f.write(json.dump(libros, f, indent=4, ensure_ascii=False))

def registrar_libro():
    libros = cargar_libros()

    titulo = input("Ingrese el título: ")
    author = input("Ingrese el author: ")
    genero = input("Ingrese el género: ")
    anio = int(input("Ingrese el año: "))

    # Validar duplicados
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print("El libro ya existe.")
            return

    nuevo = {
        "titulo": titulo,
        "author": author,
        "genero": genero,
        "anio_publicacion": anio,
        "estado": "Disponible",
        "prestado_a": None
    }

    libros.append(nuevo)
    guardar_libros(libros)
    print(f'Libro "{titulo}" registrado correctamente.')

def ver_inventario():
    libros = cargar_libros()

    if not libros:
        print("No hay libros registrados.")
        return

    print("="*70)
    print(f"{'Título':20} {'Author':20} {'Género':15} {'Estado'}")
    print("="*70)

    for l in libros:
        estado = l["estado"]
        if estado == "Prestado":
            estado += f' a {l["prestado_a"]}'

        print(f"{l['titulo']:20} {l['author']:20} {l['genero']:15} {estado}")