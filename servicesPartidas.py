from partida import Partida
from repository import Repository
import  random

class ServicePartidas():
    def __init__(self):
        self.repository = Repository()
    
    def iniciar_partida(self, nombre_jugador, dificultad, palabra=None, tipo_palabra=None):
        try:
            if len(palabra) == 0 and len(tipo_palabra) == 0:
                palabra_aleatoria = get_palabra_aleatoria()
                