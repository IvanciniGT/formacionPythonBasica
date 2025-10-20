# Hasta ahora, hemos hablado de algunos tipos de datos básicos en python:
# Números (enteros y decimales), textos (strings) y lógicos (booleanos: True/False).
# Pero en la mayoría de los programas, necesitamos trabajar no con datos sueltos...
# No con una edad, o un nombre, sino con una lista edades, una lista de nombres.

# Python tiene tipos de datos especiales para agrupar varios datos bajo un mismo nombre.

# TUPLA (tuple): Es una colección ordenada e inmutable de datos.
# Ordenada: Los datos tienen un orden fijo dentro del conjunto, y se puede acceder a ellos por su posición (índice).
# Inmutable: Una vez creada, no se pueden modificar, añadir o eliminar elementos de la tupla.

(25, 30, 35, 40)  # Tupla de números enteros
("Ana", "Luis", "María")  # Tupla de textos
# Puedo crear tuplas híbridas, con datos de distintos tipos:
(25, "Ana", True, 30.5)  # Tupla con datos
mi_tupla = (25, 30, 35, 40)  # Asigno la tupla a una variable
print(mi_tupla)  # Acceder al primer elemento de la tupla (índice 0)

mi_tupla = (1,2,3,4,5, 6,7,8,9,10)
print(mi_tupla)
# A lo mejor solo quiero el primero
primer_elemento = mi_tupla[0] # Con esta sintaxis me puedo referir a un elemento concreto.. Lo que doy es su posicion dentro del conjunto
                              # Comenzando a contar en 0. 0 es el primero, 1 es el segundo, 2 es el tercero...
print(primer_elemento)
print(mi_tupla[4]) # Quinto elemento (índice 4)
# Una tupla puedo saber su longitud, es decir, cuántos elementos tiene:
print(len(mi_tupla))  # Devuelve 10 # Len es otra de esas built-in functions que python trae de serie.

# Pregunta..Cómo puedo sacar el último elemento de la tupla?
print(mi_tupla[ len(mi_tupla) - 1 ])  # Acceder al último elemento (índice 9)
# Python me da una sintaxis más compacta para este caso:
print(mi_tupla[  - 1 ]) # Puedo evitar escribir: len(mi_tupla) 
# A qué no imaginais como sacaría el penúltimo elemento?
print(mi_tupla[ - 2 ]) # Puedo acceder al penúltimo elemento

# Esta sintaxis además, me permite extraer no solamente un elemento, sino varios a la vez:
print(mi_tupla[2:5])  # Extraer elementos desde el índice. Se incluye el elemento en la posición 2... 
                      # Pero no se incluye el elemento en la posición 5
# Si quiero los primeros 4 elementos:
print(mi_tupla[0:4]) # Pero python aquí también me da una sintaxis más compacta: Si lo primero es un 0, no me hace falta ponerlo
print(mi_tupla[:4])  # Extraer primeros 4 elementos
# Si quiero desde el elemento 5 hasta el final:
print(mi_tupla[5: len(mi_tupla)])  # Extraer elementos desde el índice 5 hasta el final
# Ahora bien... decíamos que dentro de esos corchetes, el len(mi_tupla) lo podemos obviar:
print(mi_tupla[5:])  # Extraer elementos desde el índice 5 hasta el final
# Los 3 últimos elementos
print(mi_tupla[-3:])  # Extraer los 3 últimos elementos 

colores = ("rojo", "verde", "azul", "amarillo")

print( "rojo" in colores )  # Devuelve True si el elemento está en la tupla, False si no está
print( "morado" in colores )  # Devuelve True si el elemento está en la tupla, False si no está
# Estas son nuestras tuplas.

# Hay otros 2 tipos de datos de colección: Listas y Diccionarios... pero mañana los vemos.

