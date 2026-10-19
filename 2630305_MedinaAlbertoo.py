# PORTADA
# Nombre: Alberto Manuel Medina Martínez
# Matrícula: 2630305
# Grupo: IM-3

# Resumen ejecutivo
# Los tipos int y float sirven para trabajar con números. La diferencia es que
# int guarda enteros (como una edad o las horas) y float guarda números con
# decimales (como una temperatura o el IMC). Un booleano solo puede ser True o
# False, y sale de comparar valores con operadores como >=, < o ==; con eso el
# programa decide qué hacer en un if. También es importante validar los rangos
# y evitar dividir entre cero, porque si no el programa da resultados absurdos
# o se cae. En este documento resuelvo 6 problemas, y de cada uno explico qué
# hace, qué datos recibe y qué muestra, cómo valido las entradas y cómo uso
# int, float y bool para tomar decisiones, con 3 casos de prueba y el código.

# Principios y buenas prácticas
# - Usar tipos apropiados: int para contadores, float para cantidades con
#   decimales.
# - Evitar duplicar expresiones complejas: guardar resultados intermedios en
#   variables.
# - Validar datos antes de operar (por ejemplo, que horas y salarios no sean
#   negativos).
# - Usar nombres de variables descriptivos y mensajes claros para el usuario.
# - Documentar claramente cómo se interpretan los booleanos (qué significa true
#   y qué significa false en cada contexto).


# Problem 1: Temperature converter and range flag
# Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin.
# Además, determina un valor booleano is_high_temperature que es true si la
# temperatura en Celsius es mayor o igual que 30.0 y false en caso contrario.

# Entradas:
# - temp_c (float; temperatura en °C).

# Salidas:
# Fahrenheit: <temp_f>
# Kelvin: <temp_k>
# High temperature: true|false
# (true si temp_c >= 30.0; false si temp_c < 30.0)

# Validaciones:
# - temp_c debe poder convertirse a float.
# - No se permiten temperaturas imposibles en Kelvin (temp_k < 0.0).
# - Si no se cumple, se muestra "Error: invalid input".

# Casos de prueba:
# 1) Normal: 35.0 -> Fahrenheit: 95.0
#                    Kelvin: 308.15
#                    High temperature: true
# 2) Borde:  30.0 (justo el límite) -> Fahrenheit: 86.0
#                                      Kelvin: 303.15
#                                      High temperature: true
# 3) Error:  -300 (Kelvin negativo) -> Error: invalid input

print("--- Problem 1: Temperature converter and range flag ---")
temp_text = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_text)
    is_valid_input = True
except ValueError:
    is_valid_input = False

if not is_valid_input:
    print("Error: invalid input")
else:
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0
        print(f"Fahrenheit: {round(temp_f, 2)}")
        print(f"Kelvin: {round(temp_k, 2)}")
        print(f"High temperature: {str(is_high_temperature).lower()}")
print()


# Problem 2: Work hours and overtime payment
# Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a
# hourly_rate (float). Las horas extra (más de 40) se pagan al 150% de la tarifa
# normal. Además, genera un booleano has_overtime que indica si el trabajador
# hizo horas extra.

# Entradas:
# - hours_worked (float; horas trabajadas en la semana).
# - hourly_rate (float; pago por hora).

# Salidas:
# Regular pay: <regular_pay>
# Overtime pay: <overtime_pay>
# Total pay: <total_pay>
# Has overtime: true|false
# (true si hours_worked > 40; false si hours_worked <= 40)

# Validaciones:
# - hours_worked y hourly_rate deben poder convertirse a float.
# - hours_worked >= 0
# - hourly_rate > 0
# - Si alguno no cumple, se muestra "Error: invalid input".

# Casos de prueba:
# 1) Normal: 45 horas, tarifa 100 -> Regular pay: 4000.0
#                                    Overtime pay: 750.0
#                                    Total pay: 4750.0
#                                    Has overtime: true
# 2) Borde:  40 horas, tarifa 100 (justo el límite) -> Regular pay: 4000.0
#                                                      Overtime pay: 0.0
#                                                      Total pay: 4000.0
#                                                      Has overtime: false
# 3) Error:  -5 horas, tarifa 100 -> Error: invalid input

print("--- Problem 2: Work hours and overtime payment ---")
hours_text = input("Enter hours worked: ")
rate_text = input("Enter hourly rate: ")

try:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)
    is_valid_input = True
except ValueError:
    is_valid_input = False

if not is_valid_input or hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input")
else:
    regular_hours = min(hours_worked, 40.0)
    overtime_hours = max(hours_worked - 40.0, 0.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > 40.0

    print(f"Regular pay: {round(regular_pay, 2)}")
    print(f"Overtime pay: {round(overtime_pay, 2)}")
    print(f"Total pay: {round(total_pay, 2)}")
    print(f"Has overtime: {str(has_overtime).lower()}")
print()


# Problem 3: Discount eligibility with booleans
# Determina si un cliente obtiene un descuento en su compra. La regla es:
# - Tiene descuento si:
#   - is_student es true OR
#   - is_senior es true OR
#   - purchase_total >= 1000.0
# También calcula el total a pagar aplicando un 10% de descuento cuando el
# cliente es elegible.

# Entradas:
# - purchase_total (float; total de la compra).
# - is_student_text (string; "YES" o "NO").
# - is_senior_text (string; "YES" o "NO").

# Salidas:
# Discount eligible: true|false
# Final total: <final_total>
# (true si el cliente tiene descuento; false si paga el total sin descuento)

# Validaciones:
# - purchase_total debe poder convertirse a float y ser >= 0.0
# - is_student_text e is_senior_text se normalizan con strip() y upper() y se
#   convierten a booleanos is_student e is_senior.
# - Si el texto no es "YES" ni "NO", se muestra "Error: invalid input".

# Casos de prueba:
# 1) Normal: 500, "yes", "no" -> Discount eligible: true
#                                Final total: 450.0
# 2) Borde:  1000, "NO", "NO" (justo el límite) -> Discount eligible: true
#                                                  Final total: 900.0
# 3) Error:  500, "maybe", "NO" -> Error: invalid input

print("--- Problem 3: Discount eligibility with booleans ---")
purchase_text = input("Enter purchase total: ")
is_student_text = input("Is student? (YES/NO): ").strip().upper()
is_senior_text = input("Is senior? (YES/NO): ").strip().upper()

try:
    purchase_total = float(purchase_text)
    is_valid_input = True
except ValueError:
    is_valid_input = False

if (not is_valid_input or purchase_total < 0.0
        or is_student_text not in ["YES", "NO"]
        or is_senior_text not in ["YES", "NO"]):
    print("Error: invalid input")
else:
    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"
    discount_eligible = (is_student or is_senior
                         or purchase_total >= 1000.0)

    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total

    print(f"Discount eligible: {str(discount_eligible).lower()}")
    print(f"Final total: {round(final_total, 2)}")
print()


# Problem 4: Basic statistics of three integers
# Lee tres números enteros y calcula: suma, promedio (float), valor máximo,
# valor mínimo y un booleano all_even que indica si los tres números son pares.

# Entradas:
# - n1 (int)
# - n2 (int)
# - n3 (int)

# Salidas:
# Sum: <sum_value>
# Average: <average_value>
# Max: <max_value>
# Min: <min_value>
# All even: true|false
# (true si los tres números son pares; false si al menos uno es impar)

# Validaciones:
# - Los tres valores deben poder convertirse a int.
# - No hay restricciones adicionales (se permiten negativos).
# - Si no se pueden convertir, se muestra "Error: invalid input".

# Casos de prueba:
# 1) Normal: 4, 10, 6 -> Sum: 20
#                        Average: 6.67
#                        Max: 10
#                        Min: 4
#                        All even: true
# 2) Borde:  -2, 0, 7 (negativo y cero) -> Sum: 5
#                                          Average: 1.67
#                                          Max: 7
#                                          Min: -2
#                                          All even: false
# 3) Error:  5, "abc", 8 -> Error: invalid input

print("--- Problem 4: Basic statistics of three integers ---")
n1_text = input("Enter first integer: ")
n2_text = input("Enter second integer: ")
n3_text = input("Enter third integer: ")

try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)
    is_valid_input = True
except ValueError:
    is_valid_input = False

if not is_valid_input:
    print("Error: invalid input")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")
print()


# Problem 5: Loan eligibility (income and debt ratio)
# Determina si una persona es elegible para un préstamo con base en:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
# La regla es:
# - debt_ratio = monthly_debt / monthly_income
# - eligible es true si:
#   - monthly_income >= 8000.0 AND
#   - debt_ratio <= 0.4 AND
#   - credit_score >= 650

# Entradas:
# - monthly_income (float; ingreso mensual).
# - monthly_debt (float; pagos mensuales de deuda).
# - credit_score (int; puntaje de crédito).

# Salidas:
# Debt ratio: <debt_ratio>
# Eligible: true|false
# (true si cumple las tres condiciones; false si no cumple alguna)

# Validaciones:
# - Los datos deben poder convertirse a float (ingreso y deuda) e int (puntaje).
# - monthly_income > 0.0 (evita la división entre cero).
# - monthly_debt >= 0.0
# - credit_score >= 0
# - Si no se cumple, se muestra "Error: invalid input".

# Casos de prueba:
# 1) Normal: ingreso 15000, deuda 3000, puntaje 700 -> Debt ratio: 0.2
#                                                      Eligible: true
# 2) Borde:  ingreso 8000, deuda 3200, puntaje 650 (justo en los límites) ->
#                                                      Debt ratio: 0.4
#                                                      Eligible: true
# 3) Error:  ingreso 0, deuda 500, puntaje 700 -> Error: invalid input

print("--- Problem 5: Loan eligibility ---")
income_text = input("Enter monthly income: ")
debt_text = input("Enter monthly debt: ")
score_text = input("Enter credit score: ")

try:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)
    is_valid_input = True
except ValueError:
    is_valid_input = False

if (not is_valid_input or monthly_income <= 0.0 or monthly_debt < 0.0
        or credit_score < 0):
    print("Error: invalid input")
else:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4
                and credit_score >= 650)

    print(f"Debt ratio: {round(debt_ratio, 2)}")
    print(f"Eligible: {str(eligible).lower()}")
print()


# Problem 6: Body Mass Index (BMI) and category flag
# Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
# - bmi = weight_kg / (height_m * height_m)
# Además, genera booleanos para indicar:
# - is_underweight (bmi < 18.5)
# - is_normal (18.5 <= bmi < 25.0)
# - is_overweight (bmi >= 25.0)

# Entradas:
# - weight_kg (float; peso en kilogramos).
# - height_m (float; estatura en metros).

# Salidas:
# BMI: <bmi redondeado a 2 decimales>
# Underweight: true|false
# Normal: true|false
# Overweight: true|false
# (cada booleano es true solo si el bmi está en su rango; false en otro caso)

# Validaciones:
# - weight_kg y height_m deben poder convertirse a float.
# - weight_kg > 0.0
# - height_m > 0.0 (evita la división entre cero).
# - Si no se cumple, se muestra "Error: invalid input".

# Casos de prueba:
# 1) Normal: 70 kg, 1.75 m -> BMI: 22.86
#                             Underweight: false
#                             Normal: true
#                             Overweight: false
# 2) Borde:  100 kg, 2.0 m (bmi exactamente 25.0) -> BMI: 25.0
#                                                    Underweight: false
#                                                    Normal: false
#                                                    Overweight: true
# 3) Error:  70 kg, 0 m -> Error: invalid input

print("--- Problem 6: Body Mass Index (BMI) and category flag ---")
weight_text = input("Enter weight in kg: ")
height_text = input("Enter height in meters: ")

try:
    weight_kg = float(weight_text)
    height_m = float(height_text)
    is_valid_input = True
except ValueError:
    is_valid_input = False

if not is_valid_input or weight_kg <= 0.0 or height_m <= 0.0:
    print("Error: invalid input")
else:
    bmi = weight_kg / (height_m * height_m)
    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0

    print(f"BMI: {round(bmi, 2)}")
    print(f"Underweight: {str(is_underweight).lower()}")
    print(f"Normal: {str(is_normal).lower()}")
    print(f"Overweight: {str(is_overweight).lower()}")


# CONCLUSIONES
# Con esta tarea vi que los int y los float casi siempre se usan juntos: por
# ejemplo, en el pago de horas extra mezclo horas y tarifas con decimales. Las
# comparaciones me dan booleanos, y con ellos el programa decide qué mostrar
# usando if. También entendí por qué hay que validar rangos y evitar dividir
# entre cero, como con el ingreso del préstamo o la estatura del IMC. Aprendí
# que combinar condiciones con and, or y not sirve para armar reglas más
# completas, y que este patrón se repite en nómina, descuentos, préstamos y salud.

# REFERENCIAS
# References:
# 1) Python documentation - Built-in Types: Numeric Types — int, float, complex
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Built-in Types: Boolean Type — bool
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python documentation - Python Tutorial: Numbers
#    https://docs.python.org/3/tutorial/introduction.html#numbers
# 4) Python documentation - Built-in Functions (round, min, max)
#    https://docs.python.org/3/library/functions.html
# 5) Real Python - Basic Data Types in Python
#    https://realpython.com/python-data-types/