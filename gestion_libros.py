from data import cargar_libros

def buscar_libro():
    libros = cargar_libros()
    criterio = input("Buscar por título, author o género: ").lower()

    resultados = []

    for l in libros:
        if (criterio in l["titulo"].lower() or
            criterio in l["author"].lower() or
            criterio in l["genero"].lower()):
                resultados.append(l)

    if not resultados:
        print("No se encontraron resultados.")
        return

    print("\nResultados encontrados:")
    for l in resultados:
        estado = l["estado"]
        if estado == "Prestado":
            estado += f' a {l["prestado_a"]}'

        print(f"- {l['titulo']} | {l['author']} | {estado}")