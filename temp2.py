 def un_jugador(self):
        services = ServicesPartidas()
        _nombre = input('\n----> \tIngrese su nombre: ')
        _dificultad = int(input('\n----> \tIngrese la dificultad (1-10): '))
        p1 = services.iniciar_partida(_nombre, _dificultad)
        res = 'Continua'
        while res == 'Continua':
            letra = input('\n----> \tIngrese una letra: ')
            if letra == 'salir':
                return True
            res = services.intentar_letra(p1, letra.upper())
            print('\t', p1._palabra_aciertos)
        if res == 'Gano':
            print('\n----> \tFelicitaciones {}, adivinaste!\n'
                  .format(_nombre.upper()))
            return True
        elif res == 'Perdio':
            print('\n----> \tPerdiste {}, mejor suerte la próxima.\n'
                  .format(_nombre.upper()))
            return False