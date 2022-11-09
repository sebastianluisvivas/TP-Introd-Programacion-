from principal import *
from configuracion import *
import random
import math



def nuevaPalabra(lista):
    palabra=random.choice(lista)
    return palabra
lista1=['caballo','perro','mono','leon']
print(nuevaPalabra(lista1))

def lectura(archivo, salida, largo):
    text1= archivo.readlines()
    for palabra in text1:
        if len(palabra)==largo:
            salida.append(palabra)

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if palabraCorrecta == palabra:
        for letras in palabra:
            correctas.append(letras)
        return True
    else:
        for i in len(palabra):
            if palabra[i]==palabraCorrecta[i]:
                correctas.append(palabra[i])
            elif palabra[i] in palabraCorrecta:
                casi.append(palabra[i])
        return False








