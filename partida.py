class Partida():
    def __init__ (self, palabra=None, tipo_palabra=None, intentos=None, nombre_jugador=None, palabras_aciertos=None):
        self.palabra = palabra
        self.tipo_palabra = tipo_palabra
        self.intentos = intentos
        self.nombre_jugador = nombre_jugador
        self.palabras_aciertos = palabras_aciertos

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, value):
        self._palabra = value

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, value):
        self._tipo_palabra = value

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, value):
        self._intentos = value

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, value):
        self._nombre_jugador = value

    @property
    def palabras_aciertos(self):
        return self._palabras_aciertos

    @palabras_aciertos.setter
    def palabras_aciertos(self, value):
        self._palabras_aciertos = value
