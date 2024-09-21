def calcular_precio_entrada():
    try:
        # Solicitar la edad del cliente
        edad = int(input("Introduce la edad del cliente: "))

        # Determinar el precio según la edad
        if edad < 4:
            print("La entrada es gratis.")
        elif 4 <= edad <= 18:
            print("El precio de la entrada es 5€.")
        else:
            print("El precio de la entrada es 10€.")
    except ValueError:
        print("Por favor, introduce un número válido para la edad.")

# Ejecutar la función
calcular_precio_entrada()
