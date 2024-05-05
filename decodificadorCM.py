morse_to_spanish = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '-----': '0', '--..--': ',',
    '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
    '-.--.': '(', '-.--.-': ')', '.----.': "'", '-...-': '=',
    '-.-.--': '!', '.-.-.': '+', '-..-.': '"', '-....-': '¿',
    '.--.-.': '@', '': ' ', '...---...': 'SOS'
}

def decode_morse_to_spanish(morse_code):
    words = morse_code.split('   ')  # Separar palabras
    decoded_message = ''
    for word in words:
        letters = word.split(' ')  # Separar letras
        for letter in letters:
            if letter in morse_to_spanish:
                decoded_message += morse_to_spanish[letter]
            else:
                decoded_message += '?'  # Carácter desconocido
        decoded_message += ' '  # Espacio entre palabras
    return decoded_message.strip()

morse_code = input("Introduce el código Morse: ")
decoded_message = decode_morse_to_spanish(morse_code)
print("Mensaje decodificado:", decoded_message)
