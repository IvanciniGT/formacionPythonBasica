4
3.12
5           # Colocar un número en memoria RAM. Es un dato con el que voy a trabajar
"hola"      # Colocar un texto en memoria RAM. Es un dato con el que voy a trabajar
True        # Colocar un lógico (Verdadero/Falso) en memoria RAM. Es un dato con el que voy a trabajar

# La pregunta es... cómo leches me refiero ahora al dato ese que guardé 5 líneas arriba?
numero1 = 5 # Qué ejecuta en mi máquina (cómo lo hace python)
            # 1.  "5"  -> Coloca en memoria RAM un dato de tipo numérico con valor 5
            # 2.  "numero1" -> Coge un postit y escribe en él el nombre: "numero1"
            # 3.  "=" -> Operador Asignación. Pegar el postit al lado del dato 5

            # Podríamos pensar que esta línea asigna el dato 5 a la variable numero1.
            # pero en realidad hace lo contrario:
            # Lo que hace es asignar la variable numero1 al dato 5.         numero1 ---> 5

numero1 = 8 # 1. "8"  -> Coloca en memoria RAM un dato de tipo numérico con valor 8
            #            Dónde? En el mismo sitio donde estaba el 5 o en otro? En OTRO
            #            Y llegado a este punto, en RAM tengo 2 datos numéricos: 5 y 8
            # 2. "numero1 =" -> Coge el postit con el nombre "numero1"
            #            Arrancarlo de donde lo tenía pegado (al lado del 5)
            #            Pegar el postit al lado del 8
            #            "Lo que varía es la variable". 
            #            La tenía pegada en un sitio y ahora la tengo pegada en otro.
            #            Lo que pasa es que el dato 5 ha quedado huérfano de variable.
            #            No hay ninguna variable que apunte a él. Y por ende ese dato es irrecuperable.
            #            Se convierte en basura (GARBAGE).
            #            En python tenemos lo que se llama el GARBAGE COLLECTOR, que quizás borre ese dato huérfano
            #            de la memoria RAM para aprovechar ese espacio para otros datos nuevos que vayamos creando.
numero2 = 7

numero1 + numero2

mi_variable = "hola"  # mi_variable: SNAKE CASE: Cada palabra va separada por un guión bajo y todo en minúsculas.
mi_variable = 3
mi_variable = True
# Es lo podemos hacer porque python es un lenguaje de tipado dinámico.
# Y las variables no tienen un tipo de dato asociado. CUIDADO! Eso no significa que los datos no tengan tipo.
# Por ejemplo en JAVA, que es un lenguaje de tipado estático, una variable debe tener un tipo de dato asociado.
# Por ejemplo:
# String miVariable = "hola";  # miVariable: CAMEL CASE: La primera palabra en minúscula y las siguientes con la primera letra en mayúscula.
# miVariable = 3;              # ERROR de compilación! No puedo asignar una variable preparada para apuntar a un texto a un número.