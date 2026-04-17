import json
import os
from collections import defaultdict
from gestion_libros import *
import config

def generar_reporte():
    libros = cargar_libros()

    categorias = defaultdict(list)

    for l in libros:
        estado = l["estado"]
        if estado == "Prestado":
            estado += f' a {l["prestado_a"]}'

        categorias[l["genero"]].append({
            "titulo": l["titulo"],
            "author": l["author"],
            "estado": estado
        })

    reporte = []

    print("\nREPORTE DEL INVENTARIO\n")

    for genero, lista in categorias.items():
        print(f"{genero}:")
        for libro in lista:
            print(f"- {libro['titulo']} | {libro['author']} | {libro['estado']}")

        reporte.append({
            "categoria": genero,
            "libros": lista
        })

    os.makedirs(config.ruta_absoluta/"data/reportes", exist_ok=True)

    with open(config.ruta_absoluta/"data/reportes/reporte_libros.json", "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=4, ensure_ascii=False)

    input("\nPresione ENTER para continuar...")