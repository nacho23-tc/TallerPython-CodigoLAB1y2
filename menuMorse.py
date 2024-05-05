from time import sleep
from playsound import playsound
def codificar():
    codigoMorse ={
        "A":".-", "B":"...","C":"-.-","D":"-..",
        "E":".","F":"..-.","G":"--.", "H":"....",
        "I":"..","J":".---","K":"-.-","L":".-..",
        "M":"--","N":"-.","O":"---","P":".--.",
        "Q":"--.-","R":".-.","S":"...","T":"-",
        "U":"..-","V":"...-","W":"..-","X":"-..-",
        "Y":"-.--","Z":"--.."
        }
    cadena=input ("introducce un texto a convertir en Codigo morse: ").upper()
    #.upper() ----> mayus o minus

    print("Letra\t Codigo Morse")
    for letra in cadena:
        if letra ==" ":
            sleep(1)
            continue
        if letra in codigoMorse:
            claveMorse = codigoMorse[letra]
            print("  "+letra+"\t ", end="")#formato para seguier en la misma linea
            for clave in claveMorse:
                print(clave,end="")
                if clave == ".":
                    playsound("short.mp3")
                else:
                    playsound("long.mp3")
                sleep(0.5)
        print()
    print('TEXTO CODIFICADO')
def descodificar():
    morse= {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }
    codigoMorse= input("Introduce Código Morse a traducir a letra: ")
    decodificarMsg= ""
    # Separar el código Morse en palabras
    palabras = codigoMorse.split('   ')
    # Decodificar cada palabra
    for palabra in palabras:
        # Separar la palabra en letras
        letras = palabra.split(' ')
        # Decodificar cada letra y agregar al mensaje
        for letra in letras:
            if letra in morse:
                decodificarMsg += morse[letra]
            else:
                decodificarMsg += "?"  # Carácter desconocido
        decodificarMsg += ' '  # Espacio entre palabras
    print("Mensaje decodificado:", decodificarMsg.strip())
    print ("copyright© By NachoTC ")

while True:
    print("1. Codificar")
    print("2. Descodificar")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codificar()
    elif opcion == "2":
        descodificar()
    elif opcion == "3":
        print("¡Hasta luego!" )
        print ("copyright© By NachoTC ")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")



        
