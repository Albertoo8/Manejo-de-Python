# PORTADA
# Nombre: Alberto Manuel Medina Martínez
# Matrícula: 2630305
# Grupo: IM-3

# Resumen ejecutivo
# En Python, un string (texto) no se puede modificar directamente una vez creado;
# cualquier cambio genera una cadena completamente nueva.
# Para trabajar con texto podemos unir palabras con +, medir su tamaño con len(),
# recortar trozos, buscar patrones y reemplazar partes. Además, es muy
# importante limpiar los datos con métodos como strip() o lower(), ya que la
# gente suele escribir mal o dejar espacios de más en correos y contraseñas.
# Este documento incluye 6 ejercicios prácticos con su descripción, entradas,
# salidas, código y tres casos de prueba (normal, límite y error).

# Principios y buenas prácticas
# - Los strings son inmutables: cualquier cambio genera una nueva cadena.
# - Es buena práctica normalizar la entrada con strip() y lower() antes de
#   compararla.
# - Evitar "números mágicos" en índices: documentar qué extrae cada slice
#   y usar constantes con nombre (por ejemplo, LABEL_LENGTH).
# - Usar métodos de string en lugar de reescribir lógica básica.
# - Diseñar validaciones claras: primero que no esté vacío, luego el formato.
# - Escribir código legible: nombres de variables claros y mensajes de error
#   entendibles.

# Constantes del programa
MIN_NAME_WORDS = 2
MIN_PALINDROME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
LABEL_LENGTH = 30

ERROR_MESSAGE = "Error: invalid input"


# Problem number.- 1: Full name formatter (name + initials)
# Recibe el nombre completo de una persona en una sola cadena (por ejemplo:
# "juan carlos tovar"). El programa debe:
# 1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas)
# 2) Mostrar el nombre formateado en Title Case y las iniciales (J.C.T.)

# Entradas:
# - full_name (string; nombre completo, puede venir en mayúsculas, minúsculas
#   o mezclado, con espacios extra).

# Salidas:
# Formatted name: <Name In Title Case>
# Initials: <X.X.X.>

# Validaciones:
# - full_name no debe estar vacío después de strip().
# - Debe contener al menos dos palabras (nombre y apellido).
# - No se aceptan cadenas que sean solo espacios.

# Casos de prueba:
# 1) Normal: "  juan carlos   tovar " -> Formatted name: Juan Carlos Tovar
#                                        Initials: J.C.T.
# 2) Borde:  "ANA lopez" (exactamente dos palabras) -> Formatted name: Ana Lopez
#                                                      Initials: A.L.
# 3) Error:  "juan" (una sola palabra) -> Error: invalid input

print("--- Problem 1: Full name formatter ---")
full_name = input("Enter full name: ")
clean_name = full_name.strip()
words = clean_name.split()

if clean_name == "" or len(words) < MIN_NAME_WORDS:
    print(ERROR_MESSAGE)
else:
    formatted_name = " ".join(words).title()
    initials = ""
    for word in words:
        initials = initials + word[0].upper() + "."  # word[0] = primera letra
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")
print()


# Problem number.- 2: Simple email validator (structure + domain)
# Valida si una dirección de correo tiene un formato básico correcto:
# - Contiene exactamente un '@'.
# - Después del '@' hay al menos un '.'.
# - No contiene espacios en blanco.
# Si el correo es válido, también muestra el dominio (la parte después del '@').

# Entradas:
# - email_text (string).

# Salidas:
# Valid email: true  (o)  Valid email: false
# Si es válido: Domain: <domain_part>

# Validaciones:
# - email_text no debe estar vacío tras strip().
# - Contar cuántas veces aparece '@' con count() (debe ser exactamente 1).
# - No debe haber espacios (" " not in email_text).
# - Debe haber un '.' después del '@'.

# Casos de prueba:
# 1) Normal: "student@uni.edu.mx" -> Valid email: true
#                                   Domain: uni.edu.mx
# 2) Borde:  "a@b.c" (el correo válido más corto) -> Valid email: true
#                                                    Domain: b.c
# 3) Error:  "   " (solo espacios) -> Error: invalid input

print("--- Problem 2: Simple email validator ---")
email_text = input("Enter email: ").strip()

if email_text == "":
    print(ERROR_MESSAGE)
else:
    at_count = email_text.count("@")
    at_position = email_text.find("@")
    domain_part = email_text[at_position + 1:]  # texto después del '@'

    if at_count == 1 and " " not in email_text and "." in domain_part:
        print("Valid email: true")
        print(f"Domain: {domain_part}")
    else:
        print("Valid email: false")
print()


# Problem number.- 3: Palindrome checker (ignoring spaces and case)
# Determina si una frase es un palíndromo, es decir, si se lee igual de
# izquierda a derecha y de derecha a izquierda, ignorando espacios y
# mayúsculas/minúsculas. También muestra la versión normalizada de la frase.
# Ejemplos:
# - "Anita lava la tina" -> palíndromo
# - "Hola mundo" -> no es palíndromo

# Entradas:
# - phrase (string).

# Salidas:
# Normalized: <text>
# Is palindrome: true  (o)  Is palindrome: false

# Validaciones:
# - phrase no debe estar vacía tras strip().
# - El texto limpio (sin espacios) debe tener al menos 3 caracteres.

# Casos de prueba:
# 1) Normal: "Anita lava la tina" -> Normalized: anitalavalatina
#                                    Is palindrome: true
# 2) Borde:  "aba" (longitud mínima) -> Normalized: aba
#                                       Is palindrome: true
# 3) Error:  "a b" (solo 2 caracteres sin espacios) -> Error: invalid input

print("--- Problem 3: Palindrome checker ---")
phrase = input("Enter phrase: ")
normalized_text = phrase.strip().lower().replace(" ", "")

if phrase.strip() == "" or len(normalized_text) < MIN_PALINDROME_LENGTH:
    print(ERROR_MESSAGE)
else:
    print(f"Normalized: {normalized_text}")
    # normalized_text[::-1] es el mismo texto leído al revés
    if normalized_text == normalized_text[::-1]:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")
print()


# Problem number.- 4: Sentence word stats (lengths and first/last word)
# Dada una oración, el programa debe:
# 1) Normalizar espacios (quitar los espacios al principio y al final).
# 2) Separar las palabras por espacios.
# 3) Mostrar el número total de palabras, la primera, la última, la más corta
#    y la más larga (por longitud).

# Entradas:
# - sentence (string).

# Salidas:
# Word count: <n>
# First word: <...>
# Last word: <...>
# Shortest word: <...>
# Longest word: <...>

# Validaciones:
# - sentence no debe estar vacía tras strip().
# - Debe contener al menos una palabra válida después de split().

# Casos de prueba:
# 1) Normal: "The quick brown fox jumps" -> Word count: 5, First word: The,
#    Last word: jumps, Shortest word: The, Longest word: quick
# 2) Borde:  "Hello" (una sola palabra) -> Word count: 1, y la primera, última,
#    más corta y más larga son todas "Hello"
# 3) Error:  "     " (solo espacios) -> Error: invalid input

print("--- Problem 4: Sentence word stats ---")
sentence = input("Enter sentence: ")
clean_sentence = sentence.strip()
words = clean_sentence.split()

if clean_sentence == "" or len(words) == 0:
    print(ERROR_MESSAGE)
else:
    shortest_word = words[0]
    longest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")  # índice -1 = última palabra
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")
print()


# Problem number.- 5: Password strength classifier
# Clasifica una contraseña como (weak), (medium) o (strong) según reglas mínimas:
# weak: longitud menor que 8, o solo usa un tipo de carácter (por ejemplo,
#       todo en minúsculas) o es muy simple
# medium: longitud mayor o igual a 8 y combina al menos dos tipos de carácter
#       (mayúsculas con minúsculas, o con dígitos, o con símbolos)
# strong: longitud mayor o igual a 8 y contiene al menos:
#       - una letra mayúscula
#       - una letra minúscula
#       - un dígito
#       - un símbolo no alfanumérico (por ejemplo !, @, #)

# Entradas:
# - password_input (string).

# Salidas:
# Password strength: weak
# Password strength: medium
# Password strength: strong

# Validaciones:
# - No se acepta una contraseña vacía.
# - La longitud se verifica con len().

# Casos de prueba:
# 1) Normal: "Abc123!x" -> Password strength: strong
# 2) Borde:  "Abcdefg1" (exactamente 8 caracteres, 3 tipos) -> Password
#    strength: medium
# 3) Error:  "" (vacía) -> Error: invalid input

print("--- Problem 5: Password strength classifier ---")
password_input = input("Enter password: ")

if password_input.strip() == "":
    print(ERROR_MESSAGE)
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    types_count = 0
    if has_upper:
        types_count = types_count + 1
    if has_lower:
        types_count = types_count + 1
    if has_digit:
        types_count = types_count + 1
    if has_symbol:
        types_count = types_count + 1

    if len(password_input) < MIN_PASSWORD_LENGTH:
        strength = "weak"
    elif types_count == 4:
        strength = "strong"
    elif types_count >= 2:
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")
print()


# Problem number.- 6: Product label formatter (fixed-width text)
# Dado el nombre de un producto y su precio, genera una etiqueta de una sola
# línea con el formato:
# Product: <NAME> | Price: $<PRICE>
# La cadena completa debe tener exactamente 30 caracteres:
# - Si es más corta, se rellena con espacios al final.
# - Si es más larga, se recorta a 30 caracteres.

# Entradas:
# - product_name (string).
# - price_value (se lee como string; debe poder convertirse a un número
#   positivo).

# Salidas:
# Label: "<exactamente 30 caracteres>"  (entre comillas para ver los espacios)

# Validaciones:
# - product_name no debe estar vacío tras strip().
# - price_value debe poder convertirse a un número positivo.

# Casos de prueba:
# 1) Normal: "Pen", "5" -> "Product: Pen | Price: $5      " (con relleno)
# 2) Borde:  "Notebook", "10" -> "Product: Notebook | Price: $10"
#    (exactamente 30 caracteres, sin relleno ni recorte)
# 3) Error:  "Pen", "-5" -> Error: invalid input

print("--- Problem 6: Product label formatter ---")
product_name = input("Enter product name: ").strip()
price_text = input("Enter price: ").strip()

price_is_number = price_text.replace(".", "", 1).isdecimal()

if product_name == "" or not price_is_number or float(price_text) <= 0:
    print(ERROR_MESSAGE)
else:
    label = f"Product: {product_name} | Price: ${price_text}"
    if len(label) > LABEL_LENGTH:
        label = label[:LABEL_LENGTH]  # recorta a 30 caracteres
    else:
        label = label + " " * (LABEL_LENGTH - len(label))
    print(f'Label: "{label}"')


# CONCLUSIONES
# El manejo de strings es muy importante en la entrada y salida de datos, porque
# casi todo lo que el usuario escribe llega como texto. strip() conviene al
# limpiar los bordes, lower() al comparar sin importar mayúsculas, split() para
# separar palabras y join() para volver a armarlas. Normalizar el texto antes de
# compararlo evita que "Hola", "hola " y "HOLA" se traten distinto. Validar bien
# evita errores y datos basura. Aprendí que los strings son inmutables (cada
# método devuelve una cadena nueva) y que los slices, como text[::-1], permiten
# extraer o recortar texto de forma clara.

# REFERENCIAS
# References:
# 1) Python documentation - Built-in Types: Text Sequence Type — str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - Python Tutorial: An Informal Introduction (Text)
#    https://docs.python.org/3/tutorial/introduction.html#text
# 3) Real Python - Strings and Character Data in Python
#    https://realpython.com/python-strings/
# 4) PEP 8 - Style Guide for Python Code (naming conventions)
#    https://peps.python.org/pep-0008/
# 5) Downey, A. - Think Python (Green Tea Press), capítulos sobre strings