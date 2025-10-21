# Montar el juego: piedra papel tijera

# La idea es que ordenador me pregunte mi elección (piedra, papel o tijera)
# Él hará su elección... aleatoria entre las 3 opciones

# Y determinará el ganador de la mano.
# Gana la partida el que gane 3 manos.

# Necesito que el ordenador haga una elección... ME CREO UNA FUNCION PARA ESO
# Necesito preguntar al usuario por su elección: ME CREO OTRA FUNCION PARA ESO
# Conociendo la elección del jugador y de la computadora, necesito determinar el ganador de la mano: 
# OTRA FUNCION PARA ESO

# Datos que necesito manejar:

PIEDRA      = 0       # Esto son CONSTANTES. Son solo nombres para evitar trabajar con números
                      # A la computadora le gustan los números... a mi me vuelven los números.
PAPEL       = 1
TIJERA      = 2


USUARIO     = 0
COMPUTADORA = 1
EMPATE      = 2

RESULTADOS_TEXTO = ("Has ganado tú!", "He ganado yo!", "Empate!")
# La lógica del juego es:
#
#                           USUARIO
#                            PIEDRA         PAPEL           TIJERA
#  COMPUTADORA. PIEDRA       EMPATE         USUARIO         COMPUTADORA
#               PAPEL        COMPUTADORA    EMPATE          USUARIO       <<< Cada fila, va asociada a la elección de la computadora
#               TIJERA       USUARIO        COMPUTADORA     EMPATE
#
REGLAS_JUEGO = (
    (EMPATE, USUARIO, COMPUTADORA), # Si la computadora elige PIEDRA
    (COMPUTADORA, EMPATE, USUARIO), # Si la computadora elige PAPEL
    (USUARIO, COMPUTADORA, EMPATE)  # Si la computadora elige TIJERA
    # ^           ^          ^
    # Si usuario elige:
    #  PIEDRA   PAPEL     TIJERA
)

ELECCIONES_POSIBLES       = (PIEDRA  , PAPEL  , TIJERA  )
ELECCIONES_POSIBLES_TEXTO = ("Piedra", "Papel", "Tijera")


def bienvenida():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")

def despedida():
    print("¡Gracias por jugar! ¡Hasta la próxima!")

def hay_ganador_final(tabla_resultados):
    return tabla_resultados[USUARIO] >= 3 or tabla_resultados[COMPUTADORA] >= 3

def mostrar_ganador_final(tabla_resultados):
    if tabla_resultados[USUARIO] > tabla_resultados[COMPUTADORA]:
        print("¡Felicidades! ¡Has ganado la partida!")
    else:
        print("¡Eres un pringao! Más suerte la próxima vez!")

def actualizar_marcador(ganador, tabla_resultados):
    tabla_resultados[ganador] += 1
    print("Marcador actual: Tú " + str(tabla_resultados[USUARIO]) + " - Yo " + str(tabla_resultados[COMPUTADORA]) + "\n")

def calcular_eleccion_computadora():
    import random
    return random.randint(0,len(ELECCIONES_POSIBLES)-1)

def mostrar_elecciones(eleccion_jugador, eleccion_computadora):
    print("Has elegido: "   + ELECCIONES_POSIBLES_TEXTO[eleccion_jugador]    )
    print("Yo he elegido: " + ELECCIONES_POSIBLES_TEXTO[eleccion_computadora])

def obtener_eleccion_jugador():
    while True:
        print("Opciones posibles:")
        contador = 0
        for posibilidad in ELECCIONES_POSIBLES_TEXTO:
            print(" "*2 + str(contador) + " - ["+posibilidad[0:2]+"]" + posibilidad[2:])
            contador +=1
        eleccion_texto = input("¿Cuál es tu elección? ").lower()

        contador = 0
        for posibilidad in ELECCIONES_POSIBLES_TEXTO:
            if eleccion_texto == str(contador) or eleccion_texto == posibilidad.lower()or eleccion_texto == posibilidad[0:2].lower():
                return contador
            contador +=1
        print("Elección no válida. Por favor, inténtalo de nuevo.")

def determinar_ganador_mano(eleccion_jugador, eleccion_computadora):
    ganador = REGLAS_JUEGO[eleccion_computadora][eleccion_jugador]
    print("El resultado de la mano es: " + RESULTADOS_TEXTO[ganador])
    return ganador

def jugar_una_mano():
    eleccion_jugador     = obtener_eleccion_jugador()
    eleccion_computadora = calcular_eleccion_computadora()
    mostrar_elecciones(eleccion_jugador, eleccion_computadora)
    ganador              = determinar_ganador_mano(eleccion_jugador, eleccion_computadora)
    return ganador

def jugar_piedra_papel_tijera():
    tabla_resultados = [0,0,0] # En la primera casilla, guardo las manos ganadas por el jugador
                               # En la segunda casilla, guardo las manos ganadas por la computadora
                               # En la tercera casilla, guardo los empates
    bienvenida()
    while not hay_ganador_final(tabla_resultados):
        ganador = jugar_una_mano()
        actualizar_marcador(ganador, tabla_resultados)
    mostrar_ganador_final(tabla_resultados)
    despedida()

jugar_piedra_papel_tijera()





#def determinar_ganador_mano():
#    if eleccion_jugador == eleccion_computadora:
#        return EMPATE
#    elif (eleccion_jugador == PIEDRA and eleccion_computadora == TIJERA) or \
#         (eleccion_jugador == PAPEL and eleccion_computadora == PIEDRA) or \
#         (eleccion_jugador == TIJERA and eleccion_computadora == PAPEL):   
#        return USUARIO
#    else:
#        return COMPUTADORA