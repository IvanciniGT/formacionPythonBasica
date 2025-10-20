
# Python

Lenguaje de programación.

Python es un lenguaje de propósito general, interpretado, me permite crear muchos tipo de programas diferentes.

SAS Es un lenguaje de dominio específico, interpretado, me permite crear programas de análisis estadístico.

## Instalación de python

Python es un lenguaje interpretado. Mi computadora no entiende python.. igual que tampoco entiende SAS BASE o C.
Es necesario convertir nuestros textos, documentos (programas) a un lenguaje que la computadora entienda (código máquina). Eso tenemos 2 formas de hacerlo:
- Compilación: Se traduce del lenguaje en el que yo escribo mi programa a código máquina. C, C++ son lenguajes compilados.
- Interpretación: La traducción se hace en tiempo real, mediante un interprete: Python, JS, SAS BASE.

Para los lenguajes interpretados, es necesario tener instalado el interprete en la computadora.
En el caso de python el más común (hay muchos) se llama Cython. Es un intérprete escrito en lenguaje C.
Al instalarlo no se llama cython.. lo veré como python.

## Variables y tipos de datos.

Nuestros programas manejan datos. Es el objetivo de los mismos.
Esos datos tienen un determinado tipo: Textos, números, fechas...
Esos datos, en una computadora se colocan en la memoria RAM.

### Qué es una variable?

En python una variable es una referencia a un dato que tengo en RAM.
Yo coloco un dato en la memoria RAM. Y después cómo lo recupero?
Pensad en la memoria RAM como si fuera un cuaderno de cuadrícula.
Abro por una página y escribo allí un dato (5).

Una variable es una referencia a un dato que tengo en RAM.
Es como si fuera un postit. En el postit lo que escribo no es el dato en sí (5), sino un nombre: "numero"
Y ese postit lo pego en el cuaderno (memoria RAM) al lado del dato... eso me permite referirme a ese dato más adelante.

Hay lenguajes de programación que se denominan lenguajes de tipado estático (tipado fuerte).
Y hay lenguajes de tipado dinámico (tipado débil).
Python es un lenguaje de tipado dinámico (débil).
Qué significa eso?

Todos los programas que hagamos con independencia del lenguaje de programación van a manejar datos.
Y esos datos tendrán un determinado tipo. Y en todo lenguaje de programaicón existe el concepto de tipo de dato: Textos, números, fechas...

Hay lenguajes en los que las variables también tienen un tipo de dato asociado.
Por ejemplo en C, C++ cuando yo declaro una variable debo decir qué tipo de dato
Hay lenguajes en los que las variables no tienen un tipo de dato asociado = Python, JS.
En python una variable puede apuntar a un dato de cualquier tipo.
Y más adelante apuntar a un dato de otro tipo diferente.

## Paradigmas de programación

Eso son solo nombres horteras que los desarrolladores de software usan para referirse a diferentes formas de usar un lenguaje de programación.
Pero.. en el mundo de los seres humanos... y sus lenguajes, también tenemos eso.

- Imperativo:           Le doy órdenes a la computadora que debe ir ejecutando de forma secuencial.
                        En ocasiones me interesa romper la secuencia y nos salen las estructuras de control de flujo (condicionales, bucles) IF, FOR, WHILE... Python soporta esta forma de hablar
- Procedural:           Cuando el lenguaje me permite agrupar órdenes en bloques a los que asigno un nombre
                        Y posteriormente invocar (solicitar la ejecución) de esas órdenes mediante el nombre asignado, decimos que el lenguaje soporta la programación procedural. Python soporta esta forma de hablar. Esos bloques (grupos de órdenes) es lo que llamamos:
                        Funciones, Procedimientos, Métodos, Subrutinas...
- Orientación a Objetos:    Todo lenguaje hemos dicho que me permite trabajar con datos de distintos tipos.
                            Cada lenguaje viene con una serie de tipos de datos predefinidos (números, textos, fechas...). Y los datos de esos tipos de datos, tienen sus características y sus comportamientos admitidos.

                                                 CARACTERISTICAS                                        COMPORTAMIENTOS / OPERACIONES
                            Dato de tipo Texto   La secuencia de caracteres que representa el texto     aMayusculas(), longitud()
                                                 "hola"    "adios"
                            Dato de tipo Número  El valor numérico que representa el número             +, -, *, /

                            Datos de tipo Fecha  DIA, MES, AÑO                                          caesEnBisistiesto()
                                                                                                        caesEnJueves()
                            Hay lenguajes que me permiten definir mis propios TIPOS DE DATOS Esos tipos de datos CUSTOM, los llamamos CLASES. Y los lenguajes que permioten hacer esto, decimos que soportan el paradigma de programación orientada a objetos.

                            Dato de tipo Cuenta Bancaria
                                                 Titular, IBAN, Saldo                                 ingresar(), retirar(), transferir()

                            Python soporta el paradigma de programación orientada a objetos.
- Funcional                 TO-DO!
                            Otro de los paradigmas de programación que soporta python.


> Felipe, IF (Si) hay algo que no sea una silla debajo de la ventana:   CONDICIONALES
>  Quítalo!     IMPERATIVA
> Si no hay  (IF NOT SILLA) debajo de la ventana: CONDICIONAL
>    Felipe Si no hay sillas (if silla == False) GOTO IKEA!
> Felipe, pon una silla debajo de la ventana. IMPERATIVA

> Felipe, debajo de la ventana tiene que haber una silla. Es tu responsabildad. DECLARATIVO
> Con esto, estoy delegando la responsabilidad de conseguir mi objetivo en FELIPE.
> Él es quien debe decidir cómo hacerlo.

> Computadora, pon. el dato 5 en RAM. IMPERATIVA






- Orientación a objetos

PANDAS
NUMPY
SEABORN
MATPLOTLIB
