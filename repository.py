from operaciones import Operaciones

class Repository():
    dificultadUno={1:{'_palabra':'AUTO', '_tipo_palabra':'VEHICULO'}, 2:{'_palabra':'AVION', '_tipo_palabra':'VEHICULO'},
                    3:{'_palabra':'HIJO', '_tipo_palabra':'FAMILIAR'}, 4:{'_palabra':'BUSO', '_tipo_palabra':'DEPORTE'},
                    5:{'_palabra':'BYTE','_tipo_palabra':'INFORMATICA'}, 6:{'_palabra':'BIT', '_tipo_palabra':'INFORMATICA'}}

    dificultadDos={7:{'_palabra':'PANAL', '_tipo_palabra':'NATURALEZA'}, 8:{'_palabra':'DIENTE','_tipo_palabra':'CUERPO'}, 
                    9:{'palabra':'CELULAR', '_tipo_palabra':'ELECTRONICA'}, 10:{'_palabra':'PROFESOR', '_tipo_palabra':'PROFESION'}}

    dificultadTres={11:{'_palabra':'FISICA', '_tipo_palabra':'CIENCIA'}, 12:{'_palabra':'MOUSE', '_tipo_palara':'ELECTRONICA'},
                    13:{'_palabra':'TECLADO', '_tipo_palabra':'ELECTRONICA'}, 14:{'_palabra':'COMPUTADORA', '_tipo_palabra':'ELECTRONICA'}}

    dificultadCuatro={15:{'_palabra':'FUTBOL', '_tipo_palabra':'DEPORTE'}, 16:{'_palabra':'BISNIETO','_tipo_palabra':'FAMILIAR'}}

    dificultadCinco={17:{'_palabra':'BINARIO','_tipo_palabra':'INFORMATICA'}, 18:{'_palabra':'NATACION', ' _tipo_palabra':'DEPORTE'}}

    dificultadSeis={19:{'_palabra':'MECANICO', '_tipo_palabra':'PROFESION'}, 20:{'_palabra':'ESTOMAGO', '_tipo_palabra':'CUERPO'}}

    dificultadSiete={21:{'_palabra':'FENNEC', '_tipo_palabra':'NATURALEZA'}, 22:{'_palabra':'ASTRONOMIA', '_tipo_palabra':'CIENCIA'}}

    dificultadOcho={23:{'_palabra':'TRANSISTOR', '_tipo_palabra':'ELECTRONICA'},  24:{'_palabra':'ARAUCARIA', '_tipo_palabra':'NATURALEZA'}}

    dificultadNueve={25:{'_palabra':'OMOPLATO', '_tipo_palabra':'CUERPO'}, 26:{'_palabra':'CICLISMO', '_tipo_palabra':'DEPORTE'}}

    dificultadDiez={27:{'_palabra':'HALTEROFILIA', '_tipo_palabra':'DEPORTE'}, 28:{'_palabra':'OPTOACOPLADOR','_tipo_palabra':'ELECTRONICA'}}

    def get_palabra(repository_class, key):
        if Operaciones.op_dificultad.

#Ver como manejar dificultad