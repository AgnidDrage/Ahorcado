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
    def palabra(self, palabra):
        try:
            if len(palabra) == 0 or palabra is None:
                raise ValueError("El valor de la palabra inicial no puede ser nulo")
            self._palabra = list(palabra)
        except ValueError:
            raise

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, tipo_palabra):
        try:
            if len(tipo_palabra) == 0 or tipo_palabra is None:
                raise ValueError("El valor del tipo de palabra no puede ser nulo")
            self._tipo_palabra = tipo_palabra
        except ValueError:
            raise

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, intentos):
        try:
            if intentos < 0:
                raise ValueError("El valor inicial de intentos no puede ser menor o igual a 0")
            self._intentos = intentos
        except ValueError:
            raise

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, nombre_jugador):
        try:
            if len(nombre_jugador) == 0 or  nombre_jugador is None:
                raise ValueError("El valor de Nombre  de jugador no puede ser nulo")
            self._nombre_jugador = nombre_jugador.upper()
        except ValueError:
            raise

    @property
    def palabras_aciertos(self):
        return self._palabras_aciertos

    @palabras_aciertos.setter
    def palabras_aciertos(self, palabras_aciertos):
        self._palabras_aciertos = palabras_aciertos
