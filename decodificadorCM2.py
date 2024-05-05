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
