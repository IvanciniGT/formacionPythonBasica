# Juego de adivinar un número.. Tres opciones te doy (0-10)
# Juego de adivinar un número con muy frio/frio/caliente/muy caliente (0-20). Tiene 3 opciones.
# Tres en raja
# Ahorcado (Tenéis una lista de palabras predefinidas en una tupla y que se tome una al azar)
#       Vidas: 6: Cabeza, cuerpo, 2 brazos, 2 piernas

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

# Qué datos necesitamos manejar?

diccionario_usuario = {"nombre": "Menchu", "resultados": [0,1,2,2,1]}
lista_de_jugadores  = [
                            {"nombre": "Menchu", "resultados": [0,1,2,2,1]}, 
                            {"nombre": "Luis"  , "resultados": [0,1,2,2,1]}
                      ]


# Esta lista de diccionarios, mañana, después de tener el programa hecho, la guardaremos en un fichero, para ir conservando 
# las estadísticas de los distintos jugadores.
# Y el programa , cuando arranque, lo primero que hará será leer ese fichero y cargar esa lista de diccionarios con los datos de los jugadores que ya han jugado antes.
