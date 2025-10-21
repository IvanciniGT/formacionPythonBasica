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

# Hay otros 2 tipos de datos de colección: Listas y Diccionarios

# Lista: Es igual que una tupla, pero sus valores son editables. Y de hecho, puedo incluso eliminarlos o añadir nuevos valores.

mi_lista = [25, 30, 35, 40]  # Lista de números enteros
# Les puedo aplicar lo mismo que a las tuplas:
print(mi_lista)
print(mi_lista[2])  # Acceder al tercer elemento (índice 2)
print(len(mi_lista))  # Devuelve 4
print(mi_lista[1:3])  # Extraer elementos desde el índice 1 hasta el 3 (no incluido)
print(mi_lista[-1])  # Acceder al último elemento
print(20 in mi_lista)  # Devuelve False
# Iterarlo / Recorrerlo
for numero in mi_lista:
    print(numero)

# Lo mismo que a las tuplas... pero además puedo:
mi_lista[1] = 32  # Modificar el segundo elemento (índice 1) [25, 32, 35, 40]
# Borrar un elemento:
del mi_lista[2]  # Elimina el tercer elemento (índice 2)
print(mi_lista)  # Ahora es [25, 32, 40]
# Añadir un elemento al final:
mi_lista.append(45)  # Añade 45 al final de la lista
print(mi_lista)  # Ahora es [25, 32, 40, 45]
# Insertar un elemento en una posición concreta:    
mi_lista.insert(1, 28)  # Inserta 28 en la posición 1
print(mi_lista)  # Ahora es [25, 28, 32, 40, 45]
# Eliminar un elemento por su valor:


# Diccionarios. Los usamos un montón.
# Un diccionario es como una lista... es decir, me permite agrupar muchos valores, y además editarlos (modificarlos)
# La diferencia es que, en las listas, para recuperar un elemento (o editarlo) su posición (índice).
lista = [ "valor1", "valor2", "valor3" ]
print(lista[0])
print(lista[-1])
# En los diccionarios, los elementos se recuperan (o se editan) por una clave que cada dato/valor tiene asociada.

menchu_lista = [ "menchu", 29, "Ingeniera" ] 
# Si quiero cambiar la edad de menchu a 50 años, que tengo que hacer?
menchu_lista[1] = 50
# Quiero poner a Menchu ahora que se llama Felipe.. que estas cosas pasan hoy en día:
menchu_lista[0] = "Felipe"
# Y si quiero recuperar la profesión de menchu
profesion = menchu_lista[-1]
profesion = menchu_lista[2]

# Qué tal es trabajar con esos numeritos? 0.. 1.. 2.. es cómodo?
# En lugar de usar una lista para guardar los datos de Menchu, podríamos haber usado un diccionario.
# Al hacerlo, cada dato que guardase en ese diccionario, tendría un identificador / clave que me permitiría recuperarlo o modificarlo fácilmente.
menchu_diccionario = { "nombre": "menchu", "edad": 29, "profesion": "Ingeniera" }
# Si lo pensáis.. una lista es un diccionario , en el que las claves son números secuenciales comenzando en 0.
menchu_diccionario_simulando_lista = { 0: "menchu", 1: 29, 2: "Ingeniera" }  # Esto es una lista disfrazada de diccionario

# Para sacar el nombre:
menchu_lista[0]
menchu_diccionario_simulando_lista[0]
menchu_diccionario["nombre"]

# Para editar el nombre
menchu_lista[0]                         = "Felipe"
menchu_diccionario_simulando_lista[0]   = "Felipe"
menchu_diccionario["nombre"]            = "Felipe"

# Ojo con los diccionario. A la hora de recorrerlos (hacerles un bucle). Se puede? SI
# Mientras que cuando hacíamos un for en una lista, el bucle nos daba directamente los valores...
for valor in menchu_lista:
    print(valor)
# Cuando hacemos un for en un diccionario, el bucle nos da las claves.
for clave in menchu_diccionario:
    print(clave, menchu_diccionario[clave])
# Aunque... tachann!!! Hay otra opción adicional.
# Pedir en el bucle, tanto la clave como el valor asociado a esa clave:
for clave, valor in menchu_diccionario.items():
    print(clave, valor)