from modelo.crime_type import CrimeType

class Interfaz:
    @staticmethod
    def mostrar_menu():
        print("Seleccione una opción:")
        print("1. Crear criminal")
        print("2. Agregar recuerdo personalizado")
        print("3. Iniciar simulación")
        print("4. Salir")

    @staticmethod
    def seleccionar_crimen():
        print("Seleccione el tipo de crimen:")
        print("1. Violento")
        print("2. Financiero")
        print("3. Odio")
        opcion = input("Opción: ")

        if opcion == "1":
            return CrimeType.VIOLENT
        elif opcion == "2":
            return CrimeType.FINANCIAL
        elif opcion == "3":
            return CrimeType.HATE
        else:
            print("Opción no válida")
            return None
