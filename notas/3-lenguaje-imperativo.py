
#texto = "Hola"                            # Statement.. Esto no es sino una FRASE en PYTHON
#nombre = input("Escribe tu nombre: ")     # Statement
#print(texto + " " + nombre)               # Statement

# "Hola" = DATO... el equivalente en Español sería una ???? SUSTANTIVO .
# "texto" = VARIABLE... el equivalente en Español sería una ???? PRONOMBRE!
#" El niño es guapo"
#" Él tiene doce años"  Él es un pronombre que sustituye al sustantivo "El niño".. es decir, 
# me permite referirme al sustantivo sin tener que repetirlo.
# Los operadores : +
# Y las funciones: input() y print() son los VERBOS de la oración.

# Este es un documento, escrito en lenguaje python...
# Igual que puedo escribir documentos en WORD, usando lenguaje ESPAÑOL.

# Statement: Declaración, Sentencia...
# Sentencia? Qué significa (sinónimos de Sentencia en Español)? Frase u Oración


# En lenguaje imperativo, lo que vamos es escribiendo ORDENES (STATEMENTS) que la computadora
# Irá ejecutando de forma secuencial, una tras otra, de arriba a abajo.

# print("Primer mensaje")  # Primera orden (statement)
#print("Segundo mensaje")  # Segunda orden (statement)
# print("Tercer mensaje")   # Tercera orden (statement)

# Hay veces que hay órdenes que no queremos que se ejecuten en ciertos escenarios/bajo ciertas condiciones.
# Y es la gracia de un programa.. Si siempre hay que ejecutar lo mismo... No necesito un programa

# Para conseguir este efecto, en TODOS los lenguajes de programación existen estructuras de control
# de flujo: CONDICIONALES 

edad_como_texto = input("Escribe tu edad: ")
print("Tu edad es " + edad_como_texto)

# Pregunta... que tipo de dato tiene la variable edad?
#             LAS VARIABLES EN PYTHON NO TIENEN TIPO DE DATO! Es un lenguaje de tipado dinámico.

# Pregunta... que tipo de dato tiene el dato al que apunta la variable edad?
#             El tipo de dato que devuelva la función input().. 
# Y esa función siempre devuelve un dato de tipo TEXTO (STRING)

# Puedo preguntar si la persona tiene más de 18 años?

edad_como_texto >= "8"
# Si edad_como_texto vale "10", está antes alfabéticamente el "1" que el "8".. Y eso daría False

# En muchos casos, tendremos que convertir datos de un tipo a otro
# En python lo tipos de datos tienen nombres muy especiales:
# números enteros: int
# números con decimales: float
# textos: str
# lógicos (Verdadero/Falso): bool

# Para convertir un dato a un determinado tipo, existen build -in functions (funciones integradas)
# muy sencillas de recordar.. ya que su nombre corresponde con el nombre del tipo de dato al que quiero convertir.

edad_como_numero = int(edad_como_texto)  # Convierto el texto capturado a un número entero
print(edad_como_numero >= 18)                    # Ahora sí puedo comparar correctamente si la edad es
if edad_como_numero >= 18:
 print("Enhorabuena, eres mayor de edad!")
 print("Ya puedes sacarte el carnet de conducir.")
elif edad_como_numero >= 15: # Si no tienes más de 18, pero tienes más de 15
    print("Todavia tienes que esperar un poquito para sacarte el carnet de conducir.")
    print("Paciencia, que ya queda menos!")
else:
    print("Eres un yogurín!!! Mejor a ver los dibujos y dejar de pensar en conducir!")


# Bucles: Una tarea que se debe ejecutar en más de una ocasión.
# Los hay de varios tipos.. veamos 1 de ellos.. el más simple: WHILE
# Este bucle es casi igual que un if, salvo que cuando se cumple la condición,
# en lugar de ejecutar el bloque de código 1 sola vez, lo ejecuta repetidamente, 
# hasta que la condición deja de cumplirse.

inicio_cuenta_atras = 5
if(inicio_cuenta_atras > 0):
    print(inicio_cuenta_atras)
    inicio_cuenta_atras -= 1

while(inicio_cuenta_atras > 0):
    print(inicio_cuenta_atras)
    inicio_cuenta_atras -= 1

print("Explosión")
print("Cataplan!!!!!")

# Segundo tipo de bucle que tiene python: FOR
# Este bucle me permite recorrer los elementos de una colección (ver fichero 4-colecciones.py)
# Por ahora, hemos visto ya un tipo de colección que tiene python: TUPLAS

tupla = (1, 2, 3, 4, 5)
for numero in tupla: # Para cada elemento de la tupla, haz lo siguiente:
    # Quiero hacer algo
    print(numero)

# Existe en python un bucle que me permita hacer un trabajo 100 veces? NO, en otro lenguajes si.. En python NO.
# Solo hay esos 2 tipos de bucles: WHILE y FOR.
# Si quiero ejecutar algo 100 veces.. que se os ocurre?
contador = 1
while (contador <= 100):
    print("Esta es la repetición número " + str(contador))
    contador += 1

# Esta es una forma...
# Otra? sería con un for... Pero el for hace un recorrido por una colección....
# Si quiero que se ejecute 100 veces.. necesito una tupla con 100 elementos.
tupla_larga = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
                31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
                51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,
                71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,
                91,92,93,94,95,96,97,98,99,100)
for numero in tupla_larga:
    print("Esta es la repetición número " + str(numero))    
# Con un bucle for no hay forma de hacer eso sin crear la tupla de 100 elementos.
# Lo que si podemos es ayudarnos de otra de esas built-in functions (funciones integradas) que tiene python,
# Que nos ayuda a crear esa tupla de 100 elementos en automático: range()
for numero in range(1, 10): # range(inicio, fin_exclusivo)
    print("Esta es la repetición número " + str(numero))
# La función range.. está creando una tupla de números del 1 al 100 (100 no incluido) y el for la recorre.

for numero in range(1, 10,2): # range(inicio, fin_exclusivo, paso)
    print("Esta es la repetición número " + str(numero))

for numero in range(20, 1,-5): # range(inicio, fin_exclusivo, paso)
    print("Esta es la repetición número " + str(numero))

colores = ("rojo", "verde", "azul", "amarillo")
for color in colores:
    print("El color es: " + color)
