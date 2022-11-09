
import pygame
def nuevaPalabra(lista):
    import random
    palabra=random.choice(lista)
    return palabra
lista1=['caballo','perro','mono','leon']
print(nuevaPalabra(lista1))


##lee el archivo que ya fue abierto en principal y
##carga en salida solo las palabras cuya longitud
## es el indicado en el tercer parámetro (largo)

def lectura(archivo, salida, largo): #el largo lo ponemos nosotros o no? preguntar
    text1= archivo.readlines()
    for palabra in text1:
        if len(palabra)==largo:
            salida.append(palabra)


##La función revision(palabraCorrecta, palabra,
##correctas, incorrectas, casi) chequea
##la palabra ingresada por el usuario, carga las
## letras en la lista que corresponda y
##devuelve True en caso de que la palabra sea
##la correcta y False en caso contrario.

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
# comenzamos preguntando si la palabra es igual a palabracorrecta
#si es correcta va a poner las letras en la variable correctas y devuelve true

    if palabraCorrecta == palabra:
        for letras in palabra:
            correctas.append(letras)
        return True


#si no es correcta, va a recorrer la palabra y va a poner las correctas en correctas, casi en casi, incorrectas en incorrectas
    else:
        for i in len(palabra):
            if palabra[i]==palabraCorrecta[i]:
                correctas.append(palabra[i])
            elif palabra[i] in palabraCorrecta:
                casi.append(palabra[i])
        return False


##    letracorrecta=[]
##    letrapalabra=[]
##        for letra in palabraCorrecta:
##            letracorrecta.append(letra)
##        for letra in palabra:
##            if letra==letracorrecta(letra):
##                correcta.append(letra)
##            elif letra in letracorrecta:
##                casi.append(letra)
##            else: incorrecta.append(letra)
##        return False