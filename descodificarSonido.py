import sounddevice as sd
import numpy as np
import time

# Definir el diccionario de código Morse
morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0'
}

def grabar_sonido(duracion):
    fs = 44100  # Frecuencia de muestreo (Hz)
    grabacion = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype=np.float32)
    sd.wait()  # Esperar a que termine la grabación
    return grabacion.flatten()

def analizar_sonido(sonido, umbral):
    duracion_sonido = len(sonido) / 44100  # Duración del sonido en segundos
    if duracion_sonido < umbral:
        return '.'  # Sonido corto
    else:
        return '-'  # Sonido largo

def traducir_morse(morse):
    mensaje = ''
    for letra_morse in morse.split(' '):  # Dividir el código Morse en letras
        if letra_morse in morse_dict:
            mensaje += morse_dict[letra_morse]  # Agregar la letra correspondiente al mensaje
        else:
            mensaje += '?'  # En caso de que no se reconozca el código Morse, agregar un signo de interrogación
    return mensaje

def escuchar_morse(umbral_corto=0.3, umbral_largo=0.7, tiempo_espera=0.1):
    morse_actual = ''
    while True:
        sonido = grabar_sonido(tiempo_espera)
        duracion = analizar_sonido(sonido, umbral_corto)
        if duracion == '.':
            morse_actual += '.'
        else:
            duracion = analizar_sonido(sonido, umbral_largo)
            if duracion == '-':
                morse_actual += '-'
            else:
                if morse_actual:
                    if morse_actual == ' ':
                        print(" ", end="")
                    else:
                        letra = traducir_morse(morse_actual)
                        print(letra, end="")
                    morse_actual = ''
                time.sleep(tiempo_espera)

# Escuchar y traducir el código Morse
print("Escuchando... (Presione Ctrl+C para detener)")
try:
    escuchar_morse()
except KeyboardInterrupt:
    print("\nInterpretación de código Morse finalizada.")
