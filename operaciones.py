from repository import Repository
from partida import Partida
import random

class Operaciones():
    def op_dificultad(self, palabra, dificultad):
        try:
            if dificultad < 1 and dificultad > 10:
                raise ValueError("El valor de la dificultad debe comprender entre 1 y 10")
            else:
                return len(palabra) * dificultad
        except ValueError:
            raise

    def insertar_letra(self, palabra, palabra_intento, letra):
        for i in range(len(palabra_intento)):
            palabra_intento[i] = letra if letra == palabra[i]\
                else palabra_intento[i]
        return palabra_intento

    def comparar_palabras(self, palabra, palabra_intento):
        i = 0
        while (palabra[i] == palabra_intento[i] and
                (i := i+1) < len(palabra)):
            continue
        return i == len(palabra)

    def letra(self, partida, letra):
        try:
            partida.palabra_aciertos = self.insertar_letra(partida.palabra,partida.palabra_aciertos,letra)
            letra_igual = self.comparar_palabras(partida.palabra,partida.palabra_aciertos)
            partida.intentos = partida.intentos - 1
            if letra_igual:
                return "Ha ganado el juego"
            elif partida.intentos == 0:
                return "Ha perdido el juego"
            else:
                return "Continue"
        except ValueError:
            raise
    
    def get_random_palabra(self):
        try:
            if op_dificultad == 1:
                return self.repository.

#Ver como manejar dificultad