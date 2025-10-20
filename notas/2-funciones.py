# Una función es un trozo de código que ejecuta una serie de tareas.
# Las funciones pueden o no admitir argumentos (parámetros de entrada).
# Python tiene muchas funciones ya definidas (built-in functions).
# Ejemplos de funciones que python ofrece:
# Función para redondear un número decimal:
round(3.5678)  # Devuelve 4
# v
# 4
round(3.2123)  # Devuelve 3
# Raiz cuadrada (método sqrt del módulo math). Es una función que aunque la tiene python de serie,
# esá dentro de lo que llamamos una librería (módulo math).
# Cuando queremos usar las funciones de una librería, debemos importarla primero.
import math  # Importar la librería math Es decir, quiero usar las funciones de la librería math
math.sqrt(25)  # Devuelve 5.0

# Algunas básicas que vamos a usar mucho:
print("Hola Mundo")  # Función para mostrar por pantalla un texto o dato
print(round(3.5678))  # Anidación de funciones. Primero se ejecuta la función round y su resultado se pasa a la función print
resultado_del_redondeo = round(3.5678)
print(resultado_del_redondeo)

# Captura de datos por consola:
# texto_introducir = input("Escribe tu nombre: ")  # Función para capturar datos por consola. Siempre devuelve un texto (str)
# print("Hola " + texto_introducir)

# Python tiene decenas de funciones built-in que iremos viendo a lo largo del curso.
# Y ademas tiene cientos de funciones definidas en decenas de librerías (módulos) que podemos importar y usar out of the box.
# Es decir, librerías que directamente se distribuyen con el interprete de python.

# Eso si... luego hay decenas de miles de librerías de terceros que podemos descargar de internet
# y usar en nuestros proyectos. Cada una de esas librerías tiene cientos o miles de funciones definidas.

# Y al final hay decenas de millones de funciones disponibles en internet que podemos usar en nuestros proyectos.
# TOTALMENTE IMPOSIBLE DE MEMORIZAR, aprender... ni siquiera leer.. no tenemos tiempo suficiente en una vida.
# Semántica: Diccionario... Cada librería es como un diccionario, que porta nuevas palabras (funciones) para expresar 
# nuevos conceptos (tareas que queremos ejecutar en nuestro código).

# No me agobio.. iré aprendiendo palabras según las vaya necesitando en mis proyectos.
# Si que necesito conocer un mínimo.

# Pero también podemos definir nuestras propias funciones.
def saludar():  # Aquí estamos definiendo una función
                # En este caso, una función muy simple, que tiene solo una línea de código, una orden.
                # Además esta función no tiene parámetros de entrada (argumentos)
                # Ni tampoco devuelve ningún valor (return)
   print("Hola!")

# La función ya está definida.. Si ejecuto el código ahora, cuántas veces veré la palabra "Hola!" por pantalla?
# NINGUNA! Solo he definido la función. No la he ejecutado todavía.

# Como solicitar la ejecución de una función? Escribiendo el nombre de la función seguido de paréntesis.

saludar()
saludar()
saludar()
saludar()

# Python no usa delimitadores de fin de bloque de código.
# En C, JAVA, JS, los bloques de código se encierran entre llaves { }
# En SAS BASE los bloques de código se encierran entre un BEGIN y un END.
# En python, nada de nada. SE ENTIENDE QUE UN BLOQUE DE CODIGO ACABA CUANDO CAMBIA EL SANGRADO.

def despedida():  # Definición de la función despedida
   print("Adiós!")             # Bloque de código de la función despedida
   print("Nos vemos pronto!")  # Bloque de código de la función despedida
 
despedida()  # Ejecución de la función despedida

# Los bloques de código empiezan en python con el signo ":"
# Lo que sea que haya dentro del bloque de código, debe ir sangrado al menos 1 espacio en blanco a la derecha
# con respecto a la linea donde está el símbolo de ":"
# Y acaban cuando cambia el sangrado (indentación), y vuelvo a escribir código al mismo nivel que 
# la línea donde abrí el bloque de código (donde está el símbolo de ":")

# Hay que tener especial cuidado en python con el tema de la indentación.
# Y es muy importante usar un entorno de desarrollo (una app apra escribir código)
# que automáticamente sustituya los tabuladores por espacios en blanco.
# Un tabulador, habitualmente se representa por pantalla como 4 espacios en blanco.
# Pero para la computadora, un tabulador no es lo mismo que 4 espacios en blanco.
# Y puede ser que esté viendo la definición de una función por pantalla, donde:
#  En la primera línea del bloque de código haya un tabulador (y lo que vea por pantalla sea del mismo ancho que)
#  En la segunda línea del bloque de código haya 4 espacios en blanco
# Y python me dará error de indentación, porque para python no es lo mismo un tabulador que 4 espacios en blanco.
# Por ejemplo, yo este fichero le estoy contruyendo dentro de VISUAL STUDIO CODE
# Este programa sustituye automáticamente los tabuladores por espacios en blanco.

# Podemos generar funciones que admitan parámetros de entrada (argumentos)
def saludar_a_persona(nombre):  # nombre es un parámetro de entrada (argumento) de la función saludar_a_persona
    print("Hola " + nombre + "!")  # Usamos el parámetro de entrada dentro del bloque de código de la función

saludar_a_persona("Menchu")  # Ejecución de la función saludar_a_persona con el argumento "Iván"

persona = "Federico"
saludar_a_persona(persona)

# Podemos crear también funciones que devuelvan un valor, es decir, que coloquen un dato en memoria RAM
# para que podamos al invocar la función apuntar a ese dato con una variable.

def doblar(numero):
    return numero * 2
    # Esto significa que el resultado de esa operación (lo que hay a la derecha del return)
    # Se ubica en memoria RAM como un dato nuevo.
    # Y la función devuelve una referencia a ese dato nuevo, para que podamos pegarle un postit (una variable) al lado.


doble = doblar(5)  # Ejecución de la función doblar con el argumento 5
print(doble)

# Hay más que hablar sobre funciones... pero por ahora lo dejamos aquí... este archivo tendrá SEGUNDA PARTE!