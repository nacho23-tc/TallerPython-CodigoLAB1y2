import pandas as pd
import matplotlib.pyplot as plt

def pedir_datos():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    altura = float(input("Ingrese la altura (en metros): "))
    
    try:
        datos = pd.read_excel("datos.xlsx")
    except FileNotFoundError:
        datos = pd.DataFrame(columns=["Nombre", "Edad", "Altura"])
        
    nuevo_dato = pd.DataFrame({"Nombre": [nombre], "Edad": [edad], "Altura": [altura]})
    datos = pd.concat([datos, nuevo_dato], ignore_index=True)
    
    datos.to_excel("datos.xlsx", index=False)
    print("Datos guardados en 'datos.xlsx'.")

def ver_datos():
    try:
        datos = pd.read_excel("datos.xlsx")
        print("Datos extraídos del archivo 'datos.xlsx':")
        print(datos)
    except FileNotFoundError:
        print("No se encontró el archivo 'datos.xlsx'. Primero ingrese datos para crearlo.")

def mostrar_grafico():
    try:
        datos = pd.read_excel("datos.xlsx")
        plt.figure(figsize=(8, 6))  # Ajustar el tamaño de la figura
        
        # Personalizar el gráfico de barras
        datos.plot(kind='bar', x='Nombre', y='Edad', color='skyblue', edgecolor='black', alpha=0.7)
        
        # Etiquetas y título
        plt.xlabel('Nombre', fontsize=12, fontweight='bold')
        plt.ylabel('Edad', fontsize=12, fontweight='bold')
        plt.title('Edad por Nombre', fontsize=14, fontweight='bold')
        
        # Ajustar la posición de los ticks en el eje x
        plt.xticks(rotation=45, ha='right')
        
        # Mostrar el gráfico
        plt.show()
    except FileNotFoundError:
        print("No se encontró el archivo 'datos.xlsx'. Primero ingrese datos para crearlo.")

def salir():
    print("¡Hasta luego!")

while True:
    print("\nMENU")
    print("1. Pedir datos & guardar en Excel")
    print("2. Ver datos extraídos de Excel")
    print("3. Mostrar gráfico")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        pedir_datos()
    elif opcion == "2":
        ver_datos()
    elif opcion == "3":
        mostrar_grafico()
    elif opcion == "4":
        salir()
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
