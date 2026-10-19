# PORTADA
# Nombre: Alberto Manuel Medina Martínez
# Matrícula: 2630305
# Grupo: IM-3

# Resumen ejecutivo
# Una lista y una tupla sirven para guardar varios datos en orden, y los dos se
# consultan por posición usando índices. La diferencia es que la lista se puede
# modificar (agregar, quitar o cambiar elementos) y la tupla no, por eso se dice
# que una es mutable y la otra inmutable. Usé listas para lo que cambia, como
# una lista de compras, y tuplas para lo que debe quedarse fijo, como las
# coordenadas de un punto. En este documento resuelvo 2 problemas: la lista de
# compras y el de puntos y distancias. De cada uno explico qué hace, qué datos
# pide y qué muestra, cómo valido las entradas, y pongo 3 casos de prueba junto
# con el código.

# Principios y buenas prácticas
# - Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
# - Usar tuplas para datos que no deben cambiar (coordenadas, fechas,
#   configuraciones fijas).
# - Evitar modificar una lista mientras la recorres con un for, a menos que se
#   sepa exactamente lo que se está haciendo.
# - Validar los datos antes de procesarlos (tipos correctos y listas no
#   vacías).
# - Usar nombres de variables descriptivos y mensajes claros para el usuario.


# Problem 1: Shopping list basics (list operations)
# Trabaja con una lista de productos (strings). El programa crea una lista a
# partir de un texto separado por comas, agrega un nuevo producto al final,
# muestra la cantidad total de elementos y verifica si un producto específico
# está en la lista con un booleano.

# Entradas:
# - initial_items_text (string; por ejemplo, "apple,banana,orange").
# - new_item (string; producto a agregar).
# - search_item (string; producto a buscar).

# Salidas:
# Items list: <items_list>
# Total items: <len_list>
# Found item: true|false
# (true si search_item está en la lista; false en caso contrario)

# Validaciones:
# - initial_items_text no debe estar vacío después de strip().
# - El texto se separa por comas y a cada elemento se le quitan los espacios
#   extra. Decisión: si la lista inicial queda vacía (por ejemplo ",,"), se
#   considera una entrada inválida.
# - new_item y search_item no deben estar vacíos.
# - Si no se cumple, se muestra "Error: invalid input".

# Casos de prueba:
# 1) Normal: "apple,banana,orange", nuevo "milk", buscar "banana" ->
#                           Items list: ['apple', 'banana', 'orange', 'milk']
#                           Total items: 4
#                           Found item: true
# 2) Borde:  " apple ", nuevo "pear", buscar "kiwi" (un solo elemento con
#            espacios) -> Items list: ['apple', 'pear']
#                         Total items: 2
#                         Found item: false
# 3) Error:  "" (texto vacío) -> Error: invalid input

print("--- Problem 1: Shopping list basics ---")
initial_items_text = input("Enter initial items separated by commas: ").strip()
new_item = input("Enter a new item to add: ").strip()
search_item = input("Enter an item to search: ").strip()

items_list = []
for raw_item in initial_items_text.split(","):
    cleaned_item = raw_item.strip()
    if cleaned_item != "":
        items_list.append(cleaned_item)

if (initial_items_text == "" or len(items_list) == 0
        or new_item == "" or search_item == ""):
    print("Error: invalid input")
else:
    items_list.append(new_item)
    found_item = search_item in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {str(found_item).lower()}")
print()


# Problem 2: Points and distances with tuples
# Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2).
# El programa crea las tuplas point_a y point_b, calcula la distancia euclidiana
# entre ambos puntos y crea una nueva tupla midpoint con el punto medio.

# Entradas:
# - x1 (float; coordenada x del punto A).
# - y1 (float; coordenada y del punto A).
# - x2 (float; coordenada x del punto B).
# - y2 (float; coordenada y del punto B).

# Salidas:
# Point A: (x1, y1)
# Point B: (x2, y2)
# Distance: <distance>
# Midpoint: (mx, my)

# Validaciones:
# - Las 4 entradas deben poder convertirse a float.
# - No hay restricciones adicionales de rango (se permiten negativos).
# - Si no se cumple, se muestra "Error: invalid input".

# Casos de prueba:
# 1) Normal: (0, 0) y (3, 4) -> Point A: (0.0, 0.0)
#                               Point B: (3.0, 4.0)
#                               Distance: 5.0
#                               Midpoint: (1.5, 2.0)
# 2) Borde:  (2, 2) y (2, 2) (mismo punto) -> Point A: (2.0, 2.0)
#                                             Point B: (2.0, 2.0)
#                                             Distance: 0.0
#                                             Midpoint: (2.0, 2.0)
# 3) Error:  x1 = "abc" -> Error: invalid input

print("--- Problem 2: Points and distances with tuples ---")
x1_text = input("Enter x1: ")
y1_text = input("Enter y1: ")
x2_text = input("Enter x2: ")
y2_text = input("Enter y2: ")

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)
    is_valid_input = True
except ValueError:
    is_valid_input = False

if not is_valid_input:
    print("Error: invalid input")
else:
    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((point_b[0] - point_a[0]) ** 2
                + (point_b[1] - point_a[1]) ** 2) ** 0.5
    midpoint = ((point_a[0] + point_b[0]) / 2,
                (point_a[1] + point_b[1]) / 2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 2)}")
    print(f"Midpoint: {midpoint}")


# CONCLUSIONES
# Con esta tarea entendí mejor cuándo usar cada una. La lista me sirvió en la
# lista de compras porque pude agregar un producto con append() y luego
# contarlos y buscarlos con len() e in. La tupla me pareció ideal para los
# puntos, porque unas coordenadas no deberían cambiar una vez creadas, y aun así
# pude leerlas por índice para sacar la distancia y armar el punto medio como una
# tupla nueva. También me quedó claro que hay que validar lo que escribe el
# usuario antes de usarlo, para que el programa no se caiga con un texto vacío o
# con letras donde van números.

# REFERENCIAS
# References:
# 1) Python documentation - Built-in Types: Sequence Types — list, tuple, range
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 2) Python documentation - Python Tutorial: Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Python documentation - Built-in Functions (len, round)
#    https://docs.python.org/3/library/functions.html
# 4) PEP 8 - Style Guide for Python Code
#    https://peps.python.org/pep-0008/
# 5) Real Python - Lists and Tuples in Python
#    https://realpython.com/python-lists-tuples/