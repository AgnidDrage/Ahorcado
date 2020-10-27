from partida import Partida
from partida import Partida
from repository import Repository
import random

class ServicesPartidas():
    def iniciar_partida(self, nombre_jugador, dificultad, palabra="", tipo_palabra=""):
        try:
            if len(palabra) == 0 and len(tipo_palabra) == 0:
                random = self.get_random_palabra()
                palabra = random["palabra"]
                tipo_palabra = random["tipo_palabra"]
                intentos = self.valorIntentos(dificultad, palabra)
                return Partida(palabra, intentos, tipo_palabra, nombre_jugador)
        except Exception:
            raise
    
    def valorIntentos(self, dificultad, palabra):
        self.palabra = Partida.palabra
        try:
            if dificultad < 1 or dificultad > 10:
                raise ValueError("La dificultad debe comprender entre 1 y 10")
            else:
                intentos = len(palabra) * dificultad
                return intentos
        except ValueError:
            raise

    def get_random_palabra(self):
        return Repository.repositorioPalabras[random.randrange(1,29)]

    
    def intentar_letra(self, partida, letra):
        letra = letra.upper()
        while partida.intentos > 0:
            partida.intentos -= 1
            for i in range(0, len(partida.palabra)):
                if partida.palabra[i] == letra:
                    partida.palabra_aciertos[i] = letra
            if partida.palabra_aciertos == partida.palabra:
                return 'Gano'
            if partida.intentos == 0:
                return 'Perdio'
            if partida.palabra_aciertos != partida.palabra:
                return 'Continua'
        raise ValueError