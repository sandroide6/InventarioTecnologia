# menu.py

from inventario import Inventario, PC, Tablet  

def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Prestar dispositivo")
    print("4. Devolver dispositivo")
    print("5. Salir")

def menu():
    inventario = Inventario()  # Creamos una instancia del inventario
    while True:
        mostrar_menu()  # Mostramos el menú
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            # Agregar dispositivo
            tipo = input("¿Qué tipo de dispositivo deseas agregar? (PC/Tablet): ").lower()
            serial = input("Número de serie: ")
            marca = input("Marca: ")
            precio = float(input("Precio: "))
            
            if tipo == "pc":
                ram = input("Cantidad de RAM: ")
                disco_duro = input("Capacidad de Disco Duro: ")
                dispositivo = PC(serial, marca, precio, ram, disco_duro)  # Creamos una PC
            elif tipo == "tablet":
                tamano = input("Tamaño de la Tablet: ")
                dispositivo = Tablet(serial, marca, precio, tamano)  # Creamos una Tablet
            else:
                print("Tipo de dispositivo no válido.")
                continue
            
            inventario.agregar_dispositivo(dispositivo)
            print(f"Dispositivo {tipo.capitalize()} agregado al inventario.")

        elif opcion == "2":
            # Listar dispositivos
            print(inventario.listar_dispositivos())

        elif opcion == "3":
            # Prestar dispositivo
            serial = input("Número de serie del dispositivo a prestar: ")
            nombre_estudiante = input("Nombre del estudiante que lo tomará: ")
            print(inventario.prestar_dispositivo(serial, nombre_estudiante))

        elif opcion == "4":
            # Devolver dispositivo
            serial = input("Número de serie del dispositivo a devolver: ")
            print(inventario.devolver_dispositivo(serial))

        elif opcion == "5":
            # Salir
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor elige entre 1 y 5.")

if __name__ == "__main__":
    menu()  # Ejecutamos el menú
