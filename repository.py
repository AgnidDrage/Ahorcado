class Repository():
    repositorioPalabras={1:{'palabra':'AUTO', 'tipo_palabra':'VEHICULO'}, 2:{'palabra':'AVION', 'tipo_palabra':'VEHICULO'},
                    3:{'palabra':'HIJO', 'tipo_palabra':'FAMILIAR'}, 4:{'palabra':'BUSO', 'tipo_palabra':'DEPORTE'},
                    5:{'palabra':'BYTE','tipo_palabra':'INFORMATICA'}, 6:{'palabra':'BIT', 'tipo_palabra':'INFORMATICA'},
                    7:{'palabra':'PANAL', 'tipo_palabra':'NATURALEZA'}, 8:{'palabra':'DIENTE','tipo_palabra':'CUERPO'}, 
                    9:{'palabra':'CELULAR', 'tipo_palabra':'ELECTRONICA'}, 10:{'palabra':'PROFESOR', 'tipo_palabra':'PROFESION'},
                    11:{'palabra':'FISICA', 'tipo_palabra':'CIENCIA'}, 12:{'palabra':'MOUSE', 'tipo_palara':'ELECTRONICA'},
                    13:{'palabra':'TECLADO', 'tipo_palabra':'ELECTRONICA'}, 14:{'palabra':'COMPUTADORA', 'tipo_palabra':'ELECTRONICA'},
                    15:{'palabra':'FUTBOL', 'tipo_palabra':'DEPORTE'}, 16:{'palabra':'BISNIETO','tipo_palabra':'FAMILIAR'},
                    17:{'palabra':'BINARIO','tipo_palabra':'INFORMATICA'}, 18:{'palabra':'NATACION', ' tipo_palabra':'DEPORTE'},
                    19:{'palabra':'MECANICO', 'tipo_palabra':'PROFESION'}, 20:{'palabra':'ESTOMAGO', 'tipo_palabra':'CUERPO'},
                    21:{'palabra':'FENNEC', 'tipo_palabra':'NATURALEZA'}, 22:{'palabra':'ASTRONOMIA', 'tipo_palabra':'CIENCIA'},
                    23:{'palabra':'TRANSISTOR', 'tipo_palabra':'ELECTRONICA'},  24:{'palabra':'ARAUCARIA', 'tipo_palabra':'NATURALEZA'},
                    25:{'palabra':'OMOPLATO', 'tipo_palabra':'CUERPO'}, 26:{'palabra':'CICLISMO', 'tipo_palabra':'DEPORTE'},
                    27:{'palabra':'HALTEROFILIA', 'tipo_palabra':'DEPORTE'}, 28:{'palabra':'OPTOACOPLADOR','tipo_palabra':'ELECTRONICA'},
                    29:{'palabra':'PYTHON', 'tipo_palabra':'LENGUAJE DE PROGRAMACION'}}

class GuardarPartida():
    def __init__(self, nombre_jugador1, dificultad1, palabra_adivin1,
                nombre_jugador2, dificultad2, palabra_adivin2):
        self.nombre_jugador1 = nombre_jugador1
        self.dificultad1 = dificultad1
        self.palabra_adivin1 = palabra_adivin1
        self.nombre_jugador2 = nombre_jugador2
        self.dificultad2 = dificultad2
        self.palabra_adivin2 = palabra_adivin2

    partidaGuardada=dict()