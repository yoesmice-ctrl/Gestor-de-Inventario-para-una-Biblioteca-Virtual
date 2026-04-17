from data import registrar_libro, ver_inventario
from gestion_libros import buscar_libro # type: ignore
from prestamos import prestar_libro, devolver_libro # type: ignore
from reportes import generar_reporte

def menu():
    while True:
        print("""
==========================================
GESTOR DE INVENTARIO BIBLIOTECA
==========================================
1. Registrar libro
2. Ver inventario
3. Buscar libro
4. Prestar libro
5. Devolver libro
6. Generar reporte
7. Salir
==========================================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            prestar_libro()
        elif opcion == "5":
            devolver_libro()
        elif opcion == "6":
            generar_reporte()
        elif opcion == "7":
            print(" Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()