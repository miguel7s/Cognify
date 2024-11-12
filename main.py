from vista.interfaz import Interfaz
from controlador.controlador import Controlador

def main():
    controlador = Controlador()
    interfaz = Interfaz()
    while True:
        interfaz.mostrar_menu()
        opcion = input("Ingrese su elección: ")
        if opcion == "1":
            name = input("Ingrese el nombre del criminal: ")
            crime_type = interfaz.seleccionar_crimen()
            if crime_type:
                controlador.crear_criminal(name, crime_type)
        elif opcion == "2":
            controlador.crear_recuerdo()
        elif opcion == "3":
            controlador.iniciar_simulacion()
        elif opcion == "4":
            print("Saliendo del sistema Cognify.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
