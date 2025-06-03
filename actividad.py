def suma():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"La suma es: {num1 + num2}")

def celsius_a_fahrenheit():
    celsius = float(input("Ingrese los grados Celsius: "))
    print(f"Equivalente en Fahrenheit: {celsius * 1.8 + 32}")

def area_triangulo():
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    print(f"Área del triángulo: {(base * altura) / 2}")

def par_o_impar():
    num = int(input("Ingrese un número: "))
    print(f"El número es {'par' if num % 2 == 0 else 'impar'}.")

def intercambiar_valores():
    a = input("Ingrese el valor de A: ")
    b = input("Ingrese el valor de B: ")
    a, b = b, a
    print(f"Valores intercambiados: A = {a}, B = {b}")

def calculadora():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        resultado = num1 / num2 if num2 != 0 else "Error: División por cero"
    else:
        resultado = "Operación no válida"
    
    print(f"Resultado: {resultado}")

def edad_en_meses_dias():
    edad = int(input("Ingrese su edad en años: "))
    print(f"Aproximadamente {edad * 12} meses y {edad * 365} días.")

def numero_mayor():
    nums = [float(input(f"Ingrese el número {i+1}: ")) for i in range(3)]
    print(f"El número mayor es: {max(nums)}")

def es_multiplo():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(f"{num1} {'es' if num1 % num2 == 0 else 'no es'} múltiplo de {num2}.")

def salario_con_bonificacion():
    salario_base = float(input("Ingrese su salario base: "))
    print(f"Salario total con bonificación: {salario_base * 1.1}")

# Menú de selección de actividad
opciones = {
    1: suma,
    2: celsius_a_fahrenheit,
    3: area_triangulo,
    4: par_o_impar,
    5: intercambiar_valores,
    6: calculadora,
    7: edad_en_meses_dias,
    8: numero_mayor,
    9: es_multiplo,
    10: salario_con_bonificacion
}

while True:
    print("\n--- Actividades Python ---")
    print("1. Suma de dos números")
    print("2. Conversión de Celsius a Fahrenheit")
    print("3. Área de un triángulo")
    print("4. Par o Impar")
    print("5. Intercambiar valores")
    print("6. Calculadora")
    print("7. Edad en meses y días")
    print("8. Número mayor")
    print("9. Verificar múltiplo")
    print("10. Salario con bonificación")
    print("0. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 0:
        break
    elif opcion in opciones:
        opciones[opcion]()
    else:
        print("Opción inválida, intente nuevamente.")
