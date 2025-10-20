# En función del tipo de datos con en el que trabajemos, en python tenemos muchos operadores disponibles.

# Operador: Es un símbolo que le dice a python que tiene que hacer una operación concreta 
# con los datos que le estamos pasando.

# Operadores numéricos:
# Todos los aritméticos:

3 + 4       # Suma
5 - 2       # Resta
2 * 3       # Multiplicación
8 / 3       # División  = 2.6666666666666665
8 // 3      # División entera (sin decimales) = 2
8 % 3       # Módulo (resto de la división entera) = 2

#  8 | 3
#    +------
# -6    2
#  2 <<<< RESTO DE LA DIVISIÓN ENTERA

2 ** 3      # Potencia = 8

## Operadores relacionales (de comparación): Estos operadores devuelve True o False, 
# indicando si la comparación es verdadera o falsa, si se cumple o no se cumple la condición.
5 > 3       # Mayor que                      True
5 < 3       # Menor que                      False
5 >= 3      # Mayor o igual que              True
5 <= 3      # Menor o igual que              False
5 == 3      # Igual que                      False
5 != 3      # Distinto que                   True

## Operadores de asignación:
x = 5       # Asignación simple              Que la variable x apunte al dato 5
#x += 3      # Equivale a x = x + 3           Ahora x vale 8
x = x + 3   # Lo mismo que la línea anterior
x -= 2      # Equivale a x = x - 2           Ahora x vale 6
x *= 4      # Equivale a x = x * 4           Ahora x vale 24
x /= 6      # Equivale a x = x / 6           Ahora x vale 4.0
x //= 3     # Equivale a x = x // 3          Ahora x vale 1.0
x %= 1      # Equivale a x = x % 1           Ahora x vale 0.0
x **= 2     # Equivale a x = x ** 2          Ahora x vale 0.0

## Operadores para textos (cadenas de texto):
"hola " + "mundo"        # Concatenación de textos         "hola mundo"
"hola " * 3               # Repetición de texto             "hola hola hola "
"-" * 80                  # Línea de 80 guiones             "--------------------------------------------------------------------------------"

### Operadores relacionales aplicados a textos:
"Hola" == "Adios"         # Igual que                      False
"Hola" != "Adios"         # Distinto que                   True
"A" < "B"                 # Menor que                      True   (Orden alfabético)
"C" > "B"                 # Mayor que                      True   (Orden alfabético)    
"Hola" >= "Hola"           # Mayor o igual que              True
"Hola" <= "Adios"          # Menor o igual que              False

## Operadores lógicos:
# Estos son operadores que trabajan sobre valores lógicos y devuelven otros valores lógicos.
True and False        # AND (Y)     Devuelve True si ambos son True, sino

edad=19
casado=False

edad>18 and casado # False, ya que no estoy casado

True or False       # OR (O)      Devuelve True si al menos uno es True

edad>18 or casado  # True, aunque no está casado, tiene más de 18 años

not True            # NOT (NO)     Devuelve el valor contrario

edad>18 and not casado   # True