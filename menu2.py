def mostrar_menu():
    print("Bienvenido al menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")

def seleccionar_opcion():
    opcion = input("Por favor, seleccione una opción (1/2/3): ")
    while opcion not in ['1', '2', '3']:
        print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
        opcion = input("Por favor, seleccione una opción (1/2/3): ")
    return opcion

def manejar_opcion(opcion):
    if opcion == '1':
        print("Ha seleccionado la Opción 1.")
    elif opcion == '2':
        print("Ha seleccionado la Opción 2.")
    elif opcion == '3':
        print("Ha seleccionado la Opción 3.")

        def main():
            mostrar_menu()
            opcion = seleccionar_opcion()
            manejar_opcion(opcion)

if __name__ == "__main__":
    main()