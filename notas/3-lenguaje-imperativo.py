
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