from servicesPartidas import ServicesPartidas
from repository import GuardarPartida
import sys

class Ahorcado():
    def __init__(self):
        self.service = ServicesPartidas()
    
    def menu(self):
        seleccion = input("Seleccione 1 para un jugador, 2 para dos jugadores o salir para cerrar el juego: ")
        if seleccion == 1:
            return self.un_jugador()
        elif seleccion == 2:
            return self.dos_jugadores()
        elif seleccion == "salir":
            print("Saliendo....")
            return sys.exit()
        else:
            ValueError("Accion no contemplada")


    def jugar(self, partida):
        while True:
            try:
                letra = input("Letra: ")
                if letra == "Salir":
                    return True
                flag = self.service.intentar_letra(partida, letra)
                if flag != "Continua":
                    if flag == "Gano":
                        print("Ganaste")
                    elif flag == "Perdio":
                        print("Perdiste")
                    return True
            except ValueError:
                print("Caracter no disponible")
                continue
            except StopIteration:
                return True

    def un_jugador(self):
        self.nombre_jugador = input("Ingrese nombre del jugador: ")
        while True:
            try:
                self.dificultad = int(input("Ingrese dificultad del 1 al 10: "))
                if type(self.dificultad) == int:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Debes ingresar un numero")
        partida = self.service.iniciar_partida(self.nombre_jugador, self.dificultad, "", "")
        jugar = self.jugar(partida)
        return jugar

    def dos_jugadores(self):
        self.nombre_jugador1 = input("Ingrese nombre del jugador 1: ")
        while True:
            try:
                self.dificultad1 = int(input("Ingrese dificultad del 1 al 10: "))
                if type(self.dificultad1) == int:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Debes ingresar un numero: ")
        while True:
            try:
                self.palabra_adivin1 = input("Ingrese palabra a adivinar")
                if self.palabra_adivin1.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Esa no es una palabra valida")
        while True:
            try:
                self.tipo_pal1 = input("Ingrese tipo de palabra: ")
                if self.tipo_pal1.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print("No es un tipo de palabra valido")
        partida1 = self.service.iniciar_partida(self.nombre_jugador1, self.dificultad1, self.palabra_adivin1, self.tipo_pal1)
        jugar1 = self.jugar(partida1)
        self.nombre_jugador2 = input("Ingrese nombre jugador 2: ")
        while True:
            try:
                self.dificultad2 = int(input("Ingrese dificultad del 1 al 10: "))
                if type(self.dificultad2) == int:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Debes ingresar un numero:")
        while True:
            try:
                self.palabra_adivin2 = input("Ingrese palabra a adivinar: ")
                if self.palabra_adivin2.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print("No es una palabra valida: ")
        while True:
            try:
                self.tipo_pal2 = input("Ingrese tipo de palabra:")
                if self.tipo_pal2.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print("El tipo de palabra ingresado no es valido")
        partida2 = self.service.iniciar_partida(self.nombre_jugador2, self.dificultad2, self.palabra_adivin2, self.tipo_pal2)
        jugar2 = self.jugar(partida2)
        guardar = GuardarPartida(self.nombre_jugador1, self.dificultad1, self.palabra_adivin1,
                                   self.nombre_jugador2, self.dificultad2, self.palabra_adivin2 )
        key = len(GuardarPartida.partidaGuardada)
        GuardarPartida.partidaGuardada[key] = guardar.__dict__

        if jugar2 is True and jugar1 is True:
            return True