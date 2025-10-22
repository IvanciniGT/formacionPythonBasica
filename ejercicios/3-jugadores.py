from juego import bienvenida, jugar_piedra_papel_tijera  # Quiero que esa función que tengo en el otro fichero esté disponible en este
# Tenemos ya el juego de piedra, papel o tijera en la carpeta ejercicios.
# Vamos a modificarlo... para que:
# - Lo primero que haga es preguntar mi nombre de usuario
# - Al jugar, que guarde el resultado de la partida asociado al usuario.
# - Y que me pregunte si quiero seguir jugando más partidas o no
# - Si le digo que no, me debe preguntar si algún otro usuario quiere jugar.
# - Si le digo que si... me pedirá el nombre de ese usuario y comenzará una partida para él/ella.
#   Y al acabar, anotará asociado a ese usuario el resultado de la partida.
# - Cuando ya nadie más quiera jugar, nos mostrará el resumen de resultados de todos los usuarios que han jugado.
# - Sacaremos también quien ha sido el mejor jugador (el que más partidas haya ganado) del torneo!


#diccionario_usuario = {"nombre": "Menchu", "resultados": [0,1,2,2,1]}
#lista_de_jugadores  = [
#                            {"nombre": "Menchu", "resultados": [0,1,2,2,1]}, 
#                            {"nombre": "Luis"  , "resultados": [0,1,2,2,1]}
#                      ]

GANADO_USUARIO = 0
# Qué datos necesitamos manejar?
lista_de_jugadores = []  # Inicialmente esa lista no contiene datos de ningún jugador... estamos comenzando. Lista vacía
                         # En esta lista, cada vez que llegue un jugador nuevo, añadiré un diccionario con su nombre y con resultados vacíos:
                                            # {"nombre": "Menchu", "resultados": [] }
                         # Cuando un jugador juegue una partida y tenga esa partida un resultado, tendré que añadir el resultado de esa partida 
                         # a la lista de resultados del diccionario cuyo campo "nombre" coincida con el nombre del jugador que está jugando.
                         # Donde más voy a usar esta lista? o para que más?
                         # Necesitaré sacar las estadísticas de todos los jugadores al final... 
                         # y también necesitaré saber quién es el mejor jugador.

def nuevo_jugador(nombre_jugador):
    diccionario_usuario = {"nombre": nombre_jugador, "resultados": []}
    lista_de_jugadores.append(diccionario_usuario)
    return diccionario_usuario

def buscar_jugador(nombre_jugador):
    for diccionario_usuario in lista_de_jugadores:
        if diccionario_usuario["nombre"] == nombre_jugador:
            return diccionario_usuario
    return None # Palabra nueva que usamos en python. Indica que a una variable no le estamos asignando ningún valor.

def nuevo_resultado_para_jugador(nombre_jugador, resultado):
    if not existe_el_jugador(nombre_jugador):                             # Si no existe el jugador,
        diccionario_del_jugador = nuevo_jugador(nombre_jugador)     # lo creamos
    else:
        diccionario_del_jugador = buscar_jugador(nombre_jugador)
    diccionario_del_jugador["resultados"].append(resultado)         # Añadimos el resultado a la lista de resultados del jugador

# Sacar el listado de los ganadores del torneo (El que más ganados tenga en valor absoluto o aquel cuyo % de victorias sea el más alto)
def calcular_listado_ganadores_torneo():
    # Empezamos sin ganadores.. y con 0 victorias y 0 % de victorias
    resultados = { "max_ganados": 0, "lista_max_ganados": [], "max_porcentaje": 0, "lista_max_porcentaje": [] }
    # Ir recorriendo todo el listado de jugadores
    for diccionario_de_jugador in lista_de_jugadores:
        #   Para cada jugador, contar las partidas que ha ganado y las que ha jugado
        numero_partidas_ganadas = diccionario_de_jugador["resultados"].count(GANADO_USUARIO)
        numero_partidas_totales = len(diccionario_de_jugador["resultados"])
        #    Calcular el porcentaje de victorias del jugador
        porcentaje_victorias = 0
        if numero_partidas_totales > 0 :
            porcentaje_victorias = numero_partidas_ganadas / numero_partidas_totales
        porcentaje_victorias *= 100
        porcentaje_victorias = round(porcentaje_victorias)
        #    Si el número de victorias del jugador es mayor que el máximo actual:
        if numero_partidas_ganadas > resultados["max_ganados"]:
        #       Actualizar el máximo actual y la lista de ganadores actuales solamente debe contener a esta persona
            resultados["lista_max_ganados"] = [ diccionario_de_jugador["nombre"] ]
            resultados["max_ganados"] = numero_partidas_ganadas
        #    Si el número de victorias del jugador es igual al máximo actual:
        #       Añadir a esta persona a la lista de ganadores actuales
        elif numero_partidas_ganadas == resultados["max_ganados"]:
            resultados["lista_max_ganados"].append( diccionario_de_jugador["nombre"] )
        #    Si el porcentaje de victorias del jugador es mayor que el % máximo actual:
        if porcentaje_victorias > resultados["max_porcentaje"]:
         #       Actualizar el % máximo actual y la lista de ganadores actuales por % solamente debe contener a esta persona
            resultados["lista_max_porcentaje"] = [ diccionario_de_jugador["nombre"] ]
            resultados["max_porcentaje"] = porcentaje_victorias
        #    Si el porcentaje de victorias del jugador es igual al % máximo actual:
        #       Añadir a esta persona a la lista de ganadores actuales por %
        elif porcentaje_victorias == resultados["max_porcentaje"]:
            resultados["lista_max_porcentaje"].append( diccionario_de_jugador["nombre"] )
    # Devolver las 2 listas de ganadores y los 2 máximos
    return resultados
# Qué va a devolver nuestra función?
# 2 listas: Una con los jugadores que más victorias tienen en valor absoluto
#           Otra con los jugadores que más porcentaje de victorias tienen
# Y además 2 datos: El número máximo de victorias en valor absoluto
#                   El porcentaje máximo de victorias
# Una función puede devolver 4 cosas a la vez? A priori no.. pero puedo devolver un diccionario que contenga los 4 datos.
# { "max_ganados": 10, "lista_max_ganados": [...], "max_porcentaje": 75.0, "lista_max_porcentaje": [...] }

def mostrar_listado_ganadores_del_torneo():
    ganadores = calcular_listado_ganadores_torneo()
    print("Ganadores del torneo:")
    print("---------------------")
    print(" - Jugadores con más partidas ganadas ("+str(ganadores["max_ganados"])+"): ")
    for nombre_ganador in ganadores["lista_max_ganados"]:
        print("    - " + nombre_ganador)

    print(" - Jugadores con más porcentaje de victorias ("+str(ganadores["max_porcentaje"])+ "%): ")
    for nombre_ganador in ganadores["lista_max_porcentaje"]:
        print("    - " + nombre_ganador)

# En el mundo del desarrollo de software usamos ciertos principios que nos ayudan a la hora de trabajar. Uno de ellos es el SoC.
# Separation of Concerns. Separación de preocupaciones.
# No quiero estar continuamente pensando en TODOS LOS PROBLEMAS QUE TENGO QUE RESOLVER.  Eso es inmanejable!
# Me tengo que ir concentrando.. y tengo que aprender a hacer eso.. que no es fácil. 
# Centrarme en una cosa.. y ser muy muy concienzudo de no salir de esa cosa, al analizarla... No mezclar otras cosas.

# Cuando creamos software (que hay gente que se dedica 4/5/6 años a estudiar esto en la universidad.. y algo les enseñaran digo yo)
# Podemos hacer lo que se llama un desarrollo bottom-> up o top -> down
# Ayer hacía yo un desarrollo top -> down. Empezaba por el problema grande (el juego completo) y lo iba dividiendo en subproblemas más pequeños.
# Esta forma de trabajar funciona MUY BIEN cuando no tenemos un conocimiento muy pronfundo aún de lo que queremos que nuestro sistema haga.
# Otra opción es hacer un desarrollo bottom -> up. Empezar por problemas muy pequeños que sé que tengo que resolver y luego ir juntándolos para ir resolviendo problemas más grandes.
# Si conozco los problemas pequeños... que hay que resolver, es un buen sitio para comenzar.
# Muchas veces usamos enfoques híbridos. Algunas funciones / problemas pequeños los vamos resolviendo bottom -> up 
# y luego los vamos integrando en un desarrollo top -> down donde me hacen falta.

# - Lo primero que haga es preguntar mi nombre de usuario
def pedir_nombre_usuario():
    existe = True
    while existe:
        nombre_usuario = input("Por favor, dime tu nombre de usuario: ")
        existe = existe_el_jugador(nombre_usuario)
        if existe:
            print("Ese nombre de usuario ya existe. Por favor, elige otro.")
        else:
            print("¡Bienvenido, " + nombre_usuario + "!")
    return nombre_usuario

# - Y que me pregunte si quiero seguir jugando más partidas o no
def preguntar_si_seguir_jugando():
    #respuesta = input("¿Quieres jugar otra partida? (s/n): ")
    #if respuesta.lower() == 's':
    #    return True
    #else:
    #    return False
    respuesta = input("¿Quieres jugar otra partida? (s/n): ").lower()
    return respuesta == 's'

# - me debe preguntar si algún otro usuario quiere jugar.
def preguntar_si_otro_usuario_quiere_jugar():
    respuesta = input("¿Hay otro usuario que quiera jugar? (s/n): ").lower()
    return respuesta == 's'

def existe_el_jugador(nombre_jugador):
    return buscar_jugador(nombre_jugador) != None

def bienvenido():
    print("¡Bienvenido al torneo de Piedra, Papel o Tijera!")

def despedida():
    print("¡Gracias por participar en el torneo! ¡Hasta la próxima!")

# Tenemos ya el juego de piedra, papel o tijera en la carpeta ejercicios.
# Vamos a modificarlo... para que:
# - Lo primero que haga es preguntar mi nombre de usuario
# - Al jugar, que guarde el resultado de la partida asociado al usuario.
# - Y que me pregunte si quiero seguir jugando más partidas o no
# - Si le digo que no, me debe preguntar si algún otro usuario quiere jugar.
# - Si le digo que si... me pedirá el nombre de ese usuario y comenzará una partida para él/ella.
#   Y al acabar, anotará asociado a ese usuario el resultado de la partida.
# - Cuando ya nadie más quiera jugar, nos mostrará el resumen de resultados de todos los usuarios que han jugado.
# - Sacaremos también quien ha sido el mejor jugador (el que más partidas haya ganado) del torneo!

def jugar_torneo_piedra_papel_tijera():
    bienvenida()
    hay_alguien_dispuesto_a_jugar = True
    while hay_alguien_dispuesto_a_jugar:
        nombre_usuario = pedir_nombre_usuario()
        el_jugador_quiere_jugar = True
        while el_jugador_quiere_jugar:
            resultado = jugar_piedra_papel_tijera()
            nuevo_resultado_para_jugador(nombre_usuario, resultado)
            el_jugador_quiere_jugar = preguntar_si_seguir_jugando()
        # SI LLEGO A ESTA LINEA DE CÓDIGO QUE SIGNIFICA? Que el jugador ya no quiere jugar más
        hay_alguien_dispuesto_a_jugar = preguntar_si_otro_usuario_quiere_jugar()
    # SI LLEGO A ESTA LINEA DE CÓDIGO QUE SIGNIFICA? ya no hay nadie dispuesto a jugar. Hemos acabado el torneo! 
    mostrar_listado_ganadores_del_torneo()
    despedida()

jugar_torneo_piedra_papel_tijera()