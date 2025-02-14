mensaje = """
Bienvenidos a la calculadora
Para salir escriba 'salir'
Las operaciones son suma, resta, multi, divi
"""

operaciones = ["suma", "resta", "multi", "divi"] #array de operaciones
resultado=""

while True:
    print(mensaje)
    n1 = input("Ingresa el primer número: ")
    if n1.lower() == "salir":
        break
    n1 = int(n1)

    operacion = input("Ingresa la operación (suma, resta, multi, divi): ").lower()
    if operacion == "salir":
        break
    if operacion not in operaciones:
        print("Operación no válida. Inténtalo de nuevo.")
        continue

    n2 = input("Ingresa el siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if operacion == "suma":
        resultado = n1 + n2
    elif operacion == "resta":
        resultado = n1 - n2
    elif operacion == "multi":
        resultado = n1 * n2
    elif operacion == "divi":
        if n2 != 0:
            resultado = n1 / n2
        else:
            print("Error: División por cero no permitida.")
            continue
    print(f"El resultado es: {resultado}")
