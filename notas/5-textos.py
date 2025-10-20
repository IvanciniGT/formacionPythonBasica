texto = "Soy un texto muy bonito!"

print(texto)

# Cuántos caracteres tiene un texto:
print(len(texto))  # La función len() devuelve la longitud de un texto (número de caracteres)

# Puedo sacar un carácter solo.. por ejemplo, el primero:
print(texto[0])  # Los textos en python son colecciones de caracteres. Puedo acceder a un caracter por su posición (índice)

# Quiero sacar el último:
print(texto[-1])  # Puedo acceder al último carácter usando el índice -1

# Si quiero los 4 primeros?
print(texto[:4])  # Saco los caracteres desde la posición 0 hasta la 4 (sin incluir el 4)

# Si quiero los últimos 7 caracteres?
print(texto[-7:])  # Saco los últimos 7 caracteres

# Si os fijáis, la sintaxis es exactamente igual que la de las tuplas.
# Y no es casualidad. En python los textos internamente son Tuplas de caracteres.

# Para los textos, eso sí, tenemos algunas operaciones adicionales:

# Control de case (mayúsculas/minúsculas)
print(texto.upper())  # Pasa todo el texto a mayúsculas
print(texto.lower())  # Pasa todo el texto a minúsculas
print(texto.capitalize())  # Pasa la primera letra a mayúscula y el resto a minúsculas
print(texto.title())  # Pasa la primera letra de cada palabra a mayúscula

# Control de espacios en blanco

texto_con_espacios = "    Hola   mundo   "
print(">>" + texto_con_espacios + "<<")  # Elimina los espacios en blanco al principio
print(">>" + texto_con_espacios.strip() + "<<")  # Elimina los espacios en blanco al principio y al final
print(">>" + texto_con_espacios.lstrip() + "<<")  # Elimina los espacios en blanco al principio (LEFT)
print(">>" + texto_con_espacios.rstrip() + "<<")  # Elimina los espacios en blanco al final (RIGHT)

# Si un texto contiene un valor concreto
print( "bonito" in texto ) # Esta sintaxis también está heredada de las tuplas

# Partir textos
# Reemplazar en textos
# Aplicar expresiones regulares
# PERO... por hoy ya hemos hecho BASTANTE!