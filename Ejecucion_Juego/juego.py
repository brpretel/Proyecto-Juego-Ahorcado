import random
import time
import os

#Funcion para traer al juego las palabras del archivo (palabras.txt)
def palabra_juego():
    with open("palabras.txt","r",encoding="utf-8") as p:
        lista = [palabra.lower().strip() for palabra in p]
        palabra = random.choice(lista)
        return palabra

#Logica del juego 
def tablero(letra,palabra,palabra_jugador,vidas,letras):
    while palabra_jugador != palabra:
        letra = input("Escriba una letra: ")
        try:
            if len(letra) == 0 or len(letra) >1 or letra in letras:
                raise ValueError("No se permiten numeros, combinacion de caracteres, espacios vacios o repetir letras!!\n")
        except ValueError as v:
            print(v)

        if letra in palabra:
            palabra_jugador = list(palabra_jugador)
            for x,i in enumerate(palabra):
                if i == letra:
                    palabra_jugador[x] = i
                    letras.append(letra)
            palabra_jugador = "".join(palabra_jugador)
            print(f"\t{palabra_jugador}")

        elif letra == "":
            vidas -=1
            print(f"Te quedan {vidas} vidas")

        elif vidas == 1:
            print("\nLo siento pero haz perdido intentalo de nuevo")
            time.sleep(3)
            os.system("cls")
            return run()
        else:
            vidas -=1
            print(f"Te quedan {vidas} vidas")
            print(f"\t{palabra_jugador}")
    print("!!!!!!Haz GANADO!!!!!!")

def run():
    letras = []
    vidas = 6
    letra = ""
    palabra = palabra_juego()
    palabra_jugador = "_" * len(palabra)

    print(f"Vidas ♥♥♥♥♥♥")
    print(palabra_jugador)
    tablero(letra,palabra,palabra_jugador,vidas,letras)


if __name__ == "__main__":
    run()